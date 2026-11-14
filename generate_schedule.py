import os
import json
import datetime
import random
from collections import defaultdict

# 1. Load category registry
with open("src/pipeline/master_category_registry.json", "r", encoding="utf-8") as f:
    registry = json.load(f)["subcategories"]

# 2. Get exact list of mastered video files physically present in output/
output_files = [f for f in os.listdir("output") if f.endswith("_mastered.mp4")]
print(f"Found {len(output_files)} mastered video files in output directory.")

# 3. High-velocity viral keywords per niche
niche_keywords = {
    "human_fails": {
        "title_hooks": [
            "When Overconfidence Backfires Instantly",
            "People Realizing They Made A Huge Mistake",
            "Ranking Moments People Regretted Instantly",
            "The Most Painful Instant Regret Moments",
            "Proof That Gravity Never Loses",
            "When Showing Off Goes Terribly Wrong"
        ],
        "niche_tags": ["#fails", "#instantregret", "#funny", "#karma", "#failarmy", "#caughtoncamera"],
        "cross_trending": ["#gaming", "#gta6", "#anime", "#relatable", "#memes", "#storytime", "#streamer", "#podcast", "#satisfying"]
    },
    "instant_karma": {
        "title_hooks": [
            "When Instant Karma Strikes Back Immediately",
            "The Most Satisfying Instant Karma Moments",
            "Cocky People Getting Humbled Instantly",
            "Ranking Instant Karma Justice In Public",
            "When Bullying Someone Backfires Instantly",
            "Instant Regret Caught Live On Camera"
        ],
        "niche_tags": ["#instantkarma", "#justice", "#satisfying", "#karma", "#roadrage", "#humbled"],
        "cross_trending": ["#mrbeast", "#speed", "#fyp", "#twitch", "#storytime", "#reaction", "#viralvideo", "#foryou"]
    },
    "funny_animals": {
        "title_hooks": [
            "Animals Caught Being Absolute Chaos",
            "Pets Caught Doing Hilarious Things",
            "The Funniest Animal Moments Ever Caught",
            "Ranking The Silliest Dogs And Cats",
            "Animals Looking Suspiciously Unhinged",
            "When Pets Forget How To Animal"
        ],
        "niche_tags": ["#funnyanimals", "#pets", "#dogsoftiktok", "#catsoftiktok", "#cuteanimals", "#animalmemes"],
        "cross_trending": ["#asmr", "#satisfying", "#cozy", "#wholesome", "#dailyvlog", "#gaming", "#reaction", "#trending"]
    },
    "nature_weather": {
        "title_hooks": [
            "Nature Reminding Us Who Is Really In Charge",
            "Terrifying Weather Moments Caught On Camera",
            "The Most Shocking Nature Close Calls",
            "When Severe Weather Strikes Without Warning",
            "Ranking The Craziest Mother Nature Moments",
            "Incredible Moments Before Severe Impact"
        ],
        "niche_tags": ["#nature", "#weather", "#tornado", "#tsunami", "#stormchaser", "#caughtoncamera"],
        "cross_trending": ["#documentary", "#scary", "#science", "#travel", "#explore", "#fyp", "#trendingnow", "#reels"]
    },
    "aura_debt": {
        "title_hooks": [
            "Moments That Lost 1,000,000 Aura Instantly",
            "Trying To Look Cool And Losing All Aura",
            "The Most Embarrassing Aura Loss Moments",
            "Ranking The Worst Aura Debt Ever Recorded",
            "Bro Really Thought He Looked Majestic",
            "When The Swagger Completely Evaporates"
        ],
        "niche_tags": ["#aura", "#auraloss", "#cringe", "#relatable", "#embarrassing", "#brainrot", "#sigmamale"],
        "cross_trending": ["#skibidi", "#roblox", "#fortnite", "#speed", "#kai", "#caseoh", "#streamer", "#tiktok"]
    },
    "sports_bloopers": {
        "title_hooks": [
            "Athletes Celebrating Way Too Early",
            "The Most Unbelievable Sports Bloopers Ever",
            "When Showing Off In Sports Goes Terribly Wrong",
            "Ranking Craziest Referee Collisions In Sports",
            "Goalkeeper Brainfades That Cost The Entire Game",
            "Unbelievable Sports Fails Caught In 4K"
        ],
        "niche_tags": ["#sports", "#football", "#soccer", "#nba", "#basketball", "#sportsbloopers", "#espn"],
        "cross_trending": ["#ronaldo", "#messi", "#lebroon", "#highlights", "#fifa", "#uefa", "#superbowl", "#viral"]
    },
    "npc_glitches": {
        "title_hooks": [
            "Proof That We Are Living In A Video Game Simulation",
            "The Most Uncanny Real-Life NPC Glitches",
            "People Caught Glitching In Real Life",
            "Ranking Real-Life Matrix Glitches Caught On Tape",
            "When The Physics Engine Forgets To Load",
            "NPC Dialogue Loops Caught In Real Life"
        ],
        "niche_tags": ["#npc", "#matrixglitch", "#simulation", "#glitchinthematrix", "#videogames", "#npcglitch"],
        "cross_trending": ["#gta6", "#cyberpunk", "#backrooms", "#liminalspaces", "#creepy", "#conspiracy", "#funny", "#tiktok"]
    },
    "workplace_disasters": {
        "title_hooks": [
            "Having The Worst Shift Of Your Entire Life",
            "The Most Expensive Workplace Disasters Ever",
            "When One Little Mistake Destroys The Entire Store",
            "Ranking Catastrophic Forklift Domino Collapses",
            "Commercial Kitchen Nightmares That Escalated Instantly",
            "Retail Disasters That Cost Millions"
        ],
        "niche_tags": ["#workplace", "#fail", "#domino", "#forkliftfail", "#disaster", "#joblife", "#expensive"],
        "cross_trending": ["#relatable", "#workmemes", "#storytime", "#9to5", "#retailproblems", "#fyp", "#trending"]
    },
    "extreme_luck": {
        "title_hooks": [
            "People Who Used All Their Luck For The Rest Of Their Life",
            "Miracle Saves That Defied The Laws Of Physics",
            "Accidental Trickshots Nobody Will Ever Believe",
            "The Luckiest People Ever Caught On Camera",
            "Ranking Insane Reflex Catches That Saved Lives",
            "Vehicle 360 Recoveries That Defied Death"
        ],
        "niche_tags": ["#luck", "#miracle", "#satisfying", "#reflexes", "#dadreflexes", "#nevertellmetheodds"],
        "cross_trending": ["#dudeperfect", "#mindblown", "#insane", "#epic", "#omg", "#viralshorts", "#explorepage"]
    },
    "gym_bloopers": {
        "title_hooks": [
            "Ego Lifting Gone Completely Wrong",
            "The Funniest Gym Equipment Misuse Moments",
            "When The Spotter Looks Away At The Worst Second",
            "Ranking The Most Catastrophic Squat Rack Fails",
            "Gym Fails That Will Make You Rethink Going Heavy",
            "Bench Press Disasters That Stunned Everyone"
        ],
        "niche_tags": ["#gym", "#fitness", "#gymfails", "#egolifting", "#workout", "#gymbro", "#bodybuilding"],
        "cross_trending": ["#gymtok", "#tren", "#motivation", "#cbum", "#powerlifting", "#relatable", "#fitnessmeme"]
    },
    "wholesome_romance": {
        "title_hooks": [
            "Confessing To Your Crush And Getting This Reaction",
            "The Most Emotional Unexpected Proposals Caught On Tape",
            "Public Love Confessions That Actually Worked",
            "Cute First Date Moments That Melted The Internet",
            "Long Distance Reunions That Will Make You Tear Up",
            "Couple Surprises That Restored Faith In Love"
        ],
        "niche_tags": ["#wholesome", "#love", "#couplegoals", "#proposal", "#relationship", "#romance", "#firstdate"],
        "cross_trending": ["#taylorswift", "#cute", "#tearjerker", "#storytime", "#pov", "#grwm", "#vlog", "#foryou"]
    }
}

