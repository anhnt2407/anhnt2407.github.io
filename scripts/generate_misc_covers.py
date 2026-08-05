#!/usr/bin/env python3
"""Render the Misc cover illustrations with Qwen-Image.

The covers on the Misc and News pages share one recipe: a real environment
photographed at night or blue hour, with a luminous holographic layer drawn
into that same space. The base carries the physical setting; the overlay
carries whatever the entry is actually about. Colour follows the page
convention - cyan and blue for normal flow, green for healthy, amber for
caution, red only for a violated constraint.

Usage:
    python scripts/generate_misc_covers.py --dry-run
    python scripts/generate_misc_covers.py                     # all missing
    python scripts/generate_misc_covers.py --only 038 042      # a subset
    python scripts/generate_misc_covers.py --only 038 --force  # redo one

Weights are ~58 GB and come from Qwen/Qwen-Image (Apache 2.0, no gating).
The model is larger than a single card, so components are streamed on and off
the GPU; expect roughly a minute per image on a 48 GB card.
"""

import argparse
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW_DIR = REPO / "images" / "misc" / "_raw"
OUT_DIR = REPO / "images" / "misc"

MODEL = "Qwen/Qwen-Image"
WIDTH, HEIGHT = 1664, 928          # the model's native 16:9 bucket
FINAL_W, FINAL_H = 1200, 675       # what the page ships
STEPS = 50
TRUE_CFG = 4.0

# Applied to every prompt. Keeps the 23 covers reading as one set.
STYLE = (
    "Cinematic 3D render with photographic realism, wide establishing shot, "
    "night or blue-hour dusk. A real physical environment lit by warm practical "
    "lights, with a large luminous holographic data layer projected into that "
    "same space. Volumetric light, atmospheric haze, deep shadows, shallow depth "
    "of field. The holographic layer is cool cyan and blue; the practical lighting "
    "is warm amber. Small human silhouettes for scale, seen from behind. "
    "Ultra HD, 4K, cinematic composition."
)

# Image models render lettering as garbage, and a misdrawn map or flag is worse
# than none. Both are pushed out here rather than asked for in the positive.
NEGATIVE = (
    "text, letters, words, writing, captions, numbers, digits, labels, "
    "watermark, signature, logo, brand, map, flag, national emblem, "
    "close-up face, portrait, deformed, extra limbs, blurry, low quality, "
    "jpeg artifacts, oversaturated, garish, flat vector art, clip art, cartoon, "
    "fire, flame, burning, smoke"
)

# Some scenes have a specific failure mode worth naming. Appended to NEGATIVE
# for that slug only, so a ban needed by one cover cannot break another.
EXTRA_NEGATIVE = {
    # "layered planes" reads as aircraft here; the hangar still needs its UAV,
    # so only the holographic layer is constrained.
    "058-assurance-standards": "flying aircraft, jet fighter, airliner, wings in the sky",
}

