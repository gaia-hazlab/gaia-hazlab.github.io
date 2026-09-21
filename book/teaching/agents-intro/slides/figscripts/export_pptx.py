"""Render the agents-intro deck to PowerPoint from the same .qmd source.

Usage, from the repository root:

    python book/teaching/agents-intro/slides/figscripts/export_pptx.py OUTDIR

Needs `quarto` and `rsvg-convert` on the path (the latter via
`pixi exec -s librsvg rsvg-convert` if it is not installed). Writes
OUTDIR/agents-intro.pptx. The reveal.js-only styling (takeaway bars, amber TODO
boxes, minute tags) has no PowerPoint equivalent, so takeaways become image
captions or bold lines, TODO blocks get a visible "TODO:" prefix, and a paragraph
after a table moves into the speaker notes, because pandoc puts tables and
pictures on slides of their own.
"""
import pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
SLIDES = ROOT / "book/teaching/agents-intro/slides"
OUT = pathlib.Path(sys.argv[1]).resolve()
(OUT / "png").mkdir(parents=True, exist_ok=True)

rsvg = shutil.which("rsvg-convert")
cmd = [rsvg] if rsvg else ["pixi", "exec", "-s", "librsvg", "rsvg-convert"]
for svg in sorted((ROOT / "book/img").glob("agent*.svg")):
    png = OUT / "png" / (svg.stem + ".png")
    if not png.exists() or png.stat().st_mtime < svg.stat().st_mtime:
        subprocess.run(cmd + ["-w", "2400", "--background-color", "white", str(svg), "-o", str(png)],
                       check=True, cwd=ROOT)

src = (SLIDES / "agents-intro.qmd").read_text()
refs = (SLIDES / "refs/agents-intro_refs.qmd").read_text()

s = re.sub(r"!\[\]\(\.\./\.\./\.\./img/([a-z0-9-]+)\.svg\)(\{\.r-stretch\})?", r"![](png/\1.png)", src)
s = re.sub(r' \{background-color="#f5f3fb"\}', "", s)
s = s.replace('## {background-color="#f5f3fb"}', "## Today's question")
s = s.replace(" {.smaller}", "").replace(' {visibility="uncounted"}', "")
s = s.replace("```{.text .bigcode}", "```")
s = s.replace("[🤖]{.lecture-icon}\n\n### Today's question\n\n", "")
s = re.sub(r"::: \{\.todo\}\n(.*?)\n:::", lambda m: "TODO_PARA:: " + m.group(1).strip(), s, flags=re.S)
s = re.sub(r"::: \{\.takeaway\}\n(.*?)\n:::", lambda m: "TAKE_PARA:: " + m.group(1).strip(), s, flags=re.S)
s = re.sub(r"::: \{\.dim\}\n(.*?)\n:::", lambda m: "DIM_PARA:: " + m.group(1).strip(), s, flags=re.S)
s = re.sub(r"::: \{\.big-number\}\n(.*?) \[(.*?)\]\{\.unit\}\n:::", r"**\1** \2", s, flags=re.S)

# an image followed by a takeaway or dim paragraph: fold the paragraph into the caption
s = re.sub(r"!\[\]\((png/[a-z0-9-]+\.png)\)\n\n(?:TAKE_PARA|DIM_PARA):: (.*?)(?=\n\n)",
           lambda m: f"![{m.group(2).replace(chr(10), ' ')}]({m.group(1)})", s, flags=re.S)

# a table followed by a dim/takeaway/todo paragraph: move the paragraph into the notes
def table_fix(block):
    if "\n|" not in block:
        return block
    extras = re.findall(r"\n\n(?:TAKE_PARA|DIM_PARA|TODO_PARA):: (.*?)(?=\n\n|\Z)", block, flags=re.S)
    block = re.sub(r"\n\n(?:TAKE_PARA|DIM_PARA|TODO_PARA):: .*?(?=\n\n|\Z)", "", block, flags=re.S)
    if extras:
        extra = " ".join(e.replace("\n", " ") for e in extras)
        if "::: {.notes}" in block:
            block = block.replace("::: {.notes}\n", "::: {.notes}\nOn the slide in the HTML deck: " + extra + "\n\n", 1)
        else:
            block += "\n\n::: {.notes}\n" + extra + "\n:::\n"
    return block
parts = re.split(r"(?m)^(?=## )", s)
s = "".join(table_fix(p) for p in parts)

def para(marker, wrap):
    global s
    s = re.sub(marker + r":: (.*?)(?=\n\n|\Z)",
               lambda m: wrap(m.group(1).replace("\n", " ").strip()), s, flags=re.S)
para("TODO_PARA", lambda t: "**TODO:** " + t)
para("TAKE_PARA", lambda t: "**" + t + "**")
para("DIM_PARA", lambda t: "*" + t + "*")

r = refs
r = re.sub(r"\[(.*?)\]\{\.ref-verdict[^}]*\}", r"\1", r)
r = re.sub(r"\[(.*?)\]\{\.ref-msg\}", r"**\1**", r)
r = re.sub(r"\[(.*?)\]\{\.ref-cite\}", r"\1", r)
r = re.sub(r":::: \{\.ref-item\}\n(.*?)\n::::", lambda m: "- " + m.group(1).strip().replace("\n\n", " "), r, flags=re.S)
r = re.sub(r"<!--.*?-->\n", "", r, flags=re.S)
s = s.replace("{{< include refs/agents-intro_refs.qmd >}}", r.strip())

s = re.sub(r"^---\n.*?\n---\n", """---
title: "An introduction to AI agents for the GAIA team"
subtitle: "GAIA CSSI team · date TODO"
format:
  pptx:
    slide-level: 2
---
""", s, count=1, flags=re.S)
(OUT / "agents-intro.qmd").write_text(s)
subprocess.run(["quarto", "render", "agents-intro.qmd", "--to", "pptx"], check=True, cwd=OUT)
print("wrote", OUT / "agents-intro.pptx")
