import os

skills_data = [
    {
        "id": "taunting_animals",
        "name": "TAUNTING ANIMALS",
        "niche": "instant_karma",
        "stem": "public/audio/stems/taunting_animals_music_bed.mp3",
        "genre": "Fast Funky Bass / Brazilian Phonk",
        "bpm": 125,
        "title": "Ranking Instant Karma for Taunting Animals",
        "version": "(Never Taunt Nature)",
        "hook_title": "Ranking Instant Karma for Taunting Animals 🐒⚡ #shorts #instantkarma #animals",
        "desc": "Ranking people who taunted animals and faced instant regret! Never disrespect wildlife! 🐆💥\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #instantkarma #animals #wildlife #fails #instantregret #monkey",
        "arc": "Human arrogantly teases/pokes an animal -> Animal snaps/counter-attacks with lightning speed -> Human panics, runs away, or gets humbled.",
        "ranks": [
            ("5", "Level 1", "Poking the Sleepy Goose", "Park walker tries to shoo and mock a nesting goose.", "Goose launches into flight, chasing him into a pond."),
            ("4", "Level 2", "Zoo Glass Taunter", "Tourist aggressively taps zoo glass at a gorilla.", "Silverback slams the glass with a thunderous crack, tourist falls backwards."),
            ("3", "Level 3", "Stealing From A Baboon", "Guy waves food in front of a monkey to make it dance.", "Baboon leaps onto his head, snatches his sunglasses and backpack."),
            ("2", "Level 4", "Kicking at a Street Stray Dog", "Street tough pretends to kick at a resting dog while laughing.", "Pack of 3 dogs emerge from the alley instantly barking and chasing him down the street."),
            ("1", "Level 5", "Taunting a Ram in Pasture", "Guy holds red cape to play bullfighter with a farm ram.", "Ram charges like a missile, sends him flying 10 feet into a mud puddle.")
        ]
    },
    {
        "id": "cocky_challengers",
        "name": "COCKY CHALLENGERS HUMBLED",
        "niche": "combat_bloopers",
        "stem": "public/audio/stems/cocky_challengers_music_bed.mp3",
        "genre": "Aggressive Phonk / Trap Anthem",
        "bpm": 135,
        "title": "Ranking Cocky Challengers Humbled",
        "version": "(Ego Checked Version)",
        "hook_title": "Ranking Cocky Challengers Getting Humbled 🥊⚡ #shorts #boxing #streetfighter",
        "desc": "Ranking the most arrogant challengers who got humbled in seconds! Never celebrate before the bell! 🥊💥\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #boxing #ufc #mma #instantkarma #humbled #streetfight",
        "arc": "Arrogant challenger taunts, drops guard, or sticks tongue out -> Opponent delivers a clean, decisive counter-strike -> Challenger crashes flat onto the mat or concedes in shock.",
        "ranks": [
            ("5", "Level 1", "Arm Wrestling Smirker", "Bodybuilder laughs and taunts a scrawny arm wrestler before starting.", "Scrawny arm wrestler pins his arm in 0.2 seconds flat with pro technique."),
            ("4", "Level 2", "Street Dance Battler Taunts", "Dancer does throat-slash gesture at shy opponent.", "Opponent drops into a flawless headspin and 540 kick, leaving crowd roaring."),
            ("3", "Level 3", "Sparring Partner Hands Down", "MMA fighter lowers both hands to chest and points to chin.", "Opponent delivers a crisp head kick; arrogant fighter stumbles into cage ropes."),
            ("2", "Level 4", "Street Hoops Ankle Breaker", "Defender claps hands in shooter's face talking trash.", "Shooter executes a nasty crossover, defender falls flat on hardwood as 3-pointer drains."),
            ("1", "Level 5", "Boxer Showboating Knockout", "Boxer starts shimmying and dancing with hands behind back.", "Opponent lands a clean right hook on the jaw, sending showboater straight to dreamland.")
        ]
    },
    {
        "id": "lightning_jump_scares",
        "name": "LIGHTNING JUMP SCARES",
        "niche": "nature_weather",
        "stem": "public/audio/stems/lightning_jump_scares_music_bed.mp3",
        "genre": "Ominous Dark Ambient / Thunder Drone",
        "bpm": 90,
        "title": "Ranking Insane Lightning Jump Scares",
        "version": "(Headphones Warning)",
        "hook_title": "Ranking Insane Lightning Jump Scares ⚡😱 #shorts #nature #storm",
        "desc": "Ranking the most terrifying lightning strikes caught on camera! That last strike was way too close! ⚡💥\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #lightning #thunderstorm #nature #scary #shocking #caughtoncamera",
        "arc": "Peaceful or stormy view outside window/porch -> Sudden blinding flash and ear-splitting thunderbolt strikes nearby tree/ground -> Camera drops and occupants scream in shock.",
        "ranks": [
            ("5", "Level 1", "Porch Rain Watching", "Subject filming peaceful summer shower from front porch.", "Bolt vaporizes a lamppost across the street with explosive spark shower."),
            ("4", "Level 2", "Balcony Coffee Strike", "Filming city skyline view while drinking morning coffee.", "Lightning hits skyscraper antenna 50 yards away; camera jolts and coffee spills."),
            ("3", "Level 3", "Backyard Palm Tree Explosion", "Filming rain hitting backyard pool in Florida.", "Bolt strikes palm tree directly by pool; bark explodes into wooden shrapnel."),
            ("2", "Level 4", "Highway Driving Direct Hit", "Dashcam cruising down empty interstate during cloudburst.", "Bolt strikes concrete median barrier 15 feet in front of hood; sparks shower windshield."),
            ("1", "Level 5", "Bedroom Window Ground Zero", "Guy casually filming lightning over city through glass window.", "Bolt hits the roof gutter 3 feet from his face; entire screen goes blinding white with deafening thunderclap.")
        ]
    },
    {
        "id": "bench_press_ego_fails",
        "name": "BENCH PRESS EGO FAILS",
        "niche": "gym_bloopers",
        "stem": "public/audio/stems/bench_press_ego_fails_music_bed.mp3",
        "genre": "Heavy Phonk / Bass Drop Groove",
        "bpm": 128,
        "title": "Ranking Worst Bench Press Ego Fails",
        "version": "(Bar Of Shame Edition)",
        "hook_title": "Ranking Worst Bench Press Ego Fails 💀🏋️ #shorts #gymfails #gym",
        "desc": "Ranking the most ridiculous gym ego lifts that ended in total embarrassment! Always use safety clips and a spotter! 🏋️💥\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #gym #gymfails #benchpress #egolifting #workout #fitnessfails",
        "arc": "Lifter loads absurd weight without warmup or spotter -> Unracks with shaking elbows -> Bar pins chest -> Forced to roll the bar of shame or tilt plates off.",
        "ranks": [
            ("5", "Level 1", "The Missing Clips Slide", "Lifter puts 3 plates on each side with no barbell collars.", "Lifter tilts 5 degrees left; all plates slide off sequentially with loud clatter."),
            ("4", "Level 2", "The Half-Inch Bounce Rep", "Guy loads 315lbs, unrolls wrist wraps, screams at mirror.", "Lowers bar 2 inches, bounces violently off sternum, gets stuck halfway up."),
            ("3", "Level 3", "The Feet-In-Air Wobble", "Lifter puts both feet up on the bench pad while lifting heavy.", "Loses balance completely, rolls sideways off the bench onto the rubber floor."),
            ("2", "Level 4", "The Silent Bar of Shame Roll", "Solo lifter gets pinned under 275lbs with nobody in the gym.", "Has to awkwardly roll the heavy barbell down ribs to hips and sit up gasping."),
            ("1", "Level 5", "The Pretend Warmup Attempt", "Guy walks in wearing jeans, loads 405lbs to impress girls nearby.", "Unracks the bar; gravity immediately drops it flat to chest, spotters rush in panic.")
        ]
    },
    {
        "id": "couple_pranks_gone_wholesome",
        "name": "COUPLE PRANKS GONE WHOLESOME",
        "niche": "wholesome_romance",
        "stem": "public/audio/stems/couple_pranks_gone_wholesome_music_bed.mp3",
        "genre": "Acoustic Pop / Playful Wholesome Strum",
        "bpm": 115,
        "title": "Ranking Couple Pranks Gone Wholesome",
        "version": "(Pure Chemistry Edition)",
        "hook_title": "Ranking Couple Pranks That Turned Wholesome 🥺❤️ #shorts #couplegoals #wholesome",
        "desc": "Ranking playful couple pranks that turned into the sweetest wholesome moments! True love right here! ❤️✨\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #couplegoals #wholesome #relationship #love #funnycouples #cute",
        "arc": "Partner sets up playful prank camera -> Target is momentarily confused or startled -> Prankster reveals sweet twist or hug -> Both collapse into adorable laughter and kisses.",
        "ranks": [
            ("5", "Level 1", "The Invisible String Tap", "Girl pretends to pull invisible string attached to boyfriend across room.", "Boyfriend plays along playfully, flying dramatically across couch into a hug."),
            ("4", "Level 2", "The Lip Balm Trick", "Girl applies lip balm and asks boyfriend if it smells weird.", "Boyfriend leans in to sniff; she kisses his cheek, leaving him blushing brightly."),
            ("3", "Level 3", "The Fake Spill on New Shoes", "Boyfriend drops empty coffee cup onto girlfriend's new white sneakers.", "Girl gasps in horror, realizes cup is empty, hits his chest playfully while laughing."),
            ("2", "Level 4", "The Serious Face Challenge", "Girl tries to hold deadpan serious eye contact without smiling.", "Boyfriend makes one tiny eyebrow twitch; she bursts into breathless giggles and buries face in his neck."),
            ("1", "Level 5", "The Fake Ring Box Candy Reveal", "Boyfriend bends down on one knee holding jewelry box; opens it to reveal favorite sour candy.", "Girl gasps, screams laughing, playfully shoves him, and hugs him tightly.")
        ]
    },
    {
        "id": "husband_wife_wholesome_surprises",
        "name": "HUSBAND WIFE WHOLESOME SURPRISES",
        "niche": "wholesome_romance",
        "stem": "public/audio/stems/husband_wife_wholesome_surprises_music_bed.mp3",
        "genre": "Warm Cinematic Strings / Acoustic Piano",
        "bpm": 95,
        "title": "Ranking Wholesome Husband & Wife Surprises",
        "version": "(Heartwarming Edition)",
        "hook_title": "Ranking Emotional Husband & Wife Surprises 🥹❤️ #shorts #wholesome #marriage",
        "desc": "Ranking the most heartwarming and emotional surprises between husbands and wives! True devotion! 🥺❤️\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #wholesome #husbandwife #marriagegoals #love #family #emotional",
        "arc": "Spouse brings unexpected gift/news into the room -> Target realizes what it is -> Emotional floodgates open with tears of happiness and warm embrace.",
        "ranks": [
            ("5", "Level 1", "Work Lunch Surprise Delivery", "Husband surprises wife at her busy clinic office with her favorite hot meal.", "Wife turns around, eyes light up with immense relief and joy, giving him a giant hug."),
            ("4", "Level 2", "Dream Car Paid Off Note", "Wife hands husband a keychain envelope showing the mortgage/truck is 100% paid off.", "Husband stares in disbelief, breaks into tears, wraps his arms around her."),
            ("3", "Level 3", "Surprise Golden Retriever Puppy", "Husband brings cardboard box into living room; golden retriever puppy pokes head out.", "Wife drops to her knees sobbing tears of pure happiness cradling the puppy."),
            ("2", "Level 4", "Pregnancy Test Reveal in Coffee Mug", "Wife writes 'You are going to be a daddy' at the bottom of husband's morning coffee mug.", "Husband finishes coffee, reads message, freezes with shaking hands and weeps with joy."),
            ("1", "Level 5", "25-Year Vow Renewal Surprise Trip", "Husband hands wife tickets to Italy to renew their vows at the exact spot they first met.", "Wife covers her mouth in complete emotional shock, weeping into his chest as kids celebrate around them.")
        ]
    },
    {
        "id": "love_at_first_sight_caught",
        "name": "LOVE AT FIRST SIGHT CAUGHT ON CAMERA",
        "niche": "wholesome_romance",
        "stem": "public/audio/stems/love_at_first_sight_caught_music_bed.mp3",
        "genre": "Dreamy Lo-Fi / Romantic Soul Groove",
        "bpm": 105,
        "title": "Ranking Love At First Sight Caught On Camera",
        "version": "(Pure Chemistry Sparks)",
        "hook_title": "Ranking Love At First Sight Moments Caught On Camera 🥹✨ #shorts #romance #love",
        "desc": "Ranking moments where two strangers locked eyes and felt instant undeniable chemistry! Destiny caught on tape! ✨❤️\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #loveatfirstsight #romance #wholesome #destiny #chemistry #strangers",
        "arc": "Two strangers in public environment (subway, crosswalk, sporting event) -> Unplanned eye contact locks -> Both smile warmly and start an authentic conversation.",
        "ranks": [
            ("5", "Level 1", "Subway Train Door Eye Contact", "Guy on platform locks eyes with girl inside subway car right before doors close.", "Both smile shyly; guy types his number on phone screen and presses it to the window."),
            ("4", "Level 2", "Coffee Shop Accidental Cup Swap", "Two strangers reach for the same latte at pickup counter simultaneously.", "Hands touch; both look up and lock eyes with genuine blush and warm laughter."),
            ("3", "Level 3", "Marathon Water Station Spark", "Runner grabs water cup from volunteer; their hands linger for a split second.", "Runner stops, turns around, smiles, and asks for her name before continuing race."),
            ("2", "Level 4", "Concert Crowd Shoulder Glance", "Camera at outdoor festival captures two people dancing near each other.", "Both turn around at the same beat drop, lock eyes, and burst into synchronized dancing together."),
            ("1", "Level 5", "Baseball Kiss Cam Strangers", "Jumbotron kiss cam lands on two strangers sitting adjacent who don't know each other.", "Both look around nervously, guy asks permission, girl smiles and nods, and they share a magical movie-like kiss as stadium roars.")
        ]
    },
    {
        "id": "accidental_trickshots",
        "name": "ACCIDENTAL TRICKSHOTS",
        "niche": "extreme_luck",
        "stem": "public/audio/stems/accidental_trickshots_music_bed.mp3",
        "genre": "High-Energy Upbeat Phonk / Electronic Beat",
        "bpm": 130,
        "title": "Ranking Unbelievable Accidental Trickshots",
        "version": "(Zero Skill Pure Luck)",
        "hook_title": "Ranking Accidental Trickshots That Defied Physics 🤯🎱 #shorts #viral #amazing",
        "desc": "Ranking the luckiest accidental trickshots in history! That 1 in a billion bounce at Level 5 is impossible! 🎱💥\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #trickshot #luck #physics #impossible #clutch #satisfying #sports",
        "arc": "Subject drops or tosses an object carelessly -> Object takes multiple improbable bounces off furniture/walls -> Lands perfectly in target with zero intentional effort.",
        "ranks": [
            ("5", "Level 1", "Desk Pen Kick Into Holder", "Student drops pen off desk, reflex-kicks it with shoe.", "Pen arcs 10 feet across classroom and drops tip-down straight into teacher's pen cup."),
            ("4", "Level 2", "Kitchen Spatula Fumble", "Cook flips burger and loses grip on spatula.", "Spatula flips 3 times in air, bounces off frying pan handle, lands standing upright on counter rack."),
            ("3", "Level 3", "Basketball Full-Court Backward Toss", "Gym teacher tosses ball backward over shoulder while cleaning up.", "Ball flies 94 feet across court, hits backboard, swishes through net clean."),
            ("2", "Level 4", "Golf Ball Pool Bounce Hole-in-One", "Golfer hits severe slice into backyard swimming pool.", "Ball skips across pool surface twice, ricochets off patio umbrella pole, rolls into cup on green."),
            ("1", "Level 5", "Ping Pong Triple Ricochet Cup Swish", "Player hits wild smash off table; opponent dodges in panic.", "Ball bounces off camera tripod, off ceiling light fixture, off water bottle, and lands inside red solo cup across the room.")
        ]
    },
    {
        "id": "commercial_kitchen_nightmares",
        "name": "COMMERCIAL KITCHEN NIGHTMARES",
        "niche": "workplace_disasters",
        "stem": "public/audio/stems/commercial_kitchen_nightmares_music_bed.mp3",
        "genre": "Comedic High-Tempo Kitchen March / Foley",
        "bpm": 120,
        "title": "Ranking Commercial Kitchen Nightmares",
        "version": "(Worst Shift Edition)",
        "hook_title": "Ranking Commercial Kitchen Fails & Disasters 😱🍳 #shorts #restaurant #cheflife",
        "desc": "Ranking the most disastrous commercial kitchen fails caught on CCTV! The clean up at Level 5 took 3 days! 🍳💥\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #kitchen #chef #restaurant #disaster #fails #workplace #cheflife",
        "arc": "Busy line cook or dishwasher carrying heavy equipment/ingredients -> Foot slips on grease or shelf fails -> Massive mess of soup, sauce, or flour coats the entire floor.",
        "ranks": [
            ("5", "Level 1", "The 50lb Flour Bag Drop", "Baker lifts 50lb sack of white flour to top shelf.", "Sack tears down middle; dense white cloud covers chef and entire bakery station."),
            ("4", "Level 2", "Fryer Oil Splash Slip", "Line cook carrying tray of fries slips on wet floor near prep table.", "Fries fly across kitchen like fireworks, chef lands on rear but safely misses fryer."),
            ("3", "Level 3", "Dish Pit Tray Tower Avalanche", "Dishwasher stacks 30 plastic tray racks onto a rolling dolly.", "Dolly wheel catches drain grate; entire 8-foot tower cascades into soapy sink pit."),
            ("2", "Level 4", "The 20-Gallon Ranch Dressing Slip", "Prep cook carrying giant industrial vat of ranch dressing across tile floor.", "Steps on slick spot, slips horizontal; 20 gallons of white dressing coats entire walk-in hallway."),
            ("1", "Level 5", "The 100-Gallon Marinara Tsunami", "Kitchen staff moving giant heated steel kettle of red pasta sauce.", "Caster wheel snaps off; 100 gallons of boiling red sauce floods entire dining room entrance in a red wave.")
        ]
    },
    {
        "id": "left_hanging_public",
        "name": "LEFT HANGING IN PUBLIC",
        "niche": "human_fails",
        "stem": "public/audio/stems/left_hanging_public_music_bed.mp3",
        "genre": "Dry Comedic Funk / Quirk Beat",
        "bpm": 110,
        "title": "Ranking Worst Left Hanging Moments",
        "version": "(Secondhand Cringe)",
        "hook_title": "Ranking The Worst Left Hanging Moments Ever 💀✋ #shorts #cringe #awkward",
        "desc": "Ranking people who got left hanging on live television! The second-hand embarrassment is off the charts! 💀✋\n\nAll footages used in this video are not mine; full credit goes to the respective owners.\n\n#shorts #viral #lefthanging #awkward #cringe #funny #handshake #fails #instantregret",
        "arc": "Person extends hand for high-five/fist bump with huge smile -> Other person looks away or ignores -> Person awkwardly covers by fixing hair or stretching.",
        "ranks": [
            ("5", "Level 1", "Sideline High-Five Ghost", "Fan in front row reaches out palm as NBA player walks by.", "Player looks dead ahead, ignores hand; fan slowly turns hand into a wave."),
            ("4", "Level 2", "Press Conference Fist Bump", "Journalist raises fist bump to coach after interview.", "Coach looks at fist with confused grimace, grabs his microphone instead."),
            ("3", "Level 3", "World Leaders Double Handshake Fail", "President extends open hand for photo op on world stage.", "Other prime minister looks down, misses hand, turns away to wave at crowd."),
            ("2", "Level 4", "Live TV Broadcast Handshake to Hug", "News anchor goes for handshake; co-host goes for hug.", "Face collides into shoulder, hands flail awkwardly for 4 painful seconds on live air."),
            ("1", "Level 5", "Award Ceremony Stage Walk-Off", "Celebrity walks onto Oscar/Grammy stage and offers high-five to presenter.", "Presenter completely walks past him; celebrity awkwardly smooths hair and looks at floor.")
        ]
    }
]

