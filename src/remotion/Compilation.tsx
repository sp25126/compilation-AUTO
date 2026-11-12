import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  spring,
  staticFile,
  interpolate,
} from 'remotion';

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

export interface ClipItem {
  videoPath: string;
  durationInFrames: number;
  punchlineText?: string;
  incidentType?: string;
  impactSfx?: string;
  timingRecipe?: TimingRecipeConfig;
}

export interface CompilationProps {
  clips: ClipItem[];
  subCategoryName: string;
  audioStem?: string;
  kineticTypography?: KineticTypographyConfig;
  timingRecipe?: TimingRecipeConfig;
}

const RANK_COLORS: Record<number, string> = {
  1: '#FF1744', // Red
  2: '#00E5FF', // Cyan
  3: '#FFE600', // Yellow
  4: '#FFFFFF', // White
  5: '#FFFFFF', // White
};

export const Compilation: React.FC<CompilationProps> = ({
  clips,
  subCategoryName,
  audioStem = 'skyfall_stem.mp3',
  kineticTypography = { text: 'THIS IS THE END', color: '#FF1744', rotation: -11 },
  timingRecipe = { setupSec: 3.5, aftermathSec: 1.2, freezeHoldSec: 2.2 },
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const totalClips = clips.length;
  let accumulatedFrames = 0;
  const clipSequences = clips.map((clip, index) => {
    const startFrame = accumulatedFrames;
    accumulatedFrames += clip.durationInFrames;
    const rank = totalClips - index;
    return {
      clip,
      index,
      rank,
      startFrame,
      endFrame: accumulatedFrames,
      durationInFrames: clip.durationInFrames,
    };
  });

  let currentRank = clipSequences[0]?.rank ?? 5;
  let activeSequence = clipSequences[0];
  for (const seq of clipSequences) {
    if (frame >= seq.startFrame && frame < seq.endFrame) {
      currentRank = seq.rank;
      activeSequence = seq;
      break;
    }
  }

  const resolveRemotionPath = (rawPath: string) => {
    if (!rawPath) return '';
    if (rawPath.startsWith('http://') || rawPath.startsWith('https://') || rawPath.startsWith('file:')) {
      return rawPath;
    }
    let relative = rawPath;
    if (relative.includes('public\\')) {
      relative = relative.split('public\\')[1].replace(/\\/g, '/');
    } else if (relative.includes('public/')) {
      relative = relative.split('public/')[1];
    }
    return staticFile(relative);
  };

  return (
    <AbsoluteFill style={{ backgroundColor: '#000000' }}>
      {/* Clip Sequences */}
      {clipSequences.map((seq) => {
        const recipe = seq.clip.timingRecipe || timingRecipe;
        const freezeDurationFrames = Math.round(recipe.freezeHoldSec * fps);
        const freezeStartFrame = Math.max(0, seq.durationInFrames - freezeDurationFrames);
        const videoSrc = resolveRemotionPath(seq.clip.videoPath);
        const resolvedAudioSrc = resolveRemotionPath(audioStem);

        const punchlineRaw = seq.clip.punchlineText || kineticTypography.text || 'THIS IS THE END';
        const words = punchlineRaw.split(' ');

        return (
          <Sequence
            key={seq.index}
            from={seq.startFrame}
            durationInFrames={seq.durationInFrames}
          >
            {/* Visual Framing: Blurred Cover BG + Contained Video */}
            <AbsoluteFill>
              {/* Layer 1: Background blurred ambient fill */}
              <OffthreadVideo
                src={videoSrc}
                volume={0}
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  filter: 'blur(24px) brightness(0.4)',
                }}
              />

              {/* Layer 2: Foreground Video */}
              <div
                style={{
                  position: 'absolute',
                  top: 0,
                  left: 0,
                  width: '100%',
                  height: '100%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: '120px 20px',
                }}
              >
                <OffthreadVideo
                  src={videoSrc}
                  volume={(f) => {
                    // Drop native audio by -infinity dB 1 frame before freezeHoldSec begins
                    if (f >= freezeStartFrame - 1) return 0;
                    return 1.0;
                  }}
                  style={{
                    maxWidth: '1000px',
                    maxHeight: '1280px',
                    width: 'auto',
                    height: 'auto',
                    objectFit: 'contain',
                    borderRadius: '16px',
                    boxShadow: '0 24px 60px rgba(0, 0, 0, 0.9)',
                  }}
                />
              </div>
            </AbsoluteFill>

            {/* Audio Stem Integration: Plays during freeze frame */}
            <Sequence from={freezeStartFrame} durationInFrames={freezeDurationFrames}>
              <Audio src={resolvedAudioSrc} volume={0.9} />
            </Sequence>

            {/* Contextual Impact SFX */}
            {seq.clip.impactSfx && (
              <Sequence from={freezeStartFrame} durationInFrames={freezeDurationFrames}>
                <Audio src={resolveRemotionPath(seq.clip.impactSfx)} volume={1.0} />
              </Sequence>
            )}

            {/* Kinetic Typography Punchline */}
            <Sequence from={freezeStartFrame} durationInFrames={freezeDurationFrames}>
              <FreezeWordByWordPunchline
                words={words}
                fps={fps}
                color={kineticTypography.color}
                rotation={kineticTypography.rotation}
              />
            </Sequence>
          </Sequence>
        );
      })}

      {/* Top Header */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '195px',
          backgroundColor: '#000000',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 40,
        }}
      >
        <div
          style={{
            fontFamily: 'Impact, "Arial Black", sans-serif',
            fontSize: '52px',
            textTransform: 'uppercase',
            letterSpacing: '1px',
            lineHeight: 1.1,
          }}
        >
          <span style={{ color: '#FFFFFF' }}>Ranking </span>
          <span style={{ color: '#FFE600' }}>Best Of</span>
        </div>
        <div
          style={{
            fontFamily: 'Impact, "Arial Black", sans-serif',
            fontSize: '56px',
            color: '#FF1744',
            textTransform: 'uppercase',
            letterSpacing: '2px',
            lineHeight: 1.1,
            marginTop: '4px',
          }}
        >
          {subCategoryName}
        </div>
      </div>

      {/* Countdown Ladder (Left HUD) */}
      <div
        style={{
          position: 'absolute',
          top: '230px',
          left: '40px',
          display: 'flex',
          flexDirection: 'column',
          gap: '12px',
          zIndex: 40,
        }}
      >
        {[1, 2, 3, 4, 5].map((rankNum) => {
          const isActive = currentRank === rankNum;
          const baseColor = RANK_COLORS[rankNum] || '#FFFFFF';
          const rankColor = isActive ? kineticTypography.color || baseColor : '#888888';

          return (
            <div
              key={rankNum}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                transform: isActive ? 'scale(1.12)' : 'scale(1.0)',
                transformOrigin: 'left center',
                transition: 'transform 0.15s ease',
              }}
            >
              <span
                style={{
                  fontFamily: 'Impact, "Arial Black", sans-serif',
                  fontSize: isActive ? '64px' : '48px',
                  color: rankColor,
                  textShadow: isActive
                    ? `0 0 20px ${rankColor}, 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000`
                    : '2px 2px 0 #000, -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000',
                  lineHeight: 1,
                  display: 'inline-block',
                }}
              >
                {rankNum}.
              </span>

              {isActive && (
                <span
                  style={{
                    fontFamily: 'Impact, "Arial Black", sans-serif',
                    fontSize: '32px',
                    color: '#FFE600',
                    backgroundColor: 'rgba(0, 0, 0, 0.85)',
                    padding: '6px 14px',
                    borderRadius: '6px',
                    letterSpacing: '1.5px',
                    textTransform: 'uppercase',
                    border: '2px solid rgba(255, 230, 0, 0.6)',
                    boxShadow: '0 4px 15px rgba(0, 0, 0, 0.7)',
                  }}
                >
                  {activeSequence.clip.punchlineText || activeSequence.clip.incidentType || subCategoryName}
                </span>
              )}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

const FreezeWordByWordPunchline: React.FC<{
  words: string[];
  fps: number;
  color?: string;
  rotation?: number;
}> = ({ words, fps, color = '#FFE600', rotation = -11 }) => {
  const localFrame = useCurrentFrame();

  return (
    <div
      style={{
        position: 'absolute',
        bottom: '260px',
        width: '100%',
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'center',
        columnGap: '16px',
        rowGap: '8px',
        padding: '0 40px',
        transform: `rotate(${rotation}deg)`,
        zIndex: 50,
      }}
    >
      {words.map((word, wIdx) => {
        const delayFrames = wIdx * 4;
        const wordSpring = spring({
          frame: Math.max(0, localFrame - delayFrames),
          fps,
          config: {
            damping: 10,
            stiffness: 160,
            mass: 0.5,
          },
        });

        const scale = interpolate(wordSpring, [0, 1], [0.3, 1.15]);
        const opacity = interpolate(wordSpring, [0, 1], [0, 1]);

        return (
          <span
            key={wIdx}
            style={{
              fontFamily: 'Impact, sans-serif',
              fontSize: '84px',
              fontWeight: 900,
              color: color,
              WebkitTextStroke: '6px #000000',
              textTransform: 'uppercase',
              letterSpacing: '2px',
              transform: `scale(${scale})`,
              opacity,
              display: 'inline-block',
              margin: '0 4px',
              whiteSpace: 'nowrap',
              textShadow: '0 8px 30px rgba(0,0,0,0.95)',
            }}
          >
            {word}
          </span>
        );
      })}
    </div>
  );
};
