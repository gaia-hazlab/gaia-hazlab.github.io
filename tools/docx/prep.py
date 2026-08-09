#!/usr/bin/env python3
"""Prepare a Markdown file for pandoc -> docx.

Three fixes:
  1. Lift the leading '# Title' out as metadata so pandoc uses the Title style
     instead of rendering it twice (once as metadata, once as Heading 1).
  2. Give pipe tables proportional column widths. Pandoc derives docx column
     widths from the number of dashes in the delimiter row, so a uniform
     '|---|---|' source yields equal narrow columns and badly wrapped text.
  3. Drop standalone '---' rules; headings already separate sections and the
     Word rendering is a heavy black bar.
"""
import re, sys, pathlib

def cells(line):
    s = line.strip()
    if s.startswith('|'): s = s[1:]
    if s.endswith('|'):   s = s[:-1]
    return [c.strip() for c in s.split('|')]

def is_delim(line):
    return bool(re.fullmatch(r'\|?[\s:|-]+\|?', line.strip())) and '-' in line

MARKUP = re.compile(r'\*\*|`|\[([^\]]*)\]\([^)]*\)')

def plain(t):
    return MARKUP.sub(lambda m: m.group(1) or '', t)

def fix_table(block, total=110):
    rows = [cells(l) for l in block]
    delim = rows[1]
    ncol = len(delim)
    longest, word = [0]*ncol, [0]*ncol
    for i, r in enumerate(rows):
        if i == 1: continue
        for c in range(min(ncol, len(r))):
            t = plain(r[c])
            longest[c] = max(longest[c], len(t))
            for w in t.split():
                word[c] = max(word[c], len(w))
    # Compress the dynamic range: raw proportional widths let one long
    # column starve the rest, which is what wrapped "Quarterly, PI
    # coordination" onto three lines.
    comp = [max(l, 5) ** 0.62 for l in longest]
    scale = total / sum(comp)
    widths = [int(round(c*scale)) for c in comp]
    # never narrower than the longest unbreakable word, or 6 chars
    widths = [max(widths[c], word[c] + 2, 6) for c in range(ncol)]

    new_delim = []
    for c in range(ncol):
        d = delim[c]
        left  = d.startswith(':')
        right = d.endswith(':')
        n = widths[c] - (1 if left else 0) - (1 if right else 0)
        new_delim.append((':' if left else '') + '-'*max(3, n) + (':' if right else ''))
    block[1] = '| ' + ' | '.join(new_delim) + ' |'
    return block

def main(src, out):
    lines = pathlib.Path(src).read_text().splitlines()
    title = None
    result, i = [], 0

    # 1. leading H1 -> title
    while i < len(lines):
        if lines[i].startswith('# ') and title is None:
            title = lines[i][2:].strip(); i += 1
            while i < len(lines) and not lines[i].strip(): i += 1
            break
        if lines[i].strip():
            break
        i += 1

    while i < len(lines):
        line = lines[i]
        # 2. tables
        if line.lstrip().startswith('|') and i+1 < len(lines) and is_delim(lines[i+1]):
            block = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                block.append(lines[i]); i += 1
            result += fix_table(block)
            continue
        # 3. horizontal rules
        if re.fullmatch(r'-{3,}', line.strip()):
            i += 1; continue
        result.append(line); i += 1

    # Emit the title as YAML front matter rather than passing it back through
    # the shell — command substitution mangles em-dashes into replacement chars.
    head = ''
    if title:
        esc = title.replace('\\', '\\\\').replace('"', '\\"')
        head = '---\ntitle: "%s"\n---\n\n' % esc
    pathlib.Path(out).write_text(head + '\n'.join(result) + '\n', encoding='utf-8')
    print('ok')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
