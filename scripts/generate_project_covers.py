#!/usr/bin/env python3
"""Render the Projects page cover illustrations with Qwen-Image.

These follow the News page recipe rather than the Misc one. News covers are
bright and high-key: a clean daylight environment in smooth product-render 3D,
with a translucent cyan holographic layer drawn into that same space. The base
carries the physical setting - a hangar, a test track, a cleanroom - and the
overlay carries the method the programme actually contributed. Colour is
semantic and follows the page convention: cyan and blue for normal flow, green
for healthy or verified, amber for caution, red dashed only for a hard
constraint or a failed component.

Usage:
    python scripts/generate_project_covers.py --dry-run
    python scripts/generate_project_covers.py                        # all missing
    python scripts/generate_project_covers.py --only dyno-humanoid   # a subset
    python scripts/generate_project_covers.py --only naval --force   # redo one

Weights are ~58 GB and come from Qwen/Qwen-Image (Apache 2.0, no gating). The
model is larger than a single card, so components are streamed on and off the
GPU when there is not enough headroom to keep it resident.
"""

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW_DIR = REPO / "images" / "projects" / "_raw"
OUT_DIR = REPO / "images" / "projects"

MODEL = "Qwen/Qwen-Image"
WIDTH, HEIGHT = 1664, 928
FINAL_W, FINAL_H = 1200, 675
STEPS = 50
TRUE_CFG = 4.0

STYLE = (
    "Clean high-key 3D product render with photographic realism, wide "
    "establishing shot, bright daylight, soft even lighting from large windows. "
    "Smooth white and light-grey surfaces, polished pale floor, airy pale "
    "blue-grey palette, generous empty space. A translucent luminous holographic "
    "layer is projected into that same space in cyan and teal, with soft frosted "
    "rounded-rectangle panels floating in the scene. Soft shadows, gentle depth "
    "of field, low contrast, no gloom. Ultra HD, 4K, cinematic composition."
)

NEGATIVE = (
    "text, letters, words, writing, captions, numbers, digits, labels, "
    "typography, garbled text, fake text, signage, watermark, signature, logo, "
    "brand, map, flag, national emblem, close-up face, portrait, deformed, "
    "extra limbs, blurry, low quality, jpeg artifacts, oversaturated, garish, "
    "flat vector art, clip art, cartoon, night, darkness, moody, gritty, dirty, "
    "cluttered, rust, smoke, fire, flame"
)

EXTRA_NEGATIVE = {
    "st54-naval": "explosion, fire, war, weapons firing, missile",
    "viettel-helicopter": "military insignia, weapons, missile, army camouflage",
    "balloon-satellite": "ruler, measuring scale, gauge, tick marks, graduations, dial",
}

