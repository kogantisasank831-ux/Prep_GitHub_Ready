# Applied GenAI Roadmap — complete website

A self-contained 30-week learning site, with seven beginner alternatives, the
reference-inspired green sidebar layout, guided reading, answer reveals,
search/phase filters, completion tracking and private browser-local notes.
All 30 weeks are included in the published build. Weeks 25–30 remain optional
learning material, not prerequisites for completing the 24-week core track.

## Push this project to GitHub

Copy the contents of this project into the root of your existing **Prep** checkout.
Include the `.github` directory. Keep your existing `.git` directory; this package
does not replace Git history. Do not nest the project inside another `Prep` folder.
Review the changes, then run from your existing checkout:

```sh
git status
git add .
git commit -m "Publish the complete 30-week curriculum"
git push origin main
```

In your GitHub repository, open **Settings → Pages → Build and deployment → Source**
and choose **GitHub Actions**. The included workflow builds and checks the site,
then publishes it after a push to `main`. You can also run **Build and publish
curriculum** manually from the Actions tab. If your default branch is different,
update both `main` references and the deploy condition in `.github/workflows/pages.yml`.

Expected URL for this repository:
<https://kogantisasank831-ux.github.io/Prep/>

The site uses a Python build and static Pages deployment. Ruby/Jekyll is not
required for this workflow. Select GitHub Actions, not the previous branch-based
Jekyll source. No account credentials or model API keys are needed by the site.
The workflow uses GitHub's built-in deployment permissions.

## Preview locally on Windows

Install Python 3.12 or later. From the project root:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-site.txt
.\.venv\Scripts\python.exe scripts/build_site.py --output .preview/Prep
.\.venv\Scripts\python.exe scripts/check_built_site.py --directory .preview/Prep
.\.venv\Scripts\python.exe -m http.server 8000 --directory .preview
```

Open <http://localhost:8000/Prep/>. On macOS/Linux use `python3 -m venv .venv`
and `.venv/bin/python` in place of the Windows Python path. Serving the source
folder directly shows the dashboard but does not build lesson pages.

For a different repository name, set `--baseurl /YourRepository` in the workflow
and preview build command, and use the matching preview folder/URL. For a custom
domain or user-site root, build with `--baseurl ""` and serve the output directly.

## Edit and validate

Canonical lessons live in `content/weeks/`. `Path.md` supplies roadmap titles,
phases and learning objectives. The shared layout and JavaScript supply reading
controls. Edit Markdown and rebuild; do not manually edit generated HTML.

```sh
python -m pip install -r requirements-site.txt
python scripts/build_site.py --output _site
python scripts/check_built_site.py --directory _site
```

The build validates the 30 main lessons and seven alternatives. Link checks cover
all generated pages, local assets and anchors. The GitHub Actions workflow runs
the same commands before deployment. The output includes a no-JavaScript lesson
index at `/Prep/all-weeks/`.

Optional browser verification:

```sh
python -m pip install -r requirements-site-test.txt
python -m playwright install chromium
python scripts/check_site.py --directory _site
```

Site regression tests (after installing `requirements-site-test.txt`):
`python -m pytest -q tests/test_site_build.py --basetemp=.qa/site-tests`.
The temporary directory must stay inside the checkout for output-safety checks.

Build dependencies are pinned in `requirements-site.txt`: Python-Markdown renders
lessons, Python Liquid applies the shared layout, and PyYAML reads repository
configuration/front matter with safe loading. These run only during the build;
the deployed site serves static files. Review pinned versions before upgrading.

Existing service tests need `requirements-dev.txt` and `requirements-site-test.txt`. On Linux:
`python -m pytest -q tests --ignore=tests/test_llm_comparison.py`.
The excluded module uses Windows-only storage; the existing live-model test is
opt-in. These are service examples, not a backend required by the learning site.

## Progress and notes

The existing `applied-genai-roadmap-v1` browser-storage key is retained. Notes and
completion are shared between the dashboard and lesson pages on the same origin.
They do not sync across browsers/devices. A visible notice appears if storage is
blocked. Dark/light preference and the last visited week are remembered too.
No hosted model, analytics account, login service or runtime backend is required.

## Reconstruction and scope

The recovered GitHub source contained Weeks 1–7. The earlier downloadable archive
and its later standalone lab kits were unavailable after workspace maintenance.
Weeks 8–30 and the enhanced site were therefore **reconstructed**, not recovered
byte-for-byte. Each new lesson includes concepts, a worked case, guided and
independent practice, interview preparation, questions, answers and sources.

The original Python/SQL service examples are preserved. The previous nine advanced
lab kits and their historical 488-test report are **not included or re-claimed**.
The new weekly builds are learner exercises; this static site does not execute
agents, train models or serve an LLM. See `content/reviews/site-reconstruction.md`
for actual checks and `content/reviews/reference-topic-coverage.md` for the topic
comparison. Content is available at the owner's request; reconstructed material
has not received an independent human review.
