#! /usr/bin/env python

import re
from wordcloud import WordCloud

file_in = "../text/ondersteunende_documenten/maatschappelijke_kosten_wordcloud.txt"
file_out = "../text/ondersteunende_documenten/figuren/maatschappelijke_kosten_wordcloud.svg"
font_file = "/usr/share/texlive/texmf-dist/fonts/opentype/public/lm/lmroman17-regular.otf"

freq = {}
for line in open(file_in):
    line = line.strip()
    weight = re.match("\d+", line)
    if weight is None:
        weight_inc = 1
    else:
        weight_inc = int(weight.group(0))
        line = line[weight.end():].strip()
    if line in freq:
        freq[line] = freq[line]+weight_inc
    else:
        freq[line] = weight_inc

mask=None
wc = WordCloud(max_words=1000, mask=mask, margin=10, random_state=1,
        min_font_size = 14, font_path = font_file, width = 800, height = 600,
        background_color = "white", colormap = "hsv",
        regexp = "[:space:]{2,}"

        ).generate_from_frequencies(freq)

svg_text = wc.to_svg(embed_image=False)

svg = open(file_out, "w")
svg.write(svg_text)
svg.close()