# 4. Map each output file to its metadata
video_items = []
for fname in sorted(output_files):
    sub_id = fname.replace("_mastered.mp4", "")
    info = registry.get(sub_id, {
        "name": sub_id.replace("_", " ").title(),
        "niche": "human_fails",
        "description": "Viral compilation video"
    })
    niche = info.get("niche", "human_fails")
    video_items.append({
        "filename": fname,
        "sub_category_id": sub_id,
        "display_name": info.get("name", sub_id.replace("_", " ").title()),
        "niche": niche
    })

# 5. Intelligent randomization: Interleave niches so consecutive days have distinct genres
niche_buckets = defaultdict(list)
for item in video_items:
    niche_buckets[item["niche"]].append(item)

# Deterministic seed for reproducible balanced shuffling
rng = random.Random(42)
for niche in niche_buckets:
    rng.shuffle(niche_buckets[niche])

randomized_schedule_items = []
all_niches = list(niche_buckets.keys())
rng.shuffle(all_niches)

while any(len(b) > 0 for b in niche_buckets.values()):
    for niche in list(all_niches):
        if niche_buckets[niche]:
            if randomized_schedule_items and randomized_schedule_items[-1]["niche"] == niche:
                alt_niches = [n for n in all_niches if n != niche and len(niche_buckets[n]) > 0]
                if alt_niches:
                    pick_niche = alt_niches[0]
                    randomized_schedule_items.append(niche_buckets[pick_niche].pop(0))
                    continue
            randomized_schedule_items.append(niche_buckets[niche].pop(0))

