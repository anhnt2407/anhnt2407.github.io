---
layout: archive
title: "Teaching & Supervision"
excerpt: "Every course taught since 2020 in Vietnam, South Korea and the United States, and every student supervised or co-supervised since 2015."
permalink: /teaching/
author_profile: true
---

{%- assign courses = site.data.teaching -%}
{%- assign years = site.data.teaching_years -%}
{%- assign schools = site.data.teaching_institutions -%}
{%- assign students = site.data.students -%}
{%- assign labs = site.data.student_groups -%}

{%- assign distinct_courses = courses | map: "title" | uniq -%}
{%- assign grad_courses = courses | where: "level", "graduate" -%}
{%- assign ug_courses = courses | where: "level", "undergraduate" -%}

{%- assign enrolled = 0 -%}
{%- for c in courses -%}{%- if c.students -%}{%- assign enrolled = enrolled | plus: c.students -%}{%- endif -%}{%- endfor -%}

{%- assign supervised = 0 -%}
{%- assign phd_count = 0 -%}
{%- assign msc_count = 0 -%}
{%- assign beng_count = 0 -%}
{%- assign joint_ids = "" -%}
{%- assign joint_count = 0 -%}
{%- for s in students -%}
  {%- assign supervised = supervised | plus: s.head_count -%}
  {%- if s.degree_key == "phd" -%}{%- assign phd_count = phd_count | plus: s.head_count -%}{%- endif -%}
  {%- if s.degree_key == "msc" -%}{%- assign msc_count = msc_count | plus: s.head_count -%}{%- endif -%}
  {%- if s.degree_key == "beng" -%}{%- assign beng_count = beng_count | plus: s.head_count -%}{%- endif -%}
  {%- for p in s.publications -%}
    {%- assign marker = p | append: "," -%}
    {%- unless joint_ids contains marker -%}
      {%- assign joint_ids = joint_ids | append: marker -%}
      {%- assign joint_count = joint_count | plus: 1 -%}
    {%- endunless -%}
  {%- endfor -%}
{%- endfor -%}

