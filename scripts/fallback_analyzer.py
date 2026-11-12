import json
import os
import re
import sys

# ==============================================================================
# MASTER TWO-TIER LEXICON TAXONOMY: ALL 10 NICHES & 50 SUBCATEGORIES
# ==============================================================================
NICHE_LEXICONS = {
    # --- NICHE 1: HUMAN FAILS ---
    "people_accepting_fate": {
        "subjects": ["person", "guy", "man", "woman", "he", "she", "worker", "student", "driver"],
        "actions": ["accepting fate", "gave up", "giving up", "frozen", "freeze", "resigned", "defeat", "surrender", "stare", "he knew", "hopeless"],
        "phrases": ["accepting fate", "accepted his fate", "he knew he messed up", "moment of acceptance", "zero will to live"],
        "negative": ["gaming", "animation", "cgi", "tutorial", "podcast"],
        "community_markers": ["he knew", "rip", "accepted his fate", "priceless", "defeat", "gave up", "frozen"],
        "default_incident": "clumsy_action",
        "punchlines": ["THIS IS THE END", "FATE ACCEPTED", "ZERO WILL TO RESIST", "DEFEAT CONCEDED", "HE KNEW IMMEDIATELY"]
    },
    "clumsy_stumbles": {
        "subjects": ["person", "guy", "girl", "walker", "pedestrian", "waiter", "model", "runner"],
        "actions": ["trip", "tripped", "slip", "slipped", "stumble", "stumbled", "fall", "fell", "balance", "tumble", "faceplant", "wiped out"],
        "phrases": ["clumsy fail", "lost balance", "slip and fall", "faceplant", "wipeout of the century"],
        "negative": ["serious injury", "hospital", "gaming", "cgi", "ambulance"],
        "community_markers": ["gravity undefeated", "shoes came off", "walk it off", "smooth recovery", "physics", "slippery"],
        "default_incident": "physical_fall",
        "punchlines": ["GRAVITY WINS", "SHOES CAME OFF", "ATTEMPTED RECOVERY", "PHYSICS 1 - HUMAN 0", "CLEAN FACEPLANT"]
    },
    "diy_disasters": {
        "subjects": ["diy", "home repair", "drywall", "pipe", "plumbing", "hammer", "drill", "shelf", "remodel", "ceiling", "tile", "wall", "furniture"],
        "actions": ["collapse", "collapsed", "leak", "flood", "break", "broke", "shatter", "fail", "failed", "crack", "ruin", "fall apart"],
        "phrases": ["diy fail", "home repair disaster", "landlord special", "diy gone wrong", "shelf collapsed"],
        "negative": ["professional tutorial", "commercial", "podcast", "advertisement"],
        "community_markers": ["call a professional", "landlord special", "drywall gone", "flex tape", "rip deposit", "structural damage"],
        "default_incident": "equipment_failure",
        "punchlines": ["CALL A PROFESSIONAL", "MEASURED ONCE CUT WRONG", "LANDLORD SPECIAL", "STRUCTURAL FAILURE", "REPAIR FAILED SUCCESSFULLY"]
    },
    "miscalculated_jumps": {
        "subjects": ["jump", "leap", "hop", "parkour", "gap", "fence", "roof", "ledge", "wall", "pool", "creek", "table"],
        "actions": ["miscalculate", "miscalculated", "undershot", "short", "overjump", "slip", "fall", "missed", "drop", "failed jump"],
        "phrases": ["miscalculated jump", "parkour fail", "jump fail", "didn't make it", "jump gone wrong"],
        "negative": ["gymnastics pro", "olympics", "full extreme sports movie"],
        "community_markers": ["math was not mathing", "miscalculated", "gravity won", "rip knees", "didn't make it", "short"],
        "default_incident": "physical_fall",
        "punchlines": ["MATH WAS NOT DONE", "PHYSICS WAS NOT CONSULTED", "GRAVITY DISAGREES", "SHORT BY MILES", "PARKOUR CANCELLED"]
    },
    "everyday_malfunctions": {
        "subjects": ["blender", "microwave", "chair", "door", "umbrella", "toaster", "vacuum", "can opener", "faucet", "printer", "soda"],
        "actions": ["malfunction", "explode", "break", "broke", "spill", "snap", "stuck", "burst", "collapse", "fail"],
        "phrases": ["everyday fail", "chair broke", "blender exploded", "appliance fail", "monday mood"],
        "negative": ["advertisement", "review", "podcast", "commercial"],
        "community_markers": ["monday mood", "hate when this happens", "curse of monday", "daily struggle", "broken", "why me"],
        "default_incident": "equipment_failure",
        "punchlines": ["MONDAY MOOD", "OBJECTS WITH THREATENING AURAS", "WHY DOES THIS EXIST", "DAILY MALFUNCTION", "BETRAYED BY APPLIANCES"]
    },

    # --- NICHE 2: INSTANT KARMA ---
    "pranks_backfiring": {
        "subjects": ["prank", "prankster", "scare", "joke", "trick", "setup"],
        "actions": ["backfire", "backfired", "caught", "thwarted", "countered", "punched", "regret", "karma", "reverse", "failed prank"],
        "phrases": ["prank backfires", "prank gone wrong", "prankster gets caught", "instant karma prank", "prank backfired"],
        "negative": ["scripted", "stage", "gaming", "cgi", "actors"],
        "community_markers": ["deserved", "don't prank", "got him back", "instant karma", "instant regret", "prank gone wrong"],
        "default_incident": "prank_backfire",
        "punchlines": ["PLAN WAS NOT THOUGHT OUT", "PRANKSTER GETS PRANKED", "INSTANT KARMA DELIVERED", "REVERSE CARD PLAYED", "CHECKMATE PRANKSTER"]
    },
    "road_rage_regret": {
        "subjects": ["driver", "car", "truck", "dashcam", "road rage", "tailgater", "highway", "traffic", "suv", "vehicle"],
        "actions": ["karma", "instant karma", "brake check", "flipped", "crashed", "rammed", "cut off", "arrested", "police chase", "retaliation"],
        "phrases": ["road rage instant karma", "road rage car flips", "instant justice road rage", "brake check fail", "road rage regret"],
        "negative": ["fatal crash", "gore", "news report", "gta", "beamng", "forza"],
        "community_markers": ["deserved", "instant karma", "satisfying", "dashcam never lies", "police showed up", "rammed", "brakes"],
        "default_incident": "car_crash",
        "punchlines": ["BRO FORGOT HOW BRAKES WORK", "POLICE ENTERED THE CHAT", "KARMA CAUGHT UP FAST", "INSTANT REGRET ACTIVATED", "WHEN EGO MEETS CONCRETE"]
    },
    "taunting_gone_wrong": {
        "subjects": ["opponent", "fighter", "boxer", "player", "athlete", "taunter", "rival"],
        "actions": ["taunt", "taunting", "showboating", "flexing", "knocked out", "dropped", "humiliated", "humbled", "countered", "karma"],
        "phrases": ["taunting gone wrong", "showboating fail", "taunt to get bodied", "premature flex", "humbled instantly"],
        "negative": ["ufc official full fight", "boxing documentary"],
        "community_markers": ["too cocky", "humiliated", "sit down", "bro was humbled", "stay humble", "karma"],
        "default_incident": "instant_karma",
        "punchlines": ["TOO EARLY TO CELEBRATE", "HUMBLING OF THE CENTURY", "SIT DOWN AND BE HUMBLE", "FLEX REVERSED", "SHOWBOATING GONE WRONG"]
    },
    "cutting_in_line": {
        "subjects": ["line", "queue", "line cutter", "customer", "karen", "airport line", "traffic line", "drive thru"],
        "actions": ["cut", "cutting", "bypass", "blocked", "stopped", "ejected", "denied", "pushed back", "confronted"],
        "phrases": ["cutting in line", "line cutter instant karma", "cutting line denied", "queue justice", "line cutter gets blocked"],
        "negative": ["movie clip", "animation", "commercial"],
        "community_markers": ["justice", "satisfying", "back of the line", "entitled", "blocked", "karen"],
        "default_incident": "verbal_argument",
        "punchlines": ["NICE TRY", "BACK OF THE LINE", "ENTITLEMENT DENIED", "QUEUE JUSTICE", "BLOCKED AT THE GATE"]
    },
    "smug_celebrations": {
        "subjects": ["runner", "cyclist", "player", "driver", "racer", "team", "celebration", "athlete", "marathon", "sprinter"],
        "actions": ["celebrate", "celebrates", "celebrated", "celebrating", "premature", "early", "dropped ball", "stole victory", "lost at line", "overtaken", "choked", "beaten", "loses", "lost", "passed"],
        "phrases": ["celebrated too early", "celebrates too early", "celebrating too early", "premature celebration", "dropped the ball", "lost at the finish line", "early celebration fail", "celebrates early"],
        "negative": ["fifa official", "esports broadcast"],
        "community_markers": ["celebrated too early", "bro choked", "dropped the ball", "tragic", "embarrassing", "stolen"],
        "default_incident": "instant_karma",
        "punchlines": ["DON'T CELEBRATE YET", "CHOKED AT THE FINISH", "PREMATURE TRIUMPH", "STOLEN AT THE LINE", "CELEBRATION INTERRUPTED"]
    },

    # --- NICHE 3: FUNNY ANIMALS ---
    "pets_being_dumb": {
        "subjects": ["dog", "cat", "puppy", "kitten", "pet", "golden retriever", "husky", "orange cat", "pug", "labrador", "corgi", "canine", "animal", "feline"],
        "actions": ["dumb", "confused", "derp", "lick window", "zoomies", "stuck", "scared of", "zero braincells", "silly", "goofy", "jump", "jumped", "fall", "fell", "slip", "slipped", "slide", "slides", "wipeout", "box", "fail", "fails", "failed", "funny", "calculate", "miscalculate", "barks", "barking"],
        "phrases": ["dog being dumb", "cat being silly", "zero braincells", "pets being derps", "confused pet", "funny dog", "funny cat", "dog fail", "cat fail", "dog jump fail", "cat jump fail", "zoomies wipeout"],
        "negative": ["human talk show", "podcast", "gameplay"],
        "community_markers": ["zero braincells", "one orange braincell", "derp", "he is doing his best", "golden retriever energy", "cute idiot", "funny dog", "good boy", "silly dog"],
        "default_incident": "clumsy_action",
        "punchlines": ["ZERO BRAINCELLS", "ONE SHARED BRAINCELL", "SYSTEM REBOOT NEEDED", "HE IS TRYING HIS BEST", "PET LOGIC ERROR"]
    },
    "cats_defying_physics": {
        "subjects": ["cat", "kitten", "orange cat", "feline"],
        "actions": ["jump", "scramble", "physics", "slip", "fall", "scramble", "missed jump", "drift", "launch", "wall run fail"],
        "phrases": ["cat jump fail", "cat defying physics", "cat calculation fail", "cat traction fail", "slipping cat"],
        "negative": ["dogs", "documentary", "podcast"],
        "community_markers": ["cat error 404", "physics not found", "cat miscalculated", "orange cat behavior", "cat fail"],
        "default_incident": "physical_fall",
        "punchlines": ["PHYSICS DISCONNECTED", "CAT ENGINE CRASHED", "TRACTION NOT FOUND", "CALCULATIONS FAILED", "GRAVITY APPLIED TO CAT"]
    },
    "dramatic_reactions": {
        "subjects": ["cat", "dog", "husky", "pet", "puppy", "kitten"],
        "actions": ["dramatic", "gasp", "shocked", "reaction", "betrayed", "side eye", "scream", "drama", "offended", "traumatized"],
        "phrases": ["dramatic cat", "dramatic husky", "dramatic pet reaction", "pet side eye", "betrayed dog"],
        "negative": ["human talking", "vlog", "review"],
        "community_markers": ["the drama", "give him an oscar", "so dramatic", "that side eye", "betrayed", "husky drama"],
        "default_incident": "awkward_moment",
        "punchlines": ["THE DRAMA", "OSCAR WORTHY PERFORMANCE", "TOP 10 ANIME BETRAYALS", "SIDE EYE OF JUDGMENT", "UNFORGIVABLE BETRAYAL"]
    },
    "guilty_pets": {
        "subjects": ["dog", "cat", "puppy", "pet", "couch", "pillow", "trash"],
        "actions": ["guilty", "caught", "destroyed", "busted", "who did this", "red handed", "guilty look", "hiding", "shame"],
        "phrases": ["guilty dog", "guilty pet caught", "dog caught red handed", "who tore the couch", "busted dog"],
        "negative": ["abuse", "kennel promo", "podcast"],
        "community_markers": ["it wasn't him", "innocent until proven guilty", "he was framed", "look at that face", "busted"],
        "default_incident": "awkward_moment",
        "punchlines": ["IT WAS NOT ME", "FRAMED BEYOND REASON", "GUILTY AS CHARGED", "EVIDENCE DESTROYED", "INNOCENT BY REASON OF CUTE"]
    },
    "animal_sneak_attacks": {
        "subjects": ["cat", "kitten", "dog", "pet", "stalker", "ninja"],
        "actions": ["sneak attack", "pounce", "stalk", "ambush", "jump scare", "wiggle butt", "stealth", "leaped on", "tackle"],
        "phrases": ["cat sneak attack", "playful ambush", "cat pounces", "stealth pounce", "animal sneak attack"],
        "negative": ["hunting documentary", "blood", "safari predation"],
        "community_markers": ["ninja", "stealth 100", "the wiggle", "ambush", "sneak attack", "cat pounce"],
        "default_incident": "clumsy_action",
        "punchlines": ["ASSASSIN IN TRAINING", "STEALTH LEVEL 100", "TARGET ACQUIRED", "AMBUSH COMPLETED", "THE WIGGLE BEFORE THE STRIKE"]
    },

    # --- NICHE 4: AURA DEBT ---
    "trying_to_look_cool": {
        "subjects": ["guy", "bro", "man", "teen", "skater", "driver", "model"],
        "actions": ["look cool", "smooth", "swagger", "flex", "pose", "sunglasses", "lost aura", "failed swagger", "cringe fail"],
        "phrases": ["trying to look cool fail", "lost all aura", "bro thought he was smooth", "cool guy fail", "-10000 aura"],
        "negative": ["fashion show", "perfume ad", "podcast"],
        "community_markers": ["-10000 aura", "lost all aura", "bro thought he was him", "bro is not the main character", "cooked"],
        "default_incident": "aura_loss",
        "punchlines": ["-10000 AURA", "AURA SYSTEM CRASH", "BRO IS NOT HIM", "SWAGGER DEVALUED", "ZERO RECOVERABLE AURA"]
    },
    "failed_handshakes": {
        "subjects": ["handshake", "high five", "fist bump", "hug", "greeting"],
        "actions": ["fail", "failed", "left hanging", "awkward", "missed", "rejected", "cringe", "ignored", "misaligned"],
        "phrases": ["handshake fail", "high five miss", "left hanging", "awkward handshake", "failed fist bump"],
        "negative": ["presidential speech", "diplomatic stream"],
        "community_markers": ["secondhand embarrassment", "left hanging", "emotional damage", "cringe", "i would vanish", "awkward"],
        "default_incident": "awkward_moment",
        "punchlines": ["EMOTIONAL DAMAGE", "LEFT HANGING FOREVER", "SECONDHAND EMBARRASSMENT", "VANISH FROM THE MAP", "REJECTED AT CONTACT"]
    },
    "confident_wrong_answers": {
        "subjects": ["student", "contestant", "player", "caller", "speaker", "interviewee", "answer"],
        "actions": ["confident", "confidently incorrect", "wrong answer", "debunked", "loud and wrong", "trivia fail", "shouted wrong"],
        "phrases": ["confidently incorrect", "confident wrong answer", "loud and wrong", "trivia fail", "debunked instantly"],
        "negative": ["full quiz show", "political interview"],
        "community_markers": ["confidently incorrect", "loud and wrong", "bro was so sure", "embarrassing", "the silence", "debunked"],
        "default_incident": "awkward_moment",
        "punchlines": ["LOUD AND WRONG", "CONFIDENTLY INCORRECT", "FACT CHECKED IN 4K", "SUPREME CONFIDENCE WRONG ANSWER", "THE IMMEDIATE SILENCE"]
    },
    "public_speaking_slipups": {
        "subjects": ["presenter", "speaker", "anchor", "news anchor", "reporter", "politician", "host", "speech"],
        "actions": ["slip of tongue", "blooper", "mistake", "stumble", "tongue tied", "teleprompter", "froze", "broke character"],
        "phrases": ["news blooper", "speech blooper", "slip of the tongue", "anchor blooper", "live tv blooper"],
        "negative": ["serious news", "lecture", "eulogy"],
        "community_markers": ["teleprompter moment", "freudian slip", "anchor broke character", "broadcast history", "crying", "blooper"],
        "default_incident": "awkward_moment",
        "punchlines": ["VANISH INTO THIN AIR", "BROADCAST BLOOPER", "TELEPROMPTER MALFUNCTION", "LIVE TELEVISION HAZARDS", "SLIP OF THE CENTURY"]
    },
    "tripping_while_flexing": {
        "subjects": ["gym bro", "guy", "lifter", "mirror", "muscle", "bicep", "flex"],
        "actions": ["flexing", "posing", "trip", "tripped", "fall", "fell", "mirror flex", "humbled by floor", "dropped"],
        "phrases": ["tripping while flexing", "flexing fail", "gym mirror flex fall", "posing trip", "aura cancelled"],
        "negative": ["gym routine tutorial", "workout vlog"],
        "community_markers": ["aura cancelled", "humbled by the floor", "mirror laughed", "instant humility", "karma", "down goes ego"],
        "default_incident": "physical_fall",
        "punchlines": ["AURA CANCELLED", "HUMBLING MIRROR ENCOUNTER", "FLEX INTERRUPTED BY FLOOR", "POSTURE CHECKED", "ZERO AURA REMAINING"]
    },

    # --- NICHE 5: SPORTS BLOOPERS ---
    "open_goal_misses": {
        "subjects": ["striker", "soccer player", "footballer", "net", "goal", "ball", "open net", "sitter"],
        "actions": ["miss", "missed", "blazed over", "wide", "post", "how did he miss", "choked", "empty net miss"],
        "phrases": ["open goal miss", "missed empty net", "miss of the season", "how did he miss", "unbelievable open goal miss"],
        "negative": ["full highlights", "analysis show"],
        "community_markers": ["how did he miss", "sub him off", "sell him immediately", "unbelievable miss", "empty net", "sitter"],
        "default_incident": "sports_miss",
        "punchlines": ["HOW DID HE MISS", "OPEN NET DISASTER", "SELL HIM AT HALFTIME", "BALL DISOBEYED GOAL", "MISS OF THE DECADE"]
    },
    "referee_collisions": {
        "subjects": ["referee", "ref", "umpire", "official", "linesman", "player"],
        "actions": ["collision", "collided", "knocked down", "tackled", "hit ref", "ref falls", "bumped into ref"],
        "phrases": ["referee collision", "ref knocked down", "player tackles referee", "umpire collision", "ref wiped out"],
        "negative": ["training session", "press conference"],
        "community_markers": ["red card for ref", "ref took a hit", "ref down", "unintentional tackle", "yellow card"],
        "default_incident": "physical_fall",
        "punchlines": ["RED CARD FOR PHYSICS", "REFEREE INTERFERENCE", "OFFICIAL TAKEN DOWN", "UNSCHEDULED TACKLE", "REF DOWN IN AISLE 1"]
    },
    "mascot_shenanigans": {
        "subjects": ["mascot", "costume", "performer", "team mascot", "stunt"],
        "actions": ["tumble", "wipeout", "prank", "unhinged", "fell", "head fell off", "shenanigans", "stunt fail"],
        "phrases": ["mascot fail", "unhinged mascot", "mascot wipeout", "mascot tumble", "mascot prank gone wrong"],
        "negative": ["interview", "podcast"],
        "community_markers": ["mascot is unhinged", "who is in that suit", "mascot mvp", "mascot wipeout", "legendary mascot"],
        "default_incident": "clumsy_action",
        "punchlines": ["UNHINGED MASCOT", "MAN INSIDE THE SUIT GAVE UP", "MASCOT ROGUE PROTOCOL", "HALF TIME HAVOC", "HEAD CAME FLYING OFF"]
    },
    "bench_celebration_fails": {
        "subjects": ["bench", "teammates", "substitutes", "bench warmers", "water cooler", "team"],
        "actions": ["celebrating fail", "collision", "fell over", "knocked down", "cooler spilled", "overenthusiastic", "wipeout"],
        "phrases": ["bench celebration fail", "teammates celebrate fail", "bench collision", "bench warmer disaster"],
        "negative": ["championship recap show"],
        "community_markers": ["bench warmer disaster", "injury by celebration", "calm down guys", "bench chaos", "injured celebrating"],
        "default_incident": "physical_fall",
        "punchlines": ["TEAM BENCH DISASTER", "INJURED CELEBRATING", "ENTHUSIASM LEVEL DANGEROUS", "BENCH CHAOS UNLEASHED", "CALM DOWN ROOKIES"]
    },
    "equipment_failure": {
        "subjects": ["bat", "racket", "shoe", "sneaker", "rim", "backboard", "ball", "helmet", "uniform", "pole"],
        "actions": ["snapped", "broke", "exploded", "popped", "shattered", "ripped", "equipment failure", "gave up"],
        "phrases": ["shoe exploded", "bat snapped", "racket broke", "equipment failure", "rim shattered"],
        "negative": ["equipment review", "commercial"],
        "community_markers": ["manufacturing defect", "equipment gave up", "snapped clean", "rip shoes", "quality control"],
        "default_incident": "equipment_failure",
        "punchlines": ["MANUFACTURED DEFECT", "EQUIPMENT GAVE UP", "QUALITY CONTROL SLEEPING", "SNAPPED CLEAN IN HALF", "GEAR RESIGNATION"]
    },

    # --- NICHE 6: NPC GLITCHES ---
    "walking_into_walls": {
        "subjects": ["person", "shopper", "pedestrian", "glass door", "window", "wall", "mirror", "barrier", "glass"],
        "actions": ["walk", "walks", "walked", "run", "ran", "bonk", "bonked", "hit", "collide", "clean window", "pathfinding"],
        "phrases": ["walked into glass door", "walking into window", "clean glass fail", "npc walks into wall", "bonked on glass"],
        "negative": ["cctv time lapse", "movie scene"],
        "community_markers": ["npc pathfinding", "clean your windows", "clean glass undefeated", "bonk", "bro forgot collision"],
        "default_incident": "physical_fall",
        "punchlines": ["NPC PATHFINDING ERROR", "GLASS CLEANER WON", "COLLISION MESH LOADED", "BONK OF REALITY", "PHYSICAL BARRIER DETECTED"]
    },
    "synchronized_strangers": {
        "subjects": ["strangers", "people", "pedestrians", "crowd", "matrix", "simulation"],
        "actions": ["synchronized", "same move", "identical", "coincidental", "in sync", "same animation", "glitch"],
        "phrases": ["glitch in the matrix", "synchronized strangers", "same animation script", "real life glitch", "simulation desync"],
        "negative": ["flash mob", "choreography rehearsal"],
        "community_markers": ["matrix glitch", "simulation lag", "same animation script", "coincidence", "spooky"],
        "default_incident": "npc_glitch",
        "punchlines": ["GLITCH IN THE MATRIX", "REUSED ANIMATION SCRIPT", "SIMULATION DESYNC", "COPY PASTE STRANGERS", "NPC CLONE PROTOCOL"]
    },
    "t_pose_moments": {
        "subjects": ["person", "guy", "man", "stranger", "npc", "statue"],
        "actions": ["t pose", "t-pose", "standing rigid", "unmoving", "frozen", "asserting dominance", "unrendered"],
        "phrases": ["t pose in public", "real life t pose", "standing like npc", "unrendered npc", "reset the simulation"],
        "negative": ["3d animation tutorial", "game engine test"],
        "community_markers": ["reset simulation", "t pose to assert dominance", "loading textures", "npc stuck", "reboot"],
        "default_incident": "npc_glitch",
        "punchlines": ["RESET THE SIMULATION", "ASSERTS DOMINANCE BY RIGIDITY", "TEXTURES STILL RENDERING", "AWAITING SCRIPT UPDATE", "STANDBY MODE ACTIVATED"]
    },
    "background_npc_freeze": {
        "subjects": ["background", "guy in back", "person in background", "extra", "crowd member"],
        "actions": ["frozen", "unmoving", "staring", "statue", "buffering", "motionless", "npc behavior"],
        "phrases": ["background npc frozen", "guy in background not moving", "npc in real life", "background extra bugged"],
        "negative": ["mannequin challenge"],
        "community_markers": ["look at the guy in back", "background npc bugged", "he forgot to move", "creepy", "npc moment"],
        "default_incident": "npc_glitch",
        "punchlines": ["AWAITING RESPONSE", "BACKGROUND EXTRA FROZE", "LOW RESOURCE MODE", "IDLE ANIMATION MISSING", "CROWD BUFFER OVERFLOW"]
    },
    "repetitive_actions": {
        "subjects": ["person", "worker", "shopper", "commuter", "brain"],
        "actions": ["repetitive loop", "stuck in loop", "mechanical motion", "zoned out", "buffering", "repeated action", "looping"],
        "phrases": ["stuck in a loop", "brain buffering", "npc repetitive action", "real life loop", "zoned out loop"],
        "negative": ["music video", "vlog"],
        "community_markers": ["buffering", "brain buffer overflow", "loop unresolved", "zoned out", "reboot needed"],
        "default_incident": "npc_glitch",
        "punchlines": ["LOOP UNRESOLVED", "BRAIN BUFFERING 99%", "AUTONOMOUS LOOP TRAPPED", "CPU USAGE 100%", "RELOAD USER SESSION"]
    },

    # --- NICHE 7: WORKPLACE DISASTERS ---
    "forklift_domino": {
        "subjects": ["forklift", "pallet", "warehouse", "racks", "shelves", "cargo", "aisle"],
        "actions": ["bump", "hit rack", "collapse", "domino", "topple", "warehouse collapse", "avalanche of boxes"],
        "phrases": ["forklift accident", "warehouse rack collapse", "forklift domino", "warehouse disaster", "pallet collapse"],
        "negative": ["safety seminar", "osha training", "podcast"],
        "community_markers": ["fired immediately", "osha violation", "domino effect", "cleanup forever", "expensive mistake"],
        "default_incident": "equipment_failure",
        "punchlines": ["SOMEONE GETS FIRED", "OSHA LEVEL APOCALYPSE", "DOMINO EFFECT UNLOCKED", "WAREHOUSE DEMOLITION", "CLEANUP ESTIMATE: 3 YEARS"]
    },
    "office_pranks_gone_wrong": {
        "subjects": ["office", "cubicle", "desk", "coworker", "boss", "chair", "monitor"],
        "actions": ["prank", "backfired", "damage", "broken monitor", "smashed", "hr call", "prank fail"],
        "phrases": ["office prank fail", "cubicle prank gone wrong", "workplace prank backfires", "hr would like a word"],
        "negative": ["the office tv show", "sitcom"],
        "community_markers": ["hr meeting scheduled", "hr would like a word", "office chaos", "fired", "broken monitor"],
        "default_incident": "prank_backfire",
        "punchlines": ["HR WOULD LIKE A WORD", "MEETING WITH HR IN 5 MIN", "WORKPLACE PRIVILEGES REVOKED", "PRANK ESCALATED QUICKLY", "CORPORATE INCIDENT REPORT"]
    },
    "chef_pan_inferno": {
        "subjects": ["chef", "cook", "kitchen", "pan", "oil", "stove", "grill", "flambe"],
        "actions": ["fire", "flare up", "inferno", "grease fire", "flame burst", "shocked chef", "eyebrows burned", "extinguisher"],
        "phrases": ["chef fire fail", "kitchen flare up", "pan on fire", "cooking disaster", "chef shocked by flame"],
        "negative": ["cooking recipe show", "full documentary"],
        "community_markers": ["extra crispy", "kitchen nightmares", "fire extinguisher", "order up", "eyebrows gone"],
        "default_incident": "weather_blast",
        "punchlines": ["EXTRA CRISPY", "WELL DONE HAS A NEW MEANING", "EYEBROWS HAVE LEFT THE CHAT", "CHEF SPECIAL: CHARCOAL", "KITCHEN ALARM ACTIVATED"]
    },
    "retail_display_collapse": {
        "subjects": ["store", "supermarket", "cans", "display", "pyramid", "shelf", "bottles", "mannequin"],
        "actions": ["collapse", "collapsed", "toppled", "fell over", "domino", "crashed down", "store disaster"],
        "phrases": ["store display collapse", "can pyramid fall", "retail display crash", "cleanup in aisle 4", "shelf collapse"],
        "negative": ["ad promotion", "store tour"],
        "community_markers": ["cleanup in aisle 4", "stocker crying", "domino", "retail nightmare", "minimum wage"],
        "default_incident": "equipment_failure",
        "punchlines": ["CLEANUP IN AISLE 4", "PYRAMID ARCHITECTURE FAILED", "STOCKER RESIGNATION LETTER", "DOMINO DISPLAY CRASH", "STORE FLOOR CATASTROPHE"]
    },
    "mic_left_unmuted": {
        "subjects": ["zoom", "meeting", "mic", "microphone", "call", "teams", "conference", "hot mic"],
        "actions": ["unmuted", "forgot mic", "caught talking", "embarrassment", "hot mic", "confession", "flushed"],
        "phrases": ["hot mic moment", "forgot to mute zoom", "zoom meeting unmuted", "mic left on", "you are not on mute"],
        "negative": ["full podcast", "corporate webinar"],
        "community_markers": ["you are not on mute", "unmute panic", "corporate nightmare", "mute your mic", "career over"],
        "default_incident": "awkward_moment",
        "punchlines": ["YOU ARE NOT ON MUTE", "BROADCAST TO ENTIRE COMPANY", "MUTE BUTTON BETRAYAL", "CORPORATE CONFESSION LIVE", "RESIGNATION PENDING"]
    },

    # --- NICHE 8: EXTREME LUCK ---
    "inches_from_disaster": {
        "subjects": ["pedestrian", "car", "driver", "tree", "train", "pole", "near miss", "close call"],
        "actions": ["inches", "dodged", "narrowly avoided", "miraculously", "split second", "barely missed", "almost crushed"],
        "phrases": ["inches from disaster", "near miss close call", "guardian angel near miss", "miraculous escape", "dodged by inches"],
        "negative": ["fatal crash", "movie vfx", "podcast"],
        "community_markers": ["luck 9999", "guardian angel", "inches", "that was close", "heart stopped"],
        "default_incident": "lucky_dodge",
        "punchlines": ["LUCK LEVEL 9999", "INCHES FROM DISASTER", "GUARDIAN ANGEL CLOCKING OT", "DEATH SAID NOT TODAY", "NARROWEST ESCAPE ON CAMERA"]
    },
    "impossible_ricochets": {
        "subjects": ["ball", "bullet", "arrow", "dart", "ping pong", "puck", "object", "cup", "target"],
        "actions": ["ricochet", "bounced", "deflection", "miracle bounce", "landed in cup", "geometry", "trick shot"],
        "phrases": ["impossible ricochet", "miracle bounce trickshot", "calculated ricochet", "crazy deflection bounce"],
        "negative": ["trickshot studio compilation", "cgi fake"],
        "community_markers": ["calculated", "simple geometry", "what are the odds", "insane bounce", "trickshot"],
        "default_incident": "lucky_dodge",
        "punchlines": ["CALCULATED TOTALLY", "SIMPLE GEOMETRY AT WORK", "ONE IN A MILLION BOUNCE", "RICHOCHET MASTERCLASS", "PHYSICS DID THE HOMEWORK"]
    },
    "accidental_hero": {
        "subjects": ["guy", "stranger", "bystander", "hero", "pedestrian", "thief", "runaway"],
        "actions": ["inadvertently", "accidentally saved", "tripped the thief", "caught without looking", "accidental save", "hero purely by chance"],
        "phrases": ["accidental hero", "tripped thief by accident", "saved someone by accident", "main character energy accidental hero"],
        "negative": ["superhero movie", "trailer"],
        "community_markers": ["main character", "task failed successfully", "hero without knowing", "legend", "plot armor"],
        "default_incident": "lucky_dodge",
        "punchlines": ["MAIN CHARACTER ENERGY", "TASK FAILED SUCCESSFULLY", "ACCIDENTAL SAVIOR", "PLOT ARMOR ACTIVATED", "HEROIC BY PURE CHANCE"]
    },
    "saved_by_a_miracle": {
        "subjects": ["survivor", "person", "child", "driver", "victim", "miracle"],
        "actions": ["saved", "survived", "miracle", "impossible rescue", "second life", "untouched", "nick of time"],
        "phrases": ["saved by a miracle", "unbelievable survival", "guardian angel on duty", "impossible miracle save"],
        "negative": ["sermon", "religious broadcast"],
        "community_markers": ["guardian angel", "second life unlocked", "miracle", "insane", "blessed"],
        "default_incident": "lucky_dodge",
        "punchlines": ["GUARDIAN ANGEL ON DUTY", "SECOND CHANCE UNLOCKED", "IMPOSSIBLE OUTCOME", "PHYSICS STEPPED ASIDE", "BLESSING IN 4K"]
    },
    "bottle_flip_master": {
        "subjects": ["bottle", "water bottle", "cap", "toss", "throw", "table", "landing"],
        "actions": ["flip", "landed upright", "stuck the landing", "first try", "impossible bottle flip", "perfection"],
        "phrases": ["impossible bottle flip", "bottle flip master", "landed upright first try", "one in a billion bottle flip"],
        "negative": ["commercial", "slowmo guy"],
        "community_markers": ["one in a billion", "he peaked here", "bottle flip legend", "insane landing", "clean"],
        "default_incident": "lucky_dodge",
        "punchlines": ["ONE IN A BILLION", "PEAKED IN THIS EXACT SECOND", "LANDED PERFECTLY", "GRAVITY APPROVED", "UNREPEATABLE MASTERPIECE"]
    },

    # --- NICHE 9: GYM BLOOPERS ---
    "treadmill_ejections": {
        "subjects": ["treadmill", "runner", "gym goer", "belt", "fitness", "machine"],
        "actions": ["ejected", "launched", "flies off", "fly off", "max speed", "slip", "fall", "backward", "yeeted", "treadmill fail"],
        "phrases": ["treadmill fail", "launched by treadmill", "treadmill ejection", "treadmill max speed fail", "flies off treadmill"],
        "negative": ["workout plan", "fitness influencer podcast"],
        "community_markers": ["max speed", "yeeted", "treadmill 1 human 0", "launched", "gym fail"],
        "default_incident": "clumsy_action",
        "punchlines": ["MAX SPEED ACTIVATED", "YEETED INTO WALL", "TREADMILL DISAGREES", "EMERGENCY STOP UNUSED", "VELOCITY OVERLOAD"]
    },
    "ego_lifting_consequences": {
        "subjects": ["ego lift", "lifter", "bench press", "squat", "barbell", "heavy weight", "weights", "500 lbs", "dumbbell"],
        "actions": ["pinned", "stuck", "dropped", "too heavy", "crushed", "roll of shame", "ego lifter pinned", "failed lift"],
        "phrases": ["ego lifting fail", "ego lifter pinned", "bench press stuck", "ego lifting consequences", "check your ego"],
        "negative": ["powerlifting championship", "form check tutorial"],
        "community_markers": ["check your ego", "pinned by weights", "drop the ego", "gym fail", "lift within limits"],
        "default_incident": "equipment_failure",
        "punchlines": ["CHECK YOUR EGO", "PINNED BY GRAVITY", "EGO ZERO BARBELL ONE", "EMERGENCY ROLL OF SHAME", "LIGHTWEIGHT GONE WRONG"]
    },
    "elastic_band_snaps": {
        "subjects": ["resistance band", "elastic band", "exercise band", "workout band", "anchor"],
        "actions": ["snap", "snapped", "whipped", "slipped", "whiplash", "band hit", "band slapped"],
        "phrases": ["resistance band snap", "elastic band snaps", "band snapped fail", "workout band snap"],
        "negative": ["physical therapy lecture"],
        "community_markers": ["felt that through screen", "snap back to reality", "ouch", "band betrayed him", "whip"],
        "default_incident": "clumsy_action",
        "punchlines": ["SNAP BACK TO REALITY", "FELT THROUGH THE SCREEN", "BAND BETRAYAL COMPLETE", "WHIPLASH ACTIVATED", "PHYSICS RETALIATION"]
    },
    "cable_machine_mishaps": {
        "subjects": ["cable machine", "pulley", "weight stack", "gym cable", "pin"],
        "actions": ["snapped", "slipped", "pulled off balance", "dropped", "launched", "cable broke"],
        "phrases": ["cable machine fail", "gym cable snap", "pulley slipped fail", "cable machine mishap"],
        "negative": ["gym repair tutorial"],
        "community_markers": ["machine won", "cable snapped", "gym blooper", "equipment fail", "lost balance"],
        "default_incident": "equipment_failure",
        "punchlines": ["EQUIPMENT WON", "PULLEY SYSTEM RETALIATES", "FORCE APPLIED BACKWARDS", "WEIGHT STACK DROPPED", "UNSCHEDULED FLIGHT"]
    },
    "gym_equipment_misunderstood": {
        "subjects": ["gym equipment", "machine", "gym goer", "workout routine", "exercise"],
        "actions": ["using backward", "doing it wrong", "invented new exercise", "confused", "bizarre workout", "wrong machine"],
        "phrases": ["using gym machine wrong", "gym equipment misunderstood", "bizarre workout routine", "bro invented new exercise"],
        "negative": ["equipment instruction video"],
        "community_markers": ["new exercise unlocked", "doing it wrong", "bro is inventing exercises", "what machine is that", "gym confused"],
        "default_incident": "clumsy_action",
        "punchlines": ["NEW WORKOUT UNLOCKED", "INVENTING NEW EXERCISES", "MANUAL WAS NOT READ", "INNOVATIVE CONFUSION", "TRAINER CONFUSION 100%"]
    },

    # --- NICHE 10: NATURE & WEATHER ---
    "umbrella_inversions": {
        "subjects": ["umbrella", "parasol", "rain", "storm", "wind", "gust"],
        "actions": ["flip", "flips", "inverted", "inside out", "blown away", "destroyed", "gust of wind", "wind flips"],
        "phrases": ["umbrella flips inside out", "umbrella inverted", "wind flips umbrella", "umbrella blown away", "umbrella inversion"],
        "negative": ["meteorology report", "weather forecast show"],
        "community_markers": ["mary poppins", "umbrella said no", "wind won", "rip umbrella", "blown away"],
        "default_incident": "weather_blast",
        "punchlines": ["WIND: 1, UMBRELLA: 0", "MARY POPPINS PROTOCOL", "STRUCTURAL INVERSION", "FIBERGLASS BETRAYAL", "SHIELD DEFEATED BY GUST"]
    },
    "sudden_gusts_stealing_items": {
        "subjects": ["wind", "gust", "hat", "wig", "tent", "papers", "canopy", "toupee"],
        "actions": ["stole", "steals", "snatched", "blown away", "flies away", "chasing", "wind takes"],
        "phrases": ["wind stole hat", "wig blown away", "gust steals tent", "wind snatched wig", "chasing hat in wind"],
        "negative": ["documentary clip", "cinematic"],
        "community_markers": ["property of the wind", "wig gone", "chasing hat", "wind tax", "snatched"],
        "default_incident": "weather_blast",
        "punchlines": ["PROPERTY OF THE WIND", "WIND TAX COLLECTED", "SNATCHED INTO STRATOSPHERE", "DONATED TO THE BREEZE", "CHASING PROPERTY FOREVER"]
    },
    "slippery_ice_encounters": {
        "subjects": ["ice", "black ice", "frozen sidewalk", "snow", "freezing puddle", "walker", "driveway"],
        "actions": ["slip", "slipped", "slipping", "fall", "fell", "skate", "cartoon slip", "lost traction"],
        "phrases": ["slipping on ice", "black ice slip", "frozen sidewalk fall", "slippery ice encounter", "cartoon slip on ice"],
        "negative": ["figure skating championship"],
        "community_markers": ["black ice undefeated", "cartoon slip", "penguin walk failed", "ice cold", "down goes human"],
        "default_incident": "physical_fall",
        "punchlines": ["ICE COLD TAKEDOWN", "BLACK ICE UNDEFEATED", "CARTOON SLIP REENACTED", "TRACTION CANCELLED", "WINTER GRAVITY AMBUSH"]
    },
    "rogue_waves_at_beach": {
        "subjects": ["wave", "rogue wave", "beach", "ocean", "tide", "beachgoers", "chairs", "towels"],
        "actions": ["soaked", "swept", "washed away", "surprise wave", "flooded", "hit by wave"],
        "phrases": ["rogue wave at beach", "wave washes away chairs", "beachgoers soaked by wave", "unexpected beach wave"],
        "negative": ["surfing pro tour", "tsunami warning report"],
        "community_markers": ["ocean said no", "wave tax", "run for towels", "beach surprise", "soaked"],
        "default_incident": "weather_blast",
        "punchlines": ["OCEAN SAID NO", "TIDE ARRIVED EARLY", "TOWELS WASHED AWAY", "BEACH LOUNGE INTERRUPTED", "POSEIDON SAYS MOVE"]
    },
    "muddy_puddle_deceptions": {
        "subjects": ["puddle", "mud", "sinkhole", "road puddle", "walker", "car", "water hole"],
        "actions": ["deeper than looks", "submerged", "swallowed", "stepped into deep", "sinkhole puddle", "soaked"],
        "phrases": ["puddle deeper than it looks", "stepped into deep puddle", "muddy puddle deception", "car submerged in puddle"],
        "negative": ["offroad racing series", "vehicle test"],
        "community_markers": ["deeper than it looked", "puddle sinkhole", "lost his foot", "soaked shoe", "underestimated"],
        "default_incident": "clumsy_action",
        "punchlines": ["DEEPER THAN IT LOOKED", "PORTAL TO ATLANTIS", "UNDERESTIMATED DEPTH", "PUDDLE SINKHOLE AMBUSH", "SHALLOW PUDDLE ILLUSION"]
    },
}

