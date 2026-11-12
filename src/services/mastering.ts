import * as path from 'path';
import * as fs from 'fs';
import ffmpeg from 'fluent-ffmpeg';

function parseArgs(): { input: string; output: string } {
  const args = process.argv.slice(2);
  let input = '';
  let output = '';

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--input' && args[i + 1]) {
      input = args[i + 1];
      i++;
    } else if (args[i] === '--output' && args[i + 1]) {
      output = args[i + 1];
      i++;
    }
  }

  if (!input || !output) {
    console.error('Usage: ts-node src/services/mastering.ts --input <path> --output <path>');
    process.exit(1);
  }

  return { input, output };
}

async function masterAudio(inputPath: string, outputPath: string): Promise<void> {
  const resolvedInput = path.resolve(inputPath);
  const resolvedOutput = path.resolve(outputPath);

  if (!fs.existsSync(resolvedInput)) {
    throw new Error(`Input file does not exist: ${resolvedInput}`);
  }

  const outputDir = path.dirname(resolvedOutput);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  return new Promise((resolve, reject) => {
    console.log(`[Mastering] Processing: ${resolvedInput} -> ${resolvedOutput}`);

    ffmpeg(resolvedInput)
      .outputOptions([
        '-c:v', 'copy',
        '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11',
        '-c:a', 'aac',
        '-b:a', '320k',
      ])
      .output(resolvedOutput)
      .on('start', (cmdLine) => {
        console.log(`[Mastering] Spawned FFmpeg command: ${cmdLine}`);
      })
      .on('progress', (progress) => {
        if (progress.percent) {
          console.log(`[Mastering] Progress: ${Math.round(progress.percent)}%`);
        }
      })
      .on('error', (err, stdout, stderr) => {
        console.error(`[Mastering] Error: ${err.message}`);
        console.error(stderr);
        reject(err);
      })
      .on('end', () => {
        console.log(`[Mastering] Successfully mastered output to: ${resolvedOutput}`);
        resolve();
      })
      .run();
  });
}

async function main() {
  try {
    const { input, output } = parseArgs();
    await masterAudio(input, output);
  } catch (error) {
    console.error('[Mastering] Fatal error:', error);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