print(f"Randomized schedule successfully generated with {len(randomized_schedule_items)} items.")

# 6. Build the master publishing schedule starting from November 25, 2026 onwards
start_date = datetime.date(2026, 11, 25)
master_schedule = []

for idx, item in enumerate(randomized_schedule_items):
    post_date = start_date + datetime.timedelta(days=idx)
    niche = item["niche"]
    data = niche_keywords.get(niche, niche_keywords["human_fails"])
    
    title_hook = data["title_hooks"][idx % len(data["title_hooks"])]
    clean_title = f"{title_hook} 😱 #shorts"
    
    niche_tags = data["niche_tags"]
    cross_tags = data["cross_trending"]
    
    description = (
        f"{title_hook}! Level 1 to Level 5 ranking compilation of the most unforgettable moments caught on camera.\n\n"
        f"Which rank was the craziest? Rate it in the comments below! 👇\n\n"
        f"DISCLAIMER & CREDIT:\n"
        f"All footages used in this video are not mine; full credit goes to the respective original owners and creators.\n"
        f"If you are the content owner and have any inquiries or wish for removal/attribution, please contact us directly.\n\n"
        f"TAGS:\n"
        f"{' '.join(niche_tags)} #shorts #viral #compilation #ranking #trending\n\n"
        f"TRENDING EXPLORE TAGS:\n"
        f"{' '.join(cross_tags)} #fyp #algorithm #popular #explore"
    )
    
    entry = {
        "day_number": idx + 1,
        "publish_date": post_date.strftime("%Y-%m-%d"),
        "publish_day": post_date.strftime("%A"),
        "video_file": f"output/{item['filename']}",
        "sub_category_id": item["sub_category_id"],
        "display_name": item["display_name"],
        "niche": niche,
        "recommended_post_time_ist": "18:30 IST (Prime evening mobile peak)",
        "recommended_post_time_est": "08:00 EST (US morning commute)",
        "title": clean_title,
        "description": description,
        "focused_hashtags": niche_tags + ["#shorts", "#viral", "#ranking"],
        "unrelated_trending_tags": cross_tags,
        "credit_disclaimer": "All footages used in this video are not mine; full credit goes to the respective owners."
    }
    master_schedule.append(entry)

# Write to MASTER_60_DAY_YOUTUBE_SCHEDULE.json
with open("MASTER_60_DAY_YOUTUBE_SCHEDULE.json", "w", encoding="utf-8") as f:
    json.dump(master_schedule, f, indent=2)

print(f"Saved {len(master_schedule)} scheduled videos to MASTER_60_DAY_YOUTUBE_SCHEDULE.json")
