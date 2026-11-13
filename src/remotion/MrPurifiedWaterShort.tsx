import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
  interpolate,
  Img,
} from 'remotion';

export interface RankingClipItem {
  videoPath: string;
  freezeImagePath?: string; // exact frozen frame PNG/JPG extracted at freezeFrameOffset
  durationInFrames: number;
  freezeFrameOffset?: number; // relative frame where the climax/freeze begins (strictly AFTER cause)
  freezeDurationFrames?: number; // duration of the freeze/song hook (e.g. 90 frames = 3.0s)
  impactFrameOffset?: number; // relative frame for beat-synced snap-zoom & impact flash (non-freeze categories like Instant Karma)
  audioHookPath?: string; // path to song hook (e.g. "public/audio/stems/skyfall_this_is_the_end.mp3")
  subtitleText?: string;
  punchlineText?: string; // punchline string (e.g. "THIS IS THE END" or "INSTANT KARMA")
  voPath?: string;
  voDuration?: number;
}

export interface MrPurifiedWaterShortProps {
  titleHeader: string; // e.g. "Ranking Best Of" or "Ranking The Best"
  subjectHeader: string; // e.g. "This Is The End Moments"
  versionTag: string; // e.g. "(Surrender Version)"
  globalAudioPath?: string; // optional continuous beat-synced track across all clips (e.g. "public/audio/stems/karma_beat_master.mp3")
  showSubtitles?: boolean; // default false: omit subtitles when there is no voiceover
  enableLogoPopupDemo?: boolean; // when true: small logo popup (no black screen) after 1st clip & at last clip + Mew SFX
  clips: RankingClipItem[];
}

const ClimaxPunchlineText: React.FC<{ text: string; durationInFrames: number }> = ({
  text,
}) => {
  const frame = useCurrentFrame();
  const words = text.split(' ');
  const isTwoWord = words.length === 2;
  const line1 = isTwoWord ? words[0] : words.slice(0, 2).join(' '); // "THIS IS" or "INSTANT"
  const line2 = isTwoWord ? words[1] : words.slice(2).join(' '); // "THE END" or "KARMA"

  const scale = interpolate(frame, [0, 5, 10], [0.85, 1.08, 1.0], {
    extrapolateRight: 'clamp',
  });

  // Synced to Adele "This is... the end" (f=34) or fast 2-word beat pop (f=5)
  const showLine2 = frame >= (isTwoWord ? 5 : 34);

  return (
    <div
      style={{
        position: 'absolute',
        bottom: '250px',
        left: '50%',
        transform: `translateX(-50%) scale(${scale})`,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 150,
        width: '90%',
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          fontSize: '84px',
          fontWeight: 900,
          lineHeight: 0.98,
          color: '#FFFFFF',
          letterSpacing: '2px',
          textTransform: 'uppercase',
          textAlign: 'center',
          textShadow:
            '0 6px 18px rgba(0,0,0,0.95), 5px 5px 0 #000, -5px -5px 0 #000, 5px -5px 0 #000, -5px 5px 0 #000, 0 5px 0 #000, 0 -5px 0 #000, 5px 0 0 #000, -5px 0 0 #000',
        }}
      >
        {line1}
      </div>
      {showLine2 && line2 && (
        <div
          style={{
            fontSize: '88px',
            fontWeight: 900,
            lineHeight: 1.0,
            color: '#FFFFFF',
            letterSpacing: '2px',
            textTransform: 'uppercase',
            textAlign: 'center',
            textShadow:
              '0 6px 18px rgba(0,0,0,0.95), 5px 5px 0 #000, -5px -5px 0 #000, 5px -5px 0 #000, -5px 5px 0 #000, 0 5px 0 #000, 0 -5px 0 #000, 5px 0 0 #000, -5px 0 0 #000',
          }}
        >
          {line2}
        </div>
      )}
    </div>
  );
};


