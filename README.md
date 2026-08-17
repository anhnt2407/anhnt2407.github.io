# Tuan Anh Nguyen — personal academic website

Source for <https://anhnt2407.github.io>. Jekyll, deployed by GitHub Pages.

## Where things live

### Pages

| Page | Source | Data it reads |
| --- | --- | --- |
| `/` | `_pages/about.md` | — |
| `/news/` | `_pages/news.md` | — |
| `/research/` | `research/research.md` + three track pages | — |
| `/projects/` | `_pages/projects.md` | `projects.yml`, `project_eras.yml`, `project_domains.yml`, `project_outputs.yml` |
| `/publications/` | `_pages/publications.md` | — |
| `/teaching/` | `_pages/teaching.md` | `teaching*.yml`, `students.yml`, `student_groups.yml` |
| `/collaborators/` | `_pages/collaborators.md` | `collaborators.yml` |
| `/miscellaneous/` | `_pages/miscellaneous.md` | `misc_posts.yml`, `misc_topics.yml` |

Content that repeats in a list lives in `_data/` as YAML rather than in the page,
so it can be edited without touching markup. `_data/navigation.yml` drives the
top navigation bar.

### Styling

Theme partials sit directly in `_sass/`. Everything written for this site is in
`_sass/site/`, one partial per area, imported in order at the bottom of
`assets/css/main.scss`:

```
foundation    design tokens, base typography, small helpers
masthead      sticky masthead and the greedy navigation bar
layout        page shell, article surfaces, author sidebar
home          home hero, calls to action, focus cards
research      research track cards
news          news date stamps, story cards, illustrations
experience    experience and education cards, figure grids
publications  publication identifier tags
collaborators collaborator cards
misc          notes and links hero, theme filter, reading cards
footer        site footer
teaching      teaching and supervision hero, filter, timeline, people
projects      programme hero, Gantt timeline, filter, project cards, artwork
responsive    breakpoint overrides — must stay after the area partials
theme-dark    dark-mode corrections that a token swap cannot express
```

`foundation` defines the custom properties (`--accent`, `--surface`,
`--text-muted`, …) that every other partial builds on, so it has to be imported
first, and `responsive` overrides earlier rules, so it stays after the area
partials.

### Light and dark themes

Both themes come from one set of custom properties in `_sass/site/_foundation.scss`:
`:root` carries the light values, and the `site-dark-tokens` mixin carries the
dark ones. That mixin is applied twice — under `:root[data-theme="dark"]` for an
explicit choice, and under `:root:not([data-theme="light"])` inside a
`prefers-color-scheme: dark` media query for visitors who have expressed none. A
visitor therefore gets their operating system's setting until they press the
toggle; after that their choice is stored in `localStorage` and wins.

Because of that, colours in the partials must be written as `var(--token)`
rather than as literals. The exceptions are surfaces that are dark in *both*
themes — the home hero, the teaching route panel and the news card washes — where
white text and glazes stay hard-coded on purpose.

The toggle itself is three pieces: the button in `_includes/masthead.html` (kept
outside `#site-nav`, because the greedy navigation script claims every `button`
inside it), the click and labelling logic at the end of `_includes/scripts.html`,
and a short script in `_includes/head.html` that applies the stored choice before
the stylesheet loads so the page never flashes the wrong theme.
`_sass/site/_theme-dark.scss` holds the few dark-mode rules that a token swap
cannot express, mostly re-deriving the per-topic `--*-ink` colours, which are
dark by design, from their bright partner hue.

### Templates and assets

- `_layouts/` — page skeletons; `_includes/` — reusable fragments.
- `_includes/misc_visual.html`, `_includes/teaching_icon.html` and
  `_includes/project_visual.html` render inline SVG artwork from a name passed
  by the page. The project artwork is drawn in `var(--proj-accent)`, so a card
  simply sets that custom property and the diagram follows the card's accent in
  both themes.
- `images/` — content imagery, grouped by page and by date for news items.
- `assets/` — fonts, site JavaScript and figures used by the research pages.
- `scripts/generate_misc_covers.py` — regenerates the Notes & Links cover art.

## Working on the site

The publication list, teaching record, supervision record and project list are
transcribed from the LaTeX CV and must be kept in step with it; the identifiers
in `_pages/publications.md` are referenced from the teaching and projects pages.

`_data/projects.yml` carries two date pairs per programme: `start`/`end` are the
period Tuan Anh personally worked on it and drive the solid Gantt bar, while
`prog_start`/`prog_end` are the full funded span and drive the faint bar behind
it. Both are decimal years on a 2009–2030 axis (`(year − 2009) × 4.7619` gives
the percentage). Where the two differ, add a `programme_note` so the card says
plainly that the grant outlived the appointment.

Pushing to `master` triggers the workflow in
`.github/workflows/jekyll-gh-pages.yml`, which builds and deploys the site.
