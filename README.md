# Data Science for Health and Biomedical Sciences

This repository contains the reusable Quarto course website and a separate workspace for tutorial development.

- `index.qmd`, `content/`, `course-information/`: published learning materials.
- `content/documents/`: resources used by the published self-guided topics.
- `tutorials/week-1/` through `tutorials/week-10/`: session plans, exercises, solutions, slides and data for development. Existing tutorial pages and dedicated resources have been moved here.
- `docs/`: generated website; regenerate rather than editing by hand.

## Develop the website

Install Quarto and R, with the `rmarkdown` and `knitr` R packages. Run from the repository root:

```sh
quarto preview
```

Build and check the published output:

```sh
quarto render
python3 scripts/check-site.py
```

The explicit render list in `_quarto.yml` includes only the website source directories. Tutorial files are also excluded from resources. Do not link to `tutorials/` from website pages: linked resources can otherwise be copied during rendering. The publication workflow checks the output before deploying to GitHub Pages.

## Develop tutorials

Put each week's material in its matching `tutorials/week-N/` folder. Keep supporting files alongside the exercise, using relative links. Existing instructions are preserved for development and may refer to previous cohorts; review them before distributing them. See [the tutorial workspace guide](tutorials/README.md).

## Reuse each year

Keep academic years, dates, class times, named teaching allocations, assessment deadlines and cohort repository links in Learn. The website points students there for current arrangements. Publication years in citations and years in example datasets are intentional and should be retained.

Update the reusable learning content as needed. Pushing to `main` triggers the existing GitHub Pages workflow; tutorial content stays in the repository and is not included in the website. Repository visibility is separate from website publication: these folders are not private if the repository is public.
