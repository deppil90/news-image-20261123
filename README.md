# One Day in the World — Monday, 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/deppil90/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/deppil90/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-day news infographic summing up the world news of Monday,
23 November 2026, built for the [make.fun](https://make.fun) bounty
`news-image-20261123`.

## The image

`entry.png` (1024×1024, under 1 MiB) leads with the COP31 climate
talks failing in Antalya — the EU and others rejecting any deal
without language on phasing out fossil fuels — and covers suspected
Ukrainian sea drones hitting a Russian warship at the Benghazi naval
base, the US–Iran war widening as Houthis claim strikes on a Saudi
oil refinery and an Iranian strike wounds two in Bahrain, a Russian
drone hitting a residential building in the Kyiv region with at least
14 missing, South Korea's education minister resigning over an AI
exam-cheating scandal, and Liverpool hammering ten-man Manchester
United in Mauricio Pochettino's debut.

Every headline was checked against live reporting for 23 November 2026
(Reuters, AP, AFP, The Hindu).

## How it works

- `draw.py` draws the infographic with Pillow (session use only).
- `main.ts` (Node 22, standard library only) copies the finished
  `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no clock —
  two runs write identical bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=p2frk8rs&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
