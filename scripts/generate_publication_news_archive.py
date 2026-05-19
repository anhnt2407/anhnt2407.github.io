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
    "J42",
    "C38",
    "C50",
    "C49",
    "P05",
    "J38",
    "J30",
    "J35",
    "J34",
    "J43",
    "J37",
    "J36",
    "C37",
    "J33",
    "J31",
    "C47",
    "C48",
    "P07",
    "C35",
    "C40",
    "J29",
    "C32",
    "C30",
    "C29",
    "C31",
    "C34",
    "C33",
    "C28",
    "J28",
    "J27",
    "J32",
    "C27",
    "C22",
    "C23",
    "J26",
    "J25",
    "C26",
    "C20",
    "C18",
    "C19",
    "J24",
    "J23",
    "C25",
    "J22",
    "C24",
    "J21",
    "J17",
    "J19",
    "J18",
    "C21",
    "J20",
    "J13",
    "J16",
    "C17",
    "C16",
    "J15",
    "J14",
    "J12",
    "C15",
    "J10",
    "J09",
    "J08",
    "J11",
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


def visual_seed(entry: dict[str, str | int]) -> int:
    seed_text = f"{entry['tag']} {entry['date']} {entry['title']} {entry['venue']}"
    return sum((idx + 1) * ord(char) for idx, char in enumerate(seed_text))


def entry_text(entry: dict[str, str | int]) -> str:
    return f"{entry['title']} {entry['venue']} {entry['domain_badge']}".lower()


