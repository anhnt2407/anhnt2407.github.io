---
layout: archive
title: "Projects"
excerpt: "Sixteen funded research and engineering programmes since 2009, from a CubeSat in Hanoi to humanoid robotics, with the funding instruments, roles and published results behind each one."
permalink: /projects/
author_profile: true
---

{%- assign projects = site.data.projects -%}
{%- assign eras = site.data.project_eras -%}
{%- assign domains = site.data.project_domains -%}
{%- assign outputs = site.data.project_outputs -%}

{%- assign led = projects | where: "scope", "lead" -%}
{%- assign contributed = projects | where: "scope", "contributor" -%}
{%- assign gantt = projects | sort: "start" -%}

{%- assign pub_ids = "" -%}
{%- assign pub_count = 0 -%}
{%- for p in projects -%}
  {%- for id in p.publications -%}
    {%- assign marker = id | append: "," -%}
    {%- unless pub_ids contains marker -%}
      {%- assign pub_ids = pub_ids | append: marker -%}
      {%- assign pub_count = pub_count | plus: 1 -%}
    {%- endunless -%}
  {%- endfor -%}
{%- endfor -%}

{%- assign sw_total = 0 -%}
{%- for g in outputs.software_groups -%}{%- assign sw_total = sw_total | plus: g.count -%}{%- endfor -%}

