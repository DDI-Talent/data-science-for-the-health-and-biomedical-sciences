# Data Science for Health and Biomedical Sciences

This repository holds the reusable Quarto course website and a separate tutorial development workspace. Each website resource has one source location. Generated website files are not stored on the source branch.

## Repository layout

| Folder | Purpose and audit decision |
| --- | --- |
| `content/` | Weekly lesson sources, images and downloads. Identical standalone ZIPs and CSVs were consolidated and lesson links updated. |
| `course-information/` | Reusable course guidance. Kept as source pages, including pages accessed through search rather than the sidebar. |
| `images/` | Shared website imagery. Only the referenced course image remains. |
| `tutorials/week-1/`–`week-10/` | Tutorial sources, exercises, solutions, slides and data. Preserved; redundant generated quiz HTML and its libraries were removed. |
| `_freeze/` | Executed lesson output and supporting libraries needed to reproduce the R lessons. Kept; orphaned caches and unused figures were removed. |
| `_extensions/` | Vendored Font Awesome Quarto extension. Kept intact; matching font files in frozen HTML libraries serve a separate build dependency. |
| `.github/` | Workflow that renders, validates and publishes to the `gh-pages` branch. It does not depend on a checked-in website build. |
| `scripts/` | Publication checks. |
| `_site/` | Ignored, disposable output created by `quarto render` or `quarto preview`. Replaces the former tracked `docs/` tree. |
| `.quarto/` | Ignored, disposable local Quarto cache. |
| `.git/` | Repository history and metadata. Kept intact; removing files from the current tree does not erase historical versions. |

The remaining root files configure Quarto and RStudio, document the repository, style the site, or supply its homepage and favicon.

## Develop and publish the website

Install Quarto and R, with the `rmarkdown` and `knitr` R packages. From the repository root:

```sh
quarto preview
```

Build and check the publication output:

```sh
quarto render
python3 scripts/check-site.py
```

Do not edit generated output or reintroduce a tracked `docs/` directory. Edit source files and rebuild. The output is created in `_site/`, which is ignored by Git and can be removed after checking it. Pushing to `main` triggers the existing GitHub Pages workflow, which builds and publishes the configured output directory.

The explicit render list in `_quarto.yml` includes only website sources. Tutorial files are excluded from resource copying too. Do not link to `tutorials/` from website pages: linked resources can otherwise be copied during rendering.

## Develop tutorials

Use each `tutorials/week-N/` folder for session plans, exercises, solutions, slides and supporting data. Keep relative links to supporting files. Review historical cohort instructions before distribution. See [the tutorial workspace guide](tutorials/README.md).

The generated Week 1 quiz HTML and its `_files/` dependencies are ignored. Keep the editable `.qmd` and `.Rmd` files as the source of truth. Tutorial content is excluded from the website; it is still visible if the Git repository is public.

## Resource maintenance

The three former Week 2 project ZIP downloads were byte-identical and now share `cancelled_operations.zip`. Four identical standalone CSVs now share `phs_cancelled1.csv`. Downloads packaged as complete R projects intentionally retain their own data and original filenames so their scripts work after extraction. Editor caches, session histories and operating-system metadata have been removed from the ZIPs, preserving every teaching file.

Three unlinked supporting files remain in the repository but are excluded from publication: `phs_cancelled_tidy.Rda`, `Be_fruitful_and_multiply.pdf`, and `Combined_example.Rmd`. To publish one, link it from a lesson and remove its resource exclusion in `_quarto.yml`.

The unused-asset audit also removed five unreferenced images, the superseded `Guyan_Biomedical_sciences_slides.pdf`, an empty NHS R placeholder, two caches without source pages and two unused cached figures. The Git glossary, functions practice solutions and older “Visibility of what?” slide page remain as teaching content; absence from the sidebar alone is not a reason to delete a page.

## Reuse each year

Keep academic years, dates, class times, teaching allocations, assessment deadlines and cohort repository links in Learn. The website points students there for current arrangements. Retain publication years in citations and years in example datasets.
