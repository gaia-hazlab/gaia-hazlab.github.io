"""Generate the flow diagrams for the agents-intro lecture and deck.

Writes SVGs to book/img/agents-*.svg. Run from the repo root:

    pixi run python book/teaching/agents-intro/slides/figscripts/make_diagrams.py

Style follows book/img/agent-loop.svg and the site palette (gaia-book.css).
Edit this file, not the SVGs.
"""

from html import escape
from pathlib import Path

PURPLE = "#4b2e83"
PERI = "#6d5bd0"
PERI_LIGHT = "#c3b8f0"
LAV = "#f5f3fb"
INK = "#2a1a4f"
STONE = "#6f6890"
AMBER = "#c77d00"
AMBER_BG = "#fff7e6"
RED = "#b3402a"
FONT = "Inter, Helvetica, Arial, sans-serif"

OUT = Path(__file__).resolve().parents[4] / "img"


class Svg:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parts = []

    def box(self, x, y, w, h, lines, fill="#fff", stroke=PURPLE, dash=None,
            size=22, color=INK, bold_first=False, rx=8, sw=2):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
        n = len(lines)
        lh = size * 1.3
        y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.35
        for i, line in enumerate(lines):
            fw = ' font-weight="700"' if (bold_first and i == 0) else ""
            self.parts.append(
                f'<text x="{x + w / 2}" y="{y0 + i * lh:.1f}" text-anchor="middle" '
                f'font-size="{size}" fill="{color}"{fw}>{escape(line)}</text>')

    def text(self, x, y, s, size=20, color=STONE, anchor="start", bold=False,
             italic=False):
        fw = ' font-weight="700"' if bold else ""
        fs = ' font-style="italic"' if italic else ""
        self.parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
            f'fill="{color}"{fw}{fs}>{escape(s)}</text>')

    def arrow(self, x1, y1, x2, y2, color=PURPLE, both=False, dash=None, sw=2.5):
        m = "purple" if color == PURPLE else ("red" if color == RED else
                                              ("amber" if color == AMBER else "stone"))
        d = f' stroke-dasharray="{dash}"' if dash else ""
        ms = f' marker-start="url(#a-{m})"' if both else ""
        self.parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}"{d} marker-end="url(#a-{m})"{ms}/>')

    def path(self, d, color=PURPLE, dash=None, sw=2.5, arrow=True):
        m = "purple" if color == PURPLE else ("red" if color == RED else
                                              ("amber" if color == AMBER else "stone"))
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        me = f' marker-end="url(#a-{m})"' if arrow else ""
        self.parts.append(
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{dd}{me}/>')

    def bracket(self, x1, x2, y, label, color=STONE, above=False):
        t = -1 if above else 1
        self.path(f"M {x1} {y} L {x1} {y + 12 * t} L {x2} {y + 12 * t} L {x2} {y}",
                  color=color, sw=1.5, arrow=False)
        self.text((x1 + x2) / 2, y + (34 if not above else -20), label,
                  size=19, color=color, anchor="middle", italic=True)

    def write(self, name):
        defs = "".join(
            f'<marker id="a-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" '
            f'fill="{c}"/></marker>'
            for k, c in [("purple", PURPLE), ("red", RED), ("amber", AMBER),
                         ("stone", STONE)])
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
               f'width="{self.w}" height="{self.h}" '
               f'font-family="{FONT}" font-size="22">\n<defs>{defs}</defs>\n'
               + "\n".join(self.parts) + "\n</svg>\n")
        (OUT / name).write_text(svg)
        print("wrote", OUT / name)


def stack():
    s = Svg(1200, 640)
    # harness
    s.box(360, 120, 480, 380, [], fill="#fff", stroke=PURPLE, sw=2.5, rx=12)
    s.text(600, 155, "Harness: the loop and the permission checks", size=24,
           color=PURPLE, anchor="middle", bold=True)
    s.box(390, 180, 420, 110,
          ["context window", "system prompt · context file · tool + skill descriptions",
           "transcript · tool results"],
          fill=LAV, stroke=PERI, size=20, bold_first=True)
    s.box(400, 330, 120, 56, ["gather"], fill="#fff", stroke=PURPLE, size=22)
    s.box(540, 330, 120, 56, ["act"], fill="#fff", stroke=PURPLE, size=22)
    s.box(680, 330, 120, 56, ["verify"], fill="#fff", stroke=PURPLE, size=22)
    s.arrow(520, 358, 540, 358)
    s.arrow(660, 358, 680, 358)
    s.path("M 740 386 Q 740 430 600 430 Q 460 430 460 386", color=PURPLE)
    s.text(600, 470, "repeat until done, budget spent, or killed", size=19,
           color=STONE, anchor="middle", italic=True)
    # model
    s.box(440, 550, 320, 64, ["Model: predicts the next token"], fill="#fff",
          stroke=INK, size=22)
    s.arrow(600, 500, 600, 550, both=True)
    s.text(620, 530, "tokens in · tool calls out", size=18, color=STONE)
    # left: read every turn
    s.text(40, 150, "Loaded every turn", size=22, color=PURPLE, bold=True)
    s.box(40, 175, 280, 64, ["Context file", "CLAUDE.md → AGENTS.md"], fill="#fff",
          stroke=PURPLE, size=20, bold_first=True)
    s.box(40, 260, 280, 64, ["Tool schemas", "name · description · arguments"],
          fill="#fff", stroke=PURPLE, size=20, bold_first=True)
    s.box(40, 345, 280, 64, ["Skill descriptions", "one or two sentences each"],
          fill="#fff", stroke=PURPLE, size=20, bold_first=True)
    for y in (207, 292, 377):
        s.path(f"M 320 {y} Q 350 {y} 360 235", color=PERI, sw=2)
    s.text(40, 445, "Short files: paid for on every call.", size=19, color=STONE,
           italic=True)
    # right: on demand
    s.text(880, 150, "Called on demand", size=22, color=PURPLE, bold=True)
    s.box(880, 175, 280, 64, ["Tools", "shell · files · web · GitHub"], fill="#fff",
          stroke=PURPLE, size=20, bold_first=True)
    s.box(880, 260, 280, 64, ["Skill body", "SKILL.md, loaded on match"], fill="#fff",
          stroke=PURPLE, size=20, bold_first=True)
    s.box(880, 345, 280, 64, ["Subagent", "fresh window, one task"], fill="#fff",
          stroke=PURPLE, size=20, bold_first=True)
    s.box(880, 430, 280, 64, ["MCP server", "tools outside the harness"], fill="#fff",
          stroke=PURPLE, size=20, bold_first=True)
    for y in (207, 292, 377, 462):
        s.arrow(840, min(y, 480), 880, y, both=True, color=PERI, sw=2)
    s.write("agents-stack.svg")


def context_window():
    s = Svg(1200, 520)
    x = 60
    segs = [(["system", "prompt"], 150, "#fff"), (["context", "file"], 150, "#fff"),
            (["tool + skill", "descriptions"], 220, "#fff"),
            (["your prompts ·", "model replies"], 240, LAV),
            (["tool results"], 320, PERI_LIGHT)]
    y, h = 110, 80
    for lines, w, fill in segs:
        s.box(x, y, w, h, lines, fill=fill, stroke=PURPLE, size=19, rx=0)
        x += w
    s.text(60, 90, "One context window, in order", size=22, color=PURPLE, bold=True)
    s.bracket(60, 580, 200, "re-sent on every turn: a long AGENTS.md is paid for every call")
    s.bracket(580, 1140, 200, "the transcript: summarised when the window fills")
    s.text(1140, 290, "one cat of a log can be most of it", size=19, color=STONE,
           anchor="end", italic=True)
    # compaction
    s.box(60, 330, 260, 70, ["window full"], fill="#fff", stroke=PURPLE, size=22)
    s.arrow(320, 365, 380, 365)
    s.box(380, 330, 380, 70, ["summary of the older transcript", "lossy"],
          fill=AMBER_BG, stroke=AMBER, size=20, bold_first=True)
    s.arrow(760, 365, 820, 365)
    s.box(820, 330, 320, 70, ["continue from the summary"], fill="#fff",
          stroke=PURPLE, size=22)
    s.text(60, 450, "A rule stated in the prompt may not survive. A file read early may need re-reading.",
           size=20, color=INK)
    s.text(60, 485, "So: invariants go in the context file, big reads go to a subagent, new task means new session.",
           size=20, color=PURPLE, bold=True)
    s.write("agents-context-window.svg")


def three_modes():
    s = Svg(1200, 620)
    lanes = [(40, "Terminal", "exploration; anything you want to watch"),
             (420, "Editor", "changes you review line by line"),
             (800, "Headless: claude -p", "well specified · repeated · bounded")]
    for x, title, use in lanes:
        s.box(x, 40, 360, 540, [], fill="#fff", stroke=PERI_LIGHT, sw=1.5, rx=14)
        s.text(x + 180, 80, title, size=24, color=PURPLE, anchor="middle", bold=True)
        s.text(x + 180, 555, use, size=18, color=STONE, anchor="middle", italic=True)
    # terminal
    s.box(120, 130, 200, 60, ["human, watching"], fill=LAV, stroke=PURPLE, size=20)
    s.arrow(220, 190, 220, 250, both=True)
    s.box(120, 250, 200, 60, ["agent"], fill="#fff", stroke=PURPLE, size=22)
    s.arrow(220, 310, 220, 370, both=True)
    s.box(120, 370, 200, 60, ["repository"], fill="#fff", stroke=INK, size=22)
    s.text(220, 470, "every gated action asks first", size=18, color=STONE,
           anchor="middle", italic=True)
    # editor
    s.box(500, 130, 200, 60, ["human, in the editor"], fill=LAV, stroke=PURPLE, size=20)
    s.arrow(600, 190, 600, 250, both=True)
    s.box(500, 250, 200, 60, ["agent"], fill="#fff", stroke=PURPLE, size=22)
    s.arrow(600, 310, 600, 370)
    s.box(500, 370, 200, 60, ["diff, shown first"], fill=LAV, stroke=PERI, size=20)
    s.arrow(600, 430, 600, 480)
    s.box(500, 480, 200, 50, ["repository"], fill="#fff", stroke=INK, size=20)
    # headless
    s.box(860, 120, 240, 60, ["open GitHub issues"], fill="#fff", stroke=INK, size=20)
    s.arrow(980, 180, 980, 230)
    s.text(1000, 212, "one issue per run", size=17, color=STONE)
    s.box(860, 230, 240, 90, ["claude -p", "smallest change that",
                              "resolves the issue"], fill="#fff", stroke=PURPLE,
          size=19, bold_first=True)
    s.arrow(980, 320, 980, 370)
    s.box(860, 370, 240, 60, ["pull request"], fill="#fff", stroke=INK, size=20)
    s.path("M 1100 275 Q 1170 275 1170 330 Q 1170 380 1100 400", color=RED, dash="6 4")
    s.text(1120, 470, "looped → killed", size=19, color=RED, anchor="middle", bold=True)
    s.text(980, 510, "limits: turns · cost · wall clock", size=18, color=AMBER,
           anchor="middle", bold=True)
    s.write("agents-three-modes.svg")


def skill_flow():
    s = Svg(1200, 400)
    y = 60
    s.box(40, y, 250, 90, ["request", '"add a funding', 'acknowledgement"'],
          fill=LAV, stroke=PURPLE, size=19, bold_first=True)
    s.arrow(290, 105, 340, 105)
    s.box(340, y, 250, 90, ["harness matches the", "skill description"], fill="#fff",
          stroke=PURPLE, size=19)
    s.arrow(590, 105, 640, 105)
    s.box(640, y, 250, 90, ["loads SKILL.md body", "three instructions"], fill="#fff",
          stroke=PURPLE, size=19)
    s.arrow(890, 105, 940, 105)
    s.box(940, y, 230, 90, ["reads the wording", "from how-we-work.md"], fill="#fff",
          stroke=PURPLE, size=19)
    # second row
    s.path("M 1055 150 L 1055 200 L 765 200 L 765 230", color=PURPLE)
    s.box(640, 230, 250, 80, ["inserts it verbatim", "three award numbers"], fill="#fff",
          stroke=PURPLE, size=19)
    s.arrow(640, 270, 590, 270)
    s.box(340, 230, 250, 80, ["verify", "string match against the page"], fill=LAV,
          stroke=PURPLE, size=17, bold_first=True)
    # no-match branch
    s.path("M 465 150 L 465 200 L 165 200 L 165 230", color=AMBER, dash="6 4")
    s.box(40, 230, 250, 80, ["no match → paraphrase", "fix the description"],
          fill=AMBER_BG, stroke=AMBER, size=19)
    s.text(40, 360, "Invoked by name, the match step is skipped. Unprompted, the description is the whole test.",
           size=19, color=STONE, italic=True)
    s.write("agents-skill-flow.svg")


def subagents():
    s = Svg(1200, 560)
    s.box(450, 30, 300, 70, ["orchestrator", "its own window"], fill=LAV,
          stroke=PURPLE, size=20, bold_first=True)
    s.arrow(520, 100, 300, 160)
    s.arrow(680, 100, 900, 160)
    s.box(150, 160, 300, 90, ["subagent A", "persona: PhD student",
                              "fresh window · read-only tools"], fill="#fff",
          stroke=PURPLE, size=18, bold_first=True)
    s.box(750, 160, 300, 90, ["subagent B", "unsourced-claims check",
                              "fresh window · read-only tools"], fill="#fff",
          stroke=PURPLE, size=18, bold_first=True)
    s.box(500, 180, 200, 50, ["one book page"], fill="#fff", stroke=INK, size=19)
    s.arrow(450, 205, 500, 205, color=STONE, sw=2)
    s.arrow(750, 205, 700, 205, color=STONE, sw=2)
    s.arrow(300, 250, 520, 320)
    s.arrow(900, 250, 680, 320)
    s.text(150, 300, "only the report returns", size=17, color=STONE, italic=True)
    s.box(450, 320, 300, 70, ["merge", "each finding tagged by source"], fill="#fff",
          stroke=PURPLE, size=19, bold_first=True)
    s.text(770, 345, "injection enters here", size=18, color=AMBER, bold=True)
    s.arrow(600, 390, 600, 430)
    s.box(450, 430, 300, 60, ["permission gate: ask before create"], fill=AMBER_BG,
          stroke=AMBER, size=18)
    s.arrow(750, 460, 830, 460)
    s.box(830, 430, 170, 60, ["MCP server", "GitHub"], fill="#fff", stroke=PURPLE,
          size=18, bold_first=True)
    s.arrow(1000, 460, 1060, 460)
    s.box(1060, 430, 110, 60, ["issue"], fill="#fff", stroke=INK, size=19)
    s.text(600, 530, "Two windows do the reading; the parent only ever holds two reports.",
           size=19, color=PURPLE, anchor="middle", bold=True)
    s.write("agents-subagents.svg")


def gaia_layer():
    s = Svg(1200, 560)
    # hubs
    for x, name, sub in [(60, "DataHub", "gaia-cli · STAC · s3://cresst"),
                         (440, "ModelHub", "models · model cards"),
                         (820, "HazEvalHub", "right · cost · reproducible")]:
        s.box(x, 430, 320, 80, [name, sub], fill=LAV, stroke=PURPLE, size=20,
              bold_first=True)
    # agent layer
    s.box(30, 200, 1140, 160, [], fill="#fff", stroke=PERI, sw=2, rx=14, dash="8 5")
    s.text(50, 230, "GaiaAgent layer", size=22, color=PURPLE, bold=True)
    s.box(60, 250, 320, 90, ["Agentic data downloader", "request → staged, provenance-",
                             "tracked dataset"], fill="#fff", stroke=PURPLE, size=18,
          bold_first=True)
    s.box(440, 250, 320, 90, ["Gaia Translator", "~350-word summaries · ≤500-word",
                              "cards · refusal patterns"], fill="#fff", stroke=PURPLE,
          size=18, bold_first=True)
    s.box(820, 250, 320, 90, ["Research-software agent", "scaffold · tests · containers",
                              "FAIR-ify"], fill="#fff", stroke=PURPLE, size=18,
          bold_first=True)
    s.arrow(220, 340, 220, 430)
    s.text(240, 395, "wraps, does not replace", size=17, color=STONE, italic=True)
    s.arrow(980, 340, 980, 430)
    s.path("M 1140 470 Q 1180 470 1180 300 Q 1180 180 700 180", color=PURPLE, dash="6 4")
    s.text(700, 170, "HazEvalHub scores every agent", size=18, color=PURPLE,
           anchor="middle", bold=True)
    # top row
    s.box(60, 40, 400, 90, ["CSSI promise (derived plan)", "5 agent classes ·",
                            "gaia-template-agent counts for D1"], fill="#fff",
          stroke=INK, size=18, bold_first=True)
    s.box(740, 40, 400, 90, ["GaiaPilot on LLMaven", "TODO: not in any repo document"],
          fill=AMBER_BG, stroke=AMBER, size=18, bold_first=True, dash="6 4")
    s.arrow(260, 130, 260, 200, color=STONE, sw=2)
    s.write("agents-gaia-layer.svg")


def trajectory():
    s = Svg(1200, 420)
    s.box(40, 60, 200, 90, ["agent run"], fill=LAV, stroke=PURPLE, size=22)
    s.arrow(240, 105, 290, 105)
    s.box(290, 60, 270, 90, ["trajectory", "prompts · tool calls ·", "results · tokens"],
          fill="#fff", stroke=PURPLE, size=18, bold_first=True)
    s.arrow(560, 105, 610, 105)
    s.box(610, 60, 250, 90, ["scorecard", "right? · cost? ·", "reproducible?"],
          fill="#fff", stroke=PURPLE, size=18, bold_first=True)
    s.arrow(860, 105, 910, 105)
    s.box(910, 60, 250, 90, ["provenance record", "YAML + RO-Crate →", "Reproducibility Statement"],
          fill="#fff", stroke=PURPLE, size=18, bold_first=True)
    s.box(610, 190, 400, 70, ["capture mechanism", "TODO: four candidates, none verified"],
          fill=AMBER_BG, stroke=AMBER, size=17, bold_first=True, dash="6 4")
    s.path("M 610 225 Q 540 225 500 152", color=AMBER)
    # guardrails around the run
    s.text(40, 200, "Guardrails on the run", size=20, color=PURPLE, bold=True)
    for i, g in enumerate(["human approves anything outward-facing",
                           "no fabricated DOIs; provenance must be real",
                           "secrets never in the repository",
                           "bounded: turns · cost · wall clock",
                           "smallest change that resolves the issue"]):
        s.text(40, 235 + i * 30, "• " + g, size=18, color=INK)
    s.text(610, 310, "HazEvalHub already scores the three scorecard questions.", size=18,
           color=STONE, italic=True)
    s.text(610, 342, "The gap: the trajectory is not yet in the provenance record.", size=18,
           color=PURPLE, bold=True)
    s.write("agents-trajectory.svg")


def anatomy():
    """One specialised agent, as this repo defines it: a persona reviewer."""
    s = Svg(1200, 640)
    # left: the definition file and what it pulls in
    s.text(40, 45, "The definition: .claude/agents/gaia-review-<persona>.md", size=21,
           color=PURPLE, bold=True)
    s.box(40, 65, 400, 70, ["front matter", "name · description · tools allow-list"],
          fill=LAV, stroke=PURPLE, size=18, bold_first=True)
    s.box(40, 150, 400, 80, ["who you are  (persona SKILL.md)",
                             "checks in order · weights · vocabulary limits ·",
                             "signature question"],
          fill="#fff", stroke=PURPLE, size=17, bold_first=True)
    s.box(40, 245, 400, 80, ["how to run  (shared/method.md)",
                             "what to open · 30-minute timebox ·",
                             "read no other review"],
          fill="#fff", stroke=PURPLE, size=17, bold_first=True)
    s.box(40, 340, 400, 95, ["how to judge  (shared/rubric.md)",
                             "eight dimensions D1 to D8 · severity:",
                             "blocker / major / minor / polish ·",
                             "evidence rules · exact report format"],
          fill="#fff", stroke=PURPLE, size=17, bold_first=True)
    s.box(40, 450, 400, 70, ["hard rules", "cite the live URL · a 404 is a finding ·",
                             "say you are a simulation"],
          fill="#fff", stroke=INK, size=17, bold_first=True)
    s.text(40, 560, "References and rubric are shared files, read at run time,", size=18,
           color=STONE, italic=True)
    s.text(40, 586, "so ten personas judge against one standard.", size=18, color=STONE,
           italic=True)
    # middle: the loop
    s.box(500, 65, 240, 60, ["inputs", "live site URLs · local checkout"], fill="#fff",
          stroke=INK, size=17, bold_first=True)
    s.arrow(620, 125, 620, 165)
    for i, (lbl, sub) in enumerate([("fetch", "one page or repo"),
                                    ("check", "against the persona's list"),
                                    ("score", "D1 to D8, weighted"),
                                    ("write", "finding · severity · quote · URL")]):
        y = 165 + i * 90
        s.box(500, y, 240, 62, [lbl, sub], fill=LAV, stroke=PURPLE, size=17,
              bold_first=True)
        if i < 3:
            s.arrow(620, y + 62, 620, y + 90)
    s.path("M 740 480 Q 800 480 800 338 Q 800 196 740 196", color=PURPLE)
    s.text(620, 530, "repeat until the 30-minute timebox is spent", size=17, color=STONE,
           anchor="middle", italic=True)
    for y in (100, 190, 285, 387):
        s.path(f"M 440 {y} Q 470 {y} 500 196", color=PERI, sw=1.8)
    # right: the output
    s.box(870, 120, 300, 300, ["output: one file",
                              "review-logs/<date>/<persona>.md",
                              "",
                              "one paragraph",
                              "weighted score / 100",
                              "findings: severity · dimension",
                              "what worked · could not judge",
                              "signature question"],
          fill="#fff", stroke=PURPLE, size=17, bold_first=True)
    s.path("M 740 466 Q 830 466 870 300", color=PURPLE)
    s.arrow(1020, 420, 1020, 460)
    s.box(870, 460, 300, 56, ["synthesis merges ten of these"], fill=LAV, stroke=PERI,
          size=17)
    s.text(1020, 560, "tools: Read · Grep · Glob · Bash ·", size=15, color=STONE,
           anchor="middle")
    s.text(1020, 582, "Write · WebFetch · WebSearch", size=15, color=STONE,
           anchor="middle")
    s.write("agents-anatomy.svg")


def orchestrator_vs_specialist():
    s = Svg(1200, 660)
    s.box(400, 30, 400, 70, ["orchestrator", "goal: audit the site as ten outsiders"],
          fill=LAV, stroke=PURPLE, size=19, bold_first=True)
    names = ["PhD", "RSE", "Nat. lab", "Faculty", "Prog. off.", "Sci. adv.", "Impact",
             "Climate", "Energy", "Geo-AI"]
    xs = [55 + i * 110 for i in range(10)]
    for x, n in zip(xs, names):
        s.box(x, 190, 100, 56, [n], fill="#fff", stroke=PURPLE, size=16)
        s.arrow(600, 100, x + 50, 190, color=PERI, sw=1.5)
        s.arrow(x + 50, 246, x + 50, 300, color=STONE, sw=1.5)
        s.path(f"M {x + 50} 344 Q {x + 50} 385 600 400", color=PURPLE, sw=1.5)
    s.text(600, 165, "ten specialists, in parallel, none sees another's output", size=18,
           color=STONE, anchor="middle", italic=True)
    s.box(55, 300, 1090, 44, ["one shared rubric and method: D1 to D8 · severity · evidence rules · report format"],
          fill=LAV, stroke=PERI, size=17, rx=6)
    s.box(400, 400, 400, 96, ["synthesis", "convergent (3+ personas) · divergent, kept divergent ·",
                              "blocker table · cheap wins · pages nobody visited",
                              "scores as a table, never an average"],
          fill="#fff", stroke=PURPLE, size=15, bold_first=True)
    # contrast panel
    y0 = 540
    s.text(60, y0, "Orchestrator", size=20, color=PURPLE, bold=True)
    s.text(640, y0, "Specialist", size=20, color=PURPLE, bold=True)
    rows = [("broad goal; decides what to dispatch", "narrow role, fixed weights, own vocabulary"),
            ("holds only the ten reports", "holds the whole site, for 30 minutes"),
            ("dispatch · merge · gate outward actions", "fetch · read · write one file")]
    for i, (a, b) in enumerate(rows):
        s.text(60, y0 + 32 + i * 28, "• " + a, size=17, color=INK)
        s.text(640, y0 + 32 + i * 28, "• " + b, size=17, color=INK)
    s.write("agents-orchestrator-vs-specialist.svg")


def evaluation():
    """How GAIA scores an agent: HazEvalHub / FrugalMind and the gaia-eval harness
    (book/chapters/hazevalhub.md, project_coordination/03-ai-tools-and-evals.md)."""
    s = Svg(1200, 640)
    # task with hidden test split
    s.box(40, 60, 250, 110, ["task", "public train / validation",
                             "hidden test split"], fill="#fff", stroke=INK, size=18,
          bold_first=True)
    s.arrow(290, 115, 340, 115)
    # the four conditions under test
    s.box(340, 40, 300, 150, [], fill=LAV, stroke=PERI, rx=10)
    s.text(490, 68, "agent under test", size=18, color=PURPLE, anchor="middle", bold=True)
    s.box(360, 82, 120, 44, ["local 7B"], fill="#fff", stroke=PURPLE, size=16)
    s.box(500, 82, 120, 44, ["cloud model"], fill="#fff", stroke=PURPLE, size=16)
    s.box(360, 136, 120, 44, ["no skills"], fill="#fff", stroke=STONE, size=16, dash="5 3")
    s.box(500, 136, 120, 44, ["with skills"], fill="#fff", stroke=PURPLE, size=16)
    s.arrow(640, 115, 690, 115)
    # harness
    s.box(690, 40, 260, 150, ["gaia-eval harness", "predict(inputs) → outputs",
                              "runs in its container",
                              "declarative JSON scoring spec"],
          fill="#fff", stroke=PURPLE, size=16, bold_first=True)
    s.arrow(950, 115, 1000, 115)
    s.box(1000, 40, 170, 150, ["scorecard", "right?", "cost?", "reproducible?",
                               "+ provenance"], fill=LAV, stroke=PURPLE, size=16,
          bold_first=True)
    # downstream uses
    s.arrow(1085, 190, 1085, 250)
    s.box(880, 250, 290, 90, ["the board", "cost vs performance;",
                              "hollow = no skills, filled = with;",
                              "the line is the skill lift"],
          fill="#fff", stroke=PURPLE, size=15, bold_first=True)
    s.arrow(1085, 340, 1085, 400)
    s.box(880, 400, 290, 70, ["Metrics Observatory", "M1 · M2 · M4"], fill="#fff",
          stroke=INK, size=16, bold_first=True)
    s.path("M 1000 190 Q 760 230 760 250", color=PURPLE)
    s.box(600, 250, 240, 90, ["CI regression gate", "a PR that lowers",
                              "skill fails"], fill="#fff", stroke=PURPLE, size=16,
          bold_first=True)
    # second track: expert rubric
    s.box(40, 250, 480, 90, ["expert track  (Gaia Translator)",
                             "8-criterion rubric · 15 to 25 domain reviewers ·",
                             "inter-rater reliability"],
          fill="#fff", stroke=PURPLE, size=16, bold_first=True)
    s.text(40, 375, "Automated metrics say how a model behaves on held-out data;",
           size=17, color=STONE, italic=True)
    s.text(40, 400, "expert scoring says whether it is useful to a researcher.",
           size=17, color=STONE, italic=True)
    # result and phasing
    s.box(40, 440, 480, 70, ["early result", "local 7B + skills = cloud on configuration tasks;",
                             "not on numerical code generation"],
          fill=LAV, stroke=PERI, size=15, bold_first=True)
    s.text(40, 560, "v0 live: FrugalMind, agent tasks  →  v0.5 (Y1): first hazard task on the same board",
           size=17, color=INK)
    s.text(40, 590, "→  v1 (Y2): containerised submissions, auto-scoring  →  v2 (Y3): pillar × hazard grid",
           size=17, color=INK)
    s.text(1170, 530, "process, not only outcome: the research-workflow track scores trajectories",
           size=16, color=PURPLE, bold=True, anchor="end")
    s.write("agents-evaluation.svg")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    stack()
    context_window()
    three_modes()
    skill_flow()
    subagents()
    gaia_layer()
    trajectory()
    anatomy()
    orchestrator_vs_specialist()
    evaluation()
