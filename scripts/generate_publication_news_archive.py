#!/usr/bin/env python3

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_PATH = ROOT / "_pages" / "publications.md"
OUTPUT_PATH = ROOT / "_includes" / "publication_news_archive.html"
OUTPUT_2025_PATH = ROOT / "_includes" / "publication_news_2025.html"
OUTPUT_MISSING_PATH = ROOT / "_includes" / "publication_news_missing.html"

# Tags already represented by long-form entries in _pages/news.md. The generated
# missing archive intentionally excludes these to keep the News page complete
# without repeating the same publication twice.
NEWS_DEDICATED_TAGS = {
    "J53",
    "J52",
    "J49",
    "J51",
    "J48",
    "J47",
    "P04",
    "C46",
    "C41",
    "C42",
    "C45",
    "C43",
    "C44",
    "J44",
    "C39",
    "C51",
    "J45",
    "J46",
    "J41",
    "J40",
    "P03",
    "P02",
    "J39",
    "P06",
    "C36",
}

SPECIAL_LINKS = {
    "C48": {
        "label": "DBpia record",
        "url": "https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11658488",
        "badge": "DBpia",
    },
    "J51": {
        "label": "DOI record",
        "url": "https://doi.org/10.9708/jksci.2025.30.12.025",
        "badge": "DOI",
    },
    "C51": {
        "label": "KSAS proceedings",
        "url": "https://ksas.or.kr/proceedings/2025a/data/%EC%B2%A8%EB%B6%804.%202025%EB%85%84%EB%8F%84%EC%B6%98%EA%B3%84%ED%95%99%EC%88%A0%EB%8C%80%ED%9A%8C_%EB%85%BC%EB%AC%B8%EC%A7%91_All.pdf",
        "badge": "Proceedings",
    },
    "C49": {
        "label": "DBpia record",
        "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12058721",
        "badge": "DBpia",
    },
    "C47": {
        "label": "DBpia record",
        "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11658014",
        "badge": "DBpia",
    },
    "C50": {
        "label": "Program record",
        "url": "https://ksas.or.kr/proceedings/2024b/data/2024%EB%85%84%EB%8F%84%20%EC%B6%94%EA%B3%84%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%28%EC%95%88%29%20v9.pdf",
        "badge": "Program",
    },
}

DOMAIN_BADGES = {
    "Domain 1": "AI & Autonomy",
    "Domain 2": "Dependability & Infra",
    "Domain 3": "IoT & CPS",
    "Domain 4": "Digital Twin & UAM",
    "Domain 5": "Aerospace Systems",
}

DOMAIN_LINES = {
    "Domain 1": "artificial intelligence, reinforcement learning, autonomous control, navigation, and perception",
    "Domain 2": "dependability, performance, energy, storage, cloud, SDN, and blockchain infrastructures",
    "Domain 3": "IoT, smart environments, surveillance, healthcare, and cyber-physical infrastructures",
    "Domain 4": "digital twin systems, advanced air mobility, unmanned aerial systems, and twin-enabled dependability",
    "Domain 5": "aerospace systems, aerodynamic modeling, flight dynamics, and air vehicle design",
}

DOMAIN_HEADINGS = {
    "## B. ": "Domain 1",
    "## C. ": "Domain 2",
    "## D. ": "Domain 3",
    "## E. ": "Domain 4",
    "## F. ": "Domain 5",
}

DOMAIN_VISUAL_CLASSES = {
    "Domain 1": "publication-news-card--ai",
    "Domain 2": "publication-news-card--infra",
    "Domain 3": "publication-news-card--iot",
    "Domain 4": "publication-news-card--twin",
    "Domain 5": "publication-news-card--aero",
}

DOMAIN_VISUAL_LABELS = {
    "Domain 1": "AI autonomy",
    "Domain 2": "Dependability",
    "Domain 3": "IoT systems",
    "Domain 4": "Digital twin",
    "Domain 5": "Aerospace",
}

DOMAIN_CAPTIONS = {
    "Domain 1": "AI autonomy, perception, learning signals, and deployment evidence mapped to the paper's technical focus.",
    "Domain 2": "dependability metrics, resilient infrastructure behavior, and performance trade-offs mapped to the paper's technical focus.",
    "Domain 3": "connected sensing, cyber-physical monitoring, and operational performance metrics mapped to the paper's technical focus.",
    "Domain 4": "digital-twin feedback loops, flight simulation, and mobility-system dependability mapped to the paper's technical focus.",
    "Domain 5": "aerospace modeling, flight dynamics, and system-design evidence mapped to the paper's technical focus.",
}

TYPE_VISUAL_CLASSES = {
    "Journal article": "publication-news-card--journal",
    "Conference paper": "publication-news-card--conference",
    "Preprint": "publication-news-card--preprint",
    "Book chapter": "publication-news-card--book",
    "Submission record": "publication-news-card--record",
    "Publication record": "publication-news-card--record",
}

VISUAL_KEYWORDS = (
    ("stochastic reward", "SRN"),
    ("stochastic petri", "SPN"),
    ("petri", "SPN"),
    ("queue", "Queueing"),
    ("availability", "Availability"),
    ("dependability", "Dependability"),
    ("reliability", "Reliability"),
    ("energy", "Energy"),
    ("kubernetes", "K8s"),
    ("microservice", "Microservices"),
    ("migration", "Migration"),
    ("blockchain", "Blockchain"),
    ("hyperledger", "Fabric"),
    ("internet of medical", "IoMT"),
    ("smart city", "Smart city"),
    ("smart building", "Smart building"),
    ("surveillance", "Surveillance"),
    ("robot", "Robotics"),
    ("reinforcement", "DRL"),
    ("navigation", "Navigation"),
    ("vision", "Vision"),
    ("language model", "VLM/LLM"),
    ("deep learning", "Deep learning"),
    ("digital twin", "Digital twin"),
    ("uam", "UAM"),
    ("aam", "AAM"),
    ("evtol", "eVTOL"),
    ("aerial", "Aerial"),
    ("uav", "UAV"),
    ("airfoil", "Airfoil"),
    ("aerodynamic", "Aerodynamics"),
    ("satellite", "Satellite"),
)