<div class="proj-root">

  <section class="proj-hero" aria-labelledby="proj-hero-title">
    <div class="proj-hero__copy">
      <p class="proj-kicker">Funded research &amp; engineering</p>
      <h2 id="proj-hero-title">Sixteen programmes, from a CubeSat in Hanoi to a humanoid that has to stay upright</h2>
      <p>
        Every programme below is one I was funded to work on, in the role the contract gave me — from
        core developer on Vietnam's first pico-satellite to technical leader of a nine-year national
        research centre for urban air mobility digital twins, and now director of robot control and
        software for a humanoid platform. Where a programme outlived my appointment, the card says so.
      </p>
      <dl class="proj-hero__stats" aria-label="Project portfolio in numbers">
        <div><dt>Programmes</dt><dd>{{ projects | size }}</dd></div>
        <div><dt>Led</dt><dd>{{ led | size }}</dd></div>
        <div><dt>Since</dt><dd>2009</dd></div>
        <div><dt>Papers</dt><dd>{{ pub_count }}</dd></div>
      </dl>
      <p class="proj-hero__footnote">
        Dates on each card are the period I personally worked on the programme. Several grants run
        past that — the nine-year urban air mobility centre is funded to 2029 — and the timeline
        below draws the full funded span as a faint bar behind the solid one. <em>Papers</em> counts
        the {{ pub_count }} entries on the publications page that the cards link out to.
      </p>
    </div>

    <aside class="proj-hero__panel" aria-labelledby="proj-arc-title">
      <svg class="proj-hero__stars" viewBox="0 0 400 520" aria-hidden="true" focusable="false" preserveAspectRatio="none">
        <path class="proj-hero__grid" d="M0 96 H400 M0 196 H400 M0 296 H400 M0 396 H400 M0 472 H400" />
        <path class="proj-hero__grid" d="M74 0 V520 M154 0 V520 M234 0 V520 M314 0 V520" />
        <circle class="proj-hero__spark" cx="326" cy="66" r="3" />
        <circle class="proj-hero__spark" cx="64" cy="178" r="2" />
        <circle class="proj-hero__spark" cx="292" cy="262" r="2.5" />
        <circle class="proj-hero__spark" cx="110" cy="384" r="3" />
        <circle class="proj-hero__spark" cx="344" cy="452" r="2" />
      </svg>

      <p class="proj-arc-title" id="proj-arc-title">Four working eras</p>
      <ol class="proj-arc">
        {% for era in eras %}{% assign ec = projects | where: "era", era.slug %}
        <li class="proj-arc__stop proj-arc__stop--{{ era.accent }}">
          <span class="proj-arc__dot" aria-hidden="true"></span>
          <span class="proj-arc__label">{{ era.label }}</span>
          <span class="proj-arc__years">{{ era.span }} &middot; {{ ec | size }} programme{% unless ec.size == 1 %}s{% endunless %}</span>
        </li>
        {% endfor %}
      </ol>
    </aside>
  </section>

  <h2 class="proj-heading" id="timeline">Programme timeline</h2>
  <p class="proj-heading__lead">
    All {{ projects | size }} programmes on one axis, oldest first. The solid bar is the period I
    worked on it; the faint bar behind it is the full funded span of the programme itself.
  </p>

  <figure class="proj-gantt" aria-label="Timeline of sixteen research and engineering programmes from 2009 to 2029">
    <div class="proj-gantt__legend" aria-hidden="true">
      <span class="proj-gantt__key proj-gantt__key--solid">My involvement</span>
      <span class="proj-gantt__key proj-gantt__key--ghost">Full funded span</span>
    </div>

    <div class="proj-gantt__plot">
      <div class="proj-gantt__ticks" aria-hidden="true">
        <span style="left:4.76%">2010</span>
        <span style="left:23.81%">2014</span>
        <span style="left:42.86%">2018</span>
        <span style="left:61.90%">2022</span>
        <span style="left:80.95%">2026</span>
        <span style="left:100%">2030</span>
      </div>

      <div class="proj-gantt__body">
      <div class="proj-gantt__lines" aria-hidden="true">
        <span style="left:4.76%"></span>
        <span style="left:23.81%"></span>
        <span style="left:42.86%"></span>
        <span style="left:61.90%"></span>
        <span style="left:80.95%"></span>
        <span style="left:100%"></span>
      </div>

      <ol class="proj-gantt__rows">
        {% for p in gantt %}
        {%- assign L = p.start | minus: 2009.0 | times: 4.7619 | round: 2 -%}
        {%- assign W = p.end | minus: p.start | times: 4.7619 | round: 2 -%}
        {%- assign PL = p.prog_start | minus: 2009.0 | times: 4.7619 | round: 2 -%}
        {%- assign PW = p.prog_end | minus: p.prog_start | times: 4.7619 | round: 2 -%}
        {%- assign dom = domains | where: "slug", p.domain | first -%}
        <li class="proj-gantt__row proj-gantt__row--{{ dom.accent }}">
          <a class="proj-gantt__name" href="#project-{{ p.slug }}">{{ p.short }}</a>
          <span class="proj-gantt__track">
            <span class="proj-gantt__bar proj-gantt__bar--ghost" style="left:{{ PL }}%;width:{{ PW }}%"></span>
            <span class="proj-gantt__bar proj-gantt__bar--solid{% if p.status == 'current' %} is-current{% endif %}" style="left:{{ L }}%;width:{{ W }}%"></span>
          </span>
          <span class="proj-gantt__period">{{ p.period }}</span>
        </li>
        {% endfor %}
      </ol>
      </div>
    </div>
  </figure>

  <h2 class="proj-heading" id="programmes">The programmes</h2>
  <p class="proj-heading__lead">
    Grouped into the four eras of the work, newest first. {{ led | size }} led,
    {{ contributed | size }} contributed to as staff or core researcher. Where the work produced
    papers, the identifiers link straight to the entry on the
    <a href="{{ site.baseurl }}/publications/">publications page</a>.
  </p>

  <nav class="proj-filter" id="proj-filter" aria-label="Filter programmes" hidden>
    <div class="proj-filter__group">
      <p class="proj-filter__label" id="proj-facet-domain">Domain</p>
      <div class="proj-filter__chips" role="group" aria-labelledby="proj-facet-domain">
        <button type="button" class="proj-chip is-active" data-facet="domain" data-value="all" aria-pressed="true">All<span class="proj-chip__count">{{ projects | size }}</span></button>
        {% for d in domains %}{% assign dc = projects | where: "domain", d.slug %}
        <button type="button" class="proj-chip proj-chip--{{ d.accent }}" data-facet="domain" data-value="{{ d.slug }}" aria-pressed="false">{{ d.short }}<span class="proj-chip__count">{{ dc | size }}</span></button>
        {% endfor %}
      </div>
    </div>

    <div class="proj-filter__group">
      <p class="proj-filter__label" id="proj-facet-scope">My role</p>
      <div class="proj-filter__chips" role="group" aria-labelledby="proj-facet-scope">
        <button type="button" class="proj-chip is-active" data-facet="scope" data-value="all" aria-pressed="true">All<span class="proj-chip__count">{{ projects | size }}</span></button>
        <button type="button" class="proj-chip proj-chip--indigo" data-facet="scope" data-value="lead" aria-pressed="false">Led<span class="proj-chip__count">{{ led | size }}</span></button>
        <button type="button" class="proj-chip proj-chip--blue" data-facet="scope" data-value="contributor" aria-pressed="false">Contributed<span class="proj-chip__count">{{ contributed | size }}</span></button>
      </div>
    </div>
  </nav>

  <div class="proj-eras" id="proj-eras">
    {% for era in eras %}{% assign ep = projects | where: "era", era.slug %}
    <section class="proj-era proj-era--{{ era.accent }}" data-era="{{ era.slug }}" id="era-{{ era.slug }}" aria-labelledby="era-{{ era.slug }}-title">
      <header class="proj-era__head">
        <h3 id="era-{{ era.slug }}-title">{{ era.label }}<span class="proj-era__count">{{ era.span }}</span></h3>
        <p>{{ era.blurb }}</p>
      </header>

      <div class="proj-list">
        {% for p in ep %}{% assign dom = domains | where: "slug", p.domain | first %}
        <article class="proj-card proj-card--{{ dom.accent }}{% unless p.highlights.first %} proj-card--compact{% endunless %}"
                 id="project-{{ p.slug }}"
                 data-domain="{{ p.domain }}"
                 data-scope="{{ p.scope }}">
          <figure class="proj-card__art">
            {% if p.cover_alt %}
            <img src="{{ site.baseurl }}/images/projects/{{ p.slug }}.webp"
                 alt="{{ p.cover_alt | escape }}"
                 width="1200" height="675" loading="lazy" decoding="async">
            {% else %}
            {% include project_visual.html visual=p.visual title=p.title %}
            {% endif %}
          </figure>

          <div class="proj-card__body">
            <div class="proj-card__badges">
              <span class="proj-badge proj-badge--domain">{{ dom.short }}</span>
              <span class="proj-badge proj-badge--scope">{{ p.scope_label }}</span>
              {% if p.status == "current" %}<span class="proj-badge proj-badge--live">Active now</span>{% endif %}
              {% if p.flagship %}<span class="proj-badge proj-badge--star">Flagship programme</span>{% endif %}
              {% if p.origin %}<span class="proj-badge proj-badge--star">Where it started</span>{% endif %}
            </div>

            <h4>{{ p.title }}</h4>
            <p class="proj-card__role">{{ p.role }}</p>

            {% if p.summary %}
            <p class="proj-card__summary">{{ p.summary }}</p>
            {% endif %}

            {% if p.programme_note %}
            <p class="proj-card__note">{{ p.programme_note }}</p>
            {% endif %}

            {% if p.highlights.first %}
            <ul class="proj-card__list">
              {% for h in p.highlights %}<li>{{ h }}</li>{% endfor %}
            </ul>
            {% endif %}

            {% if p.stack.first %}
            <ul class="proj-chips" aria-label="Methods and tools used on {{ p.short | escape }}">
              {% for s in p.stack %}<li>{{ s }}</li>{% endfor %}
            </ul>
            {% endif %}

            {% if p.publications.first %}
            <div class="proj-card__pubs">
              <span class="proj-card__pubs-label">Related publications</span>
              <span class="proj-card__pubs-chips">
                {% for id in p.publications %}<a class="proj-pub-chip" href="{{ site.baseurl }}/publications/#pub-{{ id }}">{{ id }}</a>{% endfor %}
              </span>
            </div>
            {% endif %}
          </div>

          <dl class="proj-meta">
            <div><dt>Period</dt><dd>{{ p.period }}</dd></div>
            <div><dt>Host</dt><dd>{{ p.organisation }}</dd></div>
            <div><dt>Funding</dt><dd>{{ p.funder }}</dd></div>
            {% if p.grant %}<div><dt>Instrument</dt><dd>{{ p.grant }}</dd></div>{% endif %}
            {% if p.team %}<div><dt>Team</dt><dd>{{ p.team }}</dd></div>{% endif %}
            <div><dt>Where</dt><dd><span aria-hidden="true">{{ p.flag }}</span> {{ p.location }}</dd></div>
          </dl>
        </article>
        {% endfor %}
      </div>
    </section>
    {% endfor %}
  </div>

  <h2 class="proj-heading" id="outputs">Registered outputs</h2>
  <p class="proj-heading__lead">
    Beyond the papers, the programmes above produced {{ outputs.patents | size }} patent filings and
    {{ sw_total }} software registrations in South Korea, all filed between 2021 and 2024.
  </p>

  <div class="proj-outputs">
    <section class="proj-outputs__col" aria-labelledby="proj-patents-title">
      <h3 id="proj-patents-title" class="proj-outputs__title">Patents<span>{{ outputs.patents | size }}</span></h3>
      <ol class="proj-patents">
        {% for pt in outputs.patents %}{% assign src = projects | where: "slug", pt.project | first %}
        <li class="proj-patent">
          <p class="proj-patent__date">{{ pt.date }}</p>
          <p class="proj-patent__title">{{ pt.title }}</p>
          <p class="proj-patent__status">{{ pt.status }}</p>
          {% if src %}<a class="proj-patent__link" href="#project-{{ src.slug }}">{{ src.short }}</a>{% endif %}
        </li>
        {% endfor %}
      </ol>
    </section>

    <section class="proj-outputs__col" aria-labelledby="proj-software-title">
      <h3 id="proj-software-title" class="proj-outputs__title">Software registrations<span>{{ sw_total }}</span></h3>
      <div class="proj-software">
        {% for g in outputs.software_groups %}{% assign src = projects | where: "slug", g.project | first %}
        <details class="proj-software__group">
          <summary>
            <span class="proj-software__label">{{ g.label }}</span>
            <span class="proj-software__meta">{{ g.span }} &middot; {{ g.count }} registration{% unless g.count == 1 %}s{% endunless %}</span>
          </summary>
          <ul>
            {% for item in g.items %}<li>{{ item }}</li>{% endfor %}
          </ul>
          {% if src %}<a class="proj-patent__link" href="#project-{{ src.slug }}">{{ src.short }}</a>{% endif %}
        </details>
        {% endfor %}
      </div>
    </section>
  </div>
