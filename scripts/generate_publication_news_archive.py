#!/usr/bin/env python3

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_PATH = ROOT / "_pages" / "publications.md"
OUTPUT_PATH = ROOT / "_includes" / "publication_news_archive.html"

SPECIAL_LINKS = {
    13: {
        "label": "DBpia record",
        "url": "https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11658488",
        "badge": "DBpia",
    },
    23: {
        "label": "DOI record",
        "url": "https://doi.org/10.9708/jksci.2025.30.12.025",
        "badge": "DOI",
    },
    88: {
        "label": "DBpia record",
        "url": "https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE12340734",
        "badge": "DBpia",
    },
    90: {
        "label": "DBpia record",
        "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12058721",
        "badge": "DBpia",
    },
    95: {
        "label": "DBpia record",
        "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11658014",
        "badge": "DBpia",
    },
    103: {
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

TITLE_RE = re.compile(r"\*\*(.+?)\*\*")
DATE_RE = re.compile(r"\[(\d{4}-\d{2}-\d{2})\]\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
TAG_RE = re.compile(r"\[([A-Z]\d+[A-Za-z]?)\]</span>")


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
    idx = int(entry["idx"])
    link = str(entry["link"])

    if idx in SPECIAL_LINKS:
        return SPECIAL_LINKS[idx]["badge"]
    if "doi.org" in link:
        return "DOI"
    if "openreview" in link:
        return "OpenReview"
    if "dbpia" in link.lower():
        return "DBpia"
    if link:
        return "Paper"
    return "Sparse public metadata"


def lower_phrase(text: str) -> str:
    if ": " in text:
        return text.split(": ", 1)[1].strip().rstrip(".")
    return text.strip().rstrip(".")


def brochure_summary(entry: dict[str, str | int]) -> str:
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
            f"It preserves the accuracy of the published record within your {domain_line} research line."
        )

    if "withdrawn" in venue.lower():
        return (
            f"This {label} documents a public submission record for {focus}. "
            f"It remains part of your {domain_line} portfolio as a visible research trace."
        )

    if "systematic literature review" in title_lower:
        return (
            f"This {label} synthesizes the literature around {focus}. "
            f"It broadens your {domain_line} portfolio by clarifying methods, themes, and open questions."
        )

    if any(keyword in title_lower for keyword in ["framework", "architecture", "platform", "system"]):
        return (
            f"This {label} presents a structured contribution on {focus}. "
            f"It extends your {domain_line} portfolio with a design-oriented research artifact."
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
            f"This {label} highlights a model-driven view of {focus}. "
            f"It reinforces your {domain_line} research line with a quantitative publication milestone."
        )

    return (
        f"This {label} spotlights {focus}. "
        f"It contributes to your {domain_line} portfolio through the venue listed below."
    )


def format_date(value: str) -> str:
    return datetime.strptime(value, "%Y-%m-%d").strftime("%B %-d, %Y")


def find_best_link(line: str, idx: int) -> tuple[str, str]:
    if idx in SPECIAL_LINKS:
        special = SPECIAL_LINKS[idx]
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

        link, link_label = find_best_link(line, idx)
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
        entry["summary"] = brochure_summary(entry)
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
    generated_on = datetime.now(timezone.utc).strftime("%B %-d, %Y")

    html_lines = [
        "<div class=\"publication-news-root\">",
        "  <div class=\"publication-news-overview\">",
        f"    <p><strong>Coverage:</strong> {len(entries)} publications from {min_year} to {max_year}, sorted from most recent to earliest and excluding manuscripts under review.</p>",
        "    <p><strong>Archive note:</strong> This static brochure archive is generated from the Publications page metadata and the official publication links recorded there, so the News page remains stable without client-side rendering.</p>",
        f"    <p><strong>Source mix:</strong> {escape(source_summary)}.</p>",
        f"    <p><strong>Generated:</strong> {generated_on} (UTC).</p>",
        "  </div>",
    ]

    for year in years:
        html_lines.append(f"  <h2>{escape(year)}</h2>")
        html_lines.append("  <div class=\"publication-news-list\">")

        for entry in by_year[year]:
            html_lines.append("    <article class=\"publication-news-card\">")
            html_lines.append("      <div class=\"publication-news-card__top\">")
            html_lines.append(
                f"        <span class=\"publication-news-badge publication-news-badge--date\">{escape(format_date(str(entry['date'])))}</span>"
            )
            html_lines.append(
                f"        <span class=\"publication-news-badge\">{escape(str(entry['tag']))}</span>"
            )
            html_lines.append(
                f"        <span class=\"publication-news-badge\">{escape(str(entry['type']))}</span>"
            )
            html_lines.append(
                f"        <span class=\"publication-news-badge\">{escape(str(entry['domain_badge']))}</span>"
            )
            html_lines.append(
                f"        <span class=\"publication-news-badge\">{escape(str(entry['source_badge']))}</span>"
            )
            html_lines.append("      </div>")
            html_lines.append(f"      <h3>{escape(str(entry['title']))}</h3>")
            html_lines.append(f"      <p>{escape(str(entry['summary']))}</p>")
            html_lines.append(
                f"      <p class=\"publication-news-card__record\"><strong>Publication record:</strong> <em>{escape(str(entry['venue']))}</em>.</p>"
            )

            if entry["link"]:
                html_lines.append(
                    f"      <p class=\"publication-news-card__links\"><a href=\"{escape(str(entry['link']), quote=True)}\">{escape(str(entry['link_label']) or 'Official record')}</a></p>"
                )

            html_lines.append("    </article>")

        html_lines.append("  </div>")

    html_lines.append("</div>")
    return "\n".join(html_lines) + "\n"


def main() -> None:
    markdown = PUBLICATIONS_PATH.read_text(encoding="utf-8")
    entries = parse_entries(markdown)
    OUTPUT_PATH.write_text(render(entries), encoding="utf-8")
    print(f"Wrote {len(entries)} publication cards to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
