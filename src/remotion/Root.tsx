import React from 'react';
import { Composition, getInputProps } from 'remotion';
import { CleanShort, CleanShortProps } from './CleanShort';
import { MrPurifiedWaterShort, MrPurifiedWaterShortProps } from './MrPurifiedWaterShort';

const defaultProps: CleanShortProps = {
  clips: [
    { videoPath: 'clip1.mp4', durationInFrames: 180, subtitleText: 'Confidence was high, traction was zero.' },
    { videoPath: 'clip2.mp4', durationInFrames: 180, subtitleText: 'He realized his mistake immediately.' },
    { videoPath: 'clip3.mp4', durationInFrames: 180, subtitleText: 'Bro thought he had the right of way.' },
    { videoPath: 'clip4.mp4', durationInFrames: 180, subtitleText: 'Instant karma came without a warning.' },
    { videoPath: 'clip5.mp4', durationInFrames: 180, subtitleText: 'Physics always has the final word.' },
  ],
  subCategoryName: 'ROAD RAGE JUSTICE',
};

export const Root: React.FC = () => {
  const inputProps = (getInputProps() as unknown as MrPurifiedWaterShortProps) || defaultProps;
  const activeClips = inputProps.clips && inputProps.clips.length > 0 ? inputProps.clips : defaultProps.clips;

  const clipsDuration = activeClips.reduce(
    (acc, clip) => acc + (clip.durationInFrames || 180),
    0
  );
  // Add 75 frames (2.5 seconds) for the 2D Outro Branding Sequence
  const OUTRO_FRAMES = 75;
  const totalDuration = (clipsDuration || 900) + OUTRO_FRAMES;

  return (
    <>
      <Composition
        id="RankingShort"
        component={MrPurifiedWaterShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={totalDuration}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultProps as unknown as Record<string, unknown>}
      />
      <Composition
        id="MrPurifiedWaterShort"
        component={MrPurifiedWaterShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={totalDuration}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultProps as unknown as Record<string, unknown>}
      />
    </>
  );
};


