#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
from textwrap import dedent
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]

DEPRECATION_MESSAGE = (
    "Deprecated: News no longer uses generated SVG brochure cards. "
    "Use scripts/generate_publication_news_archive.py for publication briefing cards, "
    "and keep generated cover images as WebP assets under images/news/."
)


BROCHURES = [
    {
        "output": ROOT / "images/news/251201/edge-availability-brochure.svg",
        "type": "Journal Article",
        "date": "December 31, 2025",
        "title": ["Edge Availability under", "Correlated Failures"],
        "subtitle": [
            "SRN modeling with Capacity-Oriented Availability for",
            "HA and live-migration trade-offs in edge recovery.",
        ],
        "chips": [
            ("MODEL EXTENSION", "Correlated SRN", 28),
            ("RECOVERY VIEW", "HA vs HA+LM", 28),
            ("KEY THRESHOLD", "5 nodes", 34),
        ],
        "nodes": ["Failure", "HA", "LM"],
        "lines": [
            "Long intervals can favor HA+LM",
            "Large correlated faults reverse the ranking",
            "Recovery policy should adapt to fault scale",
        ],
        "venue": "Journal of The Korea Society of Computer and Information",
        "note": "Verified from DOI metadata and the official KCI article page.",
        "palette": {
            "bg0": "#f5fbff",
            "bg1": "#dbeaf6",
            "panel1": "#eff6fb",
            "stroke": "#8db5cf",
            "hero": "#0b3457",
            "title": "#17304b",
            "body": "#56697b",
            "chip1": "#0f4c81",
            "chip2": "#176476",
            "chip3": "#5c6b8c",
            "chip_soft1": "#d7ebfb",
            "chip_soft2": "#d9eff4",
            "chip_soft3": "#e5e8f4",
            "right": "#143753",
            "node1": "#d5e8f7",
            "node2": "#b8d7ed",
            "node3": "#93bedc",
            "line1": "#5fc5dc",
            "line2": "#f2c25b",
        },
    },
    {
        "output": ROOT / "images/news/251014/urban-surveillance-maintenance-brochure.svg",
        "type": "Journal Article",
        "date": "October 14, 2025",
        "title": ["Urban Surveillance", "Maintenance Planning"],
        "subtitle": [
            "Stochastic Petri net analysis of reactive, autonomous,",
            "and preventive strategies for smart-city surveillance.",
        ],
        "chips": [
            ("MAINTENANCE", "Reactive / Auto / Preventive", 22),
            ("METHOD", "Sensitivity analysis", 28),
            ("GOAL", "Higher availability", 28),
        ],
        "nodes": ["Edge", "Aging", "Repair"],
        "lines": [
            "Maintenance is treated as a design variable",
            "Sensitivity points to the highest-impact components",
            "Case studies support planner-facing decisions",
        ],
        "venue": "Computing - Published October 14, 2025",
        "note": "Verified from the Springer abstract page and DOI metadata.",
        "palette": {
            "bg0": "#fdfaf5",
            "bg1": "#f3e4d3",
            "panel1": "#fbf4ec",
            "stroke": "#d5b18e",
            "hero": "#7c4d17",
            "title": "#503219",
            "body": "#725a45",
            "chip1": "#9a5b2a",
            "chip2": "#8b7340",
            "chip3": "#5b6d4b",
            "chip_soft1": "#fdebd8",
            "chip_soft2": "#f3eccd",
            "chip_soft3": "#e7f0dd",
            "right": "#4d2e11",
            "node1": "#f8e0bf",
            "node2": "#ead2aa",
            "node3": "#d8c291",
            "line1": "#e79f45",
            "line2": "#6fc28d",
        },
    },
    {
        "output": ROOT / "images/news/250827/metacom-cloud-edge-brochure.svg",
        "type": "MetaCom Short Paper",
        "date": "August 27, 2025",
        "title": ["Aging Dependability for", "AAM Vehicle Digital Twins"],
        "subtitle": [
            "Cloud-edge-in-the-loop simulation assessed as a long-running",
            "metaverse platform for advanced air mobility experimentation.",
        ],
        "chips": [
            ("PLATFORM", "Cloud-Edge-in-the-loop", 22),
            ("SYSTEM", "AAM digital twin", 28),
            ("FOCUS", "Aging dependability", 26),
        ],
        "nodes": ["Cloud", "Edge", "Twin"],
        "lines": [
            "Moves beyond one-shot functional integration",
            "Looks at resilience in long-running testbeds",
            "Useful for dependable AAM experimentation",
        ],
        "venue": "IEEE MetaCom 2025 - Short paper, pages 82-87",
        "note": "Verified from DOI metadata, MetaCom records, and J-GLOBAL proceedings metadata.",
        "palette": {
            "bg0": "#f4fbff",
            "bg1": "#d9ecf7",
            "panel1": "#eef7fb",
            "stroke": "#93bdd6",
            "hero": "#0e4c79",
            "title": "#17324d",
            "body": "#586d80",
            "chip1": "#1b5f8b",
            "chip2": "#1c7374",
            "chip3": "#55698f",
            "chip_soft1": "#d9ecfb",
            "chip_soft2": "#daf5f3",
            "chip_soft3": "#e3e8f5",
            "right": "#103652",
            "node1": "#d7ebf8",
            "node2": "#b8d9ef",
            "node3": "#9ec4e1",
            "line1": "#67c2df",
            "line2": "#f1ba54",
        },
    },
    {
        "output": ROOT / "images/news/250827/metacom-storage-brochure.svg",
        "type": "MetaCom Conference Paper",
        "date": "August 27, 2025",
        "title": ["Metaverse Storage", "High Availability"],
        "subtitle": [
            "Stochastic reward nets for quantifying resilience in distributed",
            "storage backbones that support persistent immersive services.",
        ],
        "chips": [
            ("METHOD", "Reward nets", 30),
            ("TARGET", "Distributed storage", 26),
            ("FOCUS", "High availability", 28),
        ],
        "nodes": ["Nodes", "Replica", "Service"],
        "lines": [
            "Quantifies storage resilience, not just throughput",
            "Fits metaverse architectures and applications",
            "Extends reliability modeling into immersive storage",
        ],
        "venue": "IEEE MetaCom 2025 - Conference Session 1",
        "note": "Verified from DOI metadata, the MetaCom program, and the accepted-paper listing.",
        "palette": {
            "bg0": "#f6fbff",
            "bg1": "#e0edf6",
            "panel1": "#f0f6fb",
            "stroke": "#98b9d0",
            "hero": "#12406c",
            "title": "#18324d",
            "body": "#596c7f",
            "chip1": "#0f4c81",
            "chip2": "#406b8d",
            "chip3": "#2f716b",
            "chip_soft1": "#d7ebfb",
            "chip_soft2": "#e0e9f5",
            "chip_soft3": "#dcf0ec",
            "right": "#15344f",
            "node1": "#d9ebf9",
            "node2": "#c0d9ee",
            "node3": "#9ac2e1",
            "line1": "#63bdd8",
            "line2": "#77d0a2",
        },
    },
    {
        "output": ROOT / "images/news/250827/metacom-sim2real-brochure.svg",
        "type": "MetaCom Workshop Paper",
        "date": "August 27, 2025",
        "title": ["Sim-to-Real RL for", "TurtleBot in ROS2 + UE"],
        "subtitle": [
            "A metaverse-ready robotics pipeline that links Unreal Engine,",
            "ROS2, and reinforcement learning for deployment transfer.",
        ],
        "chips": [
            ("ROBOTICS", "TurtleBot", 32),
            ("STACK", "ROS2 + Unreal", 30),
            ("GOAL", "Sim-to-real", 32),
        ],
        "nodes": ["Sim", "Policy", "Robot"],
        "lines": [
            "Bridges virtual training and physical motion",
            "Grounded in RL and robot-control workflows",
            "Presented in MetaCom Workshop Session 1",
        ],
        "venue": "IEEE MetaCom 2025 - Workshop Session 1",
        "note": "Verified from DOI metadata, the MetaCom program, and the J-GLOBAL proceedings entry.",
        "palette": {
            "bg0": "#f7fbff",
            "bg1": "#dae9ff",
            "panel1": "#eef5ff",
            "stroke": "#96b4df",
            "hero": "#19497e",
            "title": "#1c3151",
            "body": "#5a6b86",
            "chip1": "#255e9d",
            "chip2": "#1f7185",
            "chip3": "#5f6296",
            "chip_soft1": "#dce9fb",
            "chip_soft2": "#daf3f7",
            "chip_soft3": "#e6e6f5",
            "right": "#153250",
            "node1": "#dce8fa",
            "node2": "#bdd4ef",
            "node3": "#97bae0",
            "line1": "#6ac1df",
            "line2": "#f2c45d",
        },
    },
    {
        "output": ROOT / "images/news/250827/metacom-malicious-code-brochure.svg",
        "type": "MetaCom Conference Paper",
        "date": "August 27, 2025",
        "title": ["LLM Security for", "Malicious Code Detection"],
        "subtitle": [
            "Token optimization used as a design lever for code-oriented",
            "LLM screening in metaverse security workflows.",
        ],
        "chips": [
            ("SECURITY", "Malicious code", 28),
            ("MODEL", "LLM-based detection", 24),
            ("LEVER", "Token optimization", 24),
        ],
        "nodes": ["Code", "Tokens", "Risk"],
        "lines": [
            "Positions security inside programmable metaverse stacks",
            "Treats token design as part of detection quality",
            "Presented in Security, Privacy, and Trust",
        ],
        "venue": "IEEE MetaCom 2025 - Security, Privacy, and Trust",
        "note": "Verified from DOI metadata, the MetaCom program, and the J-GLOBAL proceedings record.",
        "palette": {
            "bg0": "#fff8f5",
            "bg1": "#f2ddd8",
            "panel1": "#fdf0ec",
            "stroke": "#d6aaa2",
            "hero": "#8b3f31",
            "title": "#4f261f",
            "body": "#765852",
            "chip1": "#a34b34",
            "chip2": "#8c5d38",
            "chip3": "#6c4f86",
            "chip_soft1": "#f8e0d8",
            "chip_soft2": "#f4e2cb",
            "chip_soft3": "#ece2f2",
            "right": "#4c231d",
            "node1": "#f7dcd6",
            "node2": "#efc8bb",
            "node3": "#deafa0",
            "line1": "#ef9c63",
            "line2": "#be8ad9",
        },
    },
    {
        "output": ROOT / "images/news/250827/metacom-adaptive-prompting-brochure.svg",
        "type": "MetaCom Workshop Paper",
        "date": "August 27, 2025",
        "title": ["Adaptive Prompting", "for Metaverse Tasks"],
        "subtitle": [
            "An iterative prompt-optimization framework for improving",
            "LLM task performance across diverse application settings.",
        ],
        "chips": [
            ("LLM FLOW", "Iterative prompts", 28),
            ("TASKS", "Diverse settings", 28),
            ("GOAL", "Better performance", 26),
        ],
        "nodes": ["Prompt", "Feedback", "Task"],
        "lines": [
            "Treats prompting as an adaptive cycle",
            "Context-aware optimization is central to the design",
            "Presented in MetaCom Workshop Session 1",
        ],
        "venue": "IEEE MetaCom 2025 - Workshop Session 1",
        "note": "Verified from DOI metadata, the MetaCom program, and the J-GLOBAL proceedings entry.",
        "palette": {
            "bg0": "#fbf7ff",
            "bg1": "#eadcf7",
            "panel1": "#f6eefc",
            "stroke": "#bba1d8",
            "hero": "#6d3c99",
            "title": "#412555",
            "body": "#6d5b7b",
            "chip1": "#7d4cb0",
            "chip2": "#4967a8",
            "chip3": "#2d7669",
            "chip_soft1": "#efe2fb",
            "chip_soft2": "#e0e8fb",
            "chip_soft3": "#ddf1ec",
            "right": "#41245a",
            "node1": "#f0e2fb",
            "node2": "#d7c0ee",
            "node3": "#b99dde",
            "line1": "#b68be2",
            "line2": "#68c3d9",
        },
    },
    {
        "output": ROOT / "images/news/250827/metacom-pgelu-brochure.svg",
        "type": "MetaCom Conference Paper",
        "date": "August 27, 2025",
        "title": ["PGELU for Emotion and", "3D Object Recognition"],
        "subtitle": [
            "A parametric GELU variant aimed at stable and scalable",
            "deep learning for metaverse perception workloads.",
        ],
        "chips": [
            ("NETWORK", "Parametric GELU", 28),
            ("TARGETS", "Emotion + 3D", 28),
            ("GOAL", "Stable scaling", 28),
        ],
        "nodes": ["Input", "PGELU", "Recognition"],
        "lines": [
            "Links activation design to metaverse perception",
            "Targets both affective and 3D recognition tasks",
            "Presented in AI for the Metaverse",
        ],
        "venue": "IEEE MetaCom 2025 - Conference Session 2",
        "note": "Verified from DOI metadata, the MetaCom program, and the J-GLOBAL proceedings record.",
        "palette": {
            "bg0": "#fffaf2",
            "bg1": "#f5e4bc",
            "panel1": "#fdf4df",
            "stroke": "#ddbd79",
            "hero": "#8a5a12",
            "title": "#4c3413",
            "body": "#786246",
            "chip1": "#c88022",
            "chip2": "#8e5f30",
            "chip3": "#6e558f",
            "chip_soft1": "#fdebd0",
            "chip_soft2": "#f0e0ca",
            "chip_soft3": "#ece5f4",
            "right": "#503410",
            "node1": "#f9e7c8",
            "node2": "#ecd4a0",
            "node3": "#dfc17d",
            "line1": "#efb85c",
            "line2": "#8aa0ea",
        },
    },
    {
        "output": ROOT / "images/news/250402/vehicle-digital-twin-brochure.svg",
        "type": "Conference Paper",
        "date": "April 2, 2025",
        "title": ["Vehicle Digital Twin", "under Steady Wind"],
        "subtitle": [
            "Integration and early flight-simulation results for the KADA",
            "KP2-c eVTOL across light and moderate steady-wind cases.",
        ],
        "chips": [
            ("WIND CASES", "10 and 20 knots", 28),
            ("AIRCRAFT", "KADA KP2-c", 30),
            ("METRIC", "Yaw-rate response", 24),
        ],
        "nodes": ["Twin", "Dynamics", "Wind"],
        "lines": [
            "Moves the twin toward physics-grounded evaluation",
            "Tracks yaw-rate shifts under steady wind loading",
            "Future work points to flight-test validation",
        ],
        "venue": "KSAS Spring Conference 2025 - pages 381-382",
        "note": "Verified from the official KSAS proceedings PDF and publication metadata.",
        "palette": {
            "bg0": "#f5fbff",
            "bg1": "#dbe7f4",
            "panel1": "#eff4fb",
            "stroke": "#9ab4d2",
            "hero": "#1f4c77",
            "title": "#18324d",
            "body": "#5c6f84",
            "chip1": "#1f5f90",
            "chip2": "#3d7091",
            "chip3": "#4d6b5f",
            "chip_soft1": "#dceafb",
            "chip_soft2": "#dcecf5",
            "chip_soft3": "#e2efe8",
            "right": "#163550",
            "node1": "#dce9f9",
            "node2": "#bfd6ee",
            "node3": "#9ec0df",
            "line1": "#66bdd7",
            "line2": "#f4c35f",
        },
    },
    {
        "output": ROOT / "images/news/250313/container-migration-correction-brochure.svg",
        "type": "Correction Notice",
        "date": "March 13, 2025",
        "title": ["Publication Record", "Correction Update"],
        "subtitle": [
            "Official correction linked to the container migration study",
            "to keep the online scholarly record accurate and aligned.",
        ],
        "chips": [
            ("UPDATE", "Correction notice", 28),
            ("LINK", "Original article", 30),
            ("ROLE", "Record accuracy", 30),
        ],
        "nodes": ["Record", "Update", "Citation"],
        "lines": [
            "Correction keeps the publication trail clean",
            "Springer change history links both records",
            "Accuracy is part of dependable scholarship",
        ],
        "venue": "Computing - Published March 13, 2025",
        "note": "Verified from the Springer correction DOI and the original article change history.",
        "palette": {
            "bg0": "#fbfaf8",
            "bg1": "#e9e0d8",
            "panel1": "#f5f1ec",
            "stroke": "#c8b7a8",
            "hero": "#6d5238",
            "title": "#463223",
            "body": "#6f6256",
            "chip1": "#8a6545",
            "chip2": "#5c6f7e",
            "chip3": "#6f7074",
            "chip_soft1": "#efe2d7",
            "chip_soft2": "#e0e9f1",
            "chip_soft3": "#ebebee",
            "right": "#423125",
            "node1": "#efe1d7",
            "node2": "#d7c6b7",
            "node3": "#bea894",
            "line1": "#d2a36c",
            "line2": "#8eb5d2",
        },
    },
    {
        "output": ROOT / "images/news/250205/container-migration-brochure.svg",
        "type": "Journal Article",
        "date": "February 5, 2025",
        "title": ["Container Migration", "Strategy Evaluation"],
        "subtitle": [
            "Stochastic Petri net models compare Cold, PreCopy,",
            "PostCopy, and Hybrid policies in realistic migration settings.",
        ],
        "chips": [
            ("POLICIES", "4 strategies", 32),
            ("METRICS", "MTT, rate, discard", 23),
            ("INSIGHT", "Policy trade-offs", 28),
        ],
        "nodes": ["Cold", "Pre", "Post"],
        "lines": [
            "Cold lowers total time at high arrival pressure",
            "PostCopy yields the lowest discard probability",
            "Hybrid policy was studied with sensitivity analysis",
        ],
        "venue": "Computing - Volume 107, Article 64",
        "note": "Verified from the Springer abstract page and DOI metadata.",
        "palette": {
            "bg0": "#f5fbff",
            "bg1": "#d8e7f7",
            "panel1": "#eef5fc",
            "stroke": "#97b6da",
            "hero": "#114679",
            "title": "#183451",
            "body": "#5b6e84",
            "chip1": "#175892",
            "chip2": "#2f6e92",
            "chip3": "#556d8f",
            "chip_soft1": "#dbeafb",
            "chip_soft2": "#dbeef6",
            "chip_soft3": "#e2e8f6",
            "right": "#153450",
            "node1": "#dce9fb",
            "node2": "#bfd7ef",
            "node3": "#9ec2e1",
            "line1": "#66c1da",
            "line2": "#f2c15b",
        },
    },
    {
        "output": ROOT / "images/news/250201/disaster-detection-brochure.svg",
        "type": "Journal Article",
        "date": "February 1, 2025",
        "title": ["IoT Disaster Detection", "across Geographic Areas"],
        "subtitle": [
            "LoRaWAN-aware stochastic models for cloud-fog disaster",
            "monitoring with capacity planning over multiple regions.",
        ],
        "chips": [
            ("NETWORK", "LoRa + cloud", 30),
            ("METHOD", "SPN analysis", 30),
            ("IMPACT", "Robust monitoring", 28),
        ],
        "nodes": ["Sensors", "Fog", "Cloud"],
        "lines": [
            "Highlights stress cost-efficient capacity planning",
            "More cores reduce response time and improve throughput",
            "Built for large-area disaster monitoring scenarios",
        ],
        "venue": "ICT Express - Open access article",
        "note": "Verified from the ScienceDirect highlights/abstract page and DOI metadata.",
        "palette": {
            "bg0": "#f7fbff",
            "bg1": "#d9e9f5",
            "panel1": "#eef6fb",
            "stroke": "#96b8cf",
            "hero": "#12436f",
            "title": "#18324e",
            "body": "#5c6e81",
            "chip1": "#0f4c81",
            "chip2": "#1c6a76",
            "chip3": "#4f6f5f",
            "chip_soft1": "#d7ebfb",
            "chip_soft2": "#dcf2f2",
            "chip_soft3": "#e5f0e7",
            "right": "#16344e",
            "node1": "#dcebf8",
            "node2": "#bed9ed",
            "node3": "#9fc3df",
            "line1": "#64c0d9",
            "line2": "#81c88c",
        },
    },
    {
        "output": ROOT / "images/news/250121/mhmctd3-brochure.svg",
        "type": "TechRxiv Preprint",
        "date": "January 21, 2025",
        "title": ["mhmcTD3 for", "Autonomous Navigation"],
        "subtitle": [
            "Multi-head actor-critic learning with memory contextualisation",
            "for map-free robot navigation in dynamic environments.",
        ],
        "chips": [
            ("HEADS", "Fusion + Memory", 26),
            ("SENSING", "LiDAR-focused", 30),
            ("TRANSFER", "Sim to real", 32),
        ],
        "nodes": ["LiDAR", "Memory", "Policy"],
        "lines": [
            "Evaluated in ROS2/Gazebo and on Turtlebot3",
            "Targets small and moving obstacles in clutter",
            "Ablations confirm the value of each head",
        ],
        "venue": "TechRxiv - Posted January 21, 2025",
        "note": "Verified from the official TechRxiv PDF and DOI record.",
        "palette": {
            "bg0": "#fff9f4",
            "bg1": "#f5e2cf",
            "panel1": "#fcf1e6",
            "stroke": "#dfb58e",
            "hero": "#84501a",
            "title": "#4b2f12",
            "body": "#745a44",
            "chip1": "#c9771f",
            "chip2": "#a45c38",
            "chip3": "#345d8d",
            "chip_soft1": "#feead7",
            "chip_soft2": "#fbe4dd",
            "chip_soft3": "#dde8f8",
            "right": "#4b2d10",
            "node1": "#f8e0c0",
            "node2": "#eccca7",
            "node3": "#ddba83",
            "line1": "#efb55b",
            "line2": "#69bdd7",
        },
    },
]


