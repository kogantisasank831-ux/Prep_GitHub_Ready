# Site reconstruction and publication handoff

Reconstruction: 2026-10-07. Delivery: 2026-10-08. Source baseline: a360bd5d44904e7fb2f2b289bddd2ae181a122fa.

The owner's current request is a single pushable working site with every week.
Workspace maintenance removed the earlier local branch and ZIP. Saved-file
search/listing found no curriculum archive. GitHub contained Weeks 1–7 only.
This pass reconstructs the missing weekly pages and site enhancements; it does
not claim that unavailable source or earlier test results were recovered.

Inspected root AGENTS.md, plan.md, Path.md, the shared layout, dashboard, shell,
theme and reading scripts, original lesson front matter and service requirements.
Only root AGENTS.md applies. It describes a finance application and absent Design
folder; the user's explicit curriculum request and actual Path.md define this
work's scope. No finance-app functionality or unrelated API changes were made.

## Changes

- All thirty numbered lessons are available in the generated site, plus seven
  existing beginner alternatives. Reconstructed Weeks 8–30 contain approximately
  800–970 words each, concepts, worked cases, exercises, interview bridges,
  answer keys, completion criteria and primary links.
- The original first seven canonical lesson bodies are preserved.
- Restored a compact green/white reference-style UI and guided section reading,
  full-lesson view, answer reveals, deep links, no-JS content and print behavior.
- Shared notes/completion storage, retained the original storage key, added
  resume navigation and graceful behavior when storage is blocked.
- Added a reproducible Python Markdown/Liquid build and local-link validator.
  GitHub Actions publishes this exact static output, removing the earlier
  unverified native-Jekyll requirement. Source remains Markdown, not hand-edited HTML.
- Included Windows-friendly setup and Git push/Pages configuration instructions.

The explicit request to make the complete site pushable supersedes the earlier
plan's default withholding of later pages. Availability is not a claim of human
content approval. Metadata identifies reconstructed pages; no independent reviewer
or model experiment is invented. The owner controls the actual push/publication.

## Verification

Executed checks:

- Production builder: 37 lesson pages (all 30 weeks and seven alternatives).
- Generated output validator: 39 HTML pages; local links, assets and anchors pass.
- Browser: all 37 lessons opened; search, phase filters, guided/full reading,
  answer reveals, deep links, mobile menu, notes/completion persistence, resume,
  theme, no-JavaScript reading and blocked storage checks passed. No JavaScript
  errors or failed local requests; five screenshots captured, with desktop/mobile
  views visually inspected.
- Python regression/service tests: 30 passed, one opt-in live-model test skipped.
  The Windows-only comparison test module was excluded on Linux. Four new site
  tests cover root/custom base paths, broken-link detection and overwrite protection.
- All 44 unique primary-source URLs in reconstructed lessons resolved during
  the source check. Topic coverage is mapped in reference-topic-coverage.md.
- JavaScript syntax, Ruff, strict mypy (four new Python files) and dependency
  consistency checks passed.

Source-link resolution and software build checks do not prove every teaching
claim or external page stays current.
The model/framework exercises require the learner to run and record their own
results. No advanced backend, GPU run, hosted model or paid provider is required
to host this learning website.

## Unavailable earlier work

The old nine standalone advanced lab kits, model artifacts and 488-test report
could not be recovered. They are not silently replaced with claimed equivalent
implementations. Existing Python/SQL examples from GitHub remain included.
If the old archive becomes available, merge those kits separately without
replacing the now-working site and rebuilt content blindly.

No remote push or live deployment was performed. The local built-site/browser
checks are distinct from an actual GitHub Actions run in the owner's account.