SCENES = {
    "dyno-humanoid": (
        "A bright robotics laboratory with tall windows and a polished pale floor. "
        "A full-size white humanoid robot walks over a low ramp of stepped blocks in "
        "the centre. Receding behind it stands a row of translucent ghost copies of "
        "the same robot frozen in slightly different poses, each standing on its own "
        "small glowing cyan ring on the floor. A luminous cyan skeleton of small "
        "spheres at the joints, joined by thin light lines, is overlaid exactly on "
        "the real robot. A soft frosted rounded panel floats to the left holding one "
        "smooth rising curve."
    ),
    "viettel-helicopter": (
        "A bright spacious maintenance hangar with tall glazed walls and a clean "
        "light floor. A light-grey civil utility helicopter stands in the centre, "
        "rotor blades still, panels open. A luminous cyan spine of light runs the "
        "length of the fuselage and branches downward into four glowing translucent "
        "equipment boxes standing in a neat row on the floor beside the aircraft. A "
        "soft teal ribbon of flowing light rises from the cockpit into a frosted "
        "rounded panel holding one gentle waveform."
    ),
    "uam-digital-twin": (
        "A bright airy exhibition hall with a clean pale floor and large windows. On "
        "the left, a white boxed-wing electric aircraft with tilting rotors rests on "
        "the floor. On the right, an identical copy of the same aircraft hovers as a "
        "translucent glowing cyan wireframe above a luminous grid pedestal. Two "
        "dotted arcs of cyan light loop between the real aircraft and its wireframe "
        "twin, one arc going each way. High above both, a soft white cloud slab "
        "carrying pale rounded server cylinders, with thin threads of light dropping "
        "from the cloud to each aircraft."
    ),
    "future-automobile": (
        "A bright vehicle proving ground under a clear sky, clean pale asphalt, low "
        "white buildings and light poles soft in the distance. A white autonomous "
        "test car with a sensor pod on its roof drives toward the camera. A luminous "
        "cyan fan of scanning light sweeps forward from the roof pod onto the road, "
        "and the road ahead is overlaid with a glowing translucent grid of pale blue "
        "cells, two cells lit soft green and one amber. A frosted rounded panel "
        "floats to the right holding one smooth curve."
    ),
    "imec2": (
        "A bright miniature city seen from a low aerial angle in clean 3D, white and "
        "light-grey buildings, green trees, pale roads, small vehicles. Glowing cyan "
        "sensor nodes sit on the rooftops, joined to one another by a luminous "
        "triangular mesh of thin light lines. A soft translucent green dome of light "
        "covers the central district. Above the city floats a white cloud slab with "
        "pale rounded server cylinders, and a row of small glowing edge boxes sits "
        "just below the rooftops. One rooftop node glows amber."
    ),
    "certified-neural-control": (
        "A bright open simulation hall with a clean pale floor and high glazed walls. "
        "Three identical white tilt-rotor aircraft are arranged along a rising arc "
        "through the air: the first with its rotors pointing straight up, the second "
        "with rotors tilted halfway, the third with rotors pointing forward and wings "
        "extended. On the floor beneath the arc lies a large luminous translucent "
        "cyan bowl of concentric contour rings, with a single bright line spiralling "
        "down the inside of the bowl to a glowing point at its centre. A soft green "
        "dashed boundary ring is drawn on the floor around the bowl."
    ),
    "korea-vietnam-cloud": (
        "A bright aerial view of two clean data-centre campuses far apart on a pale "
        "landscape under thin white cloud, the nearer one surrounded by tropical "
        "broad-leaved trees. A luminous double arc of cyan light links the two sites "
        "across the distance. Over the left campus a translucent red dashed ring is "
        "drawn and its glowing racks have faded to dim grey; over the right campus "
        "the racks glow healthy green inside a soft green ring. Small motes of light "
        "stream along the arc from the left site to the right one."
    ),
    "hybrid-cloud": (
        "A bright clean studio scene on a pale floor. On the left, a low white "
        "on-premise server hall shown in cutaway with rows of softly glowing blue "
        "racks inside. On the right, a soft white cloud slab carrying pale rounded "
        "server cylinders. Between them runs a luminous cyan lane along which five "
        "small glowing translucent cubes travel, three blue and two green. A frosted "
        "rounded panel floats above the lane holding two smooth curves that cross, "
        "one cyan and one amber."
    ),
    "streaming-bigdata": (
        "A bright logistics yard at midday, a clean white warehouse, neat rows of "
        "pale shipping containers, a few small delivery trucks, wide empty apron. A "
        "luminous river of small glowing cyan motes flows above the yard from left to "
        "right and splits into two identical parallel streams, each feeding one of "
        "two mirrored white server blocks standing side by side. A soft green ring "
        "glows on the ground beneath each of the two server blocks."
    ),
    "st54-naval": (
        "A bright naval dockyard under a clear sky, clean pale water, a light-grey "
        "surface ship moored alongside a spotless quay. A luminous translucent cyan "
        "cutaway overlay shows the interior of the hull as a long row of glowing "
        "compartment cells. Two cells amidships glow amber and one glows red inside a "
        "soft red dashed outline, while cyan threads of light visibly reroute around "
        "those cells so that a continuous green-lit path still runs from bow to stern."
    ),
    "uav-reliability": (
        "A bright clean assembly hall with tall windows and a pale polished floor. A "
        "white fixed-wing unmanned aircraft rests on a low stand, with tidy work "
        "trolleys nearby. Floating around the airframe is a luminous exploded diagram "
        "in cyan: glowing translucent blocks for each subsystem, joined by thin light "
        "lines, with two of the blocks doubled side by side to show a redundant pair "
        "and one block glowing amber. A frosted rounded panel on the right holds a "
        "single smooth curve that descends gently."
    ),
    "korea-peru-uav": (
        "A bright high-altitude mountain landscape under a clear sky, pale terraced "
        "ridges, a winding river far below, thin clouds. A white fixed-wing survey "
        "aircraft flies level across the scene. A translucent luminous cyan scan "
        "swath fans downward from the aircraft onto the terrain and lays a glowing "
        "grid of survey cells across the ground, a few cells tinted soft green and "
        "one amber. A small clean white ground station with a dish antenna stands on "
        "a near ridge, thin arcs of light rising from it to the aircraft."
    ),
    "historical-3d": (
        "A bright courtyard of a traditional East Asian heritage building at midday, "
        "a sweeping tiled roof, red-brown wooden columns, clean stone paving, a few "
        "trees. A small white unmanned airship with a camera gondola hovers above the "
        "roof. A translucent luminous cyan camera frustum descends from the gondola "
        "onto the roof, and beside the real building the same roof is rebuilt in the "
        "air as a glowing translucent triangular point-cloud mesh, half complete."
    ),
    "balloon-satellite": (
        "A bright stratospheric scene: deep clear blue sky above, a brilliant white "
        "curved cloud deck far below, sunlight from the side. A white high-altitude "
        "balloon rises with a small white instrument payload box hanging on a tether "
        "beneath it. A luminous cyan telemetry arc curves down from the payload "
        "toward a small clean ground station with a dish on a distant pale hillside. "
        "A soft frosted rounded panel floats in the lower left corner, empty and "
        "featureless."
    ),
    "unmanned-spacecraft": (
        "A bright airfield apron under a clear sky, clean pale concrete, low white "
        "hangars soft in the distance. A white unmanned airship craft floats just "
        "above the apron, held by light mooring lines. Drawn in the air around it is "
        "a luminous closed control loop: four glowing translucent rounded blocks "
        "arranged in a rectangle and joined by arrowed lines of cyan light, with a "
        "bright three-axis attitude gizmo of red, green and blue arrows glowing at "
        "the centre of the craft."
    ),
    "f1-picosatellite": (
        "A bright spotless cleanroom with white walls and soft even light. A small "
        "ten-centimetre cube satellite sits on a white pedestal in the centre, its "
        "solar-panel faces catching a pale blue sheen. A blurred technician in a "
        "white coverall stands well behind, out of focus. Beside the cube floats a "
        "luminous cyan exploded view: three pairs of identical glowing translucent "
        "circuit boards stacked one pair above another, each pair doubled to show "
        "redundancy, joined back to the cube by thin light lines. Through a window "
        "behind, a soft glowing arc of the Earth's bright limb."
    ),
}

def build_prompt(scene: str) -> str:
    return f"{scene} {STYLE}"

def seed_for(slug: str) -> int:
    """Stable per-slug seed so a rerun reproduces the same cover."""
    return (list(SCENES).index(slug) + 1) * 7919 + 20260817

def to_webp(raw_path: Path, out_path: Path) -> None:
    from PIL import Image

    im = Image.open(raw_path).convert("RGB")

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
    ap.add_argument("--only", nargs="*", help="project slugs, e.g. dyno-humanoid naval")
    ap.add_argument("--force", action="store_true", help="redo covers that exist")
    ap.add_argument("--dry-run", action="store_true", help="print prompts, render nothing")
    ap.add_argument("--steps", type=int, default=STEPS)
    args = ap.parse_args()

    slugs = list(SCENES)
    if args.only:
        wanted = set(args.only)
        slugs = [s for s in slugs if s in wanted or any(w in s for w in wanted)]
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
