export interface SubCategoryEditStyle {
  subCategoryId: string;
  nicheId: string;
  name: string;
  titleHeader: string;
  subjectHeader: string;
  versionTag: string;
  audioHook: {
    stemPath: string;
    description: string;
    durationSeconds: number;
    duckNativeAudioVolume: number;
  };
  typography: {
    punchlineText: string;
    animationType: 'word_by_word_synced' | 'slam_zoom_pulse' | 'glitch_flicker' | 'buzzer_shake';
    primaryColor: string;
    secondaryColor: string;
    strokeColor: string;
    fontSize: number;
    wordsCadence?: { word: string; frameOffset: number }[];
  };
  timing: {
    buildupSeconds: number;
    freezeDurationFrames: number;
    aftermathSeconds: number;
  };
  strictFilter: {
    mustContain: string;
    mustNotContain: string[];
    motionThreshold: number;
  };
  goldenClips: {
    youtubeId: string;
    title: string;
    climaxSecond: number;
    trimStart: number;
    trimEnd: number;
    notes: string;
  }[];
}

export const SUBCATEGORY_EDIT_STYLES: Record<string, SubCategoryEditStyle> = {
  // ==========================================
  // NICHE 1: HUMAN PHYSICAL FAILS
  // ==========================================
  people_accepting_fate: {
    subCategoryId: 'people_accepting_fate',
    nicheId: 'human_fails',
    name: 'People Accepting Fate',
    titleHeader: 'Ranking Best Of',
    subjectHeader: 'This Is The End Moments',
    versionTag: '(Surrender Version)',
    audioHook: {
      stemPath: 'public/audio/stems/skyfall_this_is_the_end.mp3',
      description: 'Adele Skyfall orchestral vocal: "This is the end... hold your breath and count to ten"',
      durationSeconds: 3.19,
      duckNativeAudioVolume: 0.15,
    },
    typography: {
      punchlineText: 'THIS IS THE END',
      animationType: 'word_by_word_synced',
      primaryColor: '#FF2D55',
      secondaryColor: '#FFEB3B',
      strokeColor: '#000000',
      fontSize: 68,
      wordsCadence: [
        { word: 'THIS', frameOffset: 0 },
        { word: 'IS', frameOffset: 8 },
        { word: 'THE', frameOffset: 16 },
        { word: 'END', frameOffset: 24 },
      ],
    },
    timing: {
      buildupSeconds: 3.5,
      freezeDurationFrames: 42, // ~1.4s hold while vocal sings "This is the end..."
      aftermathSeconds: 1.8,
    },
    strictFilter: {
      mustContain: 'Person realizing impending doom/fall/slide and visibly stopping all struggle with acceptance.',
      mustNotContain: ['facecam', 'commentary', 'talking head', 'cgi', 'video games', 'animation', 'podcast'],
      motionThreshold: 0.65,
    },
    goldenClips: [
      {
        youtubeId: 'DYzT-Pk6Ogw',
        title: 'It do go down - Robert on boat waterfall',
        climaxSecond: 9.5,
        trimStart: 6.0,
        trimEnd: 12.0,
        notes: 'Robert calmly looks at waterfall while friend panics',
      },
      {
        youtubeId: 'glRlDUUG_-c',
        title: 'Man sliding 30 feet down icy driveway with total surrender',
        climaxSecond: 5.0,
        trimStart: 2.5,
        trimEnd: 7.5,
        notes: 'Completely motionless slide on back to the road curb',
      },
      {
        youtubeId: 'Yu3kzI3eeKA',
        title: 'CCTV driveway slip and motionless hill slide',
        climaxSecond: 6.5,
        trimStart: 4.0,
        trimEnd: 8.8,
        notes: 'Falls flat on back and accepts the slide down the driveway',
      },
      {
        youtubeId: 'sWHOX79StXA',
        title: 'Roof snow avalanche carrying shoveler down',
        climaxSecond: 2.5,
        trimStart: 0.5,
        trimEnd: 4.5,
        notes: 'Snow gives way and shoveler surrenders to the slide',
      },
      {
        youtubeId: '_1iObgKLMVU',
        title: 'Water park slide slip belly surrender',
        climaxSecond: 4.5,
        trimStart: 2.5,
        trimEnd: 6.5,
        notes: 'Loses footing on ramp and surrenders into belly slide',
      },
    ],
  },

  battling_gravity_losing: {
    subCategoryId: 'battling_gravity_losing',
    nicheId: 'human_fails',
    name: 'Battling Gravity & Losing',
    titleHeader: 'Ranking Funniest',
    subjectHeader: 'Gravity Winning Moments',
    versionTag: '(Balance Version)',
    audioHook: {
      stemPath: 'public/audio/stems/cartoon_slip.mp3',
      description: 'Classic slide whistle descending pitch into cartoon impact',
      durationSeconds: 2.0,
      duckNativeAudioVolume: 0.25,
    },
    typography: {
      punchlineText: 'GRAVITY WINS',
      animationType: 'slam_zoom_pulse',
      primaryColor: '#FFEB3B',
      secondaryColor: '#FF2D55',
      strokeColor: '#000000',
      fontSize: 64,
    },
    timing: { buildupSeconds: 3.8, freezeDurationFrames: 30, aftermathSeconds: 1.5 },
    strictFilter: {
      mustContain: 'Visible physical struggle against balance on ice, ladders, or roofs before slipping.',
      mustNotContain: ['serious injury', 'hospital', 'gymnastics pro', 'gaming'],
      motionThreshold: 0.7,
    },
    goldenClips: [],
  },

  // ==========================================
  // NICHE 2: INSTANT REGRET & KARMA
  // ==========================================
  road_rage_justice: {
    subCategoryId: 'road_rage_justice',
    nicheId: 'instant_karma',
    name: 'Road Rage Justice',
    titleHeader: 'Ranking Funniest',
    subjectHeader: 'Road Rage Karma Moments',
    versionTag: '(Justice Version)',
    audioHook: {
      stemPath: 'public/audio/stems/siren_short.mp3',
      description: 'Police siren wail chirp + tire screech impact',
      durationSeconds: 2.5,
      duckNativeAudioVolume: 0.25,
    },
    typography: {
      punchlineText: 'INSTANT KARMA',
      animationType: 'slam_zoom_pulse',
      primaryColor: '#00D2FF',
      secondaryColor: '#FF2D55',
      strokeColor: '#000000',
      fontSize: 66,
    },
    timing: { buildupSeconds: 4.2, freezeDurationFrames: 32, aftermathSeconds: 2.0 },
    strictFilter: {
      mustContain: 'Aggressive driver cut-off followed immediately by spin-out or unmarked police pullover.',
      mustNotContain: ['fatal crash', 'blood', 'gta', 'beamng', 'news report'],
      motionThreshold: 0.8,
    },
    goldenClips: [],
  },

  defying_warning_signs: {
    subCategoryId: 'defying_warning_signs',
    nicheId: 'instant_karma',
    name: 'Defying Warning Signs',
    titleHeader: 'Ranking Best Of',
    subjectHeader: 'Ignored Warning Signs',
    versionTag: '(Instant Karma)',
    audioHook: {
      stemPath: 'public/audio/stems/record_scratch.mp3',
      description: 'Abrupt record scratch freeze',
      durationSeconds: 1.8,
      duckNativeAudioVolume: 0.2,
    },
    typography: {
      punchlineText: 'WARNING WAS CLEAR',
      animationType: 'slam_zoom_pulse',
      primaryColor: '#FFEB3B',
      secondaryColor: '#FF2D55',
      strokeColor: '#000000',
      fontSize: 60,
    },
    timing: { buildupSeconds: 3.5, freezeDurationFrames: 30, aftermathSeconds: 1.8 },
    strictFilter: {
      mustContain: 'Person bypassing danger barrier (thin ice, wet paint, fence) followed by consequence.',
      mustNotContain: ['movie', 'scripted', 'podcast'],
      motionThreshold: 0.6,
    },
    goldenClips: [],
  },

  cocky_challengers: {
    subCategoryId: 'cocky_challengers',
    nicheId: 'instant_karma',
    name: 'Cocky Challengers',
    titleHeader: 'Ranking Best Of',
    subjectHeader: 'Early Celebration Fails',
    versionTag: '(Humbled Fast)',
    audioHook: {
      stemPath: 'public/audio/stems/fail_buzzer.mp3',
      description: 'Game show loud fail buzzer',
      durationSeconds: 2.2,
      duckNativeAudioVolume: 0.2,
    },
    typography: {
      punchlineText: 'TOO EARLY TO CELEBRATE',
      animationType: 'buzzer_shake',
      primaryColor: '#FF2D55',
      secondaryColor: '#FFFFFF',
      strokeColor: '#000000',
      fontSize: 58,
    },
    timing: { buildupSeconds: 4.0, freezeDurationFrames: 36, aftermathSeconds: 1.8 },
    strictFilter: {
      mustContain: 'Early hand raised in victory right before being passed or countered at the finish line.',
      mustNotContain: ['video game', 'fifa', 'esports'],
      motionThreshold: 0.75,
    },
    goldenClips: [],
  },

  // ==========================================
  // NICHE 3: FUNNY ANIMALS & PETS
  // ==========================================
  pets_being_dumb: {
    subCategoryId: 'pets_being_dumb',
    nicheId: 'funny_animals',
    name: 'Dogs Being Clumsy',
    titleHeader: 'Ranking Funniest',
    subjectHeader: 'Clumsy Dog Moments',
    versionTag: '(Dog Version)',
    audioHook: {
      stemPath: 'public/audio/stems/cartoon_slip.mp3',
      description: 'Cartoon slide whistle and boing',
      durationSeconds: 2.0,
      duckNativeAudioVolume: 0.3,
    },
    typography: {
      punchlineText: 'ZERO BRAINCELLS',
      animationType: 'slam_zoom_pulse',
      primaryColor: '#FFEB3B',
      secondaryColor: '#FF2D55',
      strokeColor: '#000000',
      fontSize: 66,
    },
    timing: { buildupSeconds: 3.2, freezeDurationFrames: 30, aftermathSeconds: 1.8 },
    strictFilter: {
      mustContain: 'Real dog sliding into glass door, slipping on slick floor, or misjudging couch jump.',
      mustNotContain: ['human fails', 'podcast', 'reaction', 'vlog', 'animal abuse'],
      motionThreshold: 0.7,
    },
    goldenClips: [],
  },

  // ==========================================
  // NICHE 4: INFINITE AURA LOSS
  // ==========================================
  one_million_aura_loss: {
    subCategoryId: 'one_million_aura_loss',
    nicheId: 'aura_debt',
    name: '-1,000,000 Aura Moments',
    titleHeader: 'Ranking The Worst',
    subjectHeader: '-1,000,000 Aura Moments',
    versionTag: '(Aura Loss)',
    audioHook: {
      stemPath: 'public/audio/stems/thud_whack.mp3',
      description: 'Deep resonant hollow bass drop with reverb',
      durationSeconds: 2.2,
      duckNativeAudioVolume: 0.2,
    },
    typography: {
      punchlineText: '-1,000,000 AURA',
      animationType: 'slam_zoom_pulse',
      primaryColor: '#FF2D55',
      secondaryColor: '#00D2FF',
      strokeColor: '#000000',
      fontSize: 68,
    },
    timing: { buildupSeconds: 3.5, freezeDurationFrames: 36, aftermathSeconds: 1.8 },
    strictFilter: {
      mustContain: 'Person attempting smooth or swagger pose, immediately stumbling or dropping dignity.',
      mustNotContain: ['fashion runway', 'perfume ad', 'podcast'],
      motionThreshold: 0.65,
    },
    goldenClips: [],
  },

  // ==========================================
  // NICHE 6: REAL-LIFE GLITCHES & NPCS
  // ==========================================
  unrendered_game_npcs: {
    subCategoryId: 'unrendered_game_npcs',
    nicheId: 'npc_glitches',
    name: 'Real-Life NPC Glitches',
    titleHeader: 'Ranking Craziest',
    subjectHeader: 'Real-Life NPC Glitches',
    versionTag: '(Matrix Version)',
    audioHook: {
      stemPath: 'public/audio/stems/record_scratch.mp3',
      description: 'Glitch buzz and static stutter',
      durationSeconds: 2.0,
      duckNativeAudioVolume: 0.25,
    },
    typography: {
      punchlineText: 'NPC GLITCH DETECTED',
      animationType: 'glitch_flicker',
      primaryColor: '#00D2FF',
      secondaryColor: '#FFEB3B',
      strokeColor: '#000000',
      fontSize: 58,
    },
    timing: { buildupSeconds: 3.5, freezeDurationFrames: 34, aftermathSeconds: 1.8 },
    strictFilter: {
      mustContain: 'Real human frozen in rigid T-pose, blank stare, or repetitive mechanical movement in public.',
      mustNotContain: ['3d animation', 'game engine test', 'cgi'],
      motionThreshold: 0.5,
    },
    goldenClips: [],
  },
};

