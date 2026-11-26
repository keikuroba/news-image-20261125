#!/usr/bin/env python3
"""news-image-20261125 rev1: draw one 1024x1024 PNG summarising the world news of
Wednesday 25 November 2026. Deterministic: no randomness, no timestamps, no network.
Writes to /output/entry.png (or $ENTRY_OUTPUT)."""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.png")

BASE = os.path.dirname(os.path.abspath(__file__))


def font(name, size):
    p = os.path.join(BASE, "fonts", name)
    if os.path.exists(p):
        return ImageFont.truetype(p, size)
    return ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/" + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)  # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731

PAPER = (247, 243, 234)
INK = (20, 20, 20)
NAVY = (20, 33, 61)
GOLD = (201, 162, 39)
RULE = (180, 170, 150)
MUTED = (90, 85, 75)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.text((512, 22), "THE WORLD IN ONE IMAGE", font=SERIF_B(44),
           fill=(255, 255, 255), anchor="ma")
    d.text((512, 76), "WEDNESDAY  •  25 NOVEMBER 2026", font=SANS_B(24),
           fill=GOLD, anchor="ma")

    # --- lead story ---
    d.text((48, 138), "TRADE", font=SANS_B(22), fill=(150, 30, 30))
    d.line([48, 168, 976, 168], fill=RULE, width=2)
    y = para(d, 48, 182, "U.S. proposes new tariffs on 14 trading partners",
             SERIF_B(40), 928, 48)
    y = para(d, 48, y + 8,
             "Headline rates of 20 to 40 percent, capped by existing trade deals. "
             "The Trump administration is set to unveil findings of a probe on excess "
             "factory capacity; nothing takes effect before a January 25 hearing.",
             SANS(24), 928, 32)

    # --- 2x2 grid ---
    d.line([48, 372, 976, 372], fill=RULE, width=2)
    stories = [
        ("MIDDLE EAST", "Mines hit tankers in the Strait of Hormuz",
         "Iran says four tankers and an LNG carrier struck naval mines and caught "
         "fire. The U.S. military disputes the claim; Tehran also claims it shot "
         "down two American drones."),
        ("EGYPT", "Fuel tanker crash on Cairo ring road kills at least 30",
         "A tanker carrying petroleum products overturned near Cairo and caught fire, "
         "flames spreading to nearby cars and motorcycles. Dozens were dead or injured."),
        ("SPACE", "China launches Shenzhou-24 with Pakistan's first astronaut",
         "Shenzhou-24 lifted off carrying two Chinese astronauts and Pakistan's "
         "Muhammad Zeeshan Ali, the first Pakistani in space, bound for the Tiangong "
         "station."),
        ("MARKETS", "Wall Street slides as AI shares sell off",
         "The S&P 500 fell about 2.2 percent and the Nasdaq about 3.2 percent in "
         "midday trading, on AI, inflation and tariff fears; Asian stocks fell sharply."),
    ]
    col_w, col_x = 452, [48, 524]
    row_y = [392, 592]
    for i, (kick, head, body) in enumerate(stories):
        x = col_x[i % 2]
        yy = row_y[i // 2]
        d.text((x, yy), kick, font=SANS_B(19), fill=(150, 30, 30))
        yy = para(d, x, yy + 26, head, SERIF_B(26), col_w, 32)
        para(d, x, yy + 4, body, SANS(20), col_w, 27)

    # --- ticker ---
    d.rectangle([0, 800, W, 906], fill=(232, 226, 210))
    d.text((48, 812), "ALSO TODAY", font=SANS_B(19), fill=(150, 30, 30))
    ticks = [
        "Houthis hit Riyadh's tallest tower, 11 wounded.",
        "Over 30 countries urge Russia to stop chemical agents in Ukraine.",
        "Spain heads to a snap general election on Sunday.",
        "Huawei convicted in a sprawling U.S. criminal trial over Iran business.",
        "U.S. intelligence agencies CIA and ODNI hit by a cyber breach.",
        "Nvidia reinstates Jensen Huang as chief executive.",
    ]
    yy = 842
    for t in ticks:
        d.text((48, yy), "\u2022  " + t, font=SANS(18), fill=INK)
        yy += 24

    # --- footer ---
    d.line([48, 930, 976, 930], fill=RULE, width=2)
    d.text((48, 946), "Sources: Reuters  •  Standard Topic  •  Open Chronicle",
           font=SANS(18), fill=MUTED)
    d.text((48, 972), "Drawn by program — no photograph.  make.fun news-image-20261125",
           font=SANS(18), fill=MUTED)

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    img.save(OUTPUT_PATH, format="PNG")
    print("wrote %s (%dx%d)" % (OUTPUT_PATH, W, H))


if __name__ == "__main__":
    draw()
