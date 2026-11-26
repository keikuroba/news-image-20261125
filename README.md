# Wednesday 25 November 2026 — the world in one image

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/keikuroba/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/keikuroba/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A hand-drawn newspaper front page that packs Wednesday 25 November 2026
into a single picture — five illustrated stories and a ticker of the
rest of the day:

- **Lead — Tariffs.** The US is poised to unveil findings of a probe
  into excess factory capacity, proposing country-specific tariffs on 14
  trading partners — headline rates of 20–40%, capped by existing trade
  deals. Nothing takes effect before a hearing on 25 January.
- **Conflict — Hormuz.** Iran says naval mines hit four tankers and an
  LNG carrier in the Strait of Hormuz, setting them on fire; the US
  military disputes the claim. Iran also claims it downed two US drones
  over the strait.
- **Disaster — Cairo.** A fuel tanker carrying petroleum products
  overturns on a major road near Cairo and catches fire; at least 30
  people die, flames spreading to nearby cars and motorcycles.
- **Space — Shenzhou-24.** China launches Shenzhou-24 carrying two
  Chinese astronauts and Pakistan's Muhammad Zeeshan Ali — Pakistan's
  first astronaut in space — docking at the Tiangong station.
- **Markets — Wall Street.** Wall Street slides as AI shares sell off:
  the S&P 500 falls about 2.2% and the Nasdaq about 3.2% in midday
  trading on AI, inflation and tariff fears; Asian stocks fall sharply
  too.
- **Also today.** Houthis hit Riyadh's tallest tower, 11 wounded; over
  30 countries urge Russia to stop chemical agents in Ukraine; Spain
  heads to a snap general election; Huawei convicted in a sprawling US
  criminal trial; the US CIA and ODNI suffer a cybersecurity breach;
  Nvidia reinstates Jensen Huang as CEO; Trump says US war funding
  against Iran is secured through January; Bangladesh raises garment
  workers' minimum wage 36% to $139 after protests.

## How it works

`main.py` draws the whole front page with Pillow — masthead, five
illustrated stories, ticker — and writes `/output/entry.png`, a
1024x1024 PNG. The drawing is deterministic: two runs write identical
bytes. No network, no clock, no randomness.

Run it locally with `python3 main.py` (writes `/output/entry.png`).
