"""Draw the 23 November 2026 one-day news image (1024x1024 PNG).

Session tooling: run it once with `python3 draw.py` and it writes
entry.png beside this file. The entry program (main.ts) only copies
that PNG to the output directory, so two runs write identical bytes.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (11, 18, 38)
PANEL = (22, 33, 58)
GOLD = (212, 175, 105)
WHITE = (245, 247, 250)
MUTED = (199, 208, 224)
FAINT = (148, 163, 184)
RED = (224, 82, 82)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
REG = FONT_DIR + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Split text into lines that fit `width` pixels."""
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    x = 46
    content_w = W - 2 * x

    # Header: kicker, date, gold rule.
    d.text((x, 36), "O N E   D A Y   I N   T H E   W O R L D",
           font=font(BOLD, 26), fill=GOLD)
    d.text((x, 74), "MONDAY, 23 NOVEMBER 2026",
           font=font(BOLD, 50), fill=WHITE)
    d.rectangle([x, 146, W - x, 150], fill=GOLD)

    # Lead story: COP31 climate talks fail.
    lead_top, lead_h = 168, 200
    d.rounded_rectangle([x, lead_top, W - x, lead_top + lead_h],
                        radius=14, fill=PANEL)
    d.rectangle([x, lead_top + 10, x + 8, lead_top + lead_h - 10],
                fill=RED)
    lx = x + 26
    d.text((lx, lead_top + 14), "CLIMATE  —  LEAD STORY",
           font=font(BOLD, 21), fill=RED)
    d.text((lx, lead_top + 44), "COP31 TALKS FAIL",
           font=font(BOLD, 38), fill=WHITE)
    d.text((lx, lead_top + 90), "NO FOSSIL-FUEL DEAL",
           font=font(BOLD, 38), fill=WHITE)
    lead_body = ("The Antalya summit ends with no agreement: the EU and "
                 "others reject any deal without language on phasing out "
                 "fossil fuels.")
    for i, line in enumerate(wrap(d, lead_body, font(REG, 24), content_w - 52)):
        d.text((lx, lead_top + 138 + i * 30), line,
               font=font(REG, 24), fill=MUTED)

    # Five more stories, one row each: tag chip + headline on the
    # first line, the summary wrapped over the next two lines.
    rows = [
        ("LIBYA", (70, 130, 200),
         "Sea drones hit Russian warship at Benghazi",
         "Suspected Ukrainian sea drones strike a Russian warship at "
         "the Benghazi naval base; at least 10 injured."),
        ("GULF", (46, 160, 110),
         "US-Iran war widens across the Gulf",
         "Houthis claim strikes on a Saudi oil refinery; an Iranian "
         "strike wounds two in Bahrain."),
        ("UKRAINE", (180, 130, 40),
         "14 missing after drone hits Kyiv-region block",
         "A Russian drone hits a residential building in the Kyiv "
         "region; a Russian cargo ship burns off Finland."),
        ("S. KOREA", (150, 90, 180),
         "Education minister quits in AI exam scandal",
         "South Korea's education minister resigns over AI-driven "
         "cheating in the university entrance exam."),
        ("SPORT", (40, 150, 150),
         "Liverpool rout United in Pochettino debut",
         "Liverpool hammer ten-man Manchester United; India post a "
         "record 720/9d in the Wellington Test."),
    ]
    row_top = 384
    row_h, row_gap = 104, 12
    for tag, colour, headline, body in rows:
        d.rounded_rectangle([x, row_top, W - x, row_top + row_h],
                            radius=12, fill=PANEL)
        tag_fnt = font(BOLD, 19)
        tw = d.textlength(tag, font=tag_fnt)
        d.rounded_rectangle([x + 16, row_top + 14, x + 32 + tw, row_top + 44],
                            radius=8, fill=colour)
        d.text((x + 24, row_top + 18), tag, font=tag_fnt, fill=WHITE)
        d.text((x + 44 + tw, row_top + 15), headline,
               font=font(BOLD, 27), fill=WHITE)
        for i, line in enumerate(wrap(d, body, font(REG, 22), content_w - 32)):
            d.text((x + 16, row_top + 54 + i * 25), line,
                   font=font(REG, 22), fill=MUTED)
        row_top += row_h + row_gap

    # Footer: sources.
    d.text((x, 968),
           "Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 The Hindu",
           font=font(REG, 19), fill=FAINT)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    draw()