# slug -> the scene. Ordered to match the entry numbers in _data/misc_posts.yml.
SCENES = {
    "038-sjr-quartiles": (
        "A vast library reading room at night, oak desks and green banker's lamps, "
        "tall shelves receding into darkness. Standing in the central aisle, four "
        "colossal holographic glass columns of descending height, the tallest glowing "
        "bright cyan and the shortest fading to dim amber, fine light threads linking "
        "each column to a floating stack of journal volumes above it."
    ),
    "039-jcr-master-list": (
        "A grand periodicals hall at night, brass railings, a vaulted ceiling in shadow. "
        "A luminous circular index gate hovers above the floor, rings of cyan light "
        "rotating within rings. A narrow beam passes bound journals through the gate one "
        "at a time; those that do not pass drift away sideways into darkness."
    ),
    "040-citescore-window": (
        "A long archive gallery at dusk, tall arched windows, dust suspended in the air. "
        "A luminous horizontal ribbon of cyan citation light runs the whole length of the "
        "gallery. A bright rectangular frame slides along the ribbon like a moving window, "
        "holding four glowing segments inside it while older segments dim behind."
    ),
    "041-scholar-h5": (
        "A darkened lecture auditorium, empty tiered seating, one stage light. Rising from "
        "the stage floor, a holographic forest of glowing vertical bars of unequal height, "
        "half of them shaped like thick bound volumes and half like conference lanyard "
        "badges, all standing on the same luminous baseline."
    ),
    "042-ccf-tiers": (
        "A stone amphitheatre at night, empty terraced seating. Three concentric holographic "
        "platforms float above the tiers at three clearly separated heights, the highest "
        "brilliant cyan, the middle deep blue, the lowest dim teal, thin light columns "
        "connecting each platform down to the seating below."
    ),
    "043-acceptance-rates": (
        "The entrance hall of a huge convention centre at night, a dense crowd of silhouetted "
        "people waiting in the dark. A narrow luminous cyan gateway stands at the far end; "
        "only a thin stream of glowing motes passes through it while the rest disperse into "
        "shadow. A luminous arc above the gate shows one narrow filled sector."
    ),
    "044-deadline-trackers": (
        "A dim operations room at night, banks of dark monitors, one wall of glass looking "
        "onto a city. Suspended in the room, a ring of large holographic countdown dials at "
        "different phases, most calm cyan, one glowing amber and nearly closed, thin light "
        "threads tying each dial to a small floating document."
    ),
    "045-dblp": (
        "Deep library stacks at night, narrow aisles, a single lamp far down the corridor. A "
        "luminous web of fine cyan threads runs along the shelves; each thread leaves a book "
        "and converges on one bright node hovering in the aisle, with thousands of tiny "
        "glowing record cards streaming along the threads."
    ),
    "046-openalex": (
        "A vast open atrium at night under a glass roof, tall doors standing open on every "
        "side. A colossal luminous constellation of interlinked cyan points fills the volume "
        "and drifts freely outward through the open doorways instead of being contained, "
        "brighter where clusters form."
    ),
    "047-leiden-ranking": (
        "A university quadrangle at blue hour, stone cloisters, warm lit windows. Five "
        "separate holographic gauges of different kinds float above the lawn - a curve, a "
        "ring, a cluster of bars, a scatter of points, a small network - each self-contained "
        "and equally bright, deliberately never merging into a single figure."
    ),
    "048-nature-index": (
        "A research campus seen from the air at night, laboratory blocks with lit windows and "
        "wet roadways. Luminous cyan spheres of varying size hover above individual buildings, "
        "each sphere cut into glowing wedges, thin filaments running between buildings wherever "
        "a wedge is shared."
    ),
    "049-qs-the-arwu": (
        "Three distinct university towers at night, each a different architecture, standing far "
        "apart across a dark plaza. Above each tower a holographic column of different height "
        "and different colour, one cyan, one deep blue, one warm amber, visibly disagreeing, "
        "with faint light lines failing to reconcile them."
    ),
    "050-scimago-institutions": (
        "A night skyline where a university dome, a hospital block, a corporate research tower "
        "and a government building stand side by side. One enormous luminous ring arcs over all "
        "four, divided into three unequal glowing segments, dropping light columns evenly onto "
        "every building."
    ),
    "051-ai-index": (
        "A dim data-centre corridor at night, server racks receding into the distance, cool blue "
        "indicator lights. A tall holographic wall panel rises through the corridor carrying a "
        "steeply climbing luminous cyan curve, with smaller panels branching off it, one tinted "
        "amber and lagging well behind the main curve."
    ),
    "052-arena-leaderboard": (
        "A darkened arena at night, empty tiered seating, a single circle of floor light. Two "
        "identical featureless luminous figures face each other in the ring behind a curtain of "
        "light that hides which is which, while above them a holographic ladder of ranked glowing "
        "rungs shifts, the top rungs almost touching."
    ),
    "053-benchmarks-after-pwc": (
        "A large archive hall at night after closure, empty shelving units, dust sheets over "
        "furniture. A collapsed holographic leaderboard lies broken across the floor in fading "
        "cyan fragments, while a few small bright nodes hover nearby, beginning to rebuild a much "
        "smaller structure out of the pieces."
    ),
    "054-dora-manifesto": (
        "An empty council chamber at night, curved wooden benches, one overhead light. At the "
        "centre a colossal luminous balance scale: on one pan a single hard bright glowing solid, "
        "on the other a broad softly glowing sheaf of documents, the document side hanging "
        "visibly lower."
    ),
    "055-think-check-submit": (
        "A stone gatehouse at night, an arched passage, one hanging lantern. A luminous checkpoint "
        "of concentric cyan rings fills the arch. One verified document has passed through and "
        "glows steady green on the far side, while a second document is held flat against the "
        "outer ring, greyed out and refused entry. A softly glowing directory panel stands open on "
        "a plinth beside the gate."
    ),
    "056-retraction-watch": (
        "A tall archive hall at night, ladders leaning against shelves. Several volumes are drawn "
        "out of the shelves by beams of light and banded in clear red, while cyan threads trace "
        "outward from each marked volume to dozens of other books that cite it, those threads "
        "visibly dimming."
    ),
    "057-vietnam-journal-list": (
        "A colonial-era institutional building at night in a tropical city, tall shutters, warm "
        "lanterns, wet pavement reflecting the light, broad-leaved trees. A large luminous document "
        "panel hovers above the entrance steps with a glowing gold seal impressed at its foot, cyan "
        "light threads running from the panel out to rows of floating periodicals."
    ),
    "058-assurance-standards": (
        "An aircraft hangar at night, a small quadcopter drone parked on the polished floor, work "
        "lights on stands. Directly above the drone, four flat horizontal holographic sheets are "
        "stacked one over another like the floors of a building, each sheet a dense grid of small "
        "interlocking verification cells in cyan and blue, the grid growing denser toward the "
        "lowest sheet, with one empty amber-outlined gap left unfilled in an upper sheet."
    ),
    "059-orcid-ror-doi": (
        "A registry hall at night, a long counter, brass fittings, one lamp. A single luminous human "
        "silhouette stands at the centre; fine cyan threads run outward from it and bind to floating "
        "documents, building outlines and small glowing tokens, several threads knotting into one "
        "bright persistent core."
    ),
    "060-arxiv-openreview": (
        "A quiet reading room at night, one occupied desk, a green lamp, rain on the window. A "
        "luminous stream of documents flows in through a high window; above the desk a second "
        "transparent holographic layer overlays that stream, filled with glowing annotation marks "
        "and branching comment threads in cyan, a few of them amber."
    ),
    "061-internet-of-cognition": (
        "A vast operations hall at night, a dark tiered floor, a few warm work lamps on stands. "
        "Dozens of small separate luminous figures stand far apart across the floor, each sealed "
        "inside its own small closed halo of cyan light. One enormous translucent dome of light "
        "spans the whole hall above them; fine threads rise from every figure into the dome and "
        "braid there into a single bright shared core, while a few threads near the edge fall "
        "short and hang unconnected, glowing amber."
    ),
}