# Global non-real disqualifiers
GLOBAL_NON_REAL_MARKERS = [
    "gameplay", "walkthrough", "playthrough", "gta", "gta v", "gta 5", "beamng",
    "forza", "need for speed", "roblox", "minecraft", "fortnite", "valorant",
    "apex legends", "sims", "vrchat", "3d animation", "cgi", "blender render",
    "unreal engine", "animated short", "anime", "vtuber", "ai generated", "sora"
]

COMMUNITY_EMOTION_TAXONOMY = {
    "schadenfreude_karma": ["deserved", "karma", "satisfying", "justice", "instant karma", "clown", "idiot", "cooked", "lesson"],
    "cringe_aura": ["aura", "cringe", "secondhand", "cooked", "left hanging", "vanish", "embarrassing", "bro thought"],
    "shock_miracle": ["miracle", "guardian angel", "inches", "holy", "how is that possible", "insane", "omg", "luck"],
    "disaster_failure": ["rip", "fired", "wrecked", "destroyed", "fail", "broken", "disaster", "landlord special", "osha"],
    "pet_humor": ["zero braincells", "orange cat", "derp", "doing his best", "the drama", "cute", "zoomies"],
}


class DynamicNicheEngine:
    @staticmethod
    def synthesize_for_subcategory(sub_category_id: str, strict_definition: str = "", name: str = "") -> dict:
        tokens = re.findall(r"\b[a-zA-Z]{3,}\b", f"{sub_category_id} {name} {strict_definition}".lower())
        stopwords = {
            "must", "show", "reject", "generic", "between", "the", "and", "for", "with", "from",
            "this", "that", "into", "over", "what", "when", "where", "after", "before", "their"
        }
        filtered = [t for t in tokens if t not in stopwords]
        clean_name = name.upper() if name else sub_category_id.replace("_", " ").upper()

        def_lower = strict_definition.lower()
        if any(w in def_lower for w in ["car", "crash", "driver", "vehicle", "truck", "road"]):
            incident = "car_crash"
        elif any(w in def_lower for w in ["fall", "slip", "trip", "stumble", "jump", "gravity"]):
            incident = "physical_fall"
        elif any(w in def_lower for w in ["wind", "wave", "water", "rain", "ice", "puddle", "fire"]):
            incident = "weather_blast"
        elif any(w in def_lower for w in ["prank", "taunt", "cheat", "scam"]):
            incident = "prank_backfire"
        elif any(w in def_lower for w in ["pet", "cat", "dog", "animal"]):
            incident = "clumsy_action"
        elif any(w in def_lower for w in ["handshake", "speech", "cringe", "answer", "embarrass"]):
            incident = "awkward_moment"
        elif any(w in def_lower for w in ["dodge", "luck", "miracle", "inches", "bottle"]):
            incident = "lucky_dodge"
        elif any(w in def_lower for w in ["glitch", "wall", "sync", "npc", "freeze"]):
            incident = "npc_glitch"
        else:
            incident = "clumsy_action"

        punchlines = [
            f"MOMENT OF {clean_name}",
            f"WHEN {clean_name} GOES WRONG",
            f"INSTANT {clean_name} REGRET",
            f"{clean_name} FAILED SPECTACULARLY",
            f"ABSOLUTE {clean_name} CHAOS"
        ]

        return {
            "subjects": filtered[:4] if filtered else [clean_name.lower()],
            "actions": filtered[4:] if len(filtered) > 4 else ["fail", "incident", "moment"],
            "phrases": [clean_name.lower(), sub_category_id.replace("_", " ").lower()],
            "negative": ["gameplay", "animation", "cgi", "podcast", "tutorial"],
            "community_markers": ["deserved", "rip", "karma", "epic fail", "no way"],
            "default_incident": incident,
            "punchlines": punchlines,
        }


