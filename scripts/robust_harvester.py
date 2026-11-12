import os
import sys
import json
import argparse
import subprocess
import cv2
import numpy as np

PYTHON_EXE = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
REGISTRY_PATH = "src/pipeline/master_category_registry.json"

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return res.stdout
    except subprocess.CalledProcessError as e:
        return None

def parse_duration(val, default=15.0):
    try:
        val_str = str(val).strip().lower()
        if not val_str or val_str == "na":
            return default
        # Remove 'secs', 'sec', 's'
        val_str = val_str.replace("secs", "").replace("sec", "").replace("s", "").strip()
        if ":" in val_str:
            parts = val_str.split(":")
            if len(parts) == 2:
                return float(parts[0]) * 60 + float(parts[1])
            elif len(parts) == 3:
                return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
        return float(val_str)
    except Exception:
        return default

def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        raise FileNotFoundError(f"Registry not found: {REGISTRY_PATH}")
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

class RobustSubcategoryHarvester:
    def __init__(self, subcategory_id: str, output_dir: str = "harvested_clips"):
        self.registry = load_registry()
        self.sub_id = subcategory_id
        if self.sub_id not in self.registry["subcategories"]:
            raise ValueError(f"Unknown subcategory '{self.sub_id}'.")
        self.sub_config = self.registry["subcategories"][self.sub_id]
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.universal_negatives = self.registry.get("universal_negative_filters", [])

    def tier1_search_youtube(self, max_candidates=10):
        """Tier 1: Harvest candidates using strict query patterns and duration filters."""
        queries = self.sub_config["harvester"]["primary_queries"]
        candidates = []
        
        print(f"\n[Tier 1] Querying YouTube for '{self.sub_config['name']}'...")
        for q in queries:
            search_str = f"ytsearch8:{q}"
            cmd = [
                PYTHON_EXE, "-m", "yt_dlp",
                "--print", "%(id)s | %(title)s | %(duration)s",
                "--match-filter", "duration <= 60 & duration >= 3",
                search_str
            ]
            out = run_cmd(cmd)
            if not out:
                continue
            for line in out.strip().split("\n"):
                if "|" in line:
                    parts = [p.strip() for p in line.split("|")]
                    vid_id = parts[0]
                    title = parts[1] if len(parts) > 1 else ""
                    dur = parse_duration(parts[2]) if len(parts) > 2 else 15.0
                    
                    title_lower = title.lower()
                    if any(neg in title_lower for neg in self.universal_negatives):
                        continue
                    if any(c["id"] == vid_id for c in candidates):
                        continue
                    candidates.append({"id": vid_id, "title": title, "duration": dur, "source": "tier1_search"})
                    if len(candidates) >= max_candidates:
                        break
            if len(candidates) >= max_candidates:
                break
        return candidates

    def tier2_golden_candidates(self):
        """Tier 2: Retrieve verified golden candidate clips from registry."""
        print(f"[Tier 2] Checking Golden Reference Table for '{self.sub_id}'...")
        golden = self.sub_config.get("golden_candidates", [])
        if not golden:
            fallback_queries = self.sub_config["harvester"].get("fallback_queries", [])
            print(f"  Golden table empty. Querying {len(fallback_queries)} fallback queries...")
            candidates = []
            for q in fallback_queries:
                cmd = [
                    PYTHON_EXE, "-m", "yt_dlp",
                    "--print", "%(id)s | %(title)s | %(duration)s",
                    "--match-filter", "duration <= 60 & duration >= 3",
                    f"ytsearch5:{q}"
                ]
                out = run_cmd(cmd)
                if out:
                    for line in out.strip().split("\n"):
                        if "|" in line:
                            p = [x.strip() for x in line.split("|")]
                            candidates.append({"id": p[0], "title": p[1], "duration": parse_duration(p[2]) if len(p) > 2 else 15.0, "source": "tier2_fallback"})
            return candidates
        return [{"id": g["id"], "title": g.get("title", ""), "duration": g.get("duration", 10.0), "source": "tier2_golden"} for g in golden]

    def download_candidate(self, vid_id: str):
        """Download high quality MP4 candidate."""
        dest = os.path.join(self.output_dir, f"{vid_id}.mp4")
        if os.path.exists(dest):
            return dest
        cmd = [
            PYTHON_EXE, "-m", "yt_dlp",
            "-f", "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/best",
            "--merge-output-format", "mp4",
            "-o", dest,
            f"https://www.youtube.com/shorts/{vid_id}"
        ]
        run_cmd(cmd)
        return dest if os.path.exists(dest) else None

    def tier3_vision_gatekeeper(self, video_path: str):
        """
        Tier 3: 4-Frame Keyframe Purity Gatekeeper
        Samples frames at 15%, 40%, 65%, 85% to detect:
        - Streamer facecam / PiP boxes in corners
        - Giant watermark bars or burned-in TikTok subtitles
        - Static screenshots / dead frames
        """
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            return False, "Cannot open video"
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        if total_frames < 30:
            cap.release()
            return False, "Too short (< 1s)"
            
        sample_indices = [
            int(total_frames * 0.15),
            int(total_frames * 0.40),
            int(total_frames * 0.65),
            int(total_frames * 0.85),
        ]
        
        frames = []
        for idx in sample_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)
        cap.release()

        if len(frames) < 4:
            return False, "Failed to sample 4 keyframes"

        # Check 1: Static image test (frame variance across time)
        diffs = []
        for i in range(len(frames) - 1):
            gray_a = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
            gray_b = cv2.cvtColor(frames[i+1], cv2.COLOR_BGR2GRAY)
            diff = cv2.absdiff(gray_a, gray_b)
            diffs.append(np.mean(diff))
            
        avg_motion = np.mean(diffs)
        if avg_motion < 2.5:
            return False, f"Static slide/screenshot detected (avg motion delta: {avg_motion:.2f})"

        # Check 2: Corner PiP Facecam Detector
        # Inspect bottom-right and bottom-left 25% quadrant
        h, w, _ = frames[1].shape
        for f in frames:
            br_corner = f[int(h*0.65):h, int(w*0.65):w]
            # Detect sharp circular or rectangular boundary box
            gray_corner = cv2.cvtColor(br_corner, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_corner, 100, 200)
            edge_density = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
            # If corner has high isolated edge box + high skin-tone saturation
            hsv = cv2.cvtColor(br_corner, cv2.COLOR_BGR2HSV)
            skin_mask = cv2.inRange(hsv, np.array([0, 20, 70]), np.array([25, 255, 255]))
            skin_ratio = np.sum(skin_mask > 0) / (skin_mask.shape[0] * skin_mask.shape[1])
            if edge_density > 0.08 and skin_ratio > 0.35:
                return False, "Picture-in-Picture Facecam / Streamer detected in corner"

        return True, "Passed purity gatekeeper"

    def detect_climax_offset(self, video_path: str):
        """
        Locates the climax / realization timestamp (where freeze and audio hook trigger).
        Uses motion spike followed by deceleration or steady action peak.
        """
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            return 60, 36
        
        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        prev_gray = None
        motion_profile = []
        step = max(1, int(fps / 10))
        
        frame_idx = 0
        while True:
            ret, frame = cap.read()
            if not ret or frame_idx > 300: # Scan up to 10 seconds
                break
            if frame_idx % step == 0:
                gray = cv2.cvtColor(cv2.resize(frame, (160, 90)), cv2.COLOR_BGR2GRAY)
                if prev_gray is not None:
                    delta = np.mean(cv2.absdiff(gray, prev_gray))
                    motion_profile.append((frame_idx, delta))
                prev_gray = gray
            frame_idx += 1
        cap.release()

        if not motion_profile:
            return 60, 36

        # Target climax window: between 35% and 75% of duration
        min_f = int(total_frames * 0.35)
        max_f = int(total_frames * 0.75)
        valid_points = [p for p in motion_profile if min_f <= p[0] <= max_f]
        
        if valid_points:
            best_point = max(valid_points, key=lambda x: x[1])
            climax_frame = best_point[0]
        else:
            climax_frame = int(total_frames * 0.50)

        freeze_duration = int(self.sub_config["audio_hook"].get("duration_seconds", 1.2) * 30)
        return climax_frame, freeze_duration

    def harvest_curated_clips(self, required_count=5):
        """Execute full 3-tier cascade to obtain verified raw clips."""
        # Step 1: Collect candidates
        candidates = self.tier1_search_youtube(max_candidates=15)
        if len(candidates) < required_count:
            golden = self.tier2_golden_candidates()
            candidates.extend(golden)

        verified_clips = []
        for c in candidates:
            print(f"\nEvaluating candidate {c['id']}: '{c['title']}'...")
            local_path = self.download_candidate(c["id"])
            if not local_path:
                print(f"  ❌ Download failed.")
                continue
            
            passed, reason = self.tier3_vision_gatekeeper(local_path)
            if not passed:
                print(f"  ❌ Rejected by Vision Gatekeeper: {reason}")
                continue
                
            print(f"  ✅ Approved: {reason}")
            climax_offset, freeze_duration = self.detect_climax_offset(local_path)
            
            verified_clips.append({
                "id": c["id"],
                "title": c["title"],
                "video_path": os.path.abspath(local_path),
                "duration_seconds": c.get("duration", 10.0),
                "climax_frame": climax_offset,
                "freeze_duration": freeze_duration
            })
            if len(verified_clips) >= required_count:
                break

        return verified_clips

    def export_hyperframes_timeline(self, clips, output_path="hyperframes_timeline.json"):
        """Exports the harvested clips into a fully-structured Hyperframes JSON timeline (no Remotion)."""
        blueprint_path = "src/pipeline/hyperframes_50_blueprints.json"
        base_blueprint = {}
        if os.path.exists(blueprint_path):
            with open(blueprint_path, "r", encoding="utf-8") as f:
                all_blueprints = json.load(f)
                base_blueprint = all_blueprints.get(self.sub_id, {})
        
        timeline = {
            "$schema": "https://hyperframes.org/v1/compilation.schema.json",
            "project": f"LevelZero0ne_{self.sub_id}",
            "engine": "Hyperframes",
            "version": "1.0.0",
            "canvas": {
                "width": 1080,
                "height": 1920,
                "fps": 30
            },
            "header": base_blueprint.get("header_layout", {
                "line1": self.sub_config["title_header"],
                "line2": self.sub_config["subject_header"],
                "line3": self.sub_config["version_tag"]
            }),
            "ladder": base_blueprint.get("countdown_ladder", {}),
            "camera": base_blueprint.get("dynamic_camera", {}),
            "punchline": base_blueprint.get("kinetic_punchline", {}),
            "audio": base_blueprint.get("audio_timeline", {}),
            "branding": base_blueprint.get("branding", {}),
            "clips": []
        }
        
        acc_frames = 0
        total_clips = len(clips)
        for i, c in enumerate(clips):
            dur_frames = int(c.get("duration_seconds", 5.0) * 30.0)
            rank = total_clips - i
            level = i + 1
            timeline["clips"].append({
                "rank": rank,
                "level": level,
                "start_frame": acc_frames,
                "duration_frames": dur_frames,
                "video_path": c["video_path"],
                "climax_frame": c.get("climax_frame", int(dur_frames * 0.55)),
                "freeze_duration_frames": c.get("freeze_duration", 36),
                "punchline_text": self.sub_config.get("typography", {}).get("punchline", "THIS IS THE END")
            })
            acc_frames += dur_frames
            
        timeline["total_frames"] = acc_frames + 75 # including 2.5s outro
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(timeline, f, indent=2)
            
        print(f"✅ Exported Hyperframes timeline to: {output_path}")
        return timeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Robust 50-Subcategory Harvester & Gatekeeper")
    parser.add_argument("--sub", default="people_accepting_fate", help="Subcategory ID")
    parser.add_argument("--count", type=int, default=5, help="Number of clips needed")
    parser.add_argument("--export-hyperframes", default="output/hyperframes_spec.json", help="Export Hyperframes schema")
    args = parser.parse_args()
    
    harvester = RobustSubcategoryHarvester(args.sub)
    clips = harvester.harvest_curated_clips(args.count)
    print(f"\nFinal harvest count: {len(clips)} verified clips ready.")
    if args.export_hyperframes and clips:
        harvester.export_hyperframes_timeline(clips, args.export_hyperframes)
