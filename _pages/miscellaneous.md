---
layout: archive
permalink: /miscellaneous/
title: "Notes & Links"
excerpt: "A curated reading atlas of essays, interviews, talks, rankings, and thought-provoking links related to science, technology, work, and society."
author_profile: true
---

{% assign misc_posts = site.data.misc_posts %}

<div class="misc-root">
  <section class="misc-hero" aria-labelledby="misc-hero-title">
    <div class="misc-hero__copy">
      <p class="misc-kicker">Curated reading atlas</p>
      <h2 id="misc-hero-title">Ideas worth keeping close</h2>
      <p>
        Essays, interviews, talks, rankings, and notes that connect science, AI, productivity,
        public institutions, Vietnamese development, and the small cultural habits that shape big systems.
      </p>
      <div class="misc-hero__stats" aria-label="Collection summary">
        <span><strong>{{ misc_posts | size }}</strong> readings</span>
        <span><strong>AI</strong> & society</span>
        <span><strong>Work</strong> & economy</span>
      </div>
    </div>
    <div class="misc-hero__visual" aria-hidden="true">
      <svg class="misc-constellation" viewBox="0 0 760 520" focusable="false">
        <defs>
          <linearGradient id="miscHeroRibbon" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#5fd0ff" />
            <stop offset="50%" stop-color="#8f7cff" />
            <stop offset="100%" stop-color="#ffb15f" />
          </linearGradient>
        </defs>
        <path class="misc-constellation__wash" d="M80 302 C114 116, 344 50, 512 126 C666 196, 686 382, 498 430 C298 482, 42 454, 80 302Z" />
        <path class="misc-constellation__ribbon" stroke="url(#miscHeroRibbon)" d="M90 358 C208 202, 330 296, 438 166 S622 150, 678 276" />
        <path class="misc-constellation__ribbon misc-constellation__ribbon--soft" stroke="url(#miscHeroRibbon)" d="M116 232 C240 118, 354 202, 470 280 S622 370, 700 234" />
        <g class="misc-constellation__grid">
          <path d="M116 398 H674 M158 342 H700 M204 288 H638 M178 230 H604" />
          <path d="M176 160 V432 M290 118 V448 M410 120 V438 M542 144 V424 M650 208 V386" />
        </g>
        <g class="misc-constellation__cards">
          <rect x="104" y="112" width="150" height="104" rx="20" />
          <rect x="314" y="78" width="178" height="118" rx="22" />
          <rect x="528" y="246" width="150" height="104" rx="20" />
          <rect x="220" y="330" width="176" height="112" rx="22" />
        </g>
        <g class="misc-constellation__lines">
          <line x1="178" y1="164" x2="404" y2="138" />
          <line x1="404" y1="138" x2="604" y2="298" />
          <line x1="604" y1="298" x2="308" y2="386" />
          <line x1="308" y1="386" x2="178" y2="164" />
        </g>
        <g class="misc-constellation__nodes">
          <circle cx="178" cy="164" r="16" />
          <circle cx="404" cy="138" r="18" />
          <circle cx="604" cy="298" r="16" />
          <circle cx="308" cy="386" r="18" />
          <circle cx="498" cy="232" r="12" />
          <circle cx="260" cy="260" r="12" />
        </g>
      </svg>
    </div>
  </section>

  <div class="misc-section-note">
    <p>
      Each card keeps a source trail, adds a short editorial summary, and highlights a reading lens for later reference.
    </p>
  </div>

  <div class="misc-grid" aria-label="Curated posts">
    {% for item in misc_posts %}
    <article class="misc-card misc-card--{{ item.tone | default: 'blue' }}" id="misc-{{ item.number }}">
      <figure class="misc-card__media">
        {% if item.image %}
        <img src="{{ item.image }}" alt="{{ item.image_alt | escape }}" width="1200" height="675" loading="lazy" decoding="async">
        {% else %}
        {% include misc_visual.html visual=item.visual title=item.title %}
        {% endif %}
      </figure>
      <div class="misc-card__body">
        <div class="misc-card__meta">
          <span class="misc-card__number">#{{ item.number }}</span>
          <span>{{ item.category }}</span>
          <span>{{ item.year }}</span>
        </div>
        <h3>{{ item.title }}</h3>
        <p class="misc-card__source">{{ item.source }} · {{ item.theme }}</p>
        <p class="misc-card__summary">{{ item.summary }}</p>
        <p class="misc-card__takeaway"><span>Reading lens</span>{{ item.takeaway }}</p>
        <div class="misc-card__links" aria-label="Links for {{ item.title | escape }}">
          {% for link in item.links %}
          <a href="{{ link.url | escape }}" target="_blank" rel="noopener noreferrer">{{ link.label }}</a>
          {% endfor %}
        </div>
      </div>
    </article>
    {% endfor %}
  </div>
</div>
