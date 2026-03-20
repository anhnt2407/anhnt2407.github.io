---
layout: archive
title: "Collaborators"
excerpt: "Selected academic collaborators, mentors, and research partners across dependable systems, aerospace, AI, digital twins, and networked infrastructures."
permalink: /collaborators/
author_profile: true
---

<div class="page-lead">
  <p>Selected academic collaborators, mentors, and research partners across dependable systems, aerospace, AI, digital twins, and networked infrastructures.</p>
  <p class="page-lead__note">Profiles and photos below were cross-checked against official university, lab, or researcher pages in March 2026.</p>
</div>

<div class="collaborator-grid">
{% for collaborator in site.data.collaborators %}
  <article class="collaborator-card">
    <a class="collaborator-card__media" href="{{ collaborator.profile_url }}">
      <img src="{{ site.baseurl }}{{ collaborator.photo }}" alt="Portrait of {{ collaborator.name }}" loading="lazy">
    </a>

    <div class="collaborator-card__content">
      <h2><a href="{{ collaborator.profile_url }}">{{ collaborator.name }}</a></h2>
      <p class="collaborator-card__role">{{ collaborator.position }}</p>
      <p class="collaborator-card__meta">{{ collaborator.institution }}</p>
      <p class="collaborator-card__unit">{{ collaborator.unit }}</p>
      {% if collaborator.summary %}
        <p class="collaborator-card__summary">{{ collaborator.summary }}</p>
      {% endif %}

      {% if collaborator.links %}
        <div class="collaborator-card__links">
          {% for link in collaborator.links %}
            <a href="{{ link.url }}">{{ link.label }}</a>
          {% endfor %}
        </div>
      {% endif %}
    </div>
  </article>
{% endfor %}
</div>
