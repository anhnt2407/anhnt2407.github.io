# Tuan Anh Nguyen — personal academic website

Source for <https://anhnt2407.github.io>. Jekyll, deployed by GitHub Pages.

## Where things live

### Pages

| Page | Source | Data it reads |
| --- | --- | --- |
| `/` | `_pages/about.md` | — |
| `/news/` | `_pages/news.md` | — |
| `/research/` | `research/research.md` + three track pages | — |
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
responsive    breakpoint overrides — must stay last
```

`foundation` defines the custom properties (`--accent`, `--surface`,
`--text-muted`, …) that every other partial builds on, so it has to be imported
first, and `responsive` overrides earlier rules, so it has to be imported last.

### Templates and assets

- `_layouts/` — page skeletons; `_includes/` — reusable fragments.
- `_includes/misc_visual.html` and `_includes/teaching_icon.html` render inline
  SVG artwork from a name passed by the page.
- `images/` — content imagery, grouped by page and by date for news items.
- `assets/` — fonts, site JavaScript and figures used by the research pages.
- `scripts/generate_misc_covers.py` — regenerates the Notes & Links cover art.

## Working on the site

The publication list, teaching record and supervision record are transcribed
from the LaTeX CV and must be kept in step with it; the identifiers in
`_pages/publications.md` are referenced from the teaching page.

Pushing to `master` triggers the workflow in
`.github/workflows/jekyll-gh-pages.yml`, which builds and deploys the site.
