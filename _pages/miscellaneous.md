---
layout: archive
permalink: /miscellaneous/
title: "Notes & Links"
excerpt: "A curated reading atlas of essays, interviews, talks, rankings, and thought-provoking links related to science, technology, work, and society."
author_profile: true
---

{% assign misc_posts = site.data.misc_posts %}
{% assign misc_topics = site.data.misc_topics %}
{% assign dated = misc_posts | where_exp: "p", "p.year != 'Current'" %}
{% assign years = dated | map: "year" | sort %}
{% assign sources = misc_posts | map: "source" | uniq %}

<div class="misc-root">
  <section class="misc-hero" aria-labelledby="misc-hero-title">
    <div class="misc-hero__copy">
      <p class="misc-kicker">Curated reading atlas</p>
      <h2 id="misc-hero-title">Ideas worth keeping close</h2>
      <p>
        Essays, interviews, talks, and standing references that connect artificial intelligence,
        science, economic development, and the cultural habits that quietly shape big systems.
        Every entry keeps its source trail, a short editorial summary, and a reading lens.
      </p>
      <dl class="misc-hero__stats" aria-label="Collection summary">
        <div><dt>Readings</dt><dd>{{ misc_posts | size }}</dd></div>
        <div><dt>Themes</dt><dd>{{ misc_topics | size }}</dd></div>
        <div><dt>Span</dt><dd>{{ years | first }}&ndash;{{ years | last }}</dd></div>
        <div><dt>Sources</dt><dd>{{ sources | size }}</dd></div>
      </dl>
    </div>
    <div class="misc-hero__visual">
      <img src="/images/misc/000-reading-atlas-hero.webp"
           alt="An open book on a dark wooden desk at night, with a luminous globe of light points hovering above it, joined by fine lit threads to small translucent panels of charts"
           width="1200" height="900" decoding="async">
    </div>
  </section>

  <nav class="misc-filter" id="misc-filter" aria-label="Filter readings by theme">
    <p class="misc-filter__label" id="misc-filter-label">Browse by theme</p>
    <div class="misc-filter__chips" role="group" aria-labelledby="misc-filter-label">
      <a class="misc-chip is-active" href="#misc-all" data-topic="all" aria-current="true">All<span class="misc-chip__count">{{ misc_posts | size }}</span></a>
      {% for topic in misc_topics %}{% assign topic_posts = misc_posts | where: "topic", topic.slug %}
      <a class="misc-chip misc-chip--{{ topic.accent }}" href="#topic-{{ topic.slug }}" data-topic="{{ topic.slug }}">{{ topic.label }}<span class="misc-chip__count">{{ topic_posts | size }}</span></a>
      {% endfor %}
    </div>
  </nav>

  <div class="misc-sections" id="misc-all">
    {% for topic in misc_topics %}{% assign topic_posts = misc_posts | where: "topic", topic.slug %}
    <section class="misc-section misc-section--{{ topic.accent }}" id="topic-{{ topic.slug }}" data-topic="{{ topic.slug }}" aria-labelledby="topic-{{ topic.slug }}-title">
      <header class="misc-section__head">
        <h3 id="topic-{{ topic.slug }}-title">{{ topic.label }}<span class="misc-section__count">{{ topic_posts | size }}</span></h3>
        <p>{{ topic.blurb }}</p>
      </header>

      <div class="misc-grid">
        {% for item in topic_posts %}
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
            <h4>{{ item.title }}</h4>
            <p class="misc-card__source">{{ item.source }} &middot; {{ item.theme }}</p>
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
    </section>
    {% endfor %}
  </div>
</div>

<script>(function () {
  var root = document.querySelector('.misc-root');
  if (!root) { return; }
  var filter = root.querySelector('#misc-filter');
  var chips = Array.prototype.slice.call(root.querySelectorAll('.misc-chip'));
  var sections = Array.prototype.slice.call(root.querySelectorAll('.misc-section'));
  if (!filter || !chips.length || !sections.length) { return; }

  filter.classList.add('is-interactive');

  var status = document.createElement('p');
  status.className = 'misc-filter__status';
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');
  filter.appendChild(status);

  function apply(topic, announce) {
    var shown = 0;
    sections.forEach(function (section) {
      var show = topic === 'all' || section.getAttribute('data-topic') === topic;
      section.hidden = !show;
      if (show) { shown += section.querySelectorAll('.misc-card').length; }
    });
    chips.forEach(function (chip) {
      var on = chip.getAttribute('data-topic') === topic;
      chip.classList.toggle('is-active', on);
      if (on) { chip.setAttribute('aria-current', 'true'); }
      else { chip.removeAttribute('aria-current'); }
    });
    status.textContent = announce
      ? shown + (shown === 1 ? ' reading shown' : ' readings shown')
      : '';
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function (event) {
      event.preventDefault();
      var topic = chip.getAttribute('data-topic');
      apply(topic, true);
      var hash = topic === 'all' ? '#misc-all' : '#topic-' + topic;
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, '', hash);
      }
    });
  });

  var initial = (window.location.hash || '').replace('#topic-', '');
  var known = chips.some(function (c) { return c.getAttribute('data-topic') === initial; });
  if (initial && initial !== 'misc-all' && known) { apply(initial, false); }
})();
</script>
