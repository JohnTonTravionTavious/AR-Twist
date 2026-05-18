"""
One-shot script: flood-fill the cream background of Nara.png from the
four corners and save the result as a transparent PNG for overlay use.

The original JPEG (with the cream background) stays as the 8th Wall image
target — its uniform background is fine for tracking; only the overlay
needs transparency.
"""
from PIL import Image, ImageDraw
from pathlib import Path

src = Path(r"C:\Users\lenot\Downloads\Nara.png")
dst = Path(r"C:\Users\lenot\Documents\AR-Twist\assets\Targets\nara_knife_behind_back_transparent.png")

img = Image.open(src).convert("RGBA")
w, h = img.size

# Flood-fill from each corner with a moderate color threshold.
# Tolerance 35 picks up the slight variation in the cream background
# (from ~(243,238,219) at corners to subtle gradient) without eating the
# figure (skin is ~(242,210,169) — well outside tolerance from cream).
seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
for seed in seeds:
    ImageDraw.floodfill(img, seed, (255, 255, 255, 0), thresh=35)

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