<div class="teach-root">

  <section class="teach-hero" aria-labelledby="teach-hero-title">
    <div class="teach-hero__copy">
      <p class="teach-kicker">Classroom &amp; laboratory</p>
      <h2 id="teach-hero-title">Eight courses across three countries, thirteen students supervised</h2>
      <p>
        Teaching has followed the research: dependability and cloud modelling in Seoul, digital twins
        and autonomous flight at the aerospace institute, and now machine learning and digital
        transformation for engineers in Ho Chi Minh City. This page lists every course offering on
        record and every student whose thesis I supervised or co-supervised.
      </p>
      <dl class="teach-hero__stats" aria-label="Teaching and supervision in numbers">
        <div><dt>Offerings</dt><dd>{{ courses | size }}</dd></div>
        <div><dt>Distinct courses</dt><dd>{{ distinct_courses | size }}</dd></div>
        <div><dt>Institutions</dt><dd>{{ schools | size }}</dd></div>
        <div><dt>Students</dt><dd>{{ supervised }}</dd></div>
        <div><dt>Enrolments</dt><dd>{{ enrolled }}</dd></div>
      </dl>
      <p class="teach-hero__footnote">
        Enrolments are counted per section as recorded in the course files; a student taking two of my
        courses appears in both. The three graduate seminars in Seoul and Los Angeles carry no
        headcount in the record and are not included in that figure.
      </p>
    </div>

    <aside class="teach-hero__panel" aria-labelledby="teach-route-title">
      <svg class="teach-hero__stars" viewBox="0 0 400 520" aria-hidden="true" focusable="false" preserveAspectRatio="none">
        <path class="teach-hero__grid" d="M0 90 H400 M0 190 H400 M0 290 H400 M0 390 H400 M0 470 H400" />
        <path class="teach-hero__grid" d="M70 0 V520 M150 0 V520 M230 0 V520 M310 0 V520" />
        <circle class="teach-hero__spark" cx="332" cy="72" r="3" />
        <circle class="teach-hero__spark" cx="58" cy="166" r="2" />
        <circle class="teach-hero__spark" cx="286" cy="254" r="2.5" />
        <circle class="teach-hero__spark" cx="104" cy="392" r="3" />
        <circle class="teach-hero__spark" cx="352" cy="446" r="2" />
      </svg>

      <p class="teach-route-title" id="teach-route-title">Where the teaching happened</p>
      <ol class="teach-route">
        {% for s in schools %}{% assign sc = courses | where: "institution", s.slug %}
        <li class="teach-route__stop teach-route__stop--{{ s.accent }}">
          <span class="teach-route__flag" aria-hidden="true">{{ s.flag }}</span>
          <span class="teach-route__city">{{ s.city }}, {{ s.country }}</span>
          <span class="teach-route__school">{{ s.full }}</span>
          <span class="teach-route__years">{{ s.span }} · {{ sc | size }} {% if sc.size == 1 %}offering{% else %}offerings{% endif %}</span>
        </li>
        {% endfor %}
      </ol>
    </aside>
  </section>

  <h2 class="teach-heading" id="courses">Courses taught</h2>
  <p class="teach-heading__lead">
    {{ courses | size }} offerings of {{ distinct_courses | size }} distinct courses, newest first.
    {{ grad_courses | size }} graduate and {{ ug_courses | size }} undergraduate, with course codes,
    class codes and enrolment exactly as they appear in the course files.
  </p>

  <nav class="teach-filter" id="teach-filter" aria-label="Filter courses" hidden>
    <div class="teach-filter__group">
      <p class="teach-filter__label" id="teach-facet-institution">Institution</p>
      <div class="teach-filter__chips" role="group" aria-labelledby="teach-facet-institution">
        <button type="button" class="teach-chip is-active" data-facet="institution" data-value="all" aria-pressed="true">All<span class="teach-chip__count">{{ courses | size }}</span></button>
        {% for s in schools %}{% assign sc = courses | where: "institution", s.slug %}
        <button type="button" class="teach-chip teach-chip--{{ s.accent }}" data-facet="institution" data-value="{{ s.slug }}" aria-pressed="false">{{ s.label }}<span class="teach-chip__count">{{ sc | size }}</span></button>
        {% endfor %}
      </div>
    </div>

    <div class="teach-filter__group">
      <p class="teach-filter__label" id="teach-facet-level">Level</p>
      <div class="teach-filter__chips" role="group" aria-labelledby="teach-facet-level">
        <button type="button" class="teach-chip is-active" data-facet="level" data-value="all" aria-pressed="true">All<span class="teach-chip__count">{{ courses | size }}</span></button>
        <button type="button" class="teach-chip teach-chip--indigo" data-facet="level" data-value="graduate" aria-pressed="false">Graduate<span class="teach-chip__count">{{ grad_courses | size }}</span></button>
        <button type="button" class="teach-chip teach-chip--green" data-facet="level" data-value="undergraduate" aria-pressed="false">Undergraduate<span class="teach-chip__count">{{ ug_courses | size }}</span></button>
      </div>
    </div>
  </nav>

  <div class="teach-timeline" id="teach-timeline">
    {% for y in years %}{% assign yc = courses | where: "year", y.year %}
    <section class="teach-year" data-year="{{ y.year }}" aria-labelledby="teach-year-{{ y.year }}">
      <div class="teach-year__spine" aria-hidden="true"><span class="teach-year__dot"></span></div>

      <div class="teach-year__main">
        <header class="teach-year__head">
          <h3 id="teach-year-{{ y.year }}">{{ y.year }}<span class="teach-year__count">{{ yc | size }} {% if yc.size == 1 %}offering{% else %}offerings{% endif %}</span></h3>
          <p>{{ y.note }}</p>
        </header>

        <div class="teach-year__courses">
          {% for c in yc %}
          <article class="teach-course teach-course--{{ c.institution }}"
                   id="course-{{ c.slug }}"
                   data-institution="{{ c.institution }}"
                   data-level="{{ c.level }}">
            <div class="teach-course__glyph">{% include teaching_icon.html icon=c.icon %}</div>

            <div class="teach-course__body">
              <div class="teach-course__badges">
                <span class="teach-badge teach-badge--level">{{ c.level_label }}</span>
                {% if c.status == "current" %}<span class="teach-badge teach-badge--live">Now teaching</span>{% endif %}
                {% if c.course_code %}<span class="teach-badge teach-badge--code">Course {{ c.course_code }}</span>{% endif %}
                {% if c.class_name %}<span class="teach-badge teach-badge--code">Class {{ c.class_name }}</span>{% endif %}
              </div>

              <h4>{{ c.title }}</h4>
              {% if c.programme %}<p class="teach-course__programme">{{ c.programme }}</p>{% endif %}
              <p class="teach-course__where">{{ c.unit }}<br><strong>{{ c.institution_label }}</strong> · {{ c.location }}</p>
              <p class="teach-course__term"><span>{{ c.term }}</span>{{ c.period }}</p>
              {% if c.role %}<p class="teach-course__role">{{ c.role }}</p>{% endif %}
              {% if c.venue %}<p class="teach-course__venue">{{ c.venue }}</p>{% endif %}

              {% if c.facts %}
              <dl class="teach-facts">
                {% for f in c.facts %}<div><dt>{{ f.label }}</dt><dd>{{ f.value }}</dd></div>{% endfor %}
              </dl>
              {% endif %}

              {% if c.sections %}
              <ul class="teach-sections" aria-label="Sections of {{ c.title | escape }}">
                {% for sec in c.sections %}
                <li>
                  <span class="teach-sections__class">{{ sec.class_name }}</span>
                  {% if sec.code %}<span class="teach-sections__code">§ {{ sec.code }}</span>{% endif %}
                  <span class="teach-sections__count">{{ sec.students }} students</span>
                </li>
                {% endfor %}
              </ul>
              {% endif %}
            </div>
          </article>
          {% endfor %}
        </div>
      </div>
    </section>
    {% endfor %}
  </div>

  <h2 class="teach-heading" id="supervision">Students supervised</h2>
  <p class="teach-heading__lead">
    {{ supervised }} students across {{ labs | size }} labs and faculties in South Korea and Vietnam, from
    the first master's theses on cloud dependability in 2015 to the graduation projects defended in
    Ho Chi Minh City this year. Where a thesis
    turned into joint work, the publication identifiers link straight to the entry on the
    <a href="{{ site.baseurl }}/publications/">publications page</a>.
  </p>

  <dl class="teach-degree-tally" aria-label="Supervised students by degree">
    <div class="teach-degree-tally__item teach-degree-tally__item--phd"><dt>Ph.D.</dt><dd>{{ phd_count }}</dd></div>
    <div class="teach-degree-tally__item teach-degree-tally__item--msc"><dt>M.Sc.</dt><dd>{{ msc_count }}</dd></div>
    <div class="teach-degree-tally__item teach-degree-tally__item--beng"><dt>B.Eng.</dt><dd>{{ beng_count }}</dd></div>
    <div class="teach-degree-tally__item teach-degree-tally__item--pubs"><dt>Joint publications</dt><dd>{{ joint_count }}</dd></div>
  </dl>

  <div class="teach-labs">
    {% for lab in labs %}{% assign people = students | where: "group", lab.slug %}
    <section class="teach-lab teach-lab--{{ lab.accent }}" id="lab-{{ lab.slug }}" aria-labelledby="lab-{{ lab.slug }}-title">
      <header class="teach-lab__head">
        <h3 id="lab-{{ lab.slug }}-title">{{ lab.label }}<span class="teach-lab__count">{{ people | size }}</span></h3>
        <p class="teach-lab__where">{{ lab.institution }} · {{ lab.location }} · {{ lab.span }}</p>
        <p class="teach-lab__blurb">{{ lab.blurb }}</p>
      </header>

      <div class="teach-people">
        {% for p in people %}
        <article class="teach-person" id="student-{{ p.slug }}">
          <div class="teach-person__mono {% if p.team %}teach-person__mono--team{% endif %}" aria-hidden="true">{{ p.initials }}</div>

          <div class="teach-person__body">
            <div class="teach-person__badges">
              <span class="teach-badge teach-badge--{{ p.degree_key }}">{{ p.degree }}</span>
              <span class="teach-badge teach-badge--period">{{ p.period }}</span>
              {% if p.role %}<span class="teach-badge teach-badge--role">{{ p.role }}</span>{% endif %}
            </div>

            <h4>{{ p.name }}</h4>
            <p class="teach-person__meta">{{ p.degree_label }} · {{ p.unit }}, {{ p.institution }}</p>

            <p class="teach-person__thesis">{{ p.thesis }}</p>
            {% if p.detail %}<p class="teach-person__detail">{{ p.detail }}</p>{% endif %}
            {% if p.award %}<p class="teach-person__award">{{ p.award }}</p>{% endif %}

            {% if p.now %}<p class="teach-person__now"><span>Now</span>{{ p.now }}</p>{% endif %}

            {% if p.publications %}
            <div class="teach-person__pubs">
              <span class="teach-person__pubs-label">Joint publications{% if p.cited_as %} <em>(cited as {{ p.cited_as }})</em>{% endif %}</span>
              <span class="teach-person__pubs-chips">
                {% for id in p.publications %}<a class="teach-pub-chip" href="{{ site.baseurl }}/publications/#pub-{{ id }}">{{ id }}</a>{% endfor %}
              </span>
            </div>
            {% endif %}
          </div>
        </article>
        {% endfor %}
      </div>
    </section>
    {% endfor %}
  </div>

  <h2 class="teach-heading" id="alumni">Where they went next</h2>
  <p class="teach-heading__lead">Destinations recorded for former students at the time of writing.</p>

  <div class="teach-alumni">
    <article class="teach-alumni__card teach-alumni__card--cyan">
      <p class="teach-alumni__count">3</p>
      <h3>Korea Aerospace Industries (KAI)</h3>
      <p class="teach-alumni__role">Research engineers</p>
      <p class="teach-alumni__names">Jeongseok Hyun · Min-Seok Jang · Tae-Ho Kwag</p>
    </article>

    <article class="teach-alumni__card teach-alumni__card--indigo">
      <p class="teach-alumni__count">1</p>
      <h3>Kyung Hee University</h3>
      <p class="teach-alumni__role">Ph.D. candidate</p>
      <p class="teach-alumni__names">Luyao Zhou</p>
    </article>

    <article class="teach-alumni__card teach-alumni__card--green">
      <p class="teach-alumni__count">1</p>
      <h3>Haezoom, Seoul</h3>
      <p class="teach-alumni__role">Back-end developer, first employment</p>
      <p class="teach-alumni__names">Ki-Hong Han</p>
    </article>

    <article class="teach-alumni__card teach-alumni__card--amber">
      <p class="teach-alumni__count">1</p>
      <h3>Myanmar</h3>
      <p class="teach-alumni__role">Returned home after the thesis</p>
      <p class="teach-alumni__names">Nang Lung Aung</p>
    </article>
  </div>

  <h2 class="teach-heading" id="beyond">Beyond the course list</h2>
  <p class="teach-heading__lead">Mentoring that sits outside a course code, and the credential behind the lectureship in Vietnam.</p>

  <div class="teach-notes">
    <article class="teach-note">
      <p class="teach-note__eyebrow">Research programme</p>
      <h3>AI Digital Twin for Smart Urban Air Mobility</h3>
      <p>
        Project technical leader and lead researcher of the nine-year Excellent Research Center project
        funded by Korea's National Research Foundation (approximately KRW 7.7 billion, grant
        2020R1A6A1A03046811), with a standing team of around 30 full-time M.Sc. and Ph.D. researchers.
        Most of the KADA theses on this page grew out of that programme.
      </p>
    </article>

    <article class="teach-note">
      <p class="teach-note__eyebrow">Graduate R&amp;D training</p>
      <h3>Training Experts in Future Automobile R&amp;D</h3>
      <p>
        Lead researcher on this professional education project of the Korean Ministry of Trade, Industry
        and Energy (2022–2027), designing and supervising graduate-level R&amp;D projects on autonomous
        navigation, SLAM and deep reinforcement learning, sensor-data processing and reliable vehicle
        service infrastructures, and coordinating the student researchers who carried them out.
      </p>
    </article>

    <article class="teach-note">
      <p class="teach-note__eyebrow">Credential</p>
      <h3>University lecturer standards, Vietnam</h3>
      <p>
        Certificate of Professional Development in the Professional Title Standards for University
        Lecturers, the national teaching credential required of university faculty in Vietnam, issued
        7 November 2024 by the University of Social Sciences and Humanities, VNU-HCM (cohort 7,
        programme completed 16 August – 9 October 2024).
      </p>
    </article>
  </div>
