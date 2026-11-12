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

export interface CleanClipItem {
  videoPath: string;
  voPath?: string;
  subtitleText?: string;
  durationInFrames: number;
  voDuration?: number; // seconds
}

export interface CleanShortProps {
  clips: CleanClipItem[];
  subCategoryName: string;
}

export const CleanShort: React.FC<CleanShortProps> = ({
  clips,
  subCategoryName,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Accumulate sequence offsets strictly from Rank 5 down to Rank 1 (countdown)
  const totalClips = clips.length;
  let accumulatedFrames = 0;
  const clipSequences = clips.map((clip, index) => {
    const startFrame = accumulatedFrames;
    accumulatedFrames += clip.durationInFrames;
    const rank = totalClips - index; // e.g. for 5 clips: index 0 -> Rank 5, index 4 -> Rank 1
    return {
      clip,
      index,
      rank,
      startFrame,
      endFrame: accumulatedFrames,
      durationInFrames: clip.durationInFrames,
    };
  });

  const totalClipsDuration = accumulatedFrames;
  const OUTRO_FRAMES = 75; // 2.5s outro
  const isOutroActive = frame >= totalClipsDuration;
  const outroRelFrame = Math.max(0, frame - totalClipsDuration);

  // Determine current active rank
  let currentRank = clipSequences[0]?.rank ?? 5;
  for (const seq of clipSequences) {
    if (frame >= seq.startFrame && frame < seq.endFrame) {
      currentRank = seq.rank;
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

  const earshotAudioSrc = staticFile('audio/earshot_sonic_brand.mp3');
  const logoSrc = staticFile('levelzero0ne_logo.jpg');

  // Intro 2D Animation Variables (frames 0 to 45 on first clip)
  const introScale = interpolate(frame, [0, 14, 24, 34, 45], [0, 1.18, 1.0, 1.0, 0.45], {
    extrapolateRight: 'clamp',
  });
  const introX = interpolate(frame, [0, 32, 45], [540, 540, 1080 - 35 - 55], {
    extrapolateRight: 'clamp',
  });
  const introY = interpolate(frame, [0, 32, 45], [860, 860, 230 + 55], {
    extrapolateRight: 'clamp',
  });
  const introTextOpacity = interpolate(frame, [6, 16, 30, 38], [0, 1, 1, 0], {
    extrapolateRight: 'clamp',
  });
  const introRippleScale1 = interpolate(frame, [0, 28], [0.8, 2.2], {
    extrapolateRight: 'clamp',
  });
  const introRippleOpacity1 = interpolate(frame, [0, 14, 28], [0.8, 0.4, 0], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ backgroundColor: '#000000' }}>
      {/* 1. Consistent Earshot Audio Branding (Plays on First Clip & on Outro) */}
      <Sequence from={0} durationInFrames={55}>
        <Audio src={earshotAudioSrc} volume={1.0} />
      </Sequence>
      <Sequence from={totalClipsDuration} durationInFrames={55}>
        <Audio src={earshotAudioSrc} volume={1.0} />
      </Sequence>

      {/* 2. Clip Sequences (Rank 5 down to Rank 1) */}
      {!isOutroActive &&
        clipSequences.map((seq) => {
          const videoSrc = resolveRemotionPath(seq.clip.videoPath);
          const voSrc = seq.clip.voPath ? resolveRemotionPath(seq.clip.voPath) : '';
          const voDurationFrames = Math.round((seq.clip.voDuration || 2.5) * fps);

          return (
            <Sequence
              key={seq.index}
              from={seq.startFrame}
              durationInFrames={seq.durationInFrames}
            >
              {/* Visual Framing: Blurred Background + Contained Foreground */}
              <AbsoluteFill>
                {/* Background: <OffthreadVideo> scaled to fill with blur, audio muted */}
                <OffthreadVideo
                  src={videoSrc}
                  volume={0}
                  style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                    filter: 'blur(30px) brightness(0.35)',
                  }}
                />

                {/* Foreground Container: Centered card with overflow hidden to clip any edge watermarks */}
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
                    padding: '190px 20px 140px 20px',
                  }}
                >
                  <div
                    style={{
                      maxWidth: '1000px',
                      maxHeight: '1360px',
                      borderRadius: '16px',
                      overflow: 'hidden',
                      border: '2px solid #222222',
                      boxShadow: '0 20px 50px rgba(0, 0, 0, 0.85)',
                      backgroundColor: '#000000',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                    }}
                  >
                    <OffthreadVideo
                      src={videoSrc}
                      volume={(f) => (voSrc && f < voDurationFrames ? 0.35 : 1.0)}
                      style={{
                        maxWidth: '1000px',
                        maxHeight: '1360px',
                        width: 'auto',
                        height: 'auto',
                        objectFit: 'contain',
                        transform: 'scale(1.04)', // Slight zoom to guarantee all source border watermarks are trimmed
                      }}
                    />
                  </div>
                </div>
              </AbsoluteFill>

              {/* Neural Voiceover */}
              {voSrc && (
                <Sequence from={0} durationInFrames={voDurationFrames}>
                  <Audio src={voSrc} volume={1.0} />
                </Sequence>
              )}

              {/* Single clean bottom subtitle synced to the VO */}
              {seq.clip.subtitleText && (
                <Sequence from={0} durationInFrames={voDurationFrames + 15}>
                  <div
                    style={{
                      position: 'absolute',
                      bottom: '250px',
                      width: '100%',
                      display: 'flex',
                      justifyContent: 'center',
                      padding: '0 50px',
                      zIndex: 50,
                    }}
                  >
                    <span
                      style={{
                        fontFamily: 'Montserrat, Impact, sans-serif',
                        fontSize: '48px',
                        fontWeight: 900,
                        color: '#FFFFFF',
                        WebkitTextStroke: '4px #000000',
                        textShadow: '0 4px 16px rgba(0,0,0,0.9)',
                        textAlign: 'center',
                        lineHeight: 1.2,
                      }}
                    >
                      {seq.clip.subtitleText}
                    </span>
                  </div>
                </Sequence>
              )}
            </Sequence>
          );
        })}

      {/* 3. Top Header Banner */}
      {!isOutroActive && (
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '180px',
            backgroundColor: '#000000',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 40,
            borderBottom: '2px solid #222222',
          }}
        >
          {/* Top Header Corner Brand Watermarks */}
          <div
            style={{
              position: 'absolute',
              top: '16px',
              left: '35px',
              fontFamily: 'Montserrat, sans-serif',
              fontSize: '16px',
              fontWeight: 800,
              color: 'rgba(255, 230, 0, 0.75)',
              letterSpacing: '2px',
              textTransform: 'uppercase',
            }}
          >
            ORIGINAL COUNTDOWN
          </div>
          <div
            style={{
              position: 'absolute',
              top: '16px',
              right: '35px',
              fontFamily: 'Montserrat, sans-serif',
              fontSize: '16px',
              fontWeight: 800,
              color: 'rgba(255, 255, 255, 0.65)',
              letterSpacing: '2px',
              textTransform: 'uppercase',
            }}
          >
            @LEVELZERO0NE
          </div>

          <div
            style={{
              fontFamily: 'Montserrat, Impact, sans-serif',
              fontSize: '46px',
              fontWeight: 900,
              color: '#FFFFFF',
              textTransform: 'uppercase',
              letterSpacing: '2px',
              lineHeight: 1.1,
            }}
          >
            RANKING
          </div>
          <div
            style={{
              fontFamily: 'Montserrat, Impact, sans-serif',
              fontSize: '52px',
              fontWeight: 900,
              color: '#FFE600',
              textTransform: 'uppercase',
              letterSpacing: '2px',
              lineHeight: 1.1,
              marginTop: '2px',
            }}
          >
            {subCategoryName}
          </div>
        </div>
      )}

      {/* 4. Left Countdown Ladder (5. down to 1.) */}
      {!isOutroActive && (
        <div
          style={{
            position: 'absolute',
            left: '40px',
            top: '240px',
            display: 'flex',
            flexDirection: 'column',
            gap: '16px',
            zIndex: 40,
          }}
        >
          {[...clipSequences].sort((a, b) => b.rank - a.rank).map((seq) => {
            const rankNum = seq.rank;
            const isActive = currentRank === rankNum;
            const rankColor = isActive ? '#FFE600' : '#FFFFFF';
            const scale = isActive ? 1.15 : 1.0;
            const opacity = isActive ? 1.0 : 0.3;

            return (
              <div
                key={rankNum}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  opacity,
                  transform: `scale(${scale})`,
                  transformOrigin: 'left center',
                  transition: 'all 0.2s ease',
                }}
              >
                <span
                  style={{
                    fontFamily: 'Montserrat, Impact, sans-serif',
                    fontSize: '58px',
                    fontWeight: 900,
                    color: rankColor,
                    textShadow: '3px 3px 0 #000, -3px -3px 0 #000',
                    lineHeight: 1,
                  }}
                >
                  {rankNum}.
                </span>
              </div>
            );
          })}
        </div>
      )}

      {/* 5. Persistent Right Channel Watermark (Visible after frame 45 until outro) */}
      {!isOutroActive && frame >= 45 && (
        <div
          style={{
            position: 'absolute',
            right: '35px',
            top: '230px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            zIndex: 45,
            filter: 'drop-shadow(0 6px 16px rgba(0, 0, 0, 0.85))',
          }}
        >
          <div
            style={{
              width: '110px',
              height: '110px',
              borderRadius: '50%',
              overflow: 'hidden',
              border: '3px solid #FFE600',
              boxShadow: '0 0 24px rgba(255, 230, 0, 0.5)',
              backgroundColor: '#000000',
            }}
          >
            <Img
              src={logoSrc}
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'cover',
              }}
            />
          </div>
          <span
            style={{
              fontFamily: 'Montserrat, Impact, sans-serif',
              fontSize: '20px',
              fontWeight: 900,
              color: '#FFFFFF',
              letterSpacing: '1.5px',
              marginTop: '8px',
              textTransform: 'uppercase',
              textShadow: '0 2px 8px rgba(0,0,0,0.9)',
              WebkitTextStroke: '1px #000000',
            }}
          >
            LevelZero0ne
          </span>
        </div>
      )}

      {/* 6. First Clip: Simple 2D Intro Animation (Frames 0 to 45) */}
      {!isOutroActive && frame < 45 && (
        <div
          style={{
            position: 'absolute',
            left: `${introX}px`,
            top: `${introY}px`,
            transform: `translate(-50%, -50%) scale(${introScale})`,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            zIndex: 60,
          }}
        >
          {/* Concentric 2D Vector Ripple Ring */}
          {frame < 30 && (
            <div
              style={{
                position: 'absolute',
                width: '240px',
                height: '240px',
                borderRadius: '50%',
                border: '3px solid #FFE600',
                transform: `scale(${introRippleScale1})`,
                opacity: introRippleOpacity1,
                pointerEvents: 'none',
              }}
            />
          )}

          {/* Central Logo Emblem */}
          <div
            style={{
              width: '240px',
              height: '240px',
              borderRadius: '50%',
              overflow: 'hidden',
              border: '6px solid #FFE600',
              boxShadow: '0 0 50px rgba(255, 230, 0, 0.75)',
              backgroundColor: '#000000',
            }}
          >
            <Img
              src={logoSrc}
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'cover',
              }}
            />
          </div>

          {/* Intro Text Reveal */}
          <div
            style={{
              opacity: introTextOpacity,
              marginTop: '20px',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            <span
              style={{
                fontFamily: 'Montserrat, Impact, sans-serif',
                fontSize: '44px',
                fontWeight: 900,
                color: '#FFE600',
                letterSpacing: '3px',
                textTransform: 'uppercase',
                textShadow: '0 4px 20px rgba(0,0,0,0.95)',
                WebkitTextStroke: '2px #000000',
              }}
            >
              LevelZero0ne
            </span>
            <span
              style={{
                fontFamily: 'Montserrat, sans-serif',
                fontSize: '20px',
                fontWeight: 800,
                color: '#FFFFFF',
                letterSpacing: '4px',
                textTransform: 'uppercase',
                marginTop: '4px',
                textShadow: '0 2px 10px rgba(0,0,0,0.9)',
              }}
            >
              Original Countdown
            </span>
          </div>
        </div>
      )}

      {/* 7. After Last Clip: Simple 2D Outro Animation (Sequence) */}
      {isOutroActive && (
        <Sequence from={totalClipsDuration} durationInFrames={OUTRO_FRAMES}>
          {(() => {
            const relF = outroRelFrame;
            const outroScale = interpolate(relF, [0, 16, 26], [0.3, 1.15, 1.0], {
              extrapolateRight: 'clamp',
            });
            const outroFade = interpolate(relF, [OUTRO_FRAMES - 15, OUTRO_FRAMES], [1, 0], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const floatOffset = Math.sin(relF * 0.15) * 8;
            const rippleScale = interpolate(relF, [0, 35], [0.9, 2.5], {
              extrapolateRight: 'clamp',
            });
            const rippleOpacity = interpolate(relF, [0, 18, 35], [0.8, 0.3, 0], {
              extrapolateRight: 'clamp',
            });

            return (
              <AbsoluteFill
                style={{
                  background: 'radial-gradient(circle at center, #1c1900 0%, #080808 65%, #000000 100%)',
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  opacity: outroFade,
                  zIndex: 100,
                }}
              >
                {/* Outro 2D Ripple Ring */}
                <div
                  style={{
                    position: 'absolute',
                    width: '320px',
                    height: '320px',
                    borderRadius: '50%',
                    border: '4px solid #FFE600',
                    transform: `scale(${rippleScale})`,
                    opacity: rippleOpacity,
                    pointerEvents: 'none',
                  }}
                />

                {/* Animated Floating Emblem */}
                <div
                  style={{
                    width: '280px',
                    height: '280px',
                    borderRadius: '50%',
                    overflow: 'hidden',
                    border: '6px solid #FFE600',
                    boxShadow: '0 0 60px rgba(255, 230, 0, 0.65)',
                    backgroundColor: '#000000',
                    transform: `scale(${outroScale}) translateY(${floatOffset}px)`,
                    marginBottom: '35px',
                  }}
                >
                  <Img
                    src={logoSrc}
                    style={{
                      width: '100%',
                      height: '100%',
                      objectFit: 'cover',
                    }}
                  />
                </div>

                {/* Channel Title */}
                <div
                  style={{
                    fontFamily: 'Montserrat, Impact, sans-serif',
                    fontSize: '60px',
                    fontWeight: 900,
                    color: '#FFE600',
                    letterSpacing: '4px',
                    textTransform: 'uppercase',
                    WebkitTextStroke: '2px #000000',
                    textShadow: '0 4px 30px rgba(255, 230, 0, 0.4)',
                    marginBottom: '8px',
                    transform: `scale(${outroScale})`,
                  }}
                >
                  LevelZero0ne
                </div>

                {/* Tagline */}
                <div
                  style={{
                    fontFamily: 'Montserrat, sans-serif',
                    fontSize: '24px',
                    fontWeight: 800,
                    color: 'rgba(255, 255, 255, 0.85)',
                    letterSpacing: '3px',
                    textTransform: 'uppercase',
                    marginBottom: '40px',
                  }}
                >
                  Daily Curated Rankings
                </div>

                {/* Interactive CTA Pill Button */}
                <div
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px',
                    backgroundColor: '#FF0000',
                    padding: '18px 38px',
                    borderRadius: '40px',
                    boxShadow: '0 8px 30px rgba(255, 0, 0, 0.55)',
                    border: '2px solid #FFFFFF',
                    transform: `scale(${interpolate(relF, [18, 28], [0.5, 1.0], { extrapolateRight: 'clamp' })})`,
                  }}
                >
                  {/* Bell Icon SVG */}
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="#FFFFFF">
                    <path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.63-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.64 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z" />
                  </svg>
                  <span
                    style={{
                      fontFamily: 'Montserrat, Impact, sans-serif',
                      fontSize: '28px',
                      fontWeight: 900,
                      color: '#FFFFFF',
                      letterSpacing: '2px',
                      textTransform: 'uppercase',
                    }}
                  >
                    Subscribe For More
                  </span>
                </div>
              </AbsoluteFill>
            );
          })()}
        </Sequence>
      )}
    </AbsoluteFill>
  );
};
