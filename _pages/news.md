---
layout: archive
title: "News"
excerpt: "Chronological publication news archive based on the Publications page, with externally verified records and concise research notes for each item."
permalink: /news/
author_profile: true
---

<div class="page-lead">
  <p>A chronological publication news archive generated from the Publications page and curated as of March 22, 2026.</p>
  <p class="page-lead__note">The archive below covers all publication records listed on the Publications page, sorted from most recent to earliest, and excludes manuscripts under review. Verification relies primarily on DOI records already listed on the Publications page, supplemented with OpenReview, DBpia, direct paper links, KCI, and official venue or program traces when DOI metadata is unavailable.</p>
</div>

<div id="publication-news-root" class="publication-news-root">
  <div class="publication-news-overview">
    <p><strong>Preparing publication archive...</strong></p>
    <p>The News timeline is being generated directly from the Publications source so that the archive stays synchronized with future updates.</p>
  </div>
</div>

<noscript>
  <blockquote>
    This publication news archive is rendered from the Publications source with JavaScript. If JavaScript is disabled, please use <a href="/publications/">/publications/</a>.
  </blockquote>
</noscript>

<script id="publications-markdown" type="text/plain">
{% include_relative publications.md %}
</script>

<script>
(function () {
  const root = document.getElementById("publication-news-root");
  const source = document.getElementById("publications-markdown");

  if (!root || !source) {
    return;
  }

  const specialLinks = {
    13: { label: "DBpia record", url: "https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11658488", badge: "DBpia" },
    23: { label: "DOI record", url: "https://doi.org/10.9708/jksci.2025.30.12.025", badge: "DOI" },
    88: { label: "DBpia record", url: "https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE12340734", badge: "DBpia" },
    90: { label: "DBpia record", url: "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12058721", badge: "DBpia" },
    95: { label: "DBpia record", url: "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11658014", badge: "DBpia" },
    103: { label: "Program record", url: "https://ksas.or.kr/proceedings/2024b/data/2024%EB%85%84%EB%8F%84%20%EC%B6%94%EA%B3%84%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%28%EC%95%88%29%20v9.pdf", badge: "Program" }
  };

  const domainBadges = {
    "Domain 1": "AI & Autonomy",
    "Domain 2": "Dependability & Infra",
    "Domain 3": "IoT & CPS",
    "Domain 4": "Digital Twin & UAM",
    "Domain 5": "Aerospace Systems"
  };

  const domainLines = {
    "Domain 1": "artificial intelligence, reinforcement learning, autonomous control, navigation, and perception",
    "Domain 2": "dependability, performance, energy, storage, cloud, SDN, and blockchain infrastructures",
    "Domain 3": "IoT, smart environments, surveillance, healthcare, and cyber-physical infrastructures",
    "Domain 4": "digital twin systems, advanced air mobility, unmanned aerial systems, and twin-enabled dependability",
    "Domain 5": "aerospace systems, aerodynamic modeling, flight dynamics, and air vehicle design"
  };

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function cleanVenue(value, link) {
    let venue = (value || "").replace(/\*/g, "").trim().replace(/\.+$/, "");

    while (true) {
      const trimmed = venue.replace(/\s*\([^()]*\)\s*$/, "").trim().replace(/\.+$/, "");
      if (trimmed === venue) {
        break;
      }
      venue = trimmed;
    }

    venue = venue.replace(/--/g, "-").replace(/\s{2,}/g, " ");

    if (!venue) {
      if ((link || "").toLowerCase().includes("techrxiv")) {
        return "TechRxiv";
      }
      return "External publication record";
    }

    return venue;
  }

  function typeLabel(tag, venue, link) {
    const venueLower = (venue || "").toLowerCase();
    const linkLower = (link || "").toLowerCase();

    if ((tag || "").startsWith("J")) {
      return "Journal article";
    }
    if ((tag || "").startsWith("C")) {
      return "Conference paper";
    }
    if ((tag || "").startsWith("B")) {
      return "Book chapter";
    }
    if ((tag || "").startsWith("P")) {
      if (venueLower.includes("withdrawn")) {
        return "Submission record";
      }
      if (venueLower.includes("arxiv") || venueLower.includes("research square") || linkLower.includes("techrxiv")) {
        return "Preprint";
      }
      return "Publication record";
    }
    return "Publication record";
  }

  function sourceBadge(entry) {
    if (specialLinks[entry.idx]) {
      return specialLinks[entry.idx].badge;
    }
    if ((entry.link || "").includes("doi.org")) {
      return "DOI";
    }
    if ((entry.link || "").includes("openreview")) {
      return "OpenReview";
    }
    if ((entry.link || "").toLowerCase().includes("dbpia")) {
      return "DBpia";
    }
    if (entry.link) {
      return "Paper";
    }
    return "Sparse public metadata";
  }

  function summary(entry) {
    const title = entry.title;
    const venue = entry.venue || "";
    const type = entry.type.toLowerCase();
    const domainLine = domainLines[entry.domain];
    const titleLower = title.toLowerCase();

    if (titleLower.startsWith("correction to:")) {
      const corrected = title.includes(":") ? title.split(":").slice(1).join(":").trim() : title;
      const correctedLower = corrected ? corrected.charAt(0).toLowerCase() + corrected.slice(1) : corrected;
      return "This " + type + " records an official correction linked to the earlier study on " + correctedLower + ". It preserves the accuracy of the published record within your " + domainLine + " track.";
    }

    if (venue.toLowerCase().includes("withdrawn submission")) {
      return "This " + type + " documents a withdrawn submission on " + title + ". It remains part of your " + domainLine + " portfolio as a visible public research trace.";
    }

    if (titleLower.includes("systematic literature review") || (titleLower.includes("review") && !titleLower.startsWith("correction to:"))) {
      return "This " + type + " synthesizes the literature around " + title + ". It broadens your " + domainLine + " portfolio by clarifying methods, themes, and open questions in the area.";
    }

    return "This " + type + " advances your " + domainLine + " track through work on " + title + ". It is recorded here as a publication milestone in the venue below.";
  }

  function formatDate(value) {
    const date = new Date(value + "T00:00:00Z");
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      timeZone: "UTC"
    });
  }

  function parsePublications(markdown) {
    const lines = markdown.split(/\r?\n/);
    const entries = [];
    let domain = null;

    for (const line of lines) {
      if (line.startsWith("## B. ")) {
        domain = "Domain 1";
      } else if (line.startsWith("## C. ")) {
        domain = "Domain 2";
      } else if (line.startsWith("## D. ")) {
        domain = "Domain 3";
      } else if (line.startsWith("## E. ")) {
        domain = "Domain 4";
      } else if (line.startsWith("## F. ")) {
        domain = "Domain 5";
      }

      if (!/^\d+\.\s/.test(line)) {
        continue;
      }

      const idxMatch = line.match(/^(\d+)\./);
      const titleMatch = line.match(/\*\*(.+?)\*\*/);
      const dateMatch = line.match(/\[(\d{4}-\d{2}-\d{2})\]\s*$/);

      if (!idxMatch || !titleMatch || !dateMatch || !domain) {
        continue;
      }

      const idx = Number(idxMatch[1]);
      const title = titleMatch[1].trim().replace(/\.$/, "");

      let rest = line.slice(titleMatch.index + titleMatch[0].length);
      rest = rest.replace(/\s*\[(?:doi:[^\]]+|openreview\.net\/forum\?id=[^\]]+|DBpia|paper)\]\([^)]+\)/g, "");
      rest = rest.replace(/\s*\[[^\]]*\]\s*$/, "").trim();
      rest = rest.replace(/^[.\s]+/, "").trim();

      let venue = rest;
      if (venue.startsWith("In: ")) {
        venue = venue.slice(4);
      } else if (venue.startsWith("In ")) {
        venue = venue.slice(3);
      }

      const linkMatch = line.match(/\[(doi:[^\]]+|openreview\.net\/forum\?id=[^\]]+|DBpia|paper)\]\(([^)]+)\)/);
      const link = linkMatch ? linkMatch[2] : "";
      const tagMatch = line.match(/\[([A-Z]\d+[A-Za-z]?)\]<\/span>/);
      const tag = tagMatch ? tagMatch[1] : "";

      const entry = {
        idx: idx,
        tag: tag,
        date: dateMatch[1],
        title: title,
        venue: cleanVenue(venue, link),
        link: specialLinks[idx] ? specialLinks[idx].url : link,
        linkLabel: specialLinks[idx]
          ? specialLinks[idx].label
          : link.includes("doi.org")
            ? "DOI record"
            : link.includes("openreview")
              ? "OpenReview record"
              : link.toLowerCase().includes("dbpia")
                ? "DBpia record"
                : link
                  ? "Paper link"
                  : "",
        type: "",
        domain: domain,
        domainBadge: domainBadges[domain]
      };

      entry.type = typeLabel(entry.tag, entry.venue, entry.link);
      entry.sourceBadge = sourceBadge(entry);
      entry.summary = summary(entry);
      entries.push(entry);
    }

    return entries.sort(function (a, b) {
      if (a.date === b.date) {
        return b.idx - a.idx;
      }
      return a.date < b.date ? 1 : -1;
    });
  }

  function render(entries) {
    const byYear = {};
    const sourceCounts = {};

    entries.forEach(function (entry) {
      const year = entry.date.slice(0, 4);
      byYear[year] = byYear[year] || [];
      byYear[year].push(entry);
      sourceCounts[entry.sourceBadge] = (sourceCounts[entry.sourceBadge] || 0) + 1;
    });

    const sourceSummary = Object.keys(sourceCounts)
      .sort()
      .map(function (key) {
        return key + " " + sourceCounts[key];
      })
      .join(", ");

    const years = Object.keys(byYear).sort().reverse();
    const html = [];

    html.push("<div class=\"publication-news-overview\">");
    html.push("<p><strong>Coverage:</strong> " + entries.length + " publications from 2010 to 2025.</p>");
    html.push("<p><strong>Source mix:</strong> " + escapeHtml(sourceSummary) + ".</p>");
    html.push("</div>");

    years.forEach(function (year) {
      html.push("<h2>" + escapeHtml(year) + "</h2>");
      html.push("<div class=\"publication-news-list\">");

      byYear[year].forEach(function (entry) {
        html.push("<article class=\"publication-news-card\">");
        html.push("<div class=\"publication-news-card__top\">");
        html.push("<span class=\"publication-news-badge publication-news-badge--date\">" + escapeHtml(formatDate(entry.date)) + "</span>");
        html.push("<span class=\"publication-news-badge\">" + escapeHtml(entry.tag || "Record") + "</span>");
        html.push("<span class=\"publication-news-badge\">" + escapeHtml(entry.type) + "</span>");
        html.push("<span class=\"publication-news-badge\">" + escapeHtml(entry.domainBadge) + "</span>");
        html.push("<span class=\"publication-news-badge\">" + escapeHtml(entry.sourceBadge) + "</span>");
        html.push("</div>");
        html.push("<h3>" + escapeHtml(entry.title) + "</h3>");
        html.push("<p>" + escapeHtml(entry.summary) + "</p>");
        html.push("<p class=\"publication-news-card__record\"><strong>Publication record:</strong> <em>" + escapeHtml(entry.venue) + "</em>.</p>");

        if (entry.link) {
          html.push("<p class=\"publication-news-card__links\"><a href=\"" + escapeHtml(entry.link) + "\">" + escapeHtml(entry.linkLabel || "Official record") + "</a></p>");
        }

        html.push("</article>");
      });

      html.push("</div>");
    });

    root.innerHTML = html.join("");
  }

  render(parsePublications(source.textContent || ""));
})();
</script>
