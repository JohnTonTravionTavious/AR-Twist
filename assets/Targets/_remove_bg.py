"""
One-shot script: remove the cream background from Nara.png and save as
a transparent PNG for overlay use.

Two-pass approach to kill edge fringes:
  1. Flood-fill from 4 corners with threshold 50 (more aggressive than
     the 35 first try, which left a halo of near-cream fringe pixels).
     Threshold 50 is still safely below the distance to skin (~54) so
     the figure stays intact.
  2. Erode the alpha mask by 1 pixel (MinFilter size 3) to clean up any
     remaining 1-pixel-wide fringe along the figure boundary.

The original JPEG (with the cream background) stays as the 8th Wall image
target — its uniform background is fine for tracking; only the overlay
needs transparency.
"""
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path

src = Path(r"C:\Users\lenot\Downloads\Nara.png")
dst = Path(r"C:\Users\lenot\Documents\AR-Twist\assets\Targets\nara_knife_behind_back_transparent.png")

img = Image.open(src).convert("RGBA")
w, h = img.size

seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
for seed in seeds:
    ImageDraw.floodfill(img, seed, (255, 255, 255, 0), thresh=50)

# Erode the alpha channel by 1 pixel to shave the remaining fringe.
r, g, b, a = img.split()
a = a.filter(ImageFilter.MinFilter(3))
img.putalpha(a)

img.save(dst, "PNG", optimize=True)

# Report
size_kb = dst.stat().st_size / 1024
print(f"Saved: {dst}")
print(f"Dimensions: {w}x{h}")
print(f"Size: {size_kb:.1f} KB")

# Sanity check: count transparent pixels
import struct
data = list(img.getdata())
transparent_count = sum(1 for p in data if p[3] == 0)
opaque_count = sum(1 for p in data if p[3] == 255)
partial_count = len(data) - transparent_count - opaque_count
print(f"Transparent pixels: {transparent_count} ({100*transparent_count/len(data):.1f}%)")
print(f"Opaque pixels: {opaque_count} ({100*opaque_count/len(data):.1f}%)")
print(f"Partial alpha pixels: {partial_count} ({100*partial_count/len(data):.1f}%)")