export const MrPurifiedWaterShort: React.FC<MrPurifiedWaterShortProps> = ({
  titleHeader = 'Ranking Best Of',
  subjectHeader = 'This Is The End Moments',
  versionTag = '(Surrender Version)',
  globalAudioPath,
  showSubtitles = false,
  enableLogoPopupDemo = false,
  clips = [],
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const totalClips = clips.length;

  // Build sequence timings: clips are ordered in the array from first clip shown (Rank 5) to finale (Rank 1)
  let accumulatedFrames = 0;
  const clipSequences = clips.map((clip, index) => {
    const startFrame = accumulatedFrames;
    const dur = clip.durationInFrames || 150;
    accumulatedFrames += dur;
    const rankNumber = totalClips - index; // e.g. 5, 4, 3, 2, 1
    const levelNumber = index + 1; // e.g. Level 1, Level 2, Level 3, Level 4, Level 5
    const freezeOffset = clip.freezeFrameOffset ?? Math.max(30, Math.floor(dur * 0.55));
    const freezeDuration = clip.freezeDurationFrames ?? 90;

    return {
      clip,
      index,
      rankNumber,
      levelNumber,
      startFrame,
      endFrame: accumulatedFrames,
      durationInFrames: dur,
      freezeOffset,
      freezeDuration,
    };
  });

  const totalClipsDuration = accumulatedFrames;
  const OUTRO_FRAMES = 75; // 2.5s outro
  const isOutroActive = frame >= totalClipsDuration;
  const outroRelFrame = Math.max(0, frame - totalClipsDuration);

  // Active clip sequence
  let activeSeq = clipSequences[0];
  for (const seq of clipSequences) {
    if (frame >= seq.startFrame && frame < seq.endFrame) {
      activeSeq = seq;
      break;
    }
  }

  const resolvePath = (rawPath: string) => {
    if (!rawPath) return '';
    if (rawPath.startsWith('http://') || rawPath.startsWith('https://') || rawPath.startsWith('file:')) {
      return rawPath;
    }
    let relative = rawPath.replace(/\\/g, '/');
    if (relative.startsWith('public/')) {
      relative = relative.slice('public/'.length);
    } else if (relative.startsWith('/public/')) {
      relative = relative.slice('/public/'.length);
    }
    return staticFile(relative);
  };

  const earshotAudioSrc = staticFile('audio/earshot_sonic_brand.mp3');
  const logoSrc = staticFile('levelzero0ne_logo.jpg');
  const globalAudioSrc = globalAudioPath ? resolvePath(globalAudioPath) : '';

  // Title styling logic: split prefix and highlight word
  const titleParts = titleHeader.split(' ');
  const titlePrefix = titleParts.slice(0, -1).join(' ') || 'Ranking The';
  const titleHighlight = titleParts[titleParts.length - 1] || 'Best';

  // Colors based on @MrPurifiedWater signature palette
  const RANK_COLORS: Record<number, string> = {
    1: '#FF2D55', // Vibrant Crimson Red
    2: '#00D2FF', // Electric Cyan
    3: '#FFEB3B', // Golden Yellow
    4: '#FFFFFF', // Crisp White
    5: '#FFFFFF', // Crisp White
    6: '#FFFFFF', // Crisp White
  };

  return (
    <AbsoluteFill style={{ backgroundColor: '#000000', fontFamily: 'Impact, "Arial Black", sans-serif' }}>
      {/* 1. Consistent Earshot Audio Branding on Outro + Optional Low-Volume Trending Bed */}
      {globalAudioSrc && (
        <Sequence from={0} durationInFrames={totalClipsDuration}>
          <Audio src={globalAudioSrc} volume={0.11} />
        </Sequence>
      )}
      <Sequence from={totalClipsDuration} durationInFrames={OUTRO_FRAMES}>
        <Audio src={earshotAudioSrc} volume={1.0} />
      </Sequence>

      {/* 2. Main Clip Sequences */}
      {!isOutroActive &&
        clipSequences.map((seq) => {
          const videoSrc = resolvePath(seq.clip.videoPath);
          const freezeImgSrc = seq.clip.freezeImagePath ? resolvePath(seq.clip.freezeImagePath) : '';
          const hookSrc = seq.clip.audioHookPath ? resolvePath(seq.clip.audioHookPath) : '';
          const voSrc = seq.clip.voPath ? resolvePath(seq.clip.voPath) : '';
          const voDurationFrames = Math.round((seq.clip.voDuration || 2.5) * fps);
          const relFrame = frame - seq.startFrame;
          const isFrozen = Boolean(freezeImgSrc && relFrame >= seq.freezeOffset);
          const freezeRelFrame = Math.max(0, relFrame - seq.freezeOffset);
          const freezeZoom = isFrozen
            ? interpolate(freezeRelFrame, [0, seq.freezeDuration], [1.03, 1.09], {
                extrapolateRight: 'clamp',
              })
            : 1.03;
          const impactOffset = seq.clip.impactFrameOffset ?? -1;
          const isImpactActive = impactOffset >= 0 && relFrame >= impactOffset;
          const impactRelFrame = Math.max(0, relFrame - impactOffset);
          const impactZoom = isImpactActive
            ? interpolate(impactRelFrame, [0, 4, 24], [1.03, 1.13, 1.06], {
                extrapolateRight: 'clamp',
              })
            : 1.03;
          const impactFlashOpacity =
            isImpactActive && impactRelFrame < 5
              ? interpolate(impactRelFrame, [0, 5], [0.35, 0], { extrapolateRight: 'clamp' })
              : 0;

          return (
            <Sequence
              key={seq.index}
              from={seq.startFrame}
              durationInFrames={seq.durationInFrames}
            >
              {/* Visual Framing: Blurred background + Centered Video Card */}
              <AbsoluteFill>
                {/* Premium Dark Ambient Radial Background */}
                <div
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    width: '100%',
                    height: '100%',
                    background: 'radial-gradient(circle at center, #1c1d24 0%, #08080a 100%)',
                  }}
                />

                {/* Foreground Card */}
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
                    padding: '240px 18px 120px 18px',
                  }}
                >
                  <div
                    style={{
                      width: '100%',
                      maxWidth: '1040px',
                      maxHeight: '1440px',
                      borderRadius: '18px',
                      overflow: 'hidden',
                      border: '3px solid #1a1a1a',
                      boxShadow: '0 25px 60px rgba(0, 0, 0, 0.9)',
                      backgroundColor: '#000000',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                    }}
                  >
                    {!isFrozen ? (
                      <OffthreadVideo
                        src={videoSrc}
                        volume={(f) => {
                          if (voSrc && f < voDurationFrames) return 0.35;
                          if (hookSrc && f >= seq.freezeOffset) return 0.0;
                          return 1.0;
                        }}
                        style={{
                          width: '100%',
                          maxHeight: '1400px',
                          height: 'auto',
                          objectFit: 'contain',
                          transform: 'scale(1.0)',
                        }}
                      />
                    ) : (
                      <Img
                        src={freezeImgSrc}
                        style={{
                          width: '100%',
                          maxHeight: '1400px',
                          height: 'auto',
                          objectFit: 'contain',
                          transform: `scale(${freezeZoom})`,
                          filter: 'grayscale(35%) contrast(1.12) brightness(0.92)',
                        }}
                      />
                    )}
                  </div>
                </div>
              </AbsoluteFill>

              {/* Neural Voiceover (Optional setup line, only if provided) */}
              {voSrc && (
                <Sequence from={0} durationInFrames={voDurationFrames}>
                  <Audio src={voSrc} volume={1.0} />
                </Sequence>
              )}

              {/* Signature Audio Hook (Adele Skyfall "This is the end...") */}
              {hookSrc && (
                <Sequence from={seq.freezeOffset} durationInFrames={seq.durationInFrames - seq.freezeOffset}>
                  <Audio src={hookSrc} volume={1.0} />
                </Sequence>
              )}

              {/* Clean Video Presentation - No white flashes or text popups over action */}

              {/* Subtitle Setup Text (only shown when showSubtitles is explicitly enabled) */}
              {showSubtitles && seq.clip.subtitleText && (
                <Sequence from={0} durationInFrames={voDurationFrames + 10}>
                  <div
                    style={{
                      position: 'absolute',
                      bottom: '220px',
                      width: '100%',
                      display: 'flex',
                      justifyContent: 'center',
                      padding: '0 40px',
                      zIndex: 60,
                    }}
                  >
                    <div
                      style={{
                        fontSize: '44px',
                        fontWeight: 900,
                        color: '#FFFFFF',
                        textTransform: 'uppercase',
                        textAlign: 'center',
                        textShadow:
                          '0 4px 12px rgba(0,0,0,0.95), 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000',
                        letterSpacing: '1px',
                      }}
                    >
                      {seq.clip.subtitleText}
                    </div>
                  </div>
                </Sequence>
              )}
            </Sequence>
          );
        })}

      {/* 3. Top Banner (Exact @MrPurifiedWater Architecture) */}
      {!isOutroActive && (
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '240px',
            backgroundColor: '#000000',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 100,
            borderBottom: '2px solid #1c1c1c',
            boxShadow: '0 10px 30px rgba(0,0,0,0.8)',
          }}
        >
          {/* Line 1: Ranking The [Best/Funniest] */}
          <div style={{ fontSize: '56px', fontWeight: 900, letterSpacing: '1px', lineHeight: 1.1 }}>
            <span style={{ color: '#FFFFFF' }}>{titlePrefix} </span>
            <span style={{ color: '#FFEB3B' }}>{titleHighlight}</span>
          </div>

          {/* Line 2: Subject Header (e.g. This Is The End Moments / Instant Karma Moments) */}
          <div
            style={{
              fontSize: '52px',
              fontWeight: 900,
              color: '#FF2D55',
              letterSpacing: '1px',
              lineHeight: 1.15,
              textTransform: 'capitalize',
            }}
          >
            {subjectHeader}
          </div>

          {/* Line 3: Version Tag (e.g. (Surrender Version)) */}
          {versionTag && (
            <div
              style={{
                fontSize: '32px',
                fontWeight: 800,
                color: '#00D2FF',
                letterSpacing: '1.5px',
                marginTop: '2px',
              }}
            >
              {versionTag}
            </div>
          )}
        </div>
      )}

      {/* 4. Left-Hand Ranking Ladder & Level Badge (Exact @MrPurifiedWater Ladder) */}
      {!isOutroActive && (
        <div
          style={{
            position: 'absolute',
            top: '260px',
            left: '42px',
            display: 'flex',
            flexDirection: 'column',
            gap: '14px',
            zIndex: 100,
          }}
        >
          {/* Numbers 1 down to totalClips */}
          {Array.from({ length: totalClips }, (_, i) => i + 1).map((num) => {
            const isActive = activeSeq && activeSeq.rankNumber === num;
            const rankColor = RANK_COLORS[num] || '#FFFFFF';

            return (
              <div
                key={num}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '12px',
                }}
              >
                {/* Number with thick outline */}
                <div
                  style={{
                    fontSize: '56px',
                    fontWeight: 900,
                    lineHeight: 1,
                    color: rankColor,
                    textShadow:
                      '0 4px 10px rgba(0,0,0,0.9), 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000, 0 0 14px rgba(0,0,0,0.8)',
                  }}
                >
                  {num}.
                </div>

                {/* Level Badge shown beside the currently active rank! */}
                {isActive && (
                  <div
                    style={{
                      fontSize: '34px',
                      fontWeight: 900,
                      color: '#FFFFFF',
                      letterSpacing: '1px',
                      textShadow:
                        '0 3px 8px rgba(0,0,0,0.9), 2px 2px 0 #000, -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000',
                      animation: 'pulse 1s infinite alternate',
                    }}
                  >
                    [Level {activeSeq.levelNumber}]
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* 5. Channel Watermark (Anti-Demonetization Badge) */}
      {!isOutroActive && (
        <div
          style={{
            position: 'absolute',
            bottom: '28px',
            right: '35px',
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            zIndex: 90,
            opacity: 0.85,
          }}
        >
          <div
            style={{
              width: '42px',
              height: '42px',
              borderRadius: '50%',
              overflow: 'hidden',
              border: '2px solid #FFEB3B',
              boxShadow: '0 4px 12px rgba(0,0,0,0.8)',
            }}
          >
            <Img src={logoSrc} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
          </div>
          <span
            style={{
              fontSize: '24px',
              fontWeight: 800,
              color: '#FFFFFF',
              letterSpacing: '1px',
              textShadow: '0 2px 6px rgba(0,0,0,0.9), 2px 2px 0 #000',
            }}
          >
            LevelZero0ne
          </span>
        </div>
      )}

      {/* 5b. Optional Logo Popup Demo (after 1st clip + at last clip, no black screen, Mew SFX) */}
      {enableLogoPopupDemo && clipSequences.length >= 2 && (
        <>
          {[clipSequences[0].endFrame, Math.max(0, totalClipsDuration - 42)].map((popupStart, idx) => (
            <Sequence key={`popup-${idx}`} from={popupStart} durationInFrames={38}>
              <Audio src={staticFile('audio/stems/mew_popup_sfx.mp3')} volume={0.75} />
              {(() => {
                const rel = Math.max(0, frame - popupStart);
                const popScale = interpolate(rel, [0, 6, 10, 32, 38], [0.2, 1.15, 1.0, 1.0, 0.2], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                });
                const popOpacity = interpolate(rel, [0, 4, 32, 38], [0, 1, 1, 0], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                });
                return (
                  <div
                    style={{
                      position: 'absolute',
                      bottom: '140px',
                      left: '50%',
                      transform: `translateX(-50%) scale(${popScale})`,
                      opacity: popOpacity,
                      zIndex: 180,
                      pointerEvents: 'none',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '10px',
                      backgroundColor: 'rgba(0, 0, 0, 0.72)',
                      padding: '8px 18px 8px 8px',
                      borderRadius: '999px',
                      border: '2px solid #FFEB3B',
                      boxShadow: '0 8px 24px rgba(0,0,0,0.85)',
                    }}
                  >
                    <div
                      style={{
                        width: '62px',
                        height: '62px',
                        borderRadius: '50%',
                        overflow: 'hidden',
                        border: '2px solid #FFEB3B',
                      }}
                    >
                      <Img src={logoSrc} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                    </div>
                    <span
                      style={{
                        fontSize: '26px',
                        fontWeight: 900,
                        color: '#FFEB3B',
                        letterSpacing: '1px',
                      }}
                    >
                      LevelZero0ne
                    </span>
                  </div>
                );
              })()}
            </Sequence>
          ))}
        </>
      )}

      {/* 6. Outro Branding Sequence (75 Frames) */}
      {isOutroActive && (
        <AbsoluteFill
          style={{
            backgroundColor: '#050505',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 200,
          }}
        >
          {/* Floating Mew Logo */}
          <div
            style={{
              width: '280px',
              height: '280px',
              borderRadius: '50%',
              overflow: 'hidden',
              border: '6px solid #FFEB3B',
              boxShadow: '0 0 60px rgba(255, 235, 59, 0.4), 0 20px 50px rgba(0,0,0,0.9)',
              transform: `scale(${interpolate(outroRelFrame, [0, 20], [0.8, 1.0], {
                extrapolateRight: 'clamp',
              })}) translateY(${Math.sin(outroRelFrame / 10) * 10}px)`,
              marginBottom: '35px',
            }}
          >
            <Img src={logoSrc} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
          </div>

          {/* Channel Name */}
          <div
            style={{
              fontSize: '64px',
              fontWeight: 900,
              color: '#FFEB3B',
              letterSpacing: '2px',
              marginBottom: '10px',
              textShadow: '0 6px 20px rgba(0,0,0,0.9), 0 0 30px rgba(255, 235, 59, 0.4)',
            }}
          >
            LEVELZERO0NE
          </div>

          <div
            style={{
              fontSize: '32px',
              fontWeight: 700,
              color: '#FFFFFF',
              letterSpacing: '3px',
              opacity: 0.85,
              marginBottom: '40px',
            }}
          >
            DAILY CURATED RANKINGS
          </div>

          {/* Subscribe Button */}
          <div
            style={{
              backgroundColor: '#FF2D55',
              padding: '18px 50px',
              borderRadius: '50px',
              fontSize: '34px',
              fontWeight: 900,
              color: '#FFFFFF',
              letterSpacing: '2px',
              boxShadow: '0 0 35px rgba(255, 45, 85, 0.6), 0 10px 30px rgba(0,0,0,0.8)',
              display: 'flex',
              alignItems: 'center',
              gap: '12px',
            }}
          >
            <span>🔔</span> SUBSCRIBE FOR MORE
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
