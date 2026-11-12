import os
import sys
import json
import argparse
import subprocess
import glob

REGISTRY_PATH = "src/pipeline/master_category_registry.json"

def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        raise FileNotFoundError(f"Registry not found at {REGISTRY_PATH}")
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return res.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        return None

def harvest_sub_category(sub_id, output_dir="temp_harvest"):
    reg = load_registry()
    sub_config = reg["subcategories"].get(sub_id)
    if not sub_config:
        print(f"Unknown subcategory: '{sub_id}'. Available: {list(reg['subcategories'].keys())[:10]}...")
        return False
    
    print(f"\n==========================================")
    print(f"🚀 SUB-CATEGORY HARVESTER LOGIC GATE")
    print(f"Subcategory: {sub_config['name']} ({sub_id})")
    print(f"Header: {sub_config['title_header']} {sub_config['subject_header']} {sub_config['version_tag']}")
    print(f"Audio Hook: {sub_config['audio_hook']['stem']}")
    print(f"==========================================\n")
    
    os.makedirs(output_dir, exist_ok=True)
    python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
    
    queries = sub_config["harvester"]["primary_queries"]
    universal_negatives = reg.get("universal_negative_filters", [])
    
    candidate_urls = []
    
    for q in queries:
        print(f"Searching query: '{q}'...")
        search_str = f"ytsearch6:{q}"
        cmd = [
            python_exe, "-m", "yt_dlp",
            "--print", "%(id)s | %(title)s | %(duration)s",
            search_str
        ]
        out = run_cmd(cmd)
        if out:
            for line in out.strip().split("\n"):
                if "|" in line:
                    parts = [p.strip() for p in line.split("|")]
                    vid_id = parts[0]
                    title = parts[1] if len(parts) > 1 else ""
                    dur = float(parts[2]) if len(parts) > 2 and parts[2] != "NA" else 15.0
                    
                    # Filter out negatives
                    title_lower = title.lower()
                    if any(neg in title_lower for neg in universal_negatives):
                        print(f"  ❌ Filtered out negative keyword: {title}")
                        continue
                    if dur < 3.0 or dur > 60.0:
                        continue
                        
                    candidate_urls.append({"id": vid_id, "title": title, "duration": dur})
                    if len(candidate_urls) >= 10:
                        break
        if len(candidate_urls) >= 10:
            break
            
    print(f"\nDiscovered {len(candidate_urls)} candidate raw clips.")
    return candidate_urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strict Sub-Category Harvester & Gatekeeper")
    parser.add_argument("--sub", default="people_accepting_fate", help="Subcategory ID")
    args = parser.parse_args()
    
    harvest_sub_category(args.sub)