def render_visual_particles(entry: dict[str, str | int]) -> str:
    seed = visual_seed(entry)
    particles = []
    for idx in range(22):
        x = 64 + ((seed // (idx + 3) + idx * 83) % 1072)
        y = 48 + ((seed // (idx + 7) + idx * 47) % 390)
        radius = 2.0 + ((seed + idx * 19) % 24) / 10
        opacity = 0.18 + ((seed + idx * 13) % 30) / 100
        particles.append(
            f'<circle class="publication-news-visual__spark" cx="{x}" cy="{y}" r="{radius:.1f}" opacity="{opacity:.2f}" />'
        )
    return "\n".join(particles)


def render_visual_constellation(entry: dict[str, str | int]) -> str:
    values = metric_values(entry, 7)
    nodes = []
    for idx, value in enumerate(values):
        x = 134 + idx * 154
        y = 214 + ((value * 5 + idx * 37) % 132)
        nodes.append((x, y))

    lines = "\n".join(
        f'<line class="publication-news-visual__mesh-line" x1="{nodes[idx][0]}" y1="{nodes[idx][1]}" x2="{nodes[idx + 1][0]}" y2="{nodes[idx + 1][1]}" />'
        for idx in range(len(nodes) - 1)
    )
    dots = "\n".join(
        f'<circle class="publication-news-visual__mesh-node" cx="{x}" cy="{y}" r="{5 + idx % 3}" />'
        for idx, (x, y) in enumerate(nodes)
    )
    return "\n".join(
        [
            '<g class="publication-news-visual__mesh" aria-hidden="true">',
            lines,
            dots,
            "</g>",
        ]
    )


def render_cinematic_infrastructure(entry: dict[str, str | int]) -> str:
    seed = visual_seed(entry)
    rack_specs = [
        (92, 390, 142, 110),
        (268, 326, 132, 104),
        (500, 354, 158, 120),
        (858, 364, 146, 112),
        (1016, 412, 126, 96),
    ]
    racks = []
    for idx, (x, y, width, height) in enumerate(rack_specs):
        rack_shift = (seed // (idx + 5)) % 18
        rx = x + rack_shift
        racks.extend(
            [
                f'<g class="publication-news-visual__rack" transform="translate({rx} {y})">',
                f'  <rect class="publication-news-visual__rack-shell" x="0" y="0" width="{width}" height="{height}" rx="18" />',
                f'  <rect class="publication-news-visual__rack-face" x="{width * 0.18:.1f}" y="18" width="{width * 0.36:.1f}" height="{height - 34}" rx="8" />',
                f'  <rect class="publication-news-visual__rack-face publication-news-visual__rack-face--warm" x="{width * 0.6:.1f}" y="20" width="{width * 0.22:.1f}" height="{height - 42}" rx="7" />',
                f'  <line class="publication-news-visual__rack-slot" x1="{width * 0.24:.1f}" y1="38" x2="{width * 0.47:.1f}" y2="38" />',
                f'  <line class="publication-news-visual__rack-slot" x1="{width * 0.24:.1f}" y1="58" x2="{width * 0.47:.1f}" y2="58" />',
                f'  <line class="publication-news-visual__rack-slot" x1="{width * 0.24:.1f}" y1="78" x2="{width * 0.47:.1f}" y2="78" />',
                f'  <circle class="publication-news-visual__server-light" cx="{width * 0.72:.1f}" cy="42" r="5" />',
                f'  <circle class="publication-news-visual__server-light publication-news-visual__server-light--blue" cx="{width * 0.72:.1f}" cy="66" r="5" />',
                "</g>",
            ]
        )

    cubes = []
    for idx, (x, y) in enumerate([(300, 260), (438, 206), (578, 238), (710, 194), (816, 252)]):
        hue_class = " publication-news-visual__data-cube--warm" if idx == 0 else ""
        cubes.extend(
            [
                f'<g class="publication-news-visual__data-cube{hue_class}" transform="translate({x} {y})">',
                '  <rect class="publication-news-visual__data-cube-face" x="0" y="0" width="68" height="52" rx="8" />',
                '  <path class="publication-news-visual__data-cube-edge" d="M0 0 L18 -14 H86 L68 0 Z" />',
                '  <path class="publication-news-visual__data-cube-edge" d="M68 0 L86 -14 V38 L68 52 Z" />',
                "</g>",
            ]
        )

    return "\n".join(
        [
            '<g class="publication-news-visual__infrastructure" aria-hidden="true">',
            '<path class="publication-news-visual__map-line" d="M38 520 C210 420, 382 536, 530 430 S806 348, 1140 420" />',
            '<path class="publication-news-visual__map-line publication-news-visual__map-line--thin" d="M96 476 H1076 M172 430 H1134 M240 384 H1048" />',
            '<path class="publication-news-visual__map-line publication-news-visual__map-line--thin" d="M188 330 V610 M356 292 V640 M554 286 V620 M760 272 V616 M984 314 V640" />',
            *racks,
            '<path class="publication-news-visual__transfer-arc" d="M300 320 C426 168, 660 156, 828 318" />',
            '<path class="publication-news-visual__transfer-arc publication-news-visual__transfer-arc--warm" d="M328 334 C446 218, 632 210, 794 334" />',
            *cubes,
            '<circle class="publication-news-visual__map-node" cx="196" cy="476" r="8" />',
            '<circle class="publication-news-visual__map-node publication-news-visual__map-node--warm" cx="468" cy="432" r="8" />',
            '<circle class="publication-news-visual__map-node" cx="756" cy="376" r="8" />',
            '<circle class="publication-news-visual__map-node publication-news-visual__map-node--warm" cx="1030" cy="420" r="8" />',
            "</g>",
        ]
    )


def render_metric_trace(values: list[int]) -> str:
    point_step = 48
    points = []
    bars = []

    for idx, value in enumerate(values):
        x = 44 + idx * point_step
        y = 148 - value * 0.86
        points.append(f"{x:.1f},{y:.1f}")
        bar_height = 26 + value * 0.86
        bars.append(
            f'<rect class="publication-news-visual__bar" x="{x - 7:.1f}" y="{176 - bar_height:.1f}" width="14" height="{bar_height:.1f}" rx="7" />'
        )

    circles = "\n".join(
        f'<circle class="publication-news-visual__dot" cx="{44 + idx * point_step:.1f}" cy="{148 - value * 0.86:.1f}" r="5.6" />'
        for idx, value in enumerate(values)
    )

    return "\n".join(
        [
            '<g class="publication-news-visual__metrics" transform="translate(728 322)" aria-hidden="true">',
            '  <rect class="publication-news-visual__screen" x="0" y="0" width="406" height="222" rx="28" />',
            '  <text class="publication-news-visual__small-label" x="34" y="42">system evidence</text>',
            *bars,
            f'  <polyline class="publication-news-visual__trace" points="{" ".join(points)}" />',
            circles,
            "</g>",
        ]
    )


def render_visual_chips(labels: list[str]) -> str:
    chip_lines = ['<g class="publication-news-visual__chips" aria-hidden="true">']
    for idx, label in enumerate(labels):
        x = 72 + idx * 198
        chip_lines.extend(
            [
                f'<rect class="publication-news-visual__chip-bg" x="{x}" y="586" width="176" height="42" rx="21" />',
                f'<text class="publication-news-visual__chip" x="{x + 88}" y="613" text-anchor="middle">{escape(label)}</text>',
            ]
        )
    chip_lines.append("</g>")
    return "\n".join(chip_lines)


def render_ai_motif() -> str:
    nodes = [(150, 154), (250, 96), (322, 204), (454, 128), (586, 112), (678, 212)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5)]
    edge_lines = "\n".join(
        f'<line class="publication-news-visual__line publication-news-visual__line--soft" x1="{nodes[start][0]}" y1="{nodes[start][1]}" x2="{nodes[end][0]}" y2="{nodes[end][1]}" />'
        for start, end in edges
    )
    node_lines = "\n".join(
        f'<circle class="publication-news-visual__node" cx="{x}" cy="{y}" r="{13 + idx % 3}" />'
        for idx, (x, y) in enumerate(nodes)
    )
    return "\n".join(
        [
            '<g class="publication-news-visual__scene publication-news-visual__scene--ai">',
            '<path class="publication-news-visual__halo" d="M90 262 C138 88, 350 42, 484 128 C604 204, 716 136, 784 278 C650 360, 382 350, 218 388 C126 410, 66 346, 90 262Z" />',
            '<rect class="publication-news-visual__glass" x="118" y="252" width="320" height="172" rx="32" />',
            '<rect class="publication-news-visual__glass" x="500" y="250" width="218" height="172" rx="32" />',
            edge_lines,
            node_lines,
            '<path class="publication-news-visual__line" d="M132 396 C224 292, 284 386, 370 304 S526 206, 628 320 S744 402, 828 274" />',
            '<path class="publication-news-visual__beam" d="M512 372 q78 -128 156 0 M552 372 q38 -68 76 0" />',
            '<rect class="publication-news-visual__frame" x="154" y="286" width="96" height="62" rx="14" />',
            '<rect class="publication-news-visual__frame" x="286" y="306" width="116" height="78" rx="14" />',
            '<circle class="publication-news-visual__core" cx="612" cy="332" r="42" />',
            "</g>",
        ]
    )


def render_infra_motif() -> str:
    server_lines = []
    for idx, x in enumerate([132, 274, 416, 558]):
        height = 168 + (idx % 2) * 34
        y = 370 - height
        server_lines.extend(
            [
                f'<rect class="publication-news-visual__server" x="{x}" y="{y}" width="104" height="{height}" rx="18" />',
                f'<rect class="publication-news-visual__server-face" x="{x + 18}" y="{y + 26}" width="68" height="{height - 52}" rx="10" />',
                f'<circle class="publication-news-visual__server-light" cx="{x + 34}" cy="{y + 48}" r="6" />',
                f'<circle class="publication-news-visual__server-light" cx="{x + 58}" cy="{y + 48}" r="6" />',
            ]
        )
    return "\n".join(
        [
            '<g class="publication-news-visual__scene publication-news-visual__scene--infra">',
            '<path class="publication-news-visual__halo" d="M98 218 C78 104, 174 50, 278 82 C334 8, 502 28, 546 122 C650 86, 764 144, 742 264 C720 384, 528 386, 396 372 C248 356, 118 350, 98 218Z" />',
            '<path class="publication-news-visual__cloud" d="M150 174 C186 84, 326 80, 374 158 C442 116, 568 154, 574 246 C468 282, 250 282, 150 246Z" />',
            *server_lines,
            '<path class="publication-news-visual__line" d="M236 284 H274 M378 266 H416 M520 282 H558 M196 404 C320 452, 526 448, 672 398" />',
            '<path class="publication-news-visual__beam" d="M712 174 C784 222, 834 302, 842 404" />',
            '<rect class="publication-news-visual__cube" x="704" y="318" width="72" height="72" rx="16" />',
            '<rect class="publication-news-visual__cube" x="798" y="274" width="82" height="82" rx="18" />',
            '<rect class="publication-news-visual__cube" x="890" y="342" width="62" height="62" rx="14" />',
            "</g>",
        ]
    )


def render_iot_motif() -> str:
    buildings = []
    for idx, (x, height) in enumerate([(110, 126), (214, 210), (356, 162), (478, 236), (642, 176)]):
        buildings.append(
            f'<rect class="publication-news-visual__building" x="{x}" y="{408 - height}" width="{72 + idx * 6}" height="{height}" rx="16" />'
        )
    return "\n".join(
        [
            '<g class="publication-news-visual__scene publication-news-visual__scene--iot">',
            '<path class="publication-news-visual__halo" d="M88 282 C190 130, 436 98, 708 180 C780 238, 742 370, 596 418 C400 480, 168 430, 88 282Z" />',
            *buildings,
            '<path class="publication-news-visual__line" d="M146 216 q72 -108 144 0 M180 216 q38 -58 76 0" />',
            '<path class="publication-news-visual__beam" d="M544 154 q102 -144 204 0 M596 154 q50 -76 100 0" />',
            '<circle class="publication-news-visual__node" cx="146" cy="220" r="14" />',
            '<circle class="publication-news-visual__node" cx="544" cy="158" r="16" />',
            '<line class="publication-news-visual__line publication-news-visual__line--soft" x1="146" y1="220" x2="544" y2="158" />',
            '<rect class="publication-news-visual__glass" x="724" y="248" width="180" height="116" rx="28" />',
            '<path class="publication-news-visual__camera" d="M758 310 h88 l40 -34 v86 l-40 -34 h-88 z" />',
            '<circle class="publication-news-visual__core" cx="800" cy="318" r="25" />',
            "</g>",
        ]
    )


def render_twin_motif() -> str:
    return "\n".join(
        [
            '<g class="publication-news-visual__scene publication-news-visual__scene--twin">',
            '<path class="publication-news-visual__halo" d="M96 268 C224 86, 604 72, 894 230 C782 432, 306 488, 96 268Z" />',
            '<path class="publication-news-visual__flight-path" d="M126 354 C296 182, 548 158, 862 304" />',
            '<path class="publication-news-visual__aircraft" d="M188 282 L466 206 L820 292 L486 334 Z" />',
            '<path class="publication-news-visual__aircraft publication-news-visual__aircraft--ghost" d="M292 354 L486 302 L742 362 L498 392 Z" />',
            '<line class="publication-news-visual__line" x1="486" y1="334" x2="428" y2="430" />',
            '<line class="publication-news-visual__line" x1="486" y1="334" x2="564" y2="422" />',
            '<circle class="publication-news-visual__rotor" cx="262" cy="272" r="58" />',
            '<circle class="publication-news-visual__rotor" cx="784" cy="286" r="58" />',
            '<circle class="publication-news-visual__node" cx="350" cy="142" r="17" />',
            '<circle class="publication-news-visual__node" cx="666" cy="138" r="17" />',
            '<line class="publication-news-visual__beam" x1="350" y1="142" x2="666" y2="138" />',
            '<rect class="publication-news-visual__glass" x="786" y="374" width="168" height="92" rx="24" />',
            '<path class="publication-news-visual__trace" d="M814 428 h34 l18 -34 l24 56 l24 -38 h44" />',
            "</g>",
        ]
    )


def render_aero_motif() -> str:
    return "\n".join(
        [
            '<g class="publication-news-visual__scene publication-news-visual__scene--aero">',
            '<path class="publication-news-visual__halo" d="M78 332 C292 126, 674 96, 1030 236 C784 420, 326 484, 78 332Z" />',
            '<path class="publication-news-visual__airfoil" d="M126 322 C332 210, 728 184, 1028 282 C682 330, 310 394, 126 322Z" />',
            '<path class="publication-news-visual__line publication-news-visual__line--soft" d="M98 174 C360 112, 620 112, 1008 156" />',
            '<path class="publication-news-visual__line publication-news-visual__line--soft" d="M96 460 C384 522, 690 504, 1038 404" />',
            '<path class="publication-news-visual__beam" d="M142 248 C398 186, 708 176, 978 232" />',
            '<rect class="publication-news-visual__glass" x="744" y="92" width="132" height="88" rx="22" />',
            '<line class="publication-news-visual__line" x1="810" y1="180" x2="918" y2="284" />',
            '<line class="publication-news-visual__beam" x1="714" y1="132" x2="624" y2="98" />',
            '<line class="publication-news-visual__beam" x1="884" y1="132" x2="994" y2="96" />',
            '<circle class="publication-news-visual__node" cx="918" cy="284" r="16" />',
            "</g>",
        ]
    )


def render_focus_overlay(entry: dict[str, str | int]) -> str:
    text = entry_text(entry)

    if any(keyword in text for keyword in ["blockchain", "hyperledger"]):
        return "\n".join(
            [
                '<g class="publication-news-visual__focus" aria-hidden="true">',
                '<circle class="publication-news-visual__focus-node" cx="836" cy="194" r="24" />',
                '<circle class="publication-news-visual__focus-node" cx="910" cy="238" r="24" />',
                '<circle class="publication-news-visual__focus-node" cx="984" cy="194" r="24" />',
                '<line class="publication-news-visual__beam" x1="860" y1="208" x2="886" y2="224" />',
                '<line class="publication-news-visual__beam" x1="934" y1="224" x2="960" y2="208" />',
                '<text class="publication-news-visual__small-label" x="810" y="286">ledger flow</text>',
                "</g>",
            ]
        )
    if any(keyword in text for keyword in ["kubernetes", "microservice", "storage", "cloud", "sdn"]):
        return "\n".join(
            [
                '<g class="publication-news-visual__focus" aria-hidden="true">',
                '<rect class="publication-news-visual__cube" x="820" y="176" width="70" height="70" rx="14" />',
                '<rect class="publication-news-visual__cube" x="910" y="130" width="86" height="86" rx="16" />',
                '<rect class="publication-news-visual__cube" x="1010" y="198" width="62" height="62" rx="14" />',
                '<path class="publication-news-visual__line" d="M890 212 H910 M996 178 L1010 212" />',
                '<text class="publication-news-visual__small-label" x="812" y="292">service fabric</text>',
                "</g>",
            ]
        )
    if any(keyword in text for keyword in ["robot", "navigation", "reinforcement", "vision", "language model", "deep learning"]):
        return "\n".join(
            [
                '<g class="publication-news-visual__focus" aria-hidden="true">',
                '<path class="publication-news-visual__beam" d="M806 250 C876 176, 972 178, 1048 118" />',
                '<rect class="publication-news-visual__frame" x="820" y="112" width="94" height="66" rx="12" />',
                '<rect class="publication-news-visual__frame" x="968" y="214" width="112" height="78" rx="14" />',
                '<circle class="publication-news-visual__core" cx="906" cy="246" r="28" />',
                '<text class="publication-news-visual__small-label" x="798" y="328">perception loop</text>',
                "</g>",
            ]
        )
    if any(keyword in text for keyword in ["surveillance", "camera", "medical", "smart", "sensor", "iot"]):
        return "\n".join(
            [
                '<g class="publication-news-visual__focus" aria-hidden="true">',
                '<rect class="publication-news-visual__glass" x="814" y="134" width="198" height="126" rx="24" />',
                '<path class="publication-news-visual__camera" d="M846 196 h88 l38 -32 v82 l-38 -32 h-88 z" />',
                '<circle class="publication-news-visual__node" cx="876" cy="206" r="16" />',
                '<path class="publication-news-visual__beam" d="M940 142 q74 -96 148 0 M976 142 q38 -50 76 0" />',
                '<text class="publication-news-visual__small-label" x="806" y="314">sensing field</text>',
                "</g>",
            ]
        )
    if any(keyword in text for keyword in ["digital twin", "uam", "aam", "evtol", "flight", "aerodynamic", "airfoil", "airship", "satellite", "uav"]):
        return "\n".join(
            [
                '<g class="publication-news-visual__focus" aria-hidden="true">',
                '<path class="publication-news-visual__flight-path" d="M790 222 C876 134, 996 144, 1080 226" />',
                '<path class="publication-news-visual__aircraft" d="M840 210 L938 178 L1062 218 L946 238 Z" />',
                '<circle class="publication-news-visual__rotor" cx="862" cy="204" r="28" />',
                '<circle class="publication-news-visual__rotor" cx="1040" cy="214" r="28" />',
                '<text class="publication-news-visual__small-label" x="802" y="302">flight envelope</text>',
                "</g>",
            ]
        )

    return "\n".join(
        [
            '<g class="publication-news-visual__focus" aria-hidden="true">',
            '<circle class="publication-news-visual__focus-node" cx="866" cy="196" r="30" />',
            '<circle class="publication-news-visual__focus-node" cx="962" cy="246" r="24" />',
            '<path class="publication-news-visual__beam" d="M890 210 C920 224, 934 232, 940 236" />',
            '<text class="publication-news-visual__small-label" x="814" y="306">research signal</text>',
            "</g>",
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
    glow_id = f"pub-glow-{sid}"
    pattern_id = f"pub-grid-{sid}"
    values = metric_values(entry)
    labels = visual_labels(entry)
    year = str(entry["date"])[:4]

    return "\n".join(
        [
            f'<div class="publication-news-card__visual" role="img" aria-label="Scientific illustration for {escape(title, quote=True)}">',
            '  <svg class="publication-news-illustration" viewBox="0 0 1200 675" preserveAspectRatio="xMidYMid meet" focusable="false" aria-hidden="true">',
            "    <defs>",
            f'      <linearGradient id="{gradient_id}" x1="0" y1="0" x2="1" y2="1">',
            '        <stop offset="0%" stop-color="var(--pub-wash)" />',
            '        <stop offset="46%" stop-color="#102744" />',
            '        <stop offset="100%" stop-color="var(--pub-wash-2)" />',
            "      </linearGradient>",
            f'      <radialGradient id="{glow_id}" cx="42%" cy="22%" r="74%">',
            '        <stop offset="0%" stop-color="var(--pub-accent-2)" stop-opacity="0.34" />',
            '        <stop offset="52%" stop-color="var(--pub-accent)" stop-opacity="0.12" />',
            '        <stop offset="100%" stop-color="var(--pub-accent)" stop-opacity="0" />',
            "      </radialGradient>",
            f'      <pattern id="{pattern_id}" width="64" height="64" patternUnits="userSpaceOnUse">',
            '        <path class="publication-news-visual__grid" d="M64 0H0V64" />',
            "      </pattern>",
            "    </defs>",
            f'    <rect class="publication-news-visual__backdrop" width="1200" height="675" rx="48" fill="url(#{gradient_id})" />',
            f'    <rect width="1200" height="675" rx="48" fill="url(#{glow_id})" />',
            f'    <rect width="1200" height="675" rx="48" fill="url(#{pattern_id})" />',
            '    <path class="publication-news-visual__city" d="M0 236 H42 V178 H88 V218 H132 V144 H184 V224 H238 V184 H286 V234 H348 V126 H410 V220 H462 V164 H512 V236 H594 V112 H650 V232 H700 V174 H748 V238 H812 V140 H872 V226 H930 V186 H978 V236 H1042 V128 H1098 V220 H1150 V172 H1200 V675 H0Z" />',
            '    <path class="publication-news-visual__ribbon" d="M0 536 C188 468, 340 604, 554 518 C786 424, 924 520, 1200 438 V675 H0Z" />',
            '    <path class="publication-news-visual__terrain" d="M0 602 C236 540, 396 576, 612 516 C812 462, 1018 522, 1200 476 V675 H0Z" />',
            render_visual_particles(entry),
            render_visual_constellation(entry),
            render_cinematic_infrastructure(entry),
            f'    <text class="publication-news-visual__tag" x="72" y="82">{escape(tag)}</text>',
            f'    <text class="publication-news-visual__year" x="1128" y="82" text-anchor="end">{escape(year)}</text>',
            render_domain_motif(str(entry["domain"])),
            render_focus_overlay(entry),
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
        "    <p><strong>Scope:</strong> This section focuses on older publication records that are not already represented by the detailed News stories above. Recent 2021-2026 publications with dedicated generated cover images are excluded to avoid duplication.</p>",
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
