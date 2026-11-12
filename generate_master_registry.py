import json
import os

# Complete registry of all 10 niches and 50 subcategories with strict Harvester, Audio Hook, and Timing specs
registry = {
    "channel_reference": "@MrPurifiedWater",
    "branding": {
        "channel_name": "LevelZero0ne",
        "logo_path": "public/levelzero0ne_logo.jpg",
        "sonic_brand": "public/audio/earshot_sonic_brand.mp3"
    },
    "visual_archetype": {
        "top_banner": {
            "height_px": 240,
            "background": "#000000",
            "prefix_text": "Ranking The",
            "prefix_color": "#FFFFFF",
            "highlight_color": "#FFEB3B",
            "subject_color": "#FF2D55",
            "tag_color": "#00D2FF"
        },
        "ladder": {
            "type": "level_climb",
            "direction": "bottom_to_top",
            "ranks_total": 5,
            "levels": ["[Level 1]", "[Level 2]", "[Level 3]", "[Level 4]", "[Level 5]"],
            "colors": {
                "rank_1": "#FF2D55",
                "rank_2": "#00D2FF",
                "rank_3": "#FFEB3B",
                "rank_4": "#FFFFFF",
                "rank_5": "#FFFFFF"
            }
        }
    },
    "universal_negative_filters": [
        "podcast", "interview", "commentary", "reaction", "facecam", "split screen",
        "green screen", "news report", "news anchor", "review", "vlog", "gameplay",
        "gta", "beamng", "forza", "animation", "cgi", "3d model", "slideshow", "tweet"
    ],
    "subcategories": {
        # --- NICHE 1: HUMAN PHYSICAL FAILS ---
        "people_accepting_fate": {
            "niche": "human_fails",
            "name": "People Accepting Fate",
            "title_header": "Ranking Best Of",
            "subject_header": "This Is The End Moments",
            "version_tag": "(Surrender Version)",
            "audio_hook": {
                "stem": "public/audio/stems/skyfall_this_is_the_end.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 36,
                "duck_native_volume": 0.2
            },
            "timing_rules": {
                "buildup_seconds": 3.5,
                "freeze_seconds": 1.2,
                "aftermath_seconds": 1.8
            },
            "harvester": {
                "primary_queries": [
                    "he accepted his fate fail shorts",
                    "person accepts fate fail shorts",
                    "he gave up mid fall fail shorts",
                    "slide down ice driveway helpless surrender shorts"
                ],
                "fallback_queries": [
                    "it do go down robert boat waterfall",
                    "ice slide surrender fail cctv",
                    "person sliding helplessly driveway fail"
                ],
                "strict_visual_requirements": "Must show a person recognizing an inevitable impending fail and completely freezing or surrendering."
            }
        },
        "battling_gravity_losing": {
            "niche": "human_fails",
            "name": "Battling Gravity & Losing",
            "title_header": "Ranking Funniest",
            "subject_header": "Gravity Winning Moments",
            "version_tag": "(Balance Version)",
            "audio_hook": {
                "stem": "public/audio/stems/cartoon_slip.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 30,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 4.0, "freeze_seconds": 1.0, "aftermath_seconds": 1.5 },
            "harvester": {
                "primary_queries": ["ice slip struggling to balance fail shorts", "trampoline balance fail slide shorts", "ladder balance slip fail shorts"],
                "fallback_queries": ["hammock flip balance fail funny", "person slipping on ice trying to balance cctv"],
                "strict_visual_requirements": "Physical struggle against gravity on ladder, ice, roof, or hammock."
            }
        },
        "clumsy_public_moments": {
            "niche": "human_fails",
            "name": "Clumsy Public Moments",
            "title_header": "Ranking The Best",
            "subject_header": "Public Clumsy Moments",
            "version_tag": "(Awkward Version)",
            "audio_hook": {
                "stem": "public/audio/stems/glass_shatter.mp3",
                "trigger_timing": "at_impact",
                "freeze_frames": 25,
                "duck_native_volume": 0.25
            },
            "timing_rules": { "buildup_seconds": 3.0, "freeze_seconds": 0.8, "aftermath_seconds": 2.0 },
            "harvester": {
                "primary_queries": ["walking into clean glass door fail shorts", "tripping in public funny stumble shorts", "dropping food tray in cafeteria clumsy shorts"],
                "fallback_queries": ["person walks into glass window mall cctv", "public clumsy fall coffee drop"],
                "strict_visual_requirements": "Real-life tripping, walking into glass doors, or dropping items in public."
            }
        },
        "overconfident_humbled": {
            "niche": "human_fails",
            "name": "Overconfident Humbled",
            "title_header": "Ranking Best Of",
            "subject_header": "Overconfident Fails",
            "version_tag": "(Humbled Version)",
            "audio_hook": {
                "stem": "public/audio/stems/thud_whack.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 30,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 3.8, "freeze_seconds": 1.0, "aftermath_seconds": 1.5 },
            "harvester": {
                "primary_queries": ["parkour leap miscalculated fail shorts", "skateboard boast immediate fail shorts", "gymnastics stunt overconfident fail shorts"],
                "fallback_queries": ["showing off backflip fail grass", "bro thought he could jump fail"],
                "strict_visual_requirements": "Stunt failing immediately after showboating."
            }
        },
        "moments_before_impact": {
            "niche": "human_fails",
            "name": "Moments Before Impact",
            "title_header": "Ranking Craziest",
            "subject_header": "Before Disaster Moments",
            "version_tag": "(Realization Version)",
            "audio_hook": {
                "stem": "public/audio/stems/skyfall_this_is_the_end.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 40,
                "duck_native_volume": 0.15
            },
            "timing_rules": { "buildup_seconds": 3.0, "freeze_seconds": 1.3, "aftermath_seconds": 1.5 },
            "harvester": {
                "primary_queries": ["moment before disaster realization shorts", "frozen seconds before impact funny shorts", "fast moving ball hits camera realization shorts"],
                "fallback_queries": ["slow motion realization before impact", "frozen frame right before water balloon impact"],
                "strict_visual_requirements": "Object or obstacle about to make impact, frozen at realization frame."
            }
        },

        # --- NICHE 2: INSTANT REGRET & KARMA ---
        "road_rage_justice": {
            "niche": "instant_karma",
            "name": "Road Rage Justice",
            "title_header": "Ranking Funniest",
            "subject_header": "Road Rage Karma Moments",
            "version_tag": "(Justice Version)",
            "audio_hook": {
                "stem": "public/audio/stems/siren_short.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 30,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 4.5, "freeze_seconds": 1.0, "aftermath_seconds": 2.0 },
            "harvester": {
                "primary_queries": ["road rage instant karma dashcam shorts", "aggressive driver spins out dashcam shorts", "road rage police officer instant justice shorts"],
                "fallback_queries": ["convenient cop road rage dashcam", "brake check karma instant police dashcam"],
                "strict_visual_requirements": "Raw dashcam footage showing road rage retaliation or police intervention."
            }
        },
        "defying_warning_signs": {
            "niche": "instant_karma",
            "name": "Defying Warning Signs",
            "title_header": "Ranking Best Of",
            "subject_header": "Ignored Warning Signs",
            "version_tag": "(Instant Karma)",
            "audio_hook": {
                "stem": "public/audio/stems/record_scratch.mp3",
                "trigger_timing": "at_impact",
                "freeze_frames": 30,
                "duck_native_volume": 0.2
            },
            "timing_rules": { "buildup_seconds": 3.5, "freeze_seconds": 1.0, "aftermath_seconds": 1.8 },
            "harvester": {
                "primary_queries": ["ignoring danger sign immediate regret shorts", "person trespasses thin ice falls shorts", "touching wet paint consequence shorts"],
                "fallback_queries": ["stepping on thin ice sign ignored fail", "danger sign ignored instant consequence"],
                "strict_visual_requirements": "Ignoring clear warning signs or barriers with immediate physical consequence."
            }
        },
        "pranks_backfired": {
            "niche": "instant_karma",
            "name": "Pranks Backfired",
            "title_header": "Ranking Funniest",
            "subject_header": "Pranks Gone Wrong Moments",
            "version_tag": "(Countered Version)",
            "audio_hook": {
                "stem": "public/audio/stems/fail_buzzer.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 28,
                "duck_native_volume": 0.25
            },
            "timing_rules": { "buildup_seconds": 3.5, "freeze_seconds": 0.9, "aftermath_seconds": 1.8 },
            "harvester": {
                "primary_queries": ["prank backfires instantly on prankster shorts", "prankster caught countered instant regret shorts", "scare prank backfired target retaliates shorts"],
                "fallback_queries": ["jump scare prank counter punch real", "water bucket prank backfires on thrower"],
                "strict_visual_requirements": "Unscripted raw footage of prankster receiving immediate retaliation."
            }
        },
        "taunting_animals": {
            "niche": "instant_karma",
            "name": "Taunting Animals",
            "title_header": "Ranking The Best",
            "subject_header": "Animal Karma Moments",
            "version_tag": "(Nature Fights Back)",
            "audio_hook": {
                "stem": "public/audio/stems/thud_whack.mp3",
                "trigger_timing": "at_impact",
                "freeze_frames": 30,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 3.5, "freeze_seconds": 1.0, "aftermath_seconds": 1.6 },
            "harvester": {
                "primary_queries": ["person taunting goose gets attacked shorts", "taunting dog ram immediate karma shorts", "mocking monkey gets chased karma shorts"],
                "fallback_queries": ["goose attacks guy taunting it funny", "ram headbutts taunting man karma"],
                "strict_visual_requirements": "Person provoking goose, ram, or goat and getting charged."
            }
        },
        "cocky_challengers": {
            "niche": "instant_karma",
            "name": "Cocky Challengers",
            "title_header": "Ranking Best Of",
            "subject_header": "Early Celebration Fails",
            "version_tag": "(Humbled Fast)",
            "audio_hook": {
                "stem": "public/audio/stems/fail_buzzer.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 35,
                "duck_native_volume": 0.2
            },
            "timing_rules": { "buildup_seconds": 4.0, "freeze_seconds": 1.2, "aftermath_seconds": 1.8 },
            "harvester": {
                "primary_queries": ["early celebrator countered instantly shorts", "showboater getting knocked down shorts", "taunting opponent instant karma shorts"],
                "fallback_queries": ["taunting boxer gets countered instant knockout", "racing premature celebration lost at line"],
                "strict_visual_requirements": "Premature celebration or taunting that leads directly to instant counter."
            }
        },

        # --- NICHE 3: FUNNY ANIMALS & PETS ---
        "pets_being_dumb": {
            "niche": "funny_animals",
            "name": "Dogs Being Clumsy",
            "title_header": "Ranking Funniest",
            "subject_header": "Clumsy Dog Moments",
            "version_tag": "(Dog Version)",
            "audio_hook": {
                "stem": "public/audio/stems/cartoon_slip.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 30,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 3.0, "freeze_seconds": 1.0, "aftermath_seconds": 1.8 },
            "harvester": {
                "primary_queries": [
                    "dog runs into glass door shorts",
                    "dog slips hardwood floor fail shorts",
                    "dog jump fail funny shorts",
                    "dog sliding glass door funny shorts"
                ],
                "fallback_queries": [
                    "golden retriever slips on ice funny",
                    "puppy miscalculates couch jump fail"
                ],
                "strict_visual_requirements": "Real dog running into sliding glass door or slipping on hardwood floor."
            }
        },
        "pets_being_smart": {
            "niche": "funny_animals",
            "name": "Pets Being Smart",
            "title_header": "Ranking Smartest",
            "subject_header": "Genius Pet Moments",
            "version_tag": "(200 IQ Pets)",
            "audio_hook": {
                "stem": "public/audio/stems/skyfall_this_is_the_end.mp3",
                "trigger_timing": "at_impact",
                "freeze_frames": 25,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 4.0, "freeze_seconds": 0.8, "aftermath_seconds": 2.0 },
            "harvester": {
                "primary_queries": ["dog opens door latch smart shorts", "cat unlocks cage latch tool shorts", "smart dog solving puzzle escape shorts"],
                "fallback_queries": ["cat opens door handle smart", "dog unlatches gate escape clever"],
                "strict_visual_requirements": "Animals opening doors, unlocking latches, or manipulating tools."
            }
        },
        "animal_funny_moments": {
            "niche": "funny_animals",
            "name": "Animal Funny Moments",
            "title_header": "Ranking Best Of",
            "subject_header": "Animal Chaos Moments",
            "version_tag": "(Chaos Version)",
            "audio_hook": {
                "stem": "public/audio/stems/cartoon_slip.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 30,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 3.5, "freeze_seconds": 1.0, "aftermath_seconds": 1.5 },
            "harvester": {
                "primary_queries": ["cat zoomies wipeout funny shorts", "dog chaotic slide living room shorts", "funny animal crash blooper shorts"],
                "fallback_queries": ["cat drifts on rug into wall", "dog zoomies drift fail funny"],
                "strict_visual_requirements": "Unpredictable domestic pet chaos and zoomie wipeouts."
            }
        },
        "pets_in_slow_motion": {
            "niche": "funny_animals",
            "name": "Pets In Slow Motion",
            "title_header": "Ranking The Best",
            "subject_header": "Pets In Slow Motion",
            "version_tag": "(Slow Mo Version)",
            "audio_hook": {
                "stem": "public/audio/stems/skyfall_this_is_the_end.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 40,
                "duck_native_volume": 0.2
            },
            "timing_rules": { "buildup_seconds": 3.0, "freeze_seconds": 1.5, "aftermath_seconds": 1.5 },
            "harvester": {
                "primary_queries": ["dog catching treat slow motion fail shorts", "cat leaping awkward paws slow motion shorts", "pet slow motion face distortion shorts"],
                "fallback_queries": ["golden retriever treat catch slow mo fail", "cat jump fail slow motion"],
                "strict_visual_requirements": "Facial distortion and awkward paws during mid-air leaps."
            }
        },
        "animals_becoming_scarier": {
            "niche": "funny_animals",
            "name": "Animals Becoming Scarier",
            "title_header": "Ranking Craziest",
            "subject_header": "Uncanny Animal Moments",
            "version_tag": "(Eerie Version)",
            "audio_hook": {
                "stem": "public/audio/stems/record_scratch.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 35,
                "duck_native_volume": 0.2
            },
            "timing_rules": { "buildup_seconds": 3.5, "freeze_seconds": 1.2, "aftermath_seconds": 1.8 },
            "harvester": {
                "primary_queries": ["dog walks on hind legs eerie shorts", "cat sudden intense stare standing up shorts", "uncanny animal standing on two legs shorts"],
                "fallback_queries": ["dog walks like human standing up eerie", "cat stands on two legs staring into soul"],
                "strict_visual_requirements": "Sudden stare-downs, hind-leg walks, or uncharacteristic behavior."
            }
        },

        # --- NICHE 10: NATURE & WEATHER SURPRISES ---
        "ice_driveway_slides": {
            "niche": "nature_weather",
            "name": "Ice Driveway Slides",
            "title_header": "Ranking Best Of",
            "subject_header": "Ice Driveway Slides",
            "version_tag": "(Icy Slopes)",
            "audio_hook": {
                "stem": "public/audio/stems/skyfall_this_is_the_end.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 36,
                "duck_native_volume": 0.2
            },
            "timing_rules": { "buildup_seconds": 3.5, "freeze_seconds": 1.2, "aftermath_seconds": 2.0 },
            "harvester": {
                "primary_queries": [
                    "uncontrollable slide down frozen driveway ice shorts",
                    "person sliding down icy driveway helplessly shorts",
                    "frozen driveway slide fail funny shorts"
                ],
                "fallback_queries": [
                    "steep driveway ice slide fail cctv",
                    "trash can icy driveway slide slip"
                ],
                "strict_visual_requirements": "Uncontrollable slides down frozen driveways captured on CCTV or phone."
            }
        },
        "sudden_wind_ruining_events": {
            "niche": "nature_weather",
            "name": "Sudden Wind Ruining Events",
            "title_header": "Ranking The Worst",
            "subject_header": "Wind Ruined Moments",
            "version_tag": "(Storm Version)",
            "audio_hook": {
                "stem": "public/audio/stems/cartoon_slip.mp3",
                "trigger_timing": "at_impact",
                "freeze_frames": 25,
                "duck_native_volume": 0.3
            },
            "timing_rules": { "buildup_seconds": 3.0, "freeze_seconds": 0.8, "aftermath_seconds": 2.0 },
            "harvester": {
                "primary_queries": ["sudden wind gusts umbrella inside out shorts", "bounce house canopy blown away wind storm shorts", "gust of wind tent umbrella blown away shorts"],
                "fallback_queries": ["canopy blown away backyard wind", "patio umbrella flies away wind gust"],
                "strict_visual_requirements": "Canopies, bounce houses, or umbrellas blown away by sudden gusts."
            }
        },
        "rogue_waves": {
            "niche": "nature_weather",
            "name": "Rogue Waves",
            "title_header": "Ranking Best Of",
            "subject_header": "Beach Sneak Waves",
            "version_tag": "(Wave Version)",
            "audio_hook": {
                "stem": "public/audio/stems/skyfall_this_is_the_end.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 35,
                "duck_native_volume": 0.2
            },
            "timing_rules": { "buildup_seconds": 3.5, "freeze_seconds": 1.2, "aftermath_seconds": 2.0 },
            "harvester": {
                "primary_queries": ["rogue wave washes away beach chairs towels shorts", "shoreline surge surprise beachgoers soaked shorts", "unexpected ocean wave sweeps beach chairs shorts"],
                "fallback_queries": ["sneaker wave beach chairs washed away", "high tide surprise beach picnic wave"],
                "strict_visual_requirements": "Shoreline surges washing beach chairs, towels, or sunbathers out."
            }
        },
        "wildlife_close_calls": {
            "niche": "nature_weather",
            "name": "Wildlife Close Calls",
            "title_header": "Ranking Craziest",
            "subject_header": "Wildlife Close Calls",
            "version_tag": "(Tourist Encounters)",
            "audio_hook": {
                "stem": "public/audio/stems/record_scratch.mp3",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 30,
                "duck_native_volume": 0.25
            },
            "timing_rules": { "buildup_seconds": 4.0, "freeze_seconds": 1.0, "aftermath_seconds": 1.8 },
            "harvester": {
                "primary_queries": ["wildlife close call tourist bear moose outdoor shorts", "animal approaches campsite tourist close call shorts", "wild animal surprise encounter camera shorts"],
                "fallback_queries": ["bear approaches campsite porch close call", "bison walks past tourists yellowstone"],
                "strict_visual_requirements": "Real animal approaching outdoor tourists or porches unexpectedly."
            }
        },
        "lightning_jump_scares": {
            "niche": "nature_weather",
            "name": "Lightning Jump Scares",
            "title_header": "Ranking The Best",
            "subject_header": "Lightning Jump Scares",
            "version_tag": "(Thunder Shock)",
            "audio_hook": {
                "stem": "public/audio/stems/thud_whack.mp3",
                "trigger_timing": "at_impact",
                "freeze_frames": 25,
                "duck_native_volume": 0.2
            },
            "timing_rules": { "buildup_seconds": 3.0, "freeze_seconds": 0.8, "aftermath_seconds": 1.8 },
            "harvester": {
                "primary_queries": ["nearby lightning strike jump scare security camera shorts", "lightning strikes tree next to house camera scream shorts", "close lightning strike security camera thunder shorts"],
                "fallback_queries": ["lightning strike tree backyard ring camera", "close lightning strike storm phone video scream"],
                "strict_visual_requirements": "Nearby lightning strike captured on home security or phone video."
            }
        }
    }
}

# Auto-expand remaining niches/subcategories with dedicated templates
all_subcats_raw = [
    ("aura_debt", "one_million_aura_loss", "Ranking The Worst", "-1,000,000 Aura Moments", "(Aura Loss)", "skyfall_this_is_the_end.mp3", ["trying to look cool slipping entrance shorts", "smooth swagger immediate fail shorts"]),
    ("aura_debt", "failed_swagger_poses", "Ranking Funniest", "Failed Swagger Moments", "(Swagger Fails)", "fail_buzzer.mp3", ["sunglasses falling off cool pose shorts", "slipping out of sports car fail shorts"]),
    ("aura_debt", "left_hanging_public", "Ranking The Most", "Left Hanging Moments", "(Awkward Version)", "record_scratch.mp3", ["handshake ignored broadcast live tv shorts", "left hanging stage high five miss shorts"]),
    ("aura_debt", "luxury_flexes_backfiring", "Ranking The Best", "Luxury Flexes Fails", "(Expensive Mistakes)", "fail_buzzer.mp3", ["expensive car stunt fails immediate regret shorts", "luxury watch flex dropped water shorts"]),
    ("aura_debt", "adults_humbled_by_kids", "Ranking The Funniest", "Adults Humbled By Kids", "(Humbling Version)", "thud_whack.mp3", ["adult losing sports challenge kid shorts", "dad humbled by toddler physical game shorts"]),
    
    ("sports_bloopers", "athletes_celebrating_too_early", "Ranking The Worst", "Early Celebrations", "(Don't Celebrate Yet)", "fail_buzzer.mp3", ["runner celebrates early loses at finish line shorts", "cycling premature celebration lost shorts"]),
    ("sports_bloopers", "trickshot_disasters", "Ranking Craziest", "Trickshot Disasters", "(Disaster Version)", "glass_shatter.mp3", ["trickshot breaks tv window fail shorts", "ping pong trickshot breaks lamp shorts"]),
    ("sports_bloopers", "goalkeeper_brainfades", "Ranking The Worst", "Goalkeeper Brainfades", "(Goalie Blunders)", "fail_buzzer.mp3", ["goalkeeper drops routine catch own goal shorts", "soccer goalkeeper brainfade blunder shorts"]),
    ("sports_bloopers", "gymnast_routine_mishaps", "Ranking Best Of", "Gymnast Mishap Moments", "(Landing Fails)", "cartoon_slip.mp3", ["gymnast balance beam slip mat shorts", "vault landing slides into mats fail shorts"]),
    ("sports_bloopers", "referee_collisions", "Ranking Funniest", "Referee Collisions", "(Ref Fails)", "thud_whack.mp3", ["referee collision knocked down player shorts", "umpire obstructed by player collision shorts"]),
    
    ("npc_glitches", "unrendered_game_npcs", "Ranking Craziest", "Real-Life NPC Glitches", "(Matrix Version)", "record_scratch.mp3", ["person t pose rigid public real life shorts", "blank stare motionless stranger public shorts"]),
    ("npc_glitches", "dialogue_loop_real_life", "Ranking Funniest", "Real-Life Dialogue Loops", "(Looping NPCs)", "record_scratch.mp3", ["person repeating gestures compulsive loop shorts", "real life dialogue loop glitch shorts"]),
    ("npc_glitches", "pathfinding_ai_broken", "Ranking The Best", "Broken Pathfinding NPCs", "(Glitch Version)", "cartoon_slip.mp3", ["person walks into glass obstacle repeatedly shorts", "pathfinding broken walking into barrier shorts"]),
    ("npc_glitches", "object_collision_fails", "Ranking The Most", "Object Collision Fails", "(Physics Broken)", "thud_whack.mp3", ["person drops item hand collision fail shorts", "object drops through hands glitch shorts"]),
    ("npc_glitches", "npc_idle_animations", "Ranking Craziest", "Synchronized NPCs", "(Matrix Glitches)", "record_scratch.mp3", ["synchronized unacquainted strangers public shorts", "strangers moving in identical cadence glitch shorts"]),
    
    ("workplace_disasters", "worst_shift_ever", "Ranking The Worst", "Worst Shift Moments", "(Disaster At Work)", "skyfall_this_is_the_end.mp3", ["worker spills bulk paint commercial warehouse shorts", "dropping huge milk flour pallet shift shorts"]),
    ("workplace_disasters", "forklift_domino_disasters", "Ranking Craziest", "Forklift Domino Fails", "(Warehouse Collapse)", "thud_whack.mp3", ["forklift bumps warehouse rack collapse domino shorts", "warehouse racks collapsing forklift accident shorts"]),
    ("workplace_disasters", "commercial_kitchen_nightmares", "Ranking The Worst", "Commercial Kitchen Fails", "(Kitchen Disasters)", "glass_shatter.mp3", ["dropping massive soup vat commercial kitchen shorts", "chef dropping multi tier wedding cake disaster shorts"]),
    ("workplace_disasters", "retail_display_rampage", "Ranking Funniest", "Retail Display Collapses", "(Aisle 4 Version)", "cartoon_slip.mp3", ["knocking over display pyramid supermarket shorts", "store can pyramid collapse accident shorts"]),
    ("workplace_disasters", "delivery_driver_mishaps", "Ranking Best Of", "Delivery Driver Slips", "(Porch Glides)", "skyfall_this_is_the_end.mp3", ["delivery driver slides down icy driveway shorts", "delivery driver falls on icy porch slip shorts"]),
    
    ("extreme_luck", "used_all_luck_for_life", "Ranking The Most", "Used All Luck For Life", "(Near Misses)", "skyfall_this_is_the_end.mp3", ["close call evasion falling tree vehicle inches shorts", "pedestrian narrowly avoids falling object inches shorts"]),
    ("extreme_luck", "accidental_trickshots", "Ranking Smartest", "Accidental Trickshots", "(100% Calculated)", "skyfall_this_is_the_end.mp3", ["dropped item bounces into cup upright shorts", "accidental trickshot landing bottle cup shorts"]),
    ("extreme_luck", "physics_defying_saves", "Ranking The Best", "Physics-Defying Saves", "(Miracle Saves)", "skyfall_this_is_the_end.mp3", ["ejected rider lands on feet motorcycle bicycle shorts", "skater ejected lands on feet physics defying shorts"]),
    ("extreme_luck", "unintentional_hero_catches", "Ranking Craziest", "Dad Reflex Catches", "(Dad Reflexes)", "skyfall_this_is_the_end.mp3", ["blind catch falling phone beverage infant shorts", "dad reflex blind catch falling item shorts"]),
    ("extreme_luck", "vehicle_360_recoveries", "Ranking The Best", "Vehicle 360 Recoveries", "(Clean 360s)", "siren_short.mp3", ["highway complete 360 spinout continues unharmed shorts", "car 360 spin recover in lane dashcam shorts"]),
    
    ("gym_bloopers", "bench_press_ego_fails", "Ranking The Worst", "Bench Press Ego Fails", "(Ego Lifting)", "thud_whack.mp3", ["bench press overloaded bar pins lifter fail shorts", "lifter dumps plates bench press ego fail shorts"]),
    ("gym_bloopers", "treadmill_slingshots", "Ranking Funniest", "Treadmill Slingshots", "(Max Speed Ejection)", "cartoon_slip.mp3", ["excessive treadmill speed launches runner backward shorts", "treadmill slingshot gym fail funny shorts"]),
    ("gym_bloopers", "squat_rack_blunders", "Ranking The Best", "Squat Rack Blunders", "(Bail Fails)", "thud_whack.mp3", ["squat rack lifter dumps bar on safeties shorts", "unable to stand up heavy squat bail fail shorts"]),
    ("gym_bloopers", "equipment_misuse", "Ranking Funniest", "Gym Equipment Misuse", "(Wrong Exercises)", "record_scratch.mp3", ["using gym machine backwards hilarious shorts", "inverted cable machine gym misuse blooper shorts"]),
    ("gym_bloopers", "spotter_distracted", "Ranking The Worst", "Distracted Spotter Moments", "(One Job)", "fail_buzzer.mp3", ["spotter looks away lifter misses rack shorts", "distracted gym spotter fail missed bar shorts"])
]

for niche, sub_id, pfx, subj, tag, stem, queries in all_subcats_raw:
    if sub_id not in registry["subcategories"]:
        registry["subcategories"][sub_id] = {
            "niche": niche,
            "name": subj,
            "title_header": pfx,
            "subject_header": subj,
            "version_tag": tag,
            "audio_hook": {
                "stem": f"public/audio/stems/{stem}",
                "trigger_timing": "at_climax_freeze",
                "freeze_frames": 36 if "skyfall" in stem else 28,
                "duck_native_volume": 0.25
            },
            "timing_rules": {
                "buildup_seconds": 3.5,
                "freeze_seconds": 1.2 if "skyfall" in stem else 0.9,
                "aftermath_seconds": 1.6
            },
            "harvester": {
                "primary_queries": queries,
                "fallback_queries": [q.replace("shorts", "cctv") for q in queries],
                "strict_visual_requirements": f"Real unedited footage depicting {subj}."
            }
        }

out_path = "src/pipeline/master_category_registry.json"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(registry, f, indent=2)

print(f"Successfully generated Master Category Registry with {len(registry['subcategories'])} subcategories!")