def build_prompt(scene: str) -> str:
    return f"{scene} {STYLE}"


def seed_for(slug: str) -> int:
    """Stable per-slug seed so a rerun reproduces the same cover."""
    return int(slug.split("-")[0]) * 7919 + 20260804


def to_webp(raw_path: Path, out_path: Path) -> None:
    from PIL import Image

    im = Image.open(raw_path).convert("RGB")
    # The model's 16:9 bucket is 1664x928 (1.793); the page wants exactly 1.778.
    # Trim the sides rather than squash the render.
    target = FINAL_W / FINAL_H
    w, h = im.size
    if w / h > target:
        new_w = round(h * target)
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    else:
        new_h = round(w / target)
        top = (h - new_h) // 2
        im = im.crop((0, top, w, top + new_h))
    im = im.resize((FINAL_W, FINAL_H), Image.LANCZOS)
    im.save(out_path, "WEBP", quality=88, method=6)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="entry numbers, e.g. 038 042")
    ap.add_argument("--force", action="store_true", help="redo covers that exist")
    ap.add_argument("--dry-run", action="store_true", help="print prompts, render nothing")
    ap.add_argument("--steps", type=int, default=STEPS)
    args = ap.parse_args()

    slugs = list(SCENES)
    if args.only:
        wanted = {s.lstrip("#").zfill(3) for s in args.only}
        slugs = [s for s in slugs if s.split("-")[0] in wanted]
        if not slugs:
            print(f"no slugs matched {sorted(wanted)}", file=sys.stderr)
            return 1
    if not args.force:
        slugs = [s for s in slugs if not (OUT_DIR / f"{s}.webp").exists()]

    if args.dry_run:
        for s in slugs:
            print(f"\n=== {s}  (seed {seed_for(s)}) ===\n{build_prompt(SCENES[s])}")
        print(f"\n{len(slugs)} cover(s) would be rendered")
        return 0

    if not slugs:
        print("nothing to do; all covers exist (use --force to redo)")
        return 0

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    import torch
    from diffusers import DiffusionPipeline

    print(f"loading {MODEL} ...", flush=True)
    pipe = DiffusionPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16)

    # The 20B transformer plus a 7B text encoder needs roughly 60 GB resident.
    # Keep everything on the card when it fits, and stream components on and
    # off only when it does not.
    free, _total = torch.cuda.mem_get_info()
    if free / 1e9 >= 68:
        print(f"  {free/1e9:.0f} GB free - keeping pipeline resident", flush=True)
        pipe.to("cuda")
    else:
        print(f"  {free/1e9:.0f} GB free - using model cpu offload", flush=True)
        pipe.enable_model_cpu_offload()

    for i, slug in enumerate(slugs, 1):
        raw = RAW_DIR / f"{slug}.png"
        out = OUT_DIR / f"{slug}.webp"
        print(f"[{i}/{len(slugs)}] {slug}", flush=True)
        image = pipe(
            prompt=build_prompt(SCENES[slug]),
            negative_prompt=", ".join(filter(None, [NEGATIVE, EXTRA_NEGATIVE.get(slug)])),
            width=WIDTH,
            height=HEIGHT,
            num_inference_steps=args.steps,
            true_cfg_scale=TRUE_CFG,
            generator=torch.Generator(device="cuda").manual_seed(seed_for(slug)),
        ).images[0]
        image.save(raw)
        to_webp(raw, out)
        print(f"        -> {out.relative_to(REPO)}", flush=True)

    print(f"\ndone: {len(slugs)} cover(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