TITLE_RE = re.compile(r"\*\*(.+?)\*\*")
DATE_RE = re.compile(r"\[(\d{4}-\d{2}-\d{2})\]\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
TAG_RE = re.compile(r"\[([A-Z]\d+[A-Za-z]?)\]</span>")

CURATED_SUMMARIES = {
    "J53": (
        "Published in Mathematics, this article models microservice-based distributed edge "
        "storage with stochastic reward nets across hardware failures, software failures, "
        "software aging, high availability, live migration, and rejuvenation. It compares six "
        "policy scenarios through Capacity-Oriented Availability and shows why migration must "
        "finish before rejuvenation to avoid Proactive Crash behavior."
    ),
    "J49": (
        "Published in Journal of Network and Systems Management, S-iNAS studies Ceph-based "
        "industrial storage under bursty Industry 4.0 workloads with SRN models that compare "
        "time-based and event-based scaling. The result is a practical design guide for when "
        "scheduled expansion is stable enough and when threshold-driven scaling is needed to keep "
        "latency under control."
    ),
    "J51": (
        "This article extends SRN-based edge availability modeling to correlated failures rather "
        "than isolated-fault assumptions. The public record highlights a Capacity-Oriented "
        "Availability metric that captures the overhead of high-availability and live-migration "
        "policies, giving planners a more realistic basis for resilient edge deployment decisions."
    ),
    "J48": (
        "This Journal of Network and Computer Applications paper models Kubernetes autoscaling with "
        "GSPN so that performance and energy can be evaluated together rather than separately. It "
        "turns autoscaling thresholds into workload-aware trade-offs, showing how power savings and "
        "response-time penalties can move in opposite directions."
    ),
    "J47": (
        "This Computing article brings preventive maintenance into urban surveillance dependability "
        "analysis through stochastic Petri nets. By centering sensitivity analysis, it frames "
        "maintenance planning as a data-driven way to protect availability and service continuity "
        "instead of reacting only after failures emerge."
    ),
    "P04": (
        "RT-VLM rethinks real-world object recognition robustness around four structured clues: "
        "bounding boxes, class names, object captions, and scene context. The arXiv abstract "
        "positions the method as a two-stage vision-language pipeline that uses explicit evidence "
        "and self-correction to handle domain shift, occlusion, and nearby-class confusion."
    ),
    "C46": (
        "This MetaCom 2025 short paper examines aging dependability in a cloud-edge-in-the-loop "
        "platform for AAM vehicle digital twins. It widens digital-twin evaluation from functional "
        "integration to long-running resilience, an important step for metaverse-connected aviation "
        "simulation stacks."
    ),
    "C45": (
        "This MetaCom 2025 paper tackles malicious code detection with large language models through "
        "token optimization. The contribution positions metaverse security as an inference-design "
        "problem, where how code is represented to the model can materially affect detection quality."
    ),
    "C44": (
        "This MetaCom 2025 paper introduces PGELU, a parametric GELU variant aimed at keeping "
        "emotion and 3D object recognition both stable and scalable in metaverse pipelines. It "
        "frames activation design as a lever for robustness when immersive applications mix "
        "heterogeneous perception tasks."
    ),
    "C43": (
        "This MetaCom 2025 workshop paper proposes an iterative prompt-optimization framework for "
        "improving LLM performance across diverse tasks. Rather than treating prompts as static "
        "text, it turns prompting into an adaptive loop that can be tuned and reused in metaverse "
        "application workflows."
    ),
    "C42": (
        "This MetaCom 2025 workshop paper focuses on sim-to-real reinforcement learning for "
        "TurtleBot using ROS2 and Unreal Engine. It reinforces the idea that metaverse-ready "
        "simulation can be a practical bridge from virtual training to deployable robot behavior."
    ),
    "C41": (
        "This MetaCom 2025 paper quantifies high availability in metaverse-oriented distributed "
        "storage with stochastic reward nets. It extends the reliability-modeling line into "
        "storage backends that must keep immersive services responsive and resilient under "
        "distributed demand."
    ),
    "J44": (
        "This ICT Express article uses M/M/c/K queueing models to analyze cloud-edge-sensor data "
        "harvesting, motivated by precision agriculture and other real-time IoT settings. It gives "
        "designers a way to anticipate bottlenecks and provision sensing pipelines before "
        "overbuilding the infrastructure."
    ),
    "C39": (
        "This SBRC 2025 paper applies SPN models to intelligent camera surveillance in smart "
        "buildings, studying response time, throughput, utilization, and drop probability across "
        "edge-fog configurations. The paper turns capacity planning for video analytics into a "
        "measurable engineering problem rather than an ad hoc deployment decision."
    ),
    "C51": (
        "This KSAS 2025 proceedings paper reports the integration of a vehicle digital twin stack "
        "and early flight-simulation results under steady-wind conditions. The official proceedings "
        "describe a KADA KP2-c eVTOL case study that tracks how wind intensity changes yaw-rate "
        "response, grounding the twin in flight-dynamics behavior rather than visualization alone."
    ),
    "J45": (
        "This entry records the official correction linked to the container-migration article "
        "published earlier in 2025. Keeping the corrected record visible is important for the "
        "technical accuracy and long-term reliability of the publication trail."
    ),
    "J46": (
        "This Computing article compares container-migration strategies from a systems-performance "
        "perspective, giving operators a clearer basis for choosing how to relocate running "
        "services. It adds practical evidence to live-migration decision making in cloud and edge "
        "environments where continuity and overhead must be balanced."
    ),
    "J41": (
        "This ICT Express paper models Hyperledger Fabric transaction flow with stochastic Petri "
        "nets across endorsement, ordering, and commit phases. The associated public abstract "
        "highlights how block size and transaction pressure can shift throughput, response time, and "
        "resource efficiency before deployment."
    ),
    "J40": (
        "This ICT Express article studies IoT disaster detection across multiple geographic areas "
        "with stochastic models tailored to fog-assisted sensing infrastructures. It helps planners "
        "reason about response time, drop probability, and resource sizing when disaster-monitoring "
        "coverage has to scale beyond a single site."
    ),
    "P03": (
        "Posted on TechRxiv, this preprint frames end-to-end autonomous navigation around "
        "multi-head actor-critic fusion and memory contextualisation. The central idea is that "
        "navigation policies become more robust when they combine richer sensor representations "
        "with temporal context instead of relying on a single instantaneous policy view."
    ),
}


def clean_venue(value: str, link: str) -> str:
    venue = value.replace("*", "").strip().rstrip(".")

    while True:
        trimmed = re.sub(r"\s*\([^()]*\)\s*$", "", venue).strip().rstrip(".")
        if trimmed == venue:
            break
        venue = trimmed

    venue = venue.replace("--", "-")
    venue = re.sub(r"\s{2,}", " ", venue)

    if not venue:
        if "techrxiv" in link.lower():
            return "TechRxiv"
        return "External publication record"

    return venue


def type_label(tag: str, venue: str, link: str) -> str:
    venue_lower = venue.lower()
    link_lower = link.lower()

    if tag.startswith("J"):
        return "Journal article"
    if tag.startswith("C"):
        return "Conference paper"
    if tag.startswith("B"):
        return "Book chapter"
    if tag.startswith("P"):
        if "withdrawn" in venue_lower:
            return "Submission record"
        if "arxiv" in venue_lower or "research square" in venue_lower or "techrxiv" in link_lower:
            return "Preprint"
        return "Publication record"
    return "Publication record"


def source_badge(entry: dict[str, str | int]) -> str:
    tag = str(entry["tag"])
    link = str(entry["link"])

    if tag in SPECIAL_LINKS:
        return SPECIAL_LINKS[tag]["badge"]
    if "doi.org" in link:
        return "DOI"
    if "openreview" in link:
        return "OpenReview"
    if "dbpia" in link.lower():
        return "DBpia"
    if link:
        return "Paper"
    return "Public metadata"


def normalize_phrase(text: str) -> str:
    phrase = text.strip().rstrip(".")
    if re.match(r"^(A|An|The)\s", phrase):
        return phrase[0].lower() + phrase[1:]
    if len(phrase) > 1 and phrase[0].isupper() and phrase[1].islower():
        return phrase[0].lower() + phrase[1:]
    return phrase


def lower_phrase(text: str) -> str:
    if ": " in text:
        head, tail = text.split(": ", 1)
        if len(head.split()) <= 3:
            return normalize_phrase(tail)
    return normalize_phrase(text)


def briefing_summary(entry: dict[str, str | int]) -> str:
    tag = str(entry["tag"])
    if tag in CURATED_SUMMARIES:
        return CURATED_SUMMARIES[tag]

    title = str(entry["title"])
    venue = str(entry["venue"])
    label = str(entry["type"]).lower()
    domain_line = DOMAIN_LINES[str(entry["domain"])]
    title_lower = title.lower()
    focus = lower_phrase(title)

    if title_lower.startswith("correction to:"):
        corrected = focus
        return (
            f"This {label} records an official correction linked to {corrected}. "
            f"It preserves the accuracy of the published record within the {domain_line} research line."
        )

    if "withdrawn" in venue.lower():
        return (
            f"This {label} documents a public research submission on {title}. "
            f"It remains part of the {domain_line} publication trajectory as a visible research trace."
        )

    if "systematic literature review" in title_lower:
        return (
            f"This {label} synthesizes the literature around {focus}. "
            f"It broadens the {domain_line} research line by clarifying methods, themes, and open questions."
        )

    if any(
        keyword in title_lower
        for keyword in [
            "model",
            "modeling",
            "analysis",
            "evaluation",
            "quantification",
            "performability",
            "availability",
            "sensitivity",
            "survey",
        ]
    ):
        return (
            f"This {label} presents a model-driven contribution within the {domain_line} research line. "
            "It frames the publication as a quantitative milestone rather than a purely descriptive record."
        )

    if any(keyword in title_lower for keyword in ["framework", "architecture", "platform", "system"]):
        return (
            f"This {label} presents a structured system or framework contribution within the {domain_line} research line. "
            "It emphasizes a design-oriented research artifact that can be compared with later work."
        )

    return (
        f"This {label} adds a clearly documented contribution to the {domain_line} research line. "
        "The official publication record below anchors the entry in the broader archive."
    )


def contribution_points(entry: dict[str, str | int]) -> list[str]:
    title = str(entry["title"])
    title_lower = title.lower()
    venue_lower = str(entry["venue"]).lower()
    focus = lower_phrase(title)
    domain = str(entry["domain"])

    if title_lower.startswith("correction to:"):
        return [
            "Makes the corrected scholarly record explicit instead of leaving the update hidden in citation metadata.",
            "Keeps later readers connected to the most accurate version of the underlying technical study.",
        ]

    if "withdrawn" in venue_lower:
        return [
            "Preserves a transparent public trace of the submitted research idea and its technical direction.",
            "Keeps the submission visible as part of the evolution of the broader research portfolio.",
        ]

    if "systematic literature review" in title_lower:
        return [
            f"Maps the state of the literature around {focus}, turning scattered papers into a clearer research landscape.",
            "Identifies recurring methods, open questions, and comparison points that can guide follow-up studies.",
        ]

    points: list[str] = []

    if any(keyword in title_lower for keyword in ["stochastic", "markov", "queue", "petri", "reward net"]):
        points.append(
            "Uses formal stochastic or queueing models to connect architecture choices with measurable system behavior."
        )
    elif any(
        keyword in title_lower
        for keyword in ["model", "modeling", "analysis", "evaluation", "quantification", "performability", "sensitivity"]
    ):
        points.append(
            "Turns the paper's central system question into a quantitative study, so performance, reliability, cost, or availability can be compared."
        )

    if any(keyword in title_lower for keyword in ["framework", "architecture", "platform", "system"]):
        points.append(
            "Packages the work as a structured system artifact rather than only an isolated experiment."
        )

    if any(keyword in title_lower for keyword in ["reinforcement", "navigation", "robot", "vision", "language model", "deep learning"]):
        points.append(
            "Frames AI behavior as an end-to-end autonomy problem that joins perception, decision making, and deployment constraints."
        )

    if any(keyword in title_lower for keyword in ["digital twin", "uam", "aam", "evtol", "flight", "aerodynamic", "airfoil", "uav"]):
        points.append(
            "Connects simulation, flight behavior, and operational evidence so aerospace-oriented systems can be studied before deployment."
        )

    if any(keyword in title_lower for keyword in ["iot", "sensor", "surveillance", "medical", "smart", "fog"]):
        points.append(
            "Links sensing infrastructure to concrete operating metrics such as latency, capacity, utilization, and service continuity."
        )

    if not points:
        domain_line = DOMAIN_LINES[domain]
        points.append(
            f"Adds a publication milestone to the {domain_line} line with a clearly documented technical focus."
        )

    if len(points) == 1:
        points.append(
            "Provides a reusable reference point for comparing later methods, systems, or deployment scenarios."
        )

    return points[:2]


def impact_points(entry: dict[str, str | int]) -> list[str]:
    title = str(entry["title"])
    title_lower = title.lower()
    venue_lower = str(entry["venue"]).lower()
    domain = str(entry["domain"])

    if title_lower.startswith("correction to:"):
        return [
            "Protects citation clarity for readers who depend on the paper as a modeling or evaluation reference.",
            "Signals that the News archive tracks the integrity of the research record, not only new releases.",
        ]

    if "withdrawn" in venue_lower:
        return [
            "Shows the research trajectory honestly while separating a submission record from an accepted publication.",
            "Gives future collaborators enough context to understand where the idea sat in the publication timeline.",
        ]

    if "systematic literature review" in title_lower:
        return [
            "Helps new researchers enter the area faster by surfacing the field's recurring assumptions and gaps.",
            "Creates a stronger foundation for selecting benchmarks, methods, and evaluation criteria in later work.",
        ]

    points: list[str] = []

    if any(keyword in title_lower for keyword in ["availability", "dependability", "reliability", "survivability", "disaster"]):
        points.append(
            "Supports pre-deployment design decisions for systems where downtime, failure recovery, and service loss carry real cost."
        )

    if any(keyword in title_lower for keyword in ["energy", "power", "green", "cost", "resource", "utilization"]):
        points.append(
            "Makes efficiency trade-offs visible, helping operators balance service quality with resource use and sustainability."
        )

    if any(keyword in title_lower for keyword in ["blockchain", "hyperledger", "sdn", "cloud", "microservice", "storage", "kubernetes"]):
        points.append(
            "Gives infrastructure teams a clearer way to tune configuration choices before they become expensive production incidents."
        )

    if any(keyword in title_lower for keyword in ["iot", "medical", "surveillance", "smart city", "smart building", "sensor"]):
        points.append(
            "Turns cyber-physical monitoring into an engineering problem that can be sized, stress-tested, and maintained deliberately."
        )

    if any(keyword in title_lower for keyword in ["reinforcement", "navigation", "robot", "vision", "language model", "deep learning"]):
        points.append(
            "Moves intelligent autonomy closer to real operating conditions where robustness matters more than benchmark elegance."
        )

    if any(keyword in title_lower for keyword in ["digital twin", "uam", "aam", "evtol", "flight", "aerodynamic", "airship", "satellite", "uav"]):
        points.append(
            "Strengthens the bridge between virtual experimentation and safety-aware aerospace or mobility operations."
        )

    if not points:
        points.append(
            f"Broadens the {DOMAIN_BADGES[domain]} publication narrative with a documented result readers can trace to the official record."
        )

    if len(points) == 1:
        points.append(
            "Adds continuity to the News archive by giving older records the same interpretive context as recent publications."
        )

    return points[:2]


def format_date(value: str) -> str:
    return datetime.strptime(value, "%Y-%m-%d").strftime("%B %-d, %Y")


def safe_id(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "-", value).strip("-")
    return cleaned or "publication"


def card_classes(entry: dict[str, str | int]) -> str:
    classes = ["publication-news-card", "publication-news-card--story", "publication-news-card--feature"]
    classes.append(DOMAIN_VISUAL_CLASSES[str(entry["domain"])])
    classes.append(TYPE_VISUAL_CLASSES.get(str(entry["type"]), "publication-news-card--record"))
    return " ".join(classes)


def metric_values(entry: dict[str, str | int], count: int = 8) -> list[int]:
    seed_text = f"{entry['tag']} {entry['date']} {entry['title']}"
    seed = sum((idx + 1) * ord(char) for idx, char in enumerate(seed_text))
    return [28 + ((seed // (idx + 3) + idx * 17) % 54) for idx in range(count)]


def visual_labels(entry: dict[str, str | int]) -> list[str]:
    text = f"{entry['title']} {entry['venue']}".lower()
    labels: list[str] = []

    for keyword, label in VISUAL_KEYWORDS:
        if keyword in text and label not in labels:
            labels.append(label)
        if len(labels) == 2:
            break

    domain_label = DOMAIN_VISUAL_LABELS[str(entry["domain"])]
    if domain_label not in labels:
        labels.append(domain_label)

    type_label_short = {
        "Journal article": "Journal",
        "Conference paper": "Conference",
        "Preprint": "Preprint",
        "Book chapter": "Book",
        "Submission record": "Submission",
        "Publication record": "Record",
    }.get(str(entry["type"]), "Record")
    if type_label_short not in labels:
        labels.append(type_label_short)

    return labels[:3]


def visual_caption(entry: dict[str, str | int]) -> str:
    labels = ", ".join(visual_labels(entry))
    domain_caption = DOMAIN_CAPTIONS[str(entry["domain"])]
    return f"Scientific illustration: {domain_caption} Visual cues: {labels}."


def render_metric_trace(values: list[int]) -> str:
    point_step = 40
    points = []
    bars = []

    for idx, value in enumerate(values):
        x = 42 + idx * point_step
        y = 210 - value
        points.append(f"{x},{y}")
        bar_height = 22 + value * 0.46
        bars.append(
            f'<rect class="publication-news-visual__bar" x="{x - 5:.1f}" '
            f'y="{218 - bar_height:.1f}" width="10" height="{bar_height:.1f}" rx="5" />'
        )

    circles = "\n".join(
        f'<circle class="publication-news-visual__dot" cx="{42 + idx * point_step}" '
        f'cy="{210 - value}" r="4.5" />'
        for idx, value in enumerate(values)
    )

    return "\n".join(
        [
            '<g class="publication-news-visual__metrics" aria-hidden="true">',
            *bars,
            f'  <polyline class="publication-news-visual__trace" points="{" ".join(points)}" />',
            circles,
            "</g>",
        ]
    )


def render_visual_chips(labels: list[str]) -> str:
    chip_lines = []
    for idx, label in enumerate(labels):
        x = 30 + idx * 124
        chip_lines.extend(
            [
                f'<rect class="publication-news-visual__chip-bg" x="{x}" y="224" width="112" height="24" rx="12" />',
                f'<text class="publication-news-visual__chip" x="{x + 56}" y="240" text-anchor="middle">{escape(label)}</text>',
            ]
        )
    return "\n".join(chip_lines)


def render_ai_motif() -> str:
    nodes = [(78, 78), (132, 54), (152, 122), (218, 82), (286, 64), (326, 130)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5)]
    edge_lines = "\n".join(
        f'<line class="publication-news-visual__line publication-news-visual__line--soft" '
        f'x1="{nodes[start][0]}" y1="{nodes[start][1]}" x2="{nodes[end][0]}" y2="{nodes[end][1]}" />'
        for start, end in edges
    )
    node_lines = "\n".join(
        f'<circle class="publication-news-visual__node" cx="{x}" cy="{y}" r="{7 + idx % 3}" />'
        for idx, (x, y) in enumerate(nodes)
    )
    return "\n".join(
        [
            '<path class="publication-news-visual__halo" d="M48 124 C86 28, 202 20, 250 78 C298 136, 360 88, 374 156 C326 184, 238 168, 162 178 C94 188, 52 168, 48 124Z" />',
            edge_lines,
            node_lines,
            '<path class="publication-news-visual__line" d="M64 160 C104 132, 126 164, 164 140 S236 108, 274 140 S326 172, 360 132" />',
            '<path class="publication-news-visual__line publication-news-visual__line--accent2" d="M282 164 q30 -54 60 0 M296 164 q16 -30 32 0" />',
        ]
    )


def render_infra_motif() -> str:
    return "\n".join(
        [
            '<path class="publication-news-visual__halo" d="M70 116 C62 82, 94 62, 126 74 C142 46, 190 48, 204 82 C242 74, 272 96, 266 128 C258 160, 210 158, 174 154 C130 150, 80 152, 70 116Z" />',
            '<rect class="publication-news-visual__panel" x="70" y="134" width="86" height="76" rx="14" />',
            '<rect class="publication-news-visual__panel" x="174" y="116" width="86" height="94" rx="14" />',
            '<rect class="publication-news-visual__panel" x="278" y="142" width="72" height="68" rx="14" />',
            '<line class="publication-news-visual__line" x1="156" y1="172" x2="174" y2="162" />',
            '<line class="publication-news-visual__line" x1="260" y1="162" x2="278" y2="176" />',
            '<circle class="publication-news-visual__node" cx="104" cy="158" r="5" />',
            '<circle class="publication-news-visual__node" cx="126" cy="158" r="5" />',
            '<circle class="publication-news-visual__node" cx="208" cy="142" r="5" />',
            '<circle class="publication-news-visual__node" cx="230" cy="142" r="5" />',
            '<circle class="publication-news-visual__node" cx="312" cy="166" r="5" />',
            '<path class="publication-news-visual__line publication-news-visual__line--accent2" d="M88 190 H136 M192 190 H242 M294 190 H336" />',
        ]
    )


def render_iot_motif() -> str:
    return "\n".join(
        [
            '<rect class="publication-news-visual__panel" x="56" y="146" width="52" height="64" rx="10" />',
            '<rect class="publication-news-visual__panel" x="126" y="122" width="58" height="88" rx="10" />',
            '<rect class="publication-news-visual__panel" x="206" y="136" width="48" height="74" rx="10" />',
            '<rect class="publication-news-visual__panel" x="276" y="112" width="68" height="98" rx="10" />',
            '<path class="publication-news-visual__line" d="M82 128 q36 -54 72 0 M96 128 q22 -32 44 0" />',
            '<path class="publication-news-visual__line publication-news-visual__line--accent2" d="M232 118 q42 -64 84 0 M250 118 q24 -36 48 0" />',
            '<circle class="publication-news-visual__node" cx="82" cy="124" r="7" />',
            '<circle class="publication-news-visual__node" cx="232" cy="114" r="7" />',
            '<line class="publication-news-visual__line publication-news-visual__line--soft" x1="82" y1="124" x2="232" y2="114" />',
            '<line class="publication-news-visual__line publication-news-visual__line--soft" x1="232" y1="114" x2="312" y2="104" />',
            '<circle class="publication-news-visual__halo" cx="312" cy="104" r="28" />',
        ]
    )


def render_twin_motif() -> str:
    return "\n".join(
        [
            '<path class="publication-news-visual__halo" d="M64 124 C118 54, 266 42, 346 112 C312 184, 160 196, 64 124Z" />',
            '<path class="publication-news-visual__line publication-news-visual__line--soft" d="M84 150 C138 102, 236 96, 330 146" />',
            '<path class="publication-news-visual__aircraft" d="M92 130 L190 108 L318 134 L196 146 Z" />',
            '<line class="publication-news-visual__line" x1="196" y1="146" x2="176" y2="178" />',
            '<line class="publication-news-visual__line" x1="196" y1="146" x2="228" y2="176" />',
            '<circle class="publication-news-visual__rotor" cx="116" cy="126" r="20" />',
            '<circle class="publication-news-visual__rotor" cx="302" cy="132" r="20" />',
            '<circle class="publication-news-visual__node" cx="156" cy="76" r="9" />',
            '<circle class="publication-news-visual__node" cx="264" cy="74" r="9" />',
            '<line class="publication-news-visual__line publication-news-visual__line--accent2" x1="156" y1="76" x2="264" y2="74" />',
        ]
    )


def render_aero_motif() -> str:
    return "\n".join(
        [
            '<path class="publication-news-visual__halo" d="M42 142 C116 82, 248 72, 372 116 C284 168, 146 188, 42 142Z" />',
            '<path class="publication-news-visual__airfoil" d="M58 138 C130 104, 252 92, 362 122 C250 134, 130 162, 58 138Z" />',
            '<path class="publication-news-visual__line publication-news-visual__line--soft" d="M48 92 C142 72, 232 72, 356 88" />',
            '<path class="publication-news-visual__line publication-news-visual__line--soft" d="M46 176 C144 196, 252 188, 360 160" />',
            '<rect class="publication-news-visual__panel" x="278" y="56" width="44" height="34" rx="8" />',
            '<line class="publication-news-visual__line" x1="300" y1="90" x2="330" y2="118" />',
            '<line class="publication-news-visual__line publication-news-visual__line--accent2" x1="268" y1="72" x2="240" y2="62" />',
            '<line class="publication-news-visual__line publication-news-visual__line--accent2" x1="328" y1="72" x2="356" y2="62" />',
            '<circle class="publication-news-visual__node" cx="330" cy="118" r="7" />',
        ]
    )


def render_domain_motif(domain: str) -> str:
    if domain == "Domain 1":
        return render_ai_motif()
    if domain == "Domain 2":
        return render_infra_motif()
    if domain == "Domain 3":
        return render_iot_motif()
    if domain == "Domain 4":
        return render_twin_motif()
    return render_aero_motif()


def render_visual(entry: dict[str, str | int]) -> str:
    tag = str(entry["tag"])
    title = str(entry["title"])
    sid = safe_id(tag)
    gradient_id = f"pub-grad-{sid}"
    pattern_id = f"pub-grid-{sid}"
    values = metric_values(entry)
    labels = visual_labels(entry)
    year = str(entry["date"])[:4]

    return "\n".join(
        [
            f'<div class="publication-news-card__visual" role="img" aria-label="Scientific illustration for {escape(title, quote=True)}">',
            '  <svg class="publication-news-illustration" viewBox="0 0 420 260" preserveAspectRatio="xMidYMid meet" focusable="false" aria-hidden="true">',
            "    <defs>",
            f'      <linearGradient id="{gradient_id}" x1="0" y1="0" x2="1" y2="1">',
            '        <stop offset="0%" stop-color="var(--pub-wash)" />',
            '        <stop offset="58%" stop-color="#ffffff" />',
            '        <stop offset="100%" stop-color="var(--pub-wash-2)" />',
            "      </linearGradient>",
            f'      <pattern id="{pattern_id}" width="26" height="26" patternUnits="userSpaceOnUse">',
            '        <path class="publication-news-visual__grid" d="M26 0H0V26" />',
            "      </pattern>",
            "    </defs>",
            f'    <rect width="420" height="260" rx="28" fill="url(#{gradient_id})" />',
            f'    <rect width="420" height="260" rx="28" fill="url(#{pattern_id})" />',
            '    <path class="publication-news-visual__ribbon" d="M0 210 C84 180, 136 232, 214 202 C298 170, 332 204, 420 172 V260 H0Z" />',
            f'    <text class="publication-news-visual__tag" x="30" y="52">{escape(tag)}</text>',
            f'    <text class="publication-news-visual__year" x="390" y="52" text-anchor="end">{escape(year)}</text>',
            render_domain_motif(str(entry["domain"])),
            render_metric_trace(values),
            render_visual_chips(labels),
            "  </svg>",
            "</div>",
        ]
    )


def find_best_link(line: str, tag: str) -> tuple[str, str]:
    if tag in SPECIAL_LINKS:
        special = SPECIAL_LINKS[tag]
        return special["url"], special["label"]

    for label, url in LINK_RE.findall(line):
        label_lower = label.lower()
        if label_lower.startswith("doi:"):
            return url, "DOI record"
        if "openreview.net/forum?id=" in label_lower:
            return url, "OpenReview record"
        if label == "DBpia":
            return url, "DBpia record"
        if label == "paper":
            return url, "Paper link"

    return "", ""


def parse_entries(markdown: str) -> list[dict[str, str | int]]:
    entries: list[dict[str, str | int]] = []
    domain = ""

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        for prefix, value in DOMAIN_HEADINGS.items():
            if line.startswith(prefix):
                domain = value
                break

        if not re.match(r"^\d+\.\s", line):
            continue

        idx_match = re.match(r"^(\d+)\.", line)
        title_match = TITLE_RE.search(line)
        date_match = DATE_RE.search(line)
        tag_match = TAG_RE.search(line)

        if not idx_match or not title_match or not date_match or not tag_match or not domain:
            continue

        idx = int(idx_match.group(1))
        tag = tag_match.group(1)
        title = title_match.group(1).strip().rstrip(".")
        date = date_match.group(1)

        rest = line[title_match.end():]
        rest = re.sub(r"\s*\[[^\]]+\]\([^)]+\)", "", rest)
        rest = re.sub(r"\s*\[[^\]]+\](?=\s|$)", "", rest)
        rest = re.sub(r"\s*\[\d{4}-\d{2}-\d{2}\]\s*$", "", rest)
        rest = re.sub(r"^[.\s]+", "", rest).strip()

        if rest.startswith("In: "):
            rest = rest[4:]
        elif rest.startswith("In "):
            rest = rest[3:]

        link, link_label = find_best_link(line, tag)
        venue = clean_venue(rest, link)

        entry: dict[str, str | int] = {
            "idx": idx,
            "tag": tag,
            "date": date,
            "title": title,
            "venue": venue,
            "link": link,
            "link_label": link_label,
            "type": "",
            "domain": domain,
            "domain_badge": DOMAIN_BADGES[domain],
        }

        entry["type"] = type_label(tag, venue, link)
        entry["source_badge"] = source_badge(entry)
        entry["summary"] = briefing_summary(entry)
        entries.append(entry)

    entries.sort(key=lambda item: (str(item["date"]), int(item["idx"])), reverse=True)
    return entries


def render(entries: list[dict[str, str | int]]) -> str:
    by_year: dict[str, list[dict[str, str | int]]] = defaultdict(list)
    source_counts: Counter[str] = Counter()

    for entry in entries:
        year = str(entry["date"])[:4]
        by_year[year].append(entry)
        source_counts[str(entry["source_badge"])] += 1

    years = sorted(by_year.keys(), reverse=True)
    min_year = min(years)
    max_year = max(years)
    source_summary = ", ".join(
        f"{source} {count}" for source, count in sorted(source_counts.items())
    )
    html_lines = [
        "<div class=\"publication-news-root\">",
        "  <div class=\"publication-news-overview\">",
        f"    <p><strong>Coverage:</strong> {len(entries)} publications from {min_year} to {max_year}, sorted from most recent to earliest and excluding manuscripts under review.</p>",
        "    <p><strong>Archive note:</strong> This visual briefing archive turns the Publications page metadata and official publication links into illustrated research stories that remain readable without client-side rendering.</p>",
        "    <p><strong>Narrative format:</strong> Each publication story block pairs a large scientific illustration with concise contribution and impact notes derived from the publication domain, type, date, and technical keywords.</p>",
        f"    <p><strong>Source mix:</strong> {escape(source_summary)}.</p>",
        "  </div>",
    ]

    for year in years:
        html_lines.append(f"  <h2>{escape(year)}</h2>")
        html_lines.append("  <div class=\"publication-news-list\">")
        for entry in by_year[year]:
            html_lines.extend(render_card(entry, "    "))
        html_lines.append("  </div>")

    html_lines.append("</div>")
    return "\n".join(html_lines) + "\n"


def render_card(entry: dict[str, str | int], indent: str) -> list[str]:
    inner = indent + "  "
    body = inner + "  "
    badge_indent = body + "  "
    figure = body + "  "
    contributes_items = "".join(
        f"<li>{escape(point)}</li>" for point in contribution_points(entry)
    )
    matters_items = "".join(
        f"<li>{escape(point)}</li>" for point in impact_points(entry)
    )
    lines = [
        f"{indent}<article class=\"{card_classes(entry)}\">",
        f"{inner}<div class=\"publication-news-card__body\">",
        f"{body}<div class=\"publication-news-card__top\">",
        f"{badge_indent}<span class=\"publication-news-badge publication-news-badge--date\">{escape(format_date(str(entry['date'])))}</span>",
        f"{badge_indent}<span class=\"publication-news-badge\">{escape(str(entry['tag']))}</span>",
        f"{badge_indent}<span class=\"publication-news-badge\">{escape(str(entry['type']))}</span>",
        f"{badge_indent}<span class=\"publication-news-badge\">{escape(str(entry['domain_badge']))}</span>",
        f"{badge_indent}<span class=\"publication-news-badge\">{escape(str(entry['source_badge']))}</span>",
        f"{body}</div>",
        f"{body}<h3>{escape(str(entry['title']))}</h3>",
        f"{body}<p>{escape(str(entry['summary']))}</p>",
        f"{body}<figure class=\"publication-news-card__figure\">",
        *[f"{figure}{line}" for line in render_visual(entry).splitlines()],
        f"{figure}<figcaption>{escape(visual_caption(entry))}</figcaption>",
        f"{body}</figure>",
        f"{body}<div class=\"publication-news-card__story\">",
        f"{badge_indent}<section class=\"publication-news-card__section\">",
        f"{badge_indent}  <h4>What the paper contributes</h4>",
        f"{badge_indent}  <ul>{contributes_items}</ul>",
        f"{badge_indent}</section>",
        f"{badge_indent}<section class=\"publication-news-card__section\">",
        f"{badge_indent}  <h4>Why it matters</h4>",
        f"{badge_indent}  <ul>{matters_items}</ul>",
        f"{badge_indent}</section>",
        f"{body}</div>",
        f"{body}<div class=\"publication-news-card__record\">",
        f"{badge_indent}<p><strong>Publication record:</strong>&nbsp;<em>{escape(str(entry['venue']))}</em>.</p>",
    ]

    if entry["link"]:
        lines.append(
            f"{badge_indent}<p class=\"publication-news-card__links\"><a href=\"{escape(str(entry['link']), quote=True)}\">{escape(str(entry['link_label']) or 'Official record')}</a></p>"
        )

    lines.append(f"{body}</div>")
    lines.append(f"{inner}</div>")
    lines.append(f"{indent}</article>")
    return lines


def render_2025(entries: list[dict[str, str | int]]) -> str:
    focused = [entry for entry in entries if str(entry["date"]).startswith("2025-")]
    source_counts: Counter[str] = Counter(str(entry["source_badge"]) for entry in focused)
    source_summary = ", ".join(
        f"{source} {count}" for source, count in sorted(source_counts.items())
    )
    newest = format_date(str(focused[0]["date"]))
    oldest = format_date(str(focused[-1]["date"]))

    html_lines = [
        "<div class=\"publication-news-root\">",
        "  <div class=\"publication-news-overview\">",
        f"    <p><strong>Coverage:</strong> {len(focused)} publications released in 2025, sorted from most recent to earliest ({newest} to {oldest}).</p>",
        "    <p><strong>2025 note:</strong> These publication story blocks were written against official DOI or publisher records, arXiv abstracts, and official conference proceedings or accepted-paper listings when those are the primary public traces.</p>",
        "    <p><strong>Narrative format:</strong> Each publication story block pairs a large scientific illustration with concise contribution and impact notes derived from the publication domain, type, date, and technical keywords.</p>",
        f"    <p><strong>Source mix:</strong> {escape(source_summary)}.</p>",
        "  </div>",
        "  <div class=\"publication-news-list\">",
    ]

    for entry in focused:
        html_lines.extend(render_card(entry, "    "))

    html_lines.extend(
        [
            "  </div>",
            "</div>",
        ]
    )
    return "\n".join(html_lines) + "\n"


def render_missing(entries: list[dict[str, str | int]]) -> str:
    missing = [
        entry for entry in entries if str(entry["tag"]) not in NEWS_DEDICATED_TAGS
    ]
    by_year: dict[str, list[dict[str, str | int]]] = defaultdict(list)
    source_counts: Counter[str] = Counter(str(entry["source_badge"]) for entry in missing)
    domain_counts: Counter[str] = Counter(str(entry["domain_badge"]) for entry in missing)

    for entry in missing:
        by_year[str(entry["date"])[:4]].append(entry)

    years = sorted(by_year.keys(), reverse=True)
    source_summary = ", ".join(
        f"{source} {count}" for source, count in sorted(source_counts.items())
    )
    domain_summary = ", ".join(
        f"{domain} {count}" for domain, count in sorted(domain_counts.items())
    )
    html_lines = [
        "<div class=\"publication-news-root publication-news-root--missing\">",
        "  <div class=\"publication-news-overview\">",
        f"    <p><strong>Coverage:</strong> {len(missing)} publication records from the Publications page that do not yet have a dedicated long-form News entry.</p>",
        "    <p><strong>Scope:</strong> This section focuses on publication records not already represented by the detailed News stories above, including recent journal articles, MetaCom 2025 papers, AAM-VDT, SHANGUS/FH-DRL, NOMS 2024, and the UAV delivery study.</p>",
        "    <p><strong>Narrative format:</strong> Each publication story block pairs a large scientific illustration with concise contribution and impact notes derived from the publication domain, type, date, and technical keywords.</p>",
        f"    <p><strong>Domain mix:</strong> {escape(domain_summary)}.</p>",
        f"    <p><strong>Source mix:</strong> {escape(source_summary)}.</p>",
        "  </div>",
    ]

    for year in years:
        html_lines.append(f"  <h3>{escape(year)}</h3>")
        html_lines.append("  <div class=\"publication-news-list\">")
        for entry in by_year[year]:
            html_lines.extend(render_card(entry, "    "))
        html_lines.append("  </div>")

    html_lines.append("</div>")
    return "\n".join(html_lines) + "\n"


def main() -> None:
    markdown = PUBLICATIONS_PATH.read_text(encoding="utf-8")
    entries = parse_entries(markdown)
    OUTPUT_PATH.write_text(render(entries), encoding="utf-8")
    OUTPUT_2025_PATH.write_text(render_2025(entries), encoding="utf-8")
    OUTPUT_MISSING_PATH.write_text(render_missing(entries), encoding="utf-8")
    print(f"Wrote {len(entries)} publication story blocks to {OUTPUT_PATH}")
    print(f"Wrote 2025 publication story blocks to {OUTPUT_2025_PATH}")
    missing_count = sum(1 for entry in entries if str(entry["tag"]) not in NEWS_DEDICATED_TAGS)
    print(f"Wrote {missing_count} missing-publication story blocks to {OUTPUT_MISSING_PATH}")


if __name__ == "__main__":
    main()