</div>

<script>(function () {
  var root = document.querySelector('.proj-root');
  if (!root) { return; }

  var filter = root.querySelector('#proj-filter');
  var wrap = root.querySelector('#proj-eras');
  if (!filter || !wrap) { return; }

  var chips = Array.prototype.slice.call(filter.querySelectorAll('.proj-chip'));
  var cards = Array.prototype.slice.call(wrap.querySelectorAll('.proj-card'));
  var eras = Array.prototype.slice.call(wrap.querySelectorAll('.proj-era'));
  if (!chips.length || !cards.length) { return; }

  var state = { domain: 'all', scope: 'all' };

  var status = document.createElement('p');
  status.className = 'proj-filter__status';
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');
  filter.appendChild(status);

  var reset = document.createElement('button');
  reset.type = 'button';
  reset.className = 'proj-filter__reset';
  reset.textContent = 'Show all programmes';
  reset.hidden = true;
  filter.appendChild(reset);

  function matches(card) {
    var byDomain = state.domain === 'all' ||
      card.getAttribute('data-domain') === state.domain;
    var byScope = state.scope === 'all' ||
      card.getAttribute('data-scope') === state.scope;
    return byDomain && byScope;
  }

  function apply(announce) {
    var shown = 0;

    cards.forEach(function (card) {
      var show = matches(card);
      card.hidden = !show;
      if (show) { shown += 1; }
    });

    eras.forEach(function (era) {
      era.hidden = era.querySelectorAll('.proj-card:not([hidden])').length === 0;
    });

    chips.forEach(function (chip) {
      var on = state[chip.getAttribute('data-facet')] === chip.getAttribute('data-value');
      chip.classList.toggle('is-active', on);
      chip.setAttribute('aria-pressed', on ? 'true' : 'false');
    });

    var filtered = state.domain !== 'all' || state.scope !== 'all';
    reset.hidden = !filtered;
    wrap.classList.toggle('is-filtered', filtered);

    status.textContent = announce
      ? shown + (shown === 1 ? ' programme shown' : ' programmes shown')
      : '';
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      state[chip.getAttribute('data-facet')] = chip.getAttribute('data-value');
      apply(true);
    });
  });

  reset.addEventListener('click', function () {
    state.domain = 'all';
    state.scope = 'all';
    apply(true);
  });

  filter.hidden = false;
  filter.classList.add('is-interactive');
  apply(false);
})();
</script>
