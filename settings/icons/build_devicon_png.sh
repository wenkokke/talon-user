#!/bin/bash
for svg in $(find devicon/icons -name '*.svg'); do
  png="${svg%.svg}.png"
  echo "Convert $(basename -- $svg) -> $(basename -- $png)"
  inkscape \
    --export-width=30 \
    --export-height=30 \
    --export-background-opacity=0.0 \
    --export-filename="$png" \
    "$svg"
  png_bw="${png%.png}-bw.png"
  echo "Desaturate $(basename -- $png) -> $(basename -- $png_bw)"
  convert "$png" -grayscale rec709luma "$png_bw"
done