def get_current_run_context() -> dict:
    context_path = os.path.abspath("current_run_context.json")
    if os.path.exists(context_path):
        try:
            with open(context_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def analyze_clip_heuristically(
    title: str,
    description: str,
    sub_category_id: str | None = None,
    comments: list[str] | None = None,
    tags: list[str] | None = None,
    strict_definition: str | None = None,
    negative_filters: list[str] | None = None,
) -> dict:
    if comments is None:
        comments = []
    if tags is None:
        tags = []

    # Resolve active subcategory from run context if omitted
    if not sub_category_id or sub_category_id == "road_rage_regret":
        run_ctx = get_current_run_context()
        if run_ctx.get("sub_category_id"):
            sub_category_id = run_ctx.get("sub_category_id")
            if not strict_definition:
                strict_definition = run_ctx.get("strict_definition")
            if not negative_filters:
                negative_filters = run_ctx.get("negative_filters")

    clean_cat = (sub_category_id or "road_rage_regret").lower().strip()

    full_text = f"{title or ''} {description or ''} {' '.join(tags)}".lower()
    comments_blob = " ".join(comments).lower()

    # Gate 1: Check for Gaming / CGI / Animation (Disqualifier)
    for marker in GLOBAL_NON_REAL_MARKERS:
        pattern = r"\b" + re.escape(marker) + r"\b"
        if re.search(pattern, full_text):
            return {
                "is_real_and_context_matched": False,
                "confidence": 0.95,
                "reason": f"Disqualified: Contains non-real media keyword '{marker}' in metadata.",
                "incident_type": "other",
                "punchlineText": "NOT REAL FOOTAGE",
                "method": "heuristic_filter"
            }

    # Resolve Lexicon with alias mapping
    SUB_CATEGORY_LEXICON_ALIASES = {
        "athletes_celebrating_too_early": "smug_celebrations",
        "one_million_aura_loss": "trying_to_look_cool",
        "road_rage_justice": "road_rage_regret",
        "worst_shift_ever": "retail_display_collapse",
        "used_all_luck_for_life": "inches_from_disaster",
        "bench_press_ego_fails": "ego_lifting_consequences",
        "sudden_wind_ruining_events": "sudden_gusts_stealing_items",
        "unrendered_game_npcs": "t_pose_moments",
        "real_life_npc_moments": "background_npc_freeze",
        "construction_site_fails": "forklift_domino",
        "insane_close_calls": "inches_from_disaster",
        "ego_lifting_fails": "ego_lifting_consequences",
        "sudden_microburst_winds": "sudden_gusts_stealing_items",
        "defying_warning_signs": "pranks_backfiring",
    }
    resolved_cat = SUB_CATEGORY_LEXICON_ALIASES.get(clean_cat, clean_cat)

    if resolved_cat in NICHE_LEXICONS:
        lexicon = NICHE_LEXICONS[resolved_cat]
    elif clean_cat in NICHE_LEXICONS:
        lexicon = NICHE_LEXICONS[clean_cat]
    else:
        lexicon = DynamicNicheEngine.synthesize_for_subcategory(
            sub_category_id=clean_cat,
            strict_definition=strict_definition or "",
        )

    # Gate 2: Category Negative Disqualifiers
    active_negatives = list(lexicon.get("negative", []))
    if negative_filters:
        active_negatives.extend(negative_filters)

    for neg in active_negatives:
        neg_clean = neg.strip().lower()
        if not neg_clean:
            continue
        pattern = r"\b" + re.escape(neg_clean) + r"\b"
        if re.search(pattern, full_text):
            return {
                "is_real_and_context_matched": False,
                "confidence": 0.90,
                "reason": f"Disqualified: Metadata matches category negative filter '{neg_clean}'.",
                "incident_type": "other",
                "punchlineText": "OFF-NICHE CONTENT",
                "method": "heuristic_filter"
            }

    # Gate 3: Two-Tier Semantic Scoring (Subject + Action OR Composite Phrase)
    subjects = lexicon.get("subjects", [])
    actions = lexicon.get("actions", [])
    phrases = lexicon.get("phrases", [])

    matched_subjects = [s for s in subjects if re.search(r"\b" + re.escape(s) + r"\b", full_text)]
    matched_actions = [a for a in actions if re.search(r"\b" + re.escape(a) + r"\b", full_text)]
    matched_phrases = [p for p in phrases if p in full_text]

    two_tier_match = (len(matched_subjects) >= 1 and len(matched_actions) >= 1)
    phrase_match = len(matched_phrases) >= 1
    total_pos_matches = len(matched_subjects) + len(matched_actions) + (len(matched_phrases) * 2)

    # Gate 4: Community Consensus from Comments
    community_score = 0
    community_hits = []
    for cm in lexicon.get("community_markers", []):
        matches = len(re.findall(r"\b" + re.escape(cm.lower()) + r"\b", comments_blob))
        if matches > 0:
            community_score += min(matches, 3)
            community_hits.append(f"{cm}({matches})")

    # Gate 5: Universal Emotion Taxonomy Alignment
    for emotion_cat, emotion_keywords in COMMUNITY_EMOTION_TAXONOMY.items():
        for kw in emotion_keywords:
            if re.search(r"\b" + re.escape(kw) + r"\b", comments_blob):
                community_score += 1
                if len(community_hits) < 5:
                    community_hits.append(f"{kw}*")

    # Decision Matrix
    is_matched = bool(two_tier_match or phrase_match or (len(matched_subjects) >= 1 and community_score >= 1))
    score = (total_pos_matches * 1.5) + (community_score * 0.8)
    confidence = min(0.98, max(0.50, 0.65 + (score * 0.05))) if is_matched else 0.40

    # Incident type
    incident_type = lexicon.get("default_incident", "clumsy_action")

    # Select dynamic punchline
    punchline_options = lexicon.get("punchlines", ["MOMENT OF REGRET"])
    hash_idx = sum(ord(c) for c in (title or "punchline")) % len(punchline_options)
    punchline_text = punchline_options[hash_idx]

    reason_msg = (
        f"Two-Tier Consensus for '{clean_cat}': Subjects={matched_subjects[:3]}, Actions={matched_actions[:3]}, Phrases={matched_phrases[:2]}. "
        f"Community consensus={community_score} {community_hits[:3]}."
    )

    return {
        "is_real_and_context_matched": bool(is_matched),
        "confidence": round(float(confidence), 2),
        "reason": reason_msg if is_matched else f"Insufficient subject/action or consensus match for '{clean_cat}'.",
        "incident_type": incident_type,
        "punchlineText": punchline_text,
        "method": "two_tier_community_consensus"
    }


if __name__ == "__main__":
    test_cases = [
        ("treadmill_ejections", "Guy tries running at max speed on treadmill and flies off backward into wall", "Funny gym blooper fail"),
        ("umbrella_inversions", "Sudden storm gust violently flips umbrella inside out on busy street", "Wind ruins umbrella in seconds"),
        ("ego_lifting_consequences", "Guy loads 500 lbs on bench press, gets pinned immediately and rolls of shame", "Check your ego at the door"),
        ("failed_handshakes", "Presenter goes for high five, other guy goes for fist bump, excruciating awkwardness", "Worst handshake fail in history"),
        ("inches_from_disaster", "Pedestrian miraculously dodges out of control car by inches, guardian angel watching", "Narrowest near miss close call"),
        ("forklift_domino", "Forklift bumps warehouse rack causing massive domino collapse of pallets", "Expensive warehouse disaster"),
        ("open_goal_misses", "Soccer striker misses open net point blank with nobody in goal", "How did he miss that"),
        ("walking_into_walls", "Shopper walks straight into clean glass door thinking it was open", "Clean glass strikes again"),
        ("pets_being_dumb", "Confused golden retriever gets stuck behind open door with zero braincells", "Silly dog fail"),
    ]

    print("\n========== RUNNING MASTER TWO-TIER FALLBACK ENGINE TEST ==========")
    for cat_id, test_title, test_desc in test_cases:
        res = analyze_clip_heuristically(test_title, test_desc, cat_id)
        status = "PASSED" if res["is_real_and_context_matched"] else "FAILED"
        print(f"[{status}] {cat_id:<28} | Conf={res['confidence']} | Incident={res['incident_type']:<16} | Punchline='{res['punchlineText']}'")
