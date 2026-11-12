import * as fs from 'fs';
import * as path from 'path';

export interface KineticTypographyConfig {
  text: string;
  color: string;
  rotation: number;
}

export interface TimingRecipeConfig {
  setupSec: number;
  aftermathSec: number;
  freezeHoldSec: number;
}

export interface SubCategory {
  id: string;
  name: string;
  strictDefinition: string;
  searchQueries: string[];
  subreddits: string[];
  audioStem: string;
  kineticTypography: KineticTypographyConfig;
  timingRecipe: TimingRecipeConfig;
  negativeFilters: string[];
  situationalPrompt: string;
  aliases?: string[];
}

export interface Niche {
  id: string;
  name: string;
  subCategories: SubCategory[];
}

export const NICHE_GRAPH: Niche[] = [
  // ============================================================
  // NICHE 1: HUMAN PHYSICAL FAILS (human_fails)
  // ============================================================
  {
    id: 'human_fails',
    name: 'Human Physical Fails',
    subCategories: [
      {
        id: 'people_accepting_fate',
        name: 'People Accepting Fate',
        strictDefinition: 'Must show a person recognizing an inevitable impending fail and completely freezing or surrendering with resignation.',
        searchQueries: ['he accepted his fate fail', 'person accepts fate fail shorts', 'he gave up mid fall fail'],
        subreddits: ['WatchPeopleDieInside', 'Instant_Regret'],
        audioStem: 'skyfall_stem.mp3',
        kineticTypography: { text: 'THIS IS THE END', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.2, freezeHoldSec: 2.2 },
        negativeFilters: ['cat', 'dog', 'animation', 'podcast', 'gaming', 'cgi'],
        situationalPrompt: 'Clear moment of surrender where a person stops struggling mid-fall, slide, or descent.',
      },
      {
        id: 'battling_gravity_losing',
        name: 'Battling Gravity & Losing',
        strictDefinition: 'Must show a physical balance struggle on ladders, roofs, trampolines, ice, or hammock flips.',
        searchQueries: ['losing battle with gravity ladder', 'ice slip struggling to balance fail', 'balance fail slide'],
        subreddits: ['HoldMyBeer', 'FullScorpion'],
        audioStem: 'cartoon_slip.mp3',
        kineticTypography: { text: 'GRAVITY WON 💥', color: '#FFE600', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['serious injury', 'hospital', 'gaming', 'cgi', 'podcast'],
        situationalPrompt: 'Physical balance struggle on ladders, roofs, trampolines, ice, or hammock flips.',
        aliases: ['clumsy_stumbles'],
      },
      {
        id: 'clumsy_moments_public',
        name: 'Clumsy Moments In Public',
        strictDefinition: 'Must show tripping, dropping items, or walking into glass doors in public settings.',
        searchQueries: ['tripping in public funny fail', 'walking into glass window door', 'dropping tray in public awkward'],
        subreddits: ['cringe', 'WatchPeopleDieInside'],
        audioStem: 'sad_trombone.mp3',
        kineticTypography: { text: 'DIGNITY: 0% 🤦‍♂️', color: '#00E5FF', rotation: -11 },
        timingRecipe: { setupSec: 4.0, aftermathSec: 0.8, freezeHoldSec: 2.0 },
        negativeFilters: ['gaming', 'cgi', 'podcast', 'staged'],
        situationalPrompt: 'Tripping, dropping items, or walking into glass doors in public settings.',
        aliases: ['clumsy_public_moments'],
      },
      {
        id: 'overconfident_humbled',
        name: 'Overconfident People Humbled',
        strictDefinition: 'Must show stunts (skate, parkour, gymnastics) failing immediately after a boast or setup.',
        searchQueries: ['parkour leap miscalculated fail', 'skateboard boast immediate fail', 'gymnastics stunt overconfident fail'],
        subreddits: ['Instant_Regret', 'Whatcouldgowrong'],
        audioStem: 'frying_pan_bonk.mp3',
        kineticTypography: { text: 'HUMBLING COMPLETE 💀', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 2.5, aftermathSec: 0.5, freezeHoldSec: 2.2 },
        negativeFilters: ['gymnastics pro', 'olympics', 'animation', 'podcast'],
        situationalPrompt: 'Stunts (skate, parkour, gymnastics) failing immediately after a boast or setup.',
        aliases: ['miscalculated_jumps'],
      },
      {
        id: 'moments_before_impact',
        name: 'Moments Before Impact',
        strictDefinition: 'Must show fast-moving objects or collisions frozen at the point of realization.',
        searchQueries: ['fast moving object freeze before impact', 'moment before disaster realization', 'collision frozen at point of impact'],
        subreddits: ['OneSecondBeforeDisast', 'PerfectTiming'],
        audioStem: 'sub_bass_slam.mp3',
        kineticTypography: { text: '1 SECOND BEFORE DISASTER ⚠️', color: '#FFE600', rotation: -11 },
        timingRecipe: { setupSec: 4.0, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['advertisement', 'review', 'podcast', 'gaming'],
        situationalPrompt: 'Fast-moving objects or collisions frozen at the point of realization.',
        aliases: ['everyday_malfunctions', 'diy_disasters'],
      },
    ],
  },

  // ============================================================
  // NICHE 2: INSTANT REGRET & KARMA (instant_karma)
  // ============================================================
  {
    id: 'instant_karma',
    name: 'Instant Regret & Karma',
    subCategories: [
      {
        id: 'defying_warning_signs',
        name: 'Defying Warning Signs',
        strictDefinition: 'Must show a person physically trespassing or ignoring safety barriers (thin ice, wet paint, danger signs).',
        searchQueries: ['ignoring danger sign immediate regret', 'person trespasses thin ice falls', 'touching wet paint consequence'],
        subreddits: ['Whatcouldgowrong', 'Instant_Regret'],
        audioStem: 'warning_siren.mp3',
        kineticTypography: { text: 'THE SIGN WAS RIGHT ⚠️', color: '#FFE600', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['movie clip', 'animation', 'podcast'],
        situationalPrompt: 'Person physically trespassing or ignoring safety barriers (thin ice, wet paint, danger signs).',
        aliases: ['cutting_in_line'],
      },
      {
        id: 'pranks_backfired_instantly',
        name: 'Pranks Backfired Instantly',
        strictDefinition: 'Must show an intended prankster getting immediately hit, tackled, or exposed.',
        searchQueries: ['prank backfires instantly on prankster', 'prank gone wrong instant regret', 'scare prank turns into hit'],
        subreddits: ['Instant_Regret', 'Whatcouldgowrong'],
        audioStem: 'metal_gear_alert.mp3',
        kineticTypography: { text: 'PRANK CANCELLED 🚫', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['scripted', 'staged', 'vlog', 'reaction'],
        situationalPrompt: 'An intended prankster getting immediately hit, tackled, or exposed.',
        aliases: ['pranks_backfired'],
      },
      {
        id: 'taunting_animals_gone_wrong',
        name: 'Taunting Animals Gone Wrong',
        strictDefinition: 'Must show a human teasing a bird, goat, goose, or wild animal and getting charged.',
        searchQueries: ['taunting goose gets chased', 'teasing goat headbutt instant regret', 'scaring cat gets attacked back'],
        subreddits: ['AnimalsBeingJerks', 'Instant_Regret'],
        audioStem: 'jaws_theme.mp3',
        kineticTypography: { text: 'WRONG TARGET 🪿', color: '#00E676', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.2, freezeHoldSec: 2.2 },
        negativeFilters: ['animal abuse', 'poaching', 'zoo pro'],
        situationalPrompt: 'A human teasing a bird, goat, goose, or wild animal and getting charged.',
        aliases: ['taunting_animals'],
      },
      {
        id: 'road_rage_instant_justice',
        name: 'Road Rage Instant Justice',
        strictDefinition: 'Must show aggressive driving, brake-checking, or improper passing pulled over immediately by police.',
        searchQueries: ['brake check instant karma convenient cop', 'road rage pass unmarked cop pullover', 'aggressive driver spins out highway'],
        subreddits: ['IdiotsInCars', 'ConvenientCop'],
        audioStem: 'curb_horn.mp3',
        kineticTypography: { text: 'INSTANT JUSTICE 🚔', color: '#00E5FF', rotation: -11 },
        timingRecipe: { setupSec: 4.5, aftermathSec: 2.0, freezeHoldSec: 2.0 },
        negativeFilters: ['fatal crash', 'blood', 'gta', 'beamng'],
        situationalPrompt: 'Aggressive driving, brake-checking, or improper passing pulled over immediately by police.',
        aliases: ['road_rage_justice'],
      },
      {
        id: 'cocky_challengers_humbled',
        name: 'Cocky Challengers Humbled',
        strictDefinition: 'Must show an arrogant competitor taunting before getting instantly countered or defeated.',
        searchQueries: ['cocky fighter gets knocked out', 'trash talker arm wrestle instant lose', 'showboating streetball humbled'],
        subreddits: ['Prematurecelebration', 'Instant_Regret'],
        audioStem: 'record_scratch.mp3',
        kineticTypography: { text: 'EGO CHECKED 🥊', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 0.8, freezeHoldSec: 2.0 },
        negativeFilters: ['ufc full match', 'boxing highlights', 'podcast'],
        situationalPrompt: 'An arrogant competitor taunting before getting instantly countered or defeated.',
        aliases: ['cocky_challengers'],
      },
    ],
  },

  // ============================================================
  // NICHE 3: FUNNY ANIMALS & PETS (funny_animals)
  // ============================================================
  {
    id: 'funny_animals',
    name: 'Funny Animals & Pets',
    subCategories: [
      {
        id: 'pets_being_dumb',
        name: 'Pets Being Dumb',
        strictDefinition: 'Must show cats or dogs making miscalculated jumps, running into glass doors, or derping.',
        searchQueries: ['dog misses jump into couch fail', 'cat jumps into glass door fail', 'orange cat zero brain cells funny'],
        subreddits: ['OneOrangeBraincell', 'Catculations'],
        audioStem: 'boing.mp3',
        kineticTypography: { text: '0 BRAINCELLS 🐱', color: '#FFE600', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['pet training', 'vet advice', 'sad pet'],
        situationalPrompt: 'Cats or dogs making miscalculated jumps, running into glass doors, or derping.',
      },
      {
        id: 'pets_being_smart',
        name: 'Pets Being Smart',
        strictDefinition: 'Must show dogs or cats opening doors, using tools, or outsmarting baby gates.',
        searchQueries: ['cat opens door latch handle', 'smart dog solves puzzle gate', 'pet escapes enclosure clever'],
        subreddits: ['Catculations', 'AnimalsBeingGenius'],
        audioStem: 'chime_sparkle.mp3',
        kineticTypography: { text: '200 IQ PLAY 🧠', color: '#00E5FF', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['pet product review', 'tutorial', 'talking dog'],
        situationalPrompt: 'Dogs or cats opening doors, using tools, or outsmarting baby gates.',
      },
      {
        id: 'animal_funny_moments',
        name: 'Animal Funny Moments',
        strictDefinition: 'Must show unexpected funny animal behavior, erratic zoomies, or playful antics.',
        searchQueries: ['dog zoomies furniture crash slip', 'funny ferret chaos energy', 'parrot laughing chaos moments'],
        subreddits: ['AnimalsBeingDerps', 'Zoomies'],
        audioStem: 'frying_pan_bonk.mp3',
        kineticTypography: { text: 'CHAOS AGENT 🌪️', color: '#FF007F', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['wildlife documentary', 'sad animal', 'compilation 10 hours'],
        situationalPrompt: 'Unexpected funny animal behavior, erratic zoomies, or playful antics.',
      },
      {
        id: 'pets_revealing_true_self',
        name: 'Pets In Slow Motion',
        strictDefinition: 'Must show pets in high framerate slow-motion catching treats or jumping gracefully.',
        searchQueries: ['dog catching treat slow motion face', 'cat jumping slow motion derp', 'pets in slow motion hilarious faces'],
        subreddits: ['holdmycatnip', 'aww'],
        audioStem: 'ave_maria.mp3',
        kineticTypography: { text: 'TRUE FORM REVEALED 🎭', color: '#FFD700', rotation: -11 },
        timingRecipe: { setupSec: 1.5, aftermathSec: 4.0, freezeHoldSec: 2.0 },
        negativeFilters: ['normal speed', 'low fps', 'blur'],
        situationalPrompt: 'Pets in high framerate slow-motion catching treats or jumping gracefully.',
        aliases: ['pets_in_slow_motion'],
      },
      {
        id: 'animal_becoming_scarier',
        name: 'Animals Becoming Scarier',
        strictDefinition: 'Must show pets standing on hind legs, staring intently, or doing uncanny humanoid postures.',
        searchQueries: ['dog standing on two legs looking creepy', 'cat standing like human staring', 'pets acting unnatural uncanny'],
        subreddits: ['CryptidDogs', 'WhatsWrongWithYourDog'],
        audioStem: 'horror_drone.mp3',
        kineticTypography: { text: 'UNNATURAL BEHAVIOR 👁️', color: '#D50000', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 2.5, freezeHoldSec: 2.0 },
        negativeFilters: ['aggressive dog bite', 'rabies', 'attack'],
        situationalPrompt: 'Pets standing on hind legs, staring intently, or doing uncanny humanoid postures.',
        aliases: ['animals_becoming_scarier'],
      },
    ],
  },

  // ============================================================
  // NICHE 4: INFINITE AURA & EGO LOSS (aura_debt)
  // ============================================================
  {
    id: 'aura_debt',
    name: 'Infinite Aura & Ego Loss',
    subCategories: [
      {
        id: 'moments_cost_infinite_aura',
        name: '-1,000,000 Aura Moments',
        strictDefinition: 'Must show an embarrassing stumble or fail wiping out social credit/coolness instantly.',
        searchQueries: ['cool guy trip aura loss fail', 'flip attempt faceplant aura loss', 'minus one million aura moments'],
        subreddits: ['WatchPeopleDieInside', 'cringe'],
        audioStem: 'phonk_bass.mp3',
        kineticTypography: { text: '-1,000,000 AURA 📉', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.2, freezeHoldSec: 2.2 },
        negativeFilters: ['gaming', 'podcast', 'talking head'],
        situationalPrompt: 'Embarrassing stumble or fail wiping out social credit/coolness instantly.',
        aliases: ['one_million_aura_loss'],
      },
      {
        id: 'trying_to_look_cool_gone_wrong',
        name: 'Failed Swagger & Poses',
        strictDefinition: 'Must show someone posing for camera, model walking, or attempting swagger and failing.',
        searchQueries: ['trying to look cool fail walk', 'model walk into street pole', 'sunglasses flip fail stumble'],
        subreddits: ['cringe', 'Instant_Regret'],
        audioStem: 'sad_flute.mp3',
        kineticTypography: { text: 'SIGMA CANCELLED 🚫', color: '#FFE600', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['staged skit', 'commercial', 'tiktok dance'],
        situationalPrompt: 'Someone posing for camera, model walking, or attempting swagger and failing.',
        aliases: ['failed_swagger_poses'],
      },
      {
        id: 'high_stakes_aura_gambles',
        name: 'High Stakes Aura Gambles',
        strictDefinition: 'Must show luxury car revving, expensive bottle drops, or high-stakes stunts failing.',
        searchQueries: ['revving sports car spins out leaving meet', 'expensive bottle pop drop shatter', 'luxury flex gone wrong fail'],
        subreddits: ['mildlybadass', 'IdiotsInCars'],
        audioStem: 'glass_shatter.mp3',
        kineticTypography: { text: 'AURA BANKRUPT 💸', color: '#FFD700', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 0.8, freezeHoldSec: 2.0 },
        negativeFilters: ['car review', 'vlog', 'dealership ad'],
        situationalPrompt: 'Luxury car revving, expensive bottle drops, or high-stakes stunts failing.',
        aliases: ['luxury_flexes_backfiring'],
      },
      {
        id: 'devastating_public_stumbles',
        name: 'Devastating Public Stumbles',
        strictDefinition: 'Must show a public stumble where subject pretends nothing happened or pretends to jog.',
        searchQueries: ['slip in public pretending to jog', 'slide into seat after stumble public', 'awkward stumble recovery pretending nothing happened'],
        subreddits: ['HoldMyBeer', 'cringe'],
        audioStem: 'record_scratch.mp3',
        kineticTypography: { text: 'PHANTOM ITCH ROUTINE 🤦', color: '#00E5FF', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['scripted', 'staged', 'podcast'],
        situationalPrompt: 'Public stumble where subject pretends nothing happened or pretends to jog.',
      },
      {
        id: 'romantic_aura_debt_fails',
        name: 'Romantic Aura Debt Fails',
        strictDefinition: 'Must show rejected high-fives, kiss cam swerves, or romantic overtures left hanging.',
        searchQueries: ['kiss cam rejection turned cheek', 'left hanging handshake broadcast', 'rejected high five in 4k'],
        subreddits: ['cringe', 'WatchPeopleDieInside'],
        audioStem: 'bruh.mp3',
        kineticTypography: { text: 'LEFT HANGING IN 4K ✋', color: '#B0BEC5', rotation: -11 },
        timingRecipe: { setupSec: 2.5, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['acting', 'movie clip', 'podcast interview'],
        situationalPrompt: 'Rejected high-fives, kiss cam swerves, or romantic overtures left hanging.',
        aliases: ['left_hanging_public', 'adults_humbled_by_kids'],
      },
    ],
  },

  // ============================================================
  // NICHE 5: REAL-LIFE GLITCHES & NPCS (npc_glitches)
  // ============================================================
  {
    id: 'npc_glitches',
    name: 'Real-Life Glitches & NPCs',
    subCategories: [
      {
        id: 'unrendered_game_npcs',
        name: 'Unrendered Game NPCs',
        strictDefinition: 'Must show people in public standing completely still, unresponsive, or frozen mid-step.',
        searchQueries: ['person standing completely still npc', 'npc in real life standing motionless', 'glitch in the matrix person frozen'],
        subreddits: ['NPC_irl', 'GlitchInTheMatrix'],
        audioStem: 'oblivion_harp.mp3',
        kineticTypography: { text: 'NPC DETECTED 🤖', color: '#76FF03', rotation: -11 },
        timingRecipe: { setupSec: 4.0, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['skyrim game', 'gta mod', 'video game'],
        situationalPrompt: 'People in public standing completely still, unresponsive, or frozen mid-step.',
      },
      {
        id: 'dialogue_loop_real_life',
        name: 'Dialogue Loops in Real Life',
        strictDefinition: 'Must show repetitive speech patterns, broken phrases, or customer service loops.',
        searchQueries: ['person repeating same sentence loop', 'npc dialogue loop real life subway', 'repeated glitch phrase in public'],
        subreddits: ['GlitchInTheMatrix', 'NPC_irl'],
        audioStem: 'glitch_loop.mp3',
        kineticTypography: { text: 'DIALOGUE LOOP 🔁', color: '#18FFFF', rotation: -11 },
        timingRecipe: { setupSec: 2.0, aftermathSec: 3.0, freezeHoldSec: 2.0 },
        negativeFilters: ['song remix', 'tiktok voice filter', 'podcast'],
        situationalPrompt: 'Repetitive speech patterns, broken phrases, or customer service loops.',
      },
      {
        id: 'pathfinding_ai_broken',
        name: 'Pathfinding Broken',
        strictDefinition: 'Must show people walking repeatedly into barriers, glass panes, or getting trapped by simple obstacles.',
        searchQueries: ['walking into glass door repeatedly', 'pathfinding broken person stuck on barrier', 'real life npc stuck in door frame'],
        subreddits: ['NPC_irl', 'GlitchInTheMatrix'],
        audioStem: 'windows_error.mp3',
        kineticTypography: { text: 'PATHFINDING ERROR 404', color: '#FFD600', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['gameplay', 'unity tutorial', 'unreal engine'],
        situationalPrompt: 'People walking repeatedly into barriers, glass panes, or getting trapped by simple obstacles.',
      },
      {
        id: 'object_collision_fails',
        name: 'Object Collision Fails',
        strictDefinition: 'Must show objects suspended in mid-air, wedged impossibly, or appearing to float.',
        searchQueries: ['object floating illusion glitch', 'item wedged impossibly in wall', 'matrix collision bug in real life'],
        subreddits: ['GlitchInTheMatrix', 'mildlyinteresting'],
        audioStem: 'digital_chirp.mp3',
        kineticTypography: { text: 'COLLISION ENGINE BROKE ⚠️', color: '#F50057', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['magic trick tutorial', 'cgi', 'blender render'],
        situationalPrompt: 'Objects suspended in mid-air, wedged impossibly, or appearing to float.',
      },
      {
        id: 'npc_idle_animations',
        name: 'Synchronized Stranger Idles',
        strictDefinition: 'Must show strangers in crowds doing identical motions or turns simultaneously.',
        searchQueries: ['strangers moving in sync in public', 'synchronized idle animation crowd', 'subway synchronized glitch'],
        subreddits: ['GlitchInTheMatrix', 'NPC_irl'],
        audioStem: 'synth_drone.mp3',
        kineticTypography: { text: 'SYNCHRONIZED IDLES 👥', color: '#00E676', rotation: -11 },
        timingRecipe: { setupSec: 4.5, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['flash mob', 'choreographed dance', 'theater'],
        situationalPrompt: 'Strangers in crowds doing identical motions or turns simultaneously.',
      },
    ],
  },

  // ============================================================
  // NICHE 6: SPORTS & ATHLETIC BLOOPERS (sports_bloopers)
  // ============================================================
  {
    id: 'sports_bloopers',
    name: 'Sports & Athletic Bloopers',
    subCategories: [
      {
        id: 'athletes_celebrating_too_early',
        name: 'Celebrating Too Early',
        strictDefinition: 'Must show athletes raising arms or slowing down before the line and getting passed.',
        searchQueries: ['runner celebrates too early passed at finish line', 'cycling premature celebration overtaken', 'football celebrating before touchdown stripped'],
        subreddits: ['Prematurecelebration', 'sports'],
        audioStem: 'sad_trombone.mp3',
        kineticTypography: { text: 'PREMATURE CELEBRATION 💀', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['full game replay', 'interview', 'talk show'],
        situationalPrompt: 'Athletes raising arms or slowing down before the line and getting passed.',
      },
      {
        id: 'trickshot_disasters',
        name: 'Trickshot Disasters',
        strictDefinition: 'Must show trickshots bouncing off targets and smashing household items.',
        searchQueries: ['basketball ricochet breaks chandelier', 'ping pong trickshot breaks television', 'golf swing indoor mirror smash'],
        subreddits: ['Whatcouldgowrong', 'Instant_Regret'],
        audioStem: 'glass_shatter.mp3',
        kineticTypography: { text: 'TRICKSHOT FAILED 🎯', color: '#FFEE58', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 0.5, freezeHoldSec: 2.0 },
        negativeFilters: ['dude perfect official', 'successful trickshot', 'vlog'],
        situationalPrompt: 'Trickshots bouncing off targets and smashing household items.',
      },
      {
        id: 'goalkeeper_brainfades',
        name: 'Goalkeeper Brainfades',
        strictDefinition: 'Must show soccer goalies whiffing clearances, throwing to opponents, or misjudging slow balls.',
        searchQueries: ['goalkeeper rolls ball to striker howler', 'slow backpass goalie miss kick', 'worst goalkeeper mistakes soccer'],
        subreddits: ['sports', 'soccer'],
        audioStem: 'dull_thud.mp3',
        kineticTypography: { text: 'GOALIE LEFT THE CHAT ⚽', color: '#00E5FF', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['fifa 23', 'ea fc', 'gaming', 'podcast'],
        situationalPrompt: 'Soccer goalies whiffing clearances, throwing to opponents, or misjudging slow balls.',
      },
      {
        id: 'gymnast_routine_mishaps',
        name: 'Gymnast Routine Mishaps',
        strictDefinition: 'Must show harmless gymnastics routine bloopers onto soft mats or foam pits.',
        searchQueries: ['gymnast bellyflop foam pit dismount', 'vault dismount bounce on mat funny', 'balance beam slip safe foam landing'],
        subreddits: ['FullScorpion', 'sports'],
        audioStem: 'soft_thud.mp3',
        kineticTypography: { text: 'LANDING MISCALCULATED 🤸', color: '#FF9100', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['severe injury', 'bone fracture', 'olympic gold'],
        situationalPrompt: 'Harmless gymnastics routine bloopers onto soft mats or foam pits.',
      },
      {
        id: 'referee_collision_disasters',
        name: 'Referee Collisions',
        strictDefinition: 'Must show referees getting accidentally tackled, run over, or hit by stray balls.',
        searchQueries: ['referee tackled by football player', 'referee hit with soccer ball face', 'basketball referee collision with player'],
        subreddits: ['sports', 'sportsbloopers'],
        audioStem: 'collision_whistle.mp3',
        kineticTypography: { text: 'REF DOWN 🚩', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['referee controversy debate', 'podcast', 'commentary'],
        situationalPrompt: 'Referees getting accidentally tackled, run over, or hit by stray balls.',
        aliases: ['referee_collisions'],
      },
    ],
  },

  // ============================================================
  // NICHE 7: WORKPLACE & SHIFT DISASTERS (workplace_disasters)
  // ============================================================
  {
    id: 'workplace_disasters',
    name: 'Workplace & Shift Disasters',
    subCategories: [
      {
        id: 'worst_shift_of_their_lives',
        name: 'Worst Shift Ever',
        strictDefinition: 'Must show catastrophic food spills, paint bucket avalanches, or retail messes on a shift.',
        searchQueries: ['carrying paint bucket spill entire room', 'pallet of milk bottles drops warehouse floor', 'worst shift ever customer disaster'],
        subreddits: ['Wellthatsucks', 'mildlyinfuriating'],
        audioStem: 'liquid_splash.mp3',
        kineticTypography: { text: 'CLOCK OUT NOW ⏰', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['skit', 'comedy sketch', 'commercial'],
        situationalPrompt: 'Catastrophic food spills, paint bucket avalanches, or retail messes on a shift.',
        aliases: ['worst_shift_ever'],
      },
      {
        id: 'forklift_domino_disasters',
        name: 'Forklift Catastrophes',
        strictDefinition: 'Must show warehouse racking collapsing in a domino effect after a forklift bump.',
        searchQueries: ['forklift taps shelf warehouse domino collapse', 'forklift driver knocks over entire warehouse', 'warehouse shelf collapse cctv'],
        subreddits: ['IdiotsInCars', 'Wellthatsucks'],
        audioStem: 'rack_crash.mp3',
        kineticTypography: { text: 'WAREHOUSE COLLAPSE 📦', color: '#FFD600', rotation: -11 },
        timingRecipe: { setupSec: 4.0, aftermathSec: 2.5, freezeHoldSec: 2.0 },
        negativeFilters: ['forklift simulator', 'training video', 'explainer'],
        situationalPrompt: 'Warehouse racking collapsing in a domino effect after a forklift bump.',
      },
      {
        id: 'commercial_kitchen_nightmares',
        name: 'Kitchen Nightmares',
        strictDefinition: 'Must show chefs or line cooks dropping massive pots of soup, sauce, or dough.',
        searchQueries: ['dropping huge pot of soup kitchen floor', 'chef drops 20 gallon sauce vat', 'line cook slip kitchen nightmare'],
        subreddits: ['KitchenConfidential', 'Wellthatsucks'],
        audioStem: 'soup_vat_thud.mp3',
        kineticTypography: { text: 'KITCHEN CLOSED 🍳', color: '#B0BEC5', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.2, freezeHoldSec: 2.0 },
        negativeFilters: ['gordon ramsay episode', 'recipe tutorial', 'cooking show'],
        situationalPrompt: 'Chefs or line cooks dropping massive pots of soup, sauce, or dough.',
      },
      {
        id: 'retail_display_rampage',
        name: 'Retail Display Rampage',
        strictDefinition: 'Must show supermarket pyramid can collapses or wine bottle shelf domino crashes.',
        searchQueries: ['customer pulls bottom can soda pyramid collapse', 'supermarket wine bottle display domino knock', 'store display tumble retail disaster'],
        subreddits: ['Wellthatsucks', 'IdiotsInStores'],
        audioStem: 'glass_smash_50.mp3',
        kineticTypography: { text: 'PYRAMID COLLAPSE 🛒', color: '#FFEE58', rotation: -11 },
        timingRecipe: { setupSec: 2.5, aftermathSec: 1.8, freezeHoldSec: 2.0 },
        negativeFilters: ['mrbeast', 'commercial', 'prank tv'],
        situationalPrompt: 'Supermarket pyramid can collapses or wine bottle shelf domino crashes.',
      },
      {
        id: 'delivery_driver_mishaps',
        name: 'Delivery Driver Mishaps',
        strictDefinition: 'Must show package delivery drivers slipping on icy lawns/steps while protecting the parcel.',
        searchQueries: ['delivery driver slips on icy porch stairs ring cam', 'delivery driver sliding across lawn with package', 'fedex ups driver icy driveway slide'],
        subreddits: ['IdiotsInCars', 'Wellthatsucks'],
        audioStem: 'ice_slide_whoosh.mp3',
        kineticTypography: { text: 'DELIVERY CANCELLED 📦', color: '#8D6E63', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['package unboxing', 'porch pirate theft', 'news report'],
        situationalPrompt: 'Package delivery drivers slipping on icy lawns/steps while protecting the parcel.',
      },
    ],
  },

  // ============================================================
  // NICHE 8: EXTREME LUCK & NEAR MISSES (extreme_luck)
  // ============================================================
  {
    id: 'extreme_luck',
    name: 'Extreme Luck & Near Misses',
    subCategories: [
      {
        id: 'used_all_their_luck_for_life',
        name: 'Used All Luck For Life',
        strictDefinition: 'Must show a person narrowly dodging falling debris, trees, or spinning tires by inches.',
        searchQueries: ['near miss falling tree pedestrian inches', 'spinning wheel misses pedestrian sidewalk', 'used all luck for life cctv miracle'],
        subreddits: ['nonononoyes', 'nextfuckinglevel'],
        audioStem: 'angelic_choir.mp3',
        kineticTypography: { text: 'LUCK MAXED OUT 🍀', color: '#00E5FF', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['fatal impact', 'cgi movie', 'video game'],
        situationalPrompt: 'A person narrowly dodging falling debris, trees, or spinning tires by inches.',
        aliases: ['used_all_luck_for_life'],
      },
      {
        id: 'accidental_trickshots',
        name: 'Accidental Trickshots',
        strictDefinition: 'Must show dropped items accidentally bouncing into cups, pockets, or bins.',
        searchQueries: ['dropped item bounces into cup accidental', 'dropped phone flips and lands in pocket', 'bottle flip accidental landing upright'],
        subreddits: ['nevertellmetheodds', 'mildlyinteresting'],
        audioStem: 'sharp_ping.mp3',
        kineticTypography: { text: 'CALCULATED ACCIDENT 🎱', color: '#FFD700', rotation: -11 },
        timingRecipe: { setupSec: 2.5, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['intentional trickshot', 'cgi', 'video game'],
        situationalPrompt: 'Dropped items accidentally bouncing into cups, pockets, or bins.',
      },
      {
        id: 'physics_defying_saves',
        name: 'Physics-Defying Saves',
        strictDefinition: 'Must show impossible balance recoveries, falling skateboarders landing on two feet, or cat-like flips.',
        searchQueries: ['skateboard bail landing clean on feet', 'bike wipeout front flip landing on feet', 'physics defying balance recovery'],
        subreddits: ['nextfuckinglevel', 'HoldMyRedBull'],
        audioStem: 'anime_teleport.mp3',
        kineticTypography: { text: 'CLEAN RECOVERY 🛹', color: '#D500F9', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['gymnastics routine', 'pro stunt movie', 'cgi'],
        situationalPrompt: 'Impossible balance recoveries, falling skateboarders landing on two feet, or cat-like flips.',
      },
      {
        id: 'unintentional_hero_catches',
        name: 'Unintentional Hero Catches',
        strictDefinition: 'Must show parents or bystanders catching falling children, foul balls, or items with lightning reflexes.',
        searchQueries: ['dad reflex catches falling toddler without looking', 'foul ball catch barehand while holding baby', 'insane reflex catch dropped glass'],
        subreddits: ['DadReflexes', 'nextfuckinglevel'],
        audioStem: 'hand_grab_snap.mp3',
        kineticTypography: { text: 'SPIDER-SENSE ⚡', color: '#FFC107', rotation: -11 },
        timingRecipe: { setupSec: 2.5, aftermathSec: 0.5, freezeHoldSec: 2.0 },
        negativeFilters: ['staged baby catch', 'doll prop', 'movie'],
        situationalPrompt: 'Parents or bystanders catching falling children, foul balls, or items with lightning reflexes.',
      },
      {
        id: 'crazy_vehicle_recoveries',
        name: 'Vehicle 360 Recoveries',
        strictDefinition: 'Must show vehicles executing 360 spinouts on wet or icy highways and driving away unscathed.',
        searchQueries: ['car 360 spin on icy highway keeps driving', 'truck spin recovery smooth dashcam', 'drifting recovery on highway clean save'],
        subreddits: ['IdiotsInCars', 'nextfuckinglevel'],
        audioStem: 'tire_screech.mp3',
        kineticTypography: { text: 'HIGHWAY 360 SAVE 🏎️', color: '#FFFFFF', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['drift track pro', 'tokyo drift movie', 'fatal crash'],
        situationalPrompt: 'Vehicles executing 360 spinouts on wet or icy highways and driving away unscathed.',
        aliases: ['vehicle_360_recoveries'],
      },
    ],
  },

  // ============================================================
  // NICHE 9: GYM & FITNESS BLOOPERS (gym_bloopers)
  // ============================================================
  {
    id: 'gym_bloopers',
    name: 'Gym & Fitness Bloopers',
    subCategories: [
      {
        id: 'bench_press_fails',
        name: 'Bench Press Ego Fails',
        strictDefinition: 'Must show ego-lifters getting pinned under the bench press bar and performing the roll of shame.',
        searchQueries: ['bench press roll of shame pinned', 'ego lifting too much weight trapped bench', 'bench press fail safe roll'],
        subreddits: ['GymMemes', 'fitness'],
        audioStem: 'plate_clank.mp3',
        kineticTypography: { text: 'PINNED BY THE BAR 🏋️', color: '#FF1744', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.2, freezeHoldSec: 2.0 },
        negativeFilters: ['tragedy', 'hospital', 'powerlifting meet'],
        situationalPrompt: 'Ego-lifters getting pinned under the bench press bar and performing the roll of shame.',
        aliases: ['bench_press_ego_fails'],
      },
      {
        id: 'treadmill_slingshots',
        name: 'Treadmill Slingshots',
        strictDefinition: 'Must show people sprinting at maximum speed, tripping, and getting ejected into the rear wall.',
        searchQueries: ['treadmill max speed slingshot runner fly off', 'runner falls on treadmill flies back', 'treadmill fail launched off'],
        subreddits: ['HoldMyBeer', 'GymMemes'],
        audioStem: 'drywall_thud.mp3',
        kineticTypography: { text: 'MAX SPEED SLINGSHOT 🏃', color: '#FFEA00', rotation: -11 },
        timingRecipe: { setupSec: 2.5, aftermathSec: 0.6, freezeHoldSec: 2.0 },
        negativeFilters: ['treadmill review', 'running tips', 'marathon'],
        situationalPrompt: 'People sprinting at maximum speed, tripping, and getting ejected into the rear wall.',
      },
      {
        id: 'squat_rack_blunders',
        name: 'Squat Rack Bloopers',
        strictDefinition: 'Must show lifters dumping the bar onto safety pins or sitting down at the bottom of a heavy squat.',
        searchQueries: ['squat fail bail on safety pins', 'legs give out bottom of squat safe bail', 'squat rack blooper sitting down'],
        subreddits: ['GymMemes', 'fitness'],
        audioStem: 'barbell_slam.mp3',
        kineticTypography: { text: 'LEGS GAVE OUT 💥', color: '#00E676', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['severe injury', 'torn quad', 'hospital'],
        situationalPrompt: 'Lifters dumping the bar onto safety pins or sitting down at the bottom of a heavy squat.',
      },
      {
        id: 'gym_equipment_confusions',
        name: 'Using Equipment Wrong',
        strictDefinition: 'Must show gymgoers inventing bizarre, inverted, or completely incorrect machine movements.',
        searchQueries: ['using gym machine completely wrong funny', 'cable machine inverted exercise confusion', 'muscle confusion gym sighting hilarious'],
        subreddits: ['MuscleConfusion', 'GymMemes'],
        audioStem: 'elevator_chime.mp3',
        kineticTypography: { text: 'HOW DOES THIS WORK? ❓', color: '#FF4081', rotation: -11 },
        timingRecipe: { setupSec: 4.0, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['bodybuilding tutorial', 'proper form explainer', 'workout plan'],
        situationalPrompt: 'Gymgoers inventing bizarre, inverted, or completely incorrect machine movements.',
        aliases: ['equipment_misuse'],
      },
      {
        id: 'gym_spotter_fails',
        name: 'Spotter Distracted',
        strictDefinition: 'Must show spotters looking at phones or staring into space while their partner struggles.',
        searchQueries: ['spotter on phone while lifter struggles', 'distracted spotter looking away gym', 'spotter fail gym buddy looking at phone'],
        subreddits: ['GymMemes', 'fitness'],
        audioStem: 'phone_ping.mp3',
        kineticTypography: { text: 'WORST SPOTTER EVER 📱', color: '#90A4AE', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['how to spot', 'fitness coach lecture', 'podcast'],
        situationalPrompt: 'Spotters looking at phones or staring into space while their partner struggles.',
        aliases: ['spotter_distracted'],
      },
    ],
  },

  // ============================================================
  // NICHE 10: NATURE & WEATHER SURPRISES (nature_weather)
  // ============================================================
  {
    id: 'nature_weather',
    name: 'Nature & Weather Surprises',
    subCategories: [
      {
        id: 'sudden_wind_ruining_events',
        name: 'Sudden Wind Ruining Events',
        strictDefinition: 'Must show sudden microburst winds launching bounce houses, wedding tents, or patio umbrellas.',
        searchQueries: ['marquee tent airborne sudden gust wind', 'bounce house flies away wind gust', 'patio umbrella blown away outdoor wedding'],
        subreddits: ['Wellthatsucks', 'WeatherGifs'],
        audioStem: 'canvas_rip.mp3',
        kineticTypography: { text: 'WIND SAID NO 💨', color: '#FFFFFF', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 2.0, freezeHoldSec: 2.0 },
        negativeFilters: ['hurricane disaster news', 'tornado destruction', 'fatal'],
        situationalPrompt: 'Sudden microburst winds launching bounce houses, wedding tents, or patio umbrellas.',
      },
      {
        id: 'rogue_waves_catching_beachgoers',
        name: 'Rogue Waves',
        strictDefinition: 'Must show sudden surging beach waves washing over tourists sitting on dry sand.',
        searchQueries: ['rogue surge wave sweeps beach chairs', 'unexpected big wave catches tourists on dry sand', 'beachgoers running from surge wave'],
        subreddits: ['HeavySeas', 'Wellthatsucks'],
        audioStem: 'wave_plunge.mp3',
        kineticTypography: { text: 'SURPRISE TSUNAMI 🌊', color: '#00B4D8', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.5, freezeHoldSec: 2.0 },
        negativeFilters: ['tsunami disaster', 'shipwreck', 'drowning'],
        situationalPrompt: 'Sudden surging beach waves washing over tourists sitting on dry sand.',
        aliases: ['rogue_waves'],
      },
      {
        id: 'slipping_down_ice_driveways',
        name: 'Ice Driveway Slides',
        strictDefinition: 'Must show people slipping on black ice and sliding uncontrollably 20+ feet down steep driveways.',
        searchQueries: ['person slipping down icy driveway uncontrollably', 'sliding down ice driveway with trash can', 'cctv black ice driveway slip slide'],
        subreddits: ['HoldMyBeer', 'Wellthatsucks'],
        audioStem: 'mailbox_thud.mp3',
        kineticTypography: { text: 'ZERO TRACTION 🧊', color: '#80D8FF', rotation: -11 },
        timingRecipe: { setupSec: 4.0, aftermathSec: 0.0, freezeHoldSec: 2.0 },
        negativeFilters: ['car ice crash', 'highway pileup', 'news clip'],
        situationalPrompt: 'People slipping on black ice and sliding uncontrollably 20+ feet down steep driveways.',
        aliases: ['ice_driveway_slides'],
      },
      {
        id: 'wildlife_close_calls',
        name: 'Wildlife Close Calls',
        strictDefinition: 'Must show tourists getting too close to bison, moose, or bears and getting charged.',
        searchQueries: ['tourist gets too close to bison charged', 'bear walks past hiker stationary', 'moose charges tourist recording trail'],
        subreddits: ['NationalPark', 'Whatcouldgowrong'],
        audioStem: 'bison_grunt.mp3',
        kineticTypography: { text: 'WRONG HOOD 🦬', color: '#FFAB00', rotation: -11 },
        timingRecipe: { setupSec: 3.5, aftermathSec: 1.0, freezeHoldSec: 2.0 },
        negativeFilters: ['hunting video', 'fatal attack', 'zoo lecture'],
        situationalPrompt: 'Tourists getting too close to bison, moose, or bears and getting charged.',
      },
      {
        id: 'lightning_jump_scares',
        name: 'Lightning Strikes',
        strictDefinition: 'Must show lightning striking a tree, pole, or yard mere feet from the person recording.',
        searchQueries: ['lightning strikes tree inches from person filming', 'lightning jump scare close strike thunder', 'lightning strikes backyard patio video'],
        subreddits: ['Thorgasm', 'WeatherGifs'],
        audioStem: 'thunder_crack.mp3',
        kineticTypography: { text: 'TOO CLOSE ⚡', color: '#7C4DFF', rotation: -11 },
        timingRecipe: { setupSec: 3.0, aftermathSec: 0.1, freezeHoldSec: 2.0 },
        negativeFilters: ['lightning documentary', 'science channel', 'weather forecast'],
        situationalPrompt: 'Lightning striking a tree, pole, or yard mere feet from the person recording.',
      },
    ],
  },
];

export function findSubCategory(idOrAlias: string): SubCategory | undefined {
  const target = idOrAlias.toLowerCase().trim().replace(/-/g, '_');
  for (const niche of NICHE_GRAPH) {
    for (const sub of niche.subCategories) {
      if (sub.id === target) return sub;
      if (sub.aliases && sub.aliases.includes(target)) return sub;
    }
  }
  return undefined;
}

export function getAllSubCategories(): SubCategory[] {
  return NICHE_GRAPH.flatMap((n) => n.subCategories);
}

if (require.main === module) {
  console.log(JSON.stringify(NICHE_GRAPH[0].subCategories[0]));
}