</div>

<script>(function () {
  var root = document.querySelector('.teach-root');
  if (!root) { return; }

  var filter = root.querySelector('#teach-filter');
  var timeline = root.querySelector('#teach-timeline');
  if (!filter || !timeline) { return; }

  var chips = Array.prototype.slice.call(filter.querySelectorAll('.teach-chip'));
  var courses = Array.prototype.slice.call(timeline.querySelectorAll('.teach-course'));
  var yearBlocks = Array.prototype.slice.call(timeline.querySelectorAll('.teach-year'));
  if (!chips.length || !courses.length) { return; }

  var state = { institution: 'all', level: 'all' };

  var status = document.createElement('p');
  status.className = 'teach-filter__status';
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');
  filter.appendChild(status);

  var reset = document.createElement('button');
  reset.type = 'button';
  reset.className = 'teach-filter__reset';
  reset.textContent = 'Show all courses';
  reset.hidden = true;
  filter.appendChild(reset);

  function matches(card) {
    var byInstitution = state.institution === 'all' ||
      card.getAttribute('data-institution') === state.institution;
    var byLevel = state.level === 'all' ||
      card.getAttribute('data-level') === state.level;
    return byInstitution && byLevel;
  }

  function apply(announce) {
    var shown = 0;

    courses.forEach(function (card) {
      var show = matches(card);
      card.hidden = !show;
      if (show) { shown += 1; }
    });

    yearBlocks.forEach(function (block) {
      var visible = block.querySelectorAll('.teach-course:not([hidden])').length;
      block.hidden = visible === 0;
    });

    chips.forEach(function (chip) {
      var on = state[chip.getAttribute('data-facet')] === chip.getAttribute('data-value');
      chip.classList.toggle('is-active', on);
      chip.setAttribute('aria-pressed', on ? 'true' : 'false');
    });

    var filtered = state.institution !== 'all' || state.level !== 'all';
    reset.hidden = !filtered;
    timeline.classList.toggle('is-filtered', filtered);

    status.textContent = announce
      ? shown + (shown === 1 ? ' course offering shown' : ' course offerings shown')
      : '';
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      state[chip.getAttribute('data-facet')] = chip.getAttribute('data-value');
      apply(true);
    });
  });

  reset.addEventListener('click', function () {
    state.institution = 'all';
    state.level = 'all';
    apply(true);
  });

  filter.hidden = false;
  filter.classList.add('is-interactive');
  apply(false);
})();
</script>
