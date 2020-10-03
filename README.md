## Overview
This is a simple project for generating a static webpage that displays Diablo II rune-words.

Generation occurs in 2 phases: 
- Parse HTML from Arreat Summit to extract rune and export JSON
- Render static HTML page from JSON exported above

## Parsing
The `parse.py` script parses normalized HTML from Arreat Summit rune-word pages.

The following normalization pre-processing steps are required:
- Extract rune-word table from broader HTML document
- Properly format XML attributes by including surrounding quotes (`=([^" >]+)([ >])` -> `="$1"$2`)
- Remove `<BR>` elements

The parse script looks for the following files:
- `raw/original.xml`
- `raw/110.xml`
- `raw/110_ladder.xml`
- `raw/111.xml`

Note that the exported file is included in this repo as `runewords.json`.

## Rendering
The `render.py` script renders the JSON exported from the parse step using a Jinga2 template.

The rendered HTML follows the styling from Arreat Summit.

It includes a few helpful additions:
- Combined table of all rune-words
- Column for denoting the maximum rune level
- Sorted by rune level noted above 