export function getSubCategoryEditStyle(id: string): SubCategoryEditStyle {
  if (SUBCATEGORY_EDIT_STYLES[id]) {
    return SUBCATEGORY_EDIT_STYLES[id];
  }
  // Generic fallback with verified @MrPurifiedWater visual architecture
  return {
    subCategoryId: id,
    nicheId: 'generic_viral',
    name: id.replace(/_/g, ' ').toUpperCase(),
    titleHeader: 'Ranking Best Of',
    subjectHeader: `${id.replace(/_/g, ' ').toUpperCase()} Moments`,
    versionTag: '(Viral Version)',
    audioHook: {
      stemPath: 'public/audio/stems/thud_whack.mp3',
      description: 'Impact punchline sound',
      durationSeconds: 2.0,
      duckNativeAudioVolume: 0.25,
    },
    typography: {
      punchlineText: 'MOMENT OF REGRET',
      animationType: 'slam_zoom_pulse',
      primaryColor: '#FF2D55',
      secondaryColor: '#FFEB3B',
      strokeColor: '#000000',
      fontSize: 64,
    },
    timing: { buildupSeconds: 3.5, freezeDurationFrames: 30, aftermathSeconds: 1.8 },
    strictFilter: {
      mustContain: 'Raw CCTV/dashcam/phone viral moment.',
      mustNotContain: ['facecam', 'talking head', 'news', 'podcast', 'gaming', 'cgi'],
      motionThreshold: 0.6,
    },
    goldenClips: [],
  };
}
