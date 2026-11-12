export interface IncidentSFXConfig {
  impactSfx: string[];
  ambientSfx?: string;
  defaultPunchline: string;
}

export const INCIDENT_SFX_MAP: Record<string, IncidentSFXConfig> = {
  car_crash: {
    impactSfx: ['tires_screech.mp3', 'heavy_metal_crunch.mp3'],
    ambientSfx: 'car_horn_fade.mp3',
    defaultPunchline: 'BRO THOUGHT HE HAD BRAKES',
  },
  pedestrian_slip: {
    impactSfx: ['cartoon_slip.mp3', 'wii_bowling_strike.mp3'],
    ambientSfx: 'crowd_ooh.mp3',
    defaultPunchline: 'GRAVITY WAS UNFORGIVING',
  },
  physical_fall: {
    impactSfx: ['thud_whack.mp3', 'glass_shatter.mp3'],
    ambientSfx: 'crowd_gasp.mp3',
    defaultPunchline: 'PHYSICS WON TODAY',
  },
  verbal_argument: {
    impactSfx: ['record_scratch.mp3', 'crickets.mp3'],
    ambientSfx: 'awkward_cough.mp3',
    defaultPunchline: 'SILENCE WAS DEAFENING',
  },
  prank_backfire: {
    impactSfx: ['evil_laugh_cut.mp3', 'fail_buzzer.mp3'],
    ambientSfx: 'crickets.mp3',
    defaultPunchline: 'PLAN WAS NOT THOUGHT OUT',
  },
  clumsy_action: {
    impactSfx: ['boing.mp3', 'cartoon_slip.mp3'],
    ambientSfx: 'sad_trombone.mp3',
    defaultPunchline: 'ZERO COORDINATION',
  },
  instant_karma: {
    impactSfx: ['boom_reverb.mp3', 'siren_short.mp3'],
    ambientSfx: 'siren_short.mp3',
    defaultPunchline: 'KARMA SERVED IMMEDIATELY',
  },
  chase: {
    impactSfx: ['tires_screech.mp3', 'police_radio.mp3'],
    ambientSfx: 'siren_short.mp3',
    defaultPunchline: 'FAILED GETAWAY',
  },
  other: {
    impactSfx: ['thud_whack.mp3'],
    ambientSfx: 'crickets.mp3',
    defaultPunchline: 'EXPECT THE UNEXPECTED',
  },
};

export const NICHE_AUDIO_STEMS: Record<string, string> = {
  people_accepting_fate: 'skyfall_stem.mp3',
  instant_karma: 'phonk_bass_drop.mp3',
  road_rage_regret: 'phonk_bass_drop.mp3',
  funny_animals: 'boing.mp3',
  aura_debt: 'vine_boom.mp3',
  sports_bloopers: 'airhorn_choke.mp3',
  npc_glitches: 'matrix_dejavu.mp3',
  workplace_disasters: 'industrial_crash.mp3',
  extreme_luck: 'angelic_choir.mp3',
  gym_bloopers: 'metal_clang_heavy.mp3',
  nature_weather: 'wind_whoosh_pop.mp3',
};

export function getIncidentSFX(incidentType: string): IncidentSFXConfig {
  const normalized = (incidentType || 'other').toLowerCase();
  return INCIDENT_SFX_MAP[normalized] || INCIDENT_SFX_MAP.other;
}

export function getNicheAudioStem(subCategoryId: string): string {
  return NICHE_AUDIO_STEMS[subCategoryId] || 'skyfall_stem.mp3';
}

/**
 * Calculates audio ducking volume in Remotion:
 * - Native video plays at 100% (volume = 1.0) during the buildup.
 * - During impact/loud SFX or freeze frame, background music ducks by -14 dB (linear ~0.20).
 * - Silent zones return BGM to full volume (linear 1.0).
 */
export function calculateBGMDuckingVolume(
  currentFrame: number,
  impactFrame: number,
  freezeDurationFrames: number,
  isVoiceOrLoudSfxPlaying: boolean = false
): number {
  const duckedLevel = Math.pow(10, -14 / 20); // ~0.20 (-14 dB)

  // Duck during impact and freeze frame
  const isInImpactOrFreeze =
    currentFrame >= impactFrame && currentFrame <= impactFrame + freezeDurationFrames;

  if (isInImpactOrFreeze || isVoiceOrLoudSfxPlaying) {
    return duckedLevel;
  }
  return 1.0;
}