template = """---
sub_category_id: {id}
sub_category_name: {name}
niche: {niche}
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: {stem}
audio_stem_bpm: {bpm}
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `{id}` ("{name}")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip must follow the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"{name}"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** {arc}
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `{name}` (`#FF2D55`)
  - Line 3: `{version}` (`#00D2FF`)
- **Color Progression Ladder:**
  - Rank 5 [Level 1]: `#FF2D55`
  - Rank 4 [Level 2]: `#00D2FF`
  - Rank 3 [Level 3]: `#FFEB3B`
  - Rank 2 [Level 4]: `#FFFFFF`
  - Rank 1 [Level 5]: `#FFFFFF` (Climax Finale)
- **Subtitles:** Strictly disabled (`showSubtitles: false`).
- **Watermark & Outro:** Circular `LevelZero0ne` watermark + 75-frame Earshot sonic brand outro (`public/audio/earshot_sonic_brand.mp3`).

---

## 3. Anti-Stuttering Pipeline Protocol
- **Compositor Engine:** Remotion `<OffthreadVideo>` in `src/remotion/MrPurifiedWaterShort.tsx`.
- **Pre-Processing Command:** Strict 30fps CFR re-encode with dense `-g 15` keyframe interval:
  ```bash
  ffmpeg -y -i raw_input.mp4 -vf "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -c:a aac -ar 48000 -b:a 320k normalized_clip.mp4
  ```

---

## 4. Audio Stem & Music Bed Design
- **Track Genre:** {genre}
- **Stem File:** `{stem}`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction |
| :---: | :---: | :--- | :--- | :--- |
{ranks_table}

---

## 6. QA Verification Gate
- [ ] 0 black frames detected in 1fps contact sheet.
- [ ] 0 third-party watermarks or channel repost logos.
- [ ] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [ ] True Peak: `<= -1.5 dBTP`.
- [ ] Contact sheet: `output/{id}_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `{hook_title}`
- **Description:**
  ```text
{desc}
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
"""

for item in skills_data:
    ranks_lines = []
    for r, lvl, arc, cause, payoff in item["ranks"]:
        ranks_lines.append(f"| **{r}** | {lvl} | **{arc}** | {cause} | {payoff} |")
    ranks_table = "\n".join(ranks_lines)
    
    content = template.format(
        id=item["id"],
        name=item["name"],
        niche=item["niche"],
        stem=item["stem"],
        genre=item["genre"],
        bpm=item["bpm"],
        version=item["version"],
        hook_title=item["hook_title"],
        desc=item["desc"],
        arc=item["arc"],
        ranks_table=ranks_table
    )
    
    out_path = os.path.join("subcategory_skills", f"{item['id']}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created detailed skill: {out_path} ({len(content)} bytes)")
