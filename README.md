# Bloom &amp; Rise

Homepage concept for **Roshunda M. Hartison, MEd, LPC** — online therapy for Texas, Virginia, and Colorado.

`index.html` is a single self-contained file. All CSS, JavaScript, fonts config, and imagery are inlined, so it opens with no build step and no server.

## Preview

Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## Structure

```
index.html        the site, fully self-contained
build.py          regenerates index.html from source/
source/           watercolour plates and the portrait composite
```

## Rebuilding

`build.py` embeds the images in `source/` as base64 and writes `index.html`.

```
python3 build.py
```

Source art is cropped inside the illustrations' own drawn rules so no frame lines
carry into the layout. The portrait composite places the cutout against foliage
sampled from the hero plate.

## Design notes

- Palette drawn from the artwork: monarch orange, leaf green, coneflower pink, morning yellow, on warm paper
- Type: Fraunces (SOFT + WONK axes) for display, Inter Tight for text
- Page background warms as the visitor scrolls, night toward morning
- Reduced-motion respected throughout

## Scope and compliance

Therapy is limited to clients physically located in Texas, Virginia, or Colorado.
Workshops are educational and open to any state. Crisis routing, HIPAA notice, and
scope-of-practice language are in the footer and beside the contact form.

Forms are not wired to a backend in this concept.

## Status

Concept for client review. Copy is drawn from Roshunda's own published profiles and
is pending her sign-off.
