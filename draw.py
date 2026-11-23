#!/usr/bin/env python3
"""Draw the one-day news infographic for Monday, 23 November 2026.

Pillow-only, no network, no clock: the same script always renders the
same 1024x1024 PNG. Run with `python3 draw.py`; the output is entry.png
next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 46
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"

BG = (11, 16, 38)
CARD = (20, 27, 51)
WHITE = (255, 255, 255)
GREY = (205, 211, 224)
MUTED = (148, 156, 178)
GOLD = (212, 175, 105)
RED = (226, 88, 88)
BLUE = (96, 165, 250)
GREEN = (52, 199, 123)
AMBER = (245, 178, 66)
PURPLE = (178, 120, 235)
TEAL = (45, 196, 178)


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_tracked(draw, x, y, text, fnt, fill, tracking):
    """Draw text with extra space between characters."""
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


def card(draw, x, y, w, h, radius=14):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=CARD)


def story_card(draw, y, tag, tag_color, headline, summary):
    """One secondary story card; returns the y just below it."""
    x = MARGIN
    w = W - 2 * MARGIN
    inner = x + 16
    head_f = font("DejaVuSans-Bold.ttf", 26)
    body_f = font("DejaVuSans.ttf", 21)
    max_w = w - 32

    # Tag pill width decides how much room the headline gets.
    pill_w = draw.textlength(tag, font=head_f) + 24
    head_lines = wrap(draw, headline, head_f, max_w - pill_w - 12)
    body_lines = wrap(draw, summary, body_f, max_w)
    h = 8 + 30 + len(head_lines) * 30 + len(body_lines) * 23 + 6
    card(draw, x, y, w, h)

    # Tag pill.
    pill_y = y + 8
    draw.rounded_rectangle(
        [inner, pill_y, inner + pill_w, pill_y + 30], radius=8, fill=tag_color
    )
    draw.text((inner + 12, pill_y + 3), tag, font=head_f, fill=WHITE)

    # Headline to the right of the pill.
    hx = inner + pill_w + 12
    hy = y + 11
    for line in head_lines:
        draw.text((hx, hy), line, font=head_f, fill=WHITE)
        hy += 30

    # Summary underneath, full width.
    by = y + 8 + 30 + len(head_lines) * 30
    for line in body_lines:
        draw.text((inner, by), line, font=body_f, fill=GREY)
        by += 23
    return y + h + 6


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Masthead.
    kicker_f = font("DejaVuSans-Bold.ttf", 26)
    # Shrink the date until it fits between the margins.
    date_size = 60
    while True:
        date_f = font("DejaVuSans-Bold.ttf", date_size)
        if d.textlength("MONDAY, 23 NOVEMBER 2026", font=date_f) <= W - 2 * MARGIN:
            break
        date_size -= 1
    draw_tracked(d, MARGIN, 34, "ONE DAY IN THE WORLD", kicker_f, GOLD, 6)
    d.text((MARGIN, 68), "MONDAY, 23 NOVEMBER 2026", font=date_f, fill=WHITE)
    d.rectangle([MARGIN, 138, W - MARGIN, 142], fill=GOLD)

    # Lead story card.
    y = 152
    w = W - 2 * MARGIN
    lead_kicker_f = font("DejaVuSans-Bold.ttf", 24)
    lead_head_f = font("DejaVuSans-Bold.ttf", 40)
    lead_body_f = font("DejaVuSans.ttf", 23)
    lead = (
        "The Antalya summit ends with no agreement: the EU and others "
        "reject any deal without language on phasing out fossil fuels."
    )
    lead_lines = wrap(d, lead, lead_body_f, w - 52)
    lead_h = 12 + 28 + 2 * 48 + len(lead_lines) * 28 + 12
    card(d, MARGIN, y, w, lead_h)
    d.rectangle([MARGIN, y + 8, MARGIN + 8, y + lead_h - 8], fill=RED)
    d.text((MARGIN + 26, y + 14), "CLIMATE  —  LEAD STORY",
           font=lead_kicker_f, fill=RED)
    d.text((MARGIN + 26, y + 46), "COP31 TALKS FAIL",
           font=lead_head_f, fill=WHITE)
    d.text((MARGIN + 26, y + 94), "NO FOSSIL-FUEL DEAL",
           font=lead_head_f, fill=WHITE)
    by = y + 46 + 2 * 48
    for line in lead_lines:
        d.text((MARGIN + 26, by), line, font=lead_body_f, fill=GREY)
        by += 28

    y = y + lead_h + 6
    y = story_card(
        d, y, "LIBYA", BLUE,
        "Sea drones hit Russian warship at Benghazi",
        "Suspected Ukrainian sea drones strike a Russian warship at the "
        "Benghazi naval base; at least 10 injured.",
    )
    y = story_card(
        d, y, "GULF", GREEN,
        "US-Iran war widens across the Gulf",
        "Houthis claim strikes on a Saudi oil refinery; an Iranian strike "
        "wounds two in Bahrain.",
    )
    y = story_card(
        d, y, "UKRAINE", AMBER,
        "14 missing after drone hits Kyiv-region block",
        "A Russian drone hits a residential building in the Kyiv region; a "
        "Russian cargo ship burns off Finland.",
    )
    y = story_card(
        d, y, "S. KOREA", PURPLE,
        "Education minister quits in AI exam scandal",
        "South Korea's education minister resigns over AI-driven cheating "
        "in the university entrance exam.",
    )
    y = story_card(
        d, y, "SPORT", TEAL,
        "Liverpool rout United in Pochettino debut",
        "Liverpool hammer ten-man Manchester United; India post a record "
        "720/9d in the Wellington Test.",
    )

    # Footer.
    foot_f = font("DejaVuSans.ttf", 21)
    d.text((MARGIN, H - 34), "Sources: Reuters · AP · AFP · The Hindu",
           font=foot_f, fill=MUTED)

    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