def make_text_block(x: int, y: int, lines: list[str], size: int, fill: str, family: str, weight: int, line_gap: int) -> str:
    tspans = []
    for idx, line in enumerate(lines):
        dy = "0" if idx == 0 else str(line_gap)
        tspans.append(f'    <tspan x="{x}" dy="{dy}">{escape(line)}</tspan>')
    return "\n".join(
        [
            f'  <text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" font-weight="{weight}">',
            *tspans,
            "  </text>",
        ]
    )


def render(entry: dict) -> str:
    p = entry["palette"]
    chip_positions = [84, 312, 540]
    chip_width = 210
    chip_lines = []
    for idx, (label, value, value_size) in enumerate(entry["chips"]):
        x = chip_positions[idx]
        chip_color = p[f"chip{idx + 1}"]
        chip_soft = p[f"chip_soft{idx + 1}"]
        chip_lines.extend(
            [
                f'  <rect x="{x}" y="432" width="{chip_width}" height="112" rx="22" fill="{chip_color}"/>',
                f'  <text x="{x + 22}" y="468" fill="{chip_soft}" font-family="Arial, sans-serif" font-size="18" font-weight="700">{escape(label)}</text>',
                f'  <text x="{x + 22}" y="510" fill="#ffffff" font-family="Georgia, serif" font-size="{value_size}" font-weight="700">{escape(value)}</text>',
            ]
        )

    node_labels = entry["nodes"]
    node_boxes = [
        (850, 180, p["node1"], node_labels[0]),
        (950, 180, p["node1"], node_labels[1]),
        (900, 270, p["node2"], node_labels[2]),
    ]
    node_lines = []
    for x, y, fill, label in node_boxes:
        node_lines.extend(
            [
                f'  <rect x="{x}" y="{y}" width="78" height="52" rx="14" fill="{fill}"/>',
                f'  <text x="{x + 18}" y="{y + 33}" fill="{p["hero"]}" font-family="Arial, sans-serif" font-size="18" font-weight="700">{escape(label)}</text>',
            ]
        )

    panel_lines = []
    for idx, line in enumerate(entry["lines"]):
        panel_lines.append(
            f'  <text x="846" y="{498 + (idx * 30)}" fill="#dcecf8" font-family="Arial, sans-serif" font-size="18" font-weight="700">{escape(line)}</text>'
        )

    return dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720" role="img" aria-labelledby="title desc">
          <title id="title">{escape(" / ".join(entry["title"]))} brochure card</title>
          <desc id="desc">{escape(" ".join(entry["subtitle"]))}</desc>
          <defs>
            <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="{p["bg0"]}"/>
              <stop offset="100%" stop-color="{p["bg1"]}"/>
            </linearGradient>
            <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#ffffff"/>
              <stop offset="100%" stop-color="{p["panel1"]}"/>
            </linearGradient>
          </defs>
          <rect width="1200" height="720" fill="url(#bg)"/>
          <circle cx="1060" cy="116" r="124" fill="{p["node1"]}"/>
          <circle cx="1094" cy="610" r="138" fill="{p["bg0"]}"/>
          <rect x="48" y="48" width="1104" height="624" rx="34" fill="url(#panel)" stroke="{p["stroke"]}" stroke-width="2"/>
          <text x="84" y="102" fill="{p["hero"]}" font-family="Arial, sans-serif" font-size="22" font-weight="700">{escape(entry["type"])} - {escape(entry["date"])}</text>
        {make_text_block(84, 170, entry["title"], 50, p["title"], "Georgia, serif", 700, 56)}
        {make_text_block(84, 302, entry["subtitle"], 25, p["body"], "Arial, sans-serif", 400, 34)}
        {"".join(chip_lines)}
          <rect x="808" y="124" width="288" height="430" rx="28" fill="{p["right"]}"/>
          <text x="846" y="160" fill="#dcecf8" font-family="Arial, sans-serif" font-size="19" font-weight="700">BROCHURE INSIGHTS</text>
        {"".join(node_lines)}
          <line x1="928" y1="232" x2="928" y2="270" stroke="{p["line1"]}" stroke-width="8" stroke-linecap="round"/>
          <line x1="972" y1="232" x2="950" y2="270" stroke="{p["line1"]}" stroke-width="8" stroke-linecap="round"/>
          <path d="M878 354 C918 314 978 314 1020 354" fill="none" stroke="{p["line2"]}" stroke-width="8" stroke-linecap="round"/>
          <path d="M878 382 C918 344 978 344 1020 382" fill="none" stroke="{p["line1"]}" stroke-width="8" stroke-linecap="round"/>
        {"".join(panel_lines)}
          <text x="84" y="610" fill="{p["hero"]}" font-family="Arial, sans-serif" font-size="18" font-weight="700">{escape(entry["venue"])}</text>
          <text x="84" y="638" fill="{p["body"]}" font-family="Arial, sans-serif" font-size="17">{escape(entry["note"])}</text>
        </svg>
        """
    ).strip() + "\n"


def main() -> None:
    print(DEPRECATION_MESSAGE)


if __name__ == "__main__":
    main()
