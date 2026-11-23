// One-day news image entry for make.fun news-image-20261123
// (Node 22, standard library only). The image is entry.png beside
// this file: a 1024x1024 infographic summing up Monday,
// 23 November 2026. The program just writes those exact bytes to
// the output directory, so every run produces the same file.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// In the grader the output directory is /output.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const image = readFileSync(join(here, "entry.png"));

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.png"), image);
