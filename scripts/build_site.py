"""Build every curriculum page from canonical Markdown for GitHub Pages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import TypedDict
from html import escape
import re
import shutil

import markdown
from liquid import Environment
import yaml

ROOT = Path(__file__).resolve().parents[1]
ASSETS = (
    "index.html",
    "styles.css",
    "week.css",
    "theme.js",
    "shell.js",
    "app.js",
    "week.js",
    "reader.js",
    "storage.js",
    "Path.md",
)


class LessonPage(TypedDict):
    week: int
    beginner: bool
    url: str
    title: str
    words: int


class BuildManifest(TypedDict):
    baseurl: str
    pages: list[LessonPage]
    publication: str


def frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    found = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)", text, re.S)
    if not found:
        raise ValueError(f"{path.name}: missing front matter")
    meta = yaml.safe_load(found[1])
    if not isinstance(meta, dict):
        raise ValueError(f"{path.name}: invalid metadata")
    return meta, found[2]


def build(output: Path, baseurl: str) -> BuildManifest:
    if baseurl and not re.fullmatch(r"/[A-Za-z0-9_-]+", baseurl):
        raise ValueError("baseurl must be empty or one URL-safe path component")
    output = output.resolve()
    if output == ROOT or not output.is_relative_to(ROOT):
        raise ValueError("output must be a new build directory inside the repository")
    if (
        output.exists()
        and any(output.iterdir())
        and not (output / ".prep-build").exists()
    ):
        raise ValueError(
            "refusing to overwrite a directory not created by this builder"
        )
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    (output / ".prep-build").write_text("generated\n")
    site = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    site["baseurl"] = baseurl
    env = Environment()
    env.add_filter("relative_url", lambda value: baseurl + "/" + str(value).lstrip("/"))
    template = env.from_string(
        (ROOT / "_layouts/week.html").read_text(encoding="utf-8")
    )
    expected = {
        int(n): title
        for n, title in re.findall(
            r"^## Week (\d+) — (.+)$",
            (ROOT / "Path.md").read_text(encoding="utf-8"),
            re.M,
        )
    }
    if set(expected) != set(range(1, 31)):
        raise ValueError("Path.md must define weeks 1..30")
    pages: list[LessonPage] = []
    for path in sorted((ROOT / "content/weeks").glob("week-*.md")):
        meta, body = frontmatter(path)
        title = meta.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"{path.name}: missing title")
        number = int(path.name[5:7])
        if meta.get("week", number) != number:
            raise ValueError(f"{path.name}: week metadata mismatch")
        meta["week"] = number
        beginner = path.stem.endswith("-beginner")
        if number not in expected:
            raise ValueError(f"{path.name}: unknown week")
        url = f"/weeks/week-{number:02}/" + ("beginner/" if beginner else "")
        if meta.get("permalink") != url or meta.get("layout") != "week":
            raise ValueError(f"{path.name}: invalid page path/layout")
        if not beginner and number >= 8:
            for required in (
                "## Walk through one case",
                "## Guided practice",
                "## Knowledge check",
                "### Answer key",
                "## Definition of done",
                "## Primary sources",
            ):
                if required not in body:
                    raise ValueError(f"{path.name}: missing {required}")
            if len(body.split()) < 450:
                raise ValueError(f"{path.name}: incomplete lesson")
        meta["previous_url"] = f"/weeks/week-{number - 1:02}/" if number > 1 else None
        meta["next_url"] = f"/weeks/week-{number + 1:02}/" if number < 30 else None
        # Markdown is trusted repository content; it is not rendered from visitor input.
        body = re.sub(
            r"\{\{\s*(['\"])(/[^'\"]*)\1\s*\|\s*relative_url\s*\}\}",
            lambda m: baseurl + m[2],
            body,
        )
        content = markdown.markdown(
            body, extensions=["extra", "toc", "sane_lists"], output_format="html"
        )
        content = re.sub(
            r'href="/(?!/)([^"]*)"',
            lambda m: (
                'href="' + baseurl + "/" + m[1] + '"'
                if not (baseurl and m[1].startswith(baseurl.lstrip("/") + "/"))
                else m[0]
            ),
            content,
        )
        rendered = template.render(page=meta, site=site, content=content)
        destination = output / url.strip("/") / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")
        pages.append(
            {
                "week": number,
                "beginner": beginner,
                "url": url,
                "title": title,
                "words": len(body.split()),
            }
        )
    if len(pages) != 37 or sum(not p["beginner"] for p in pages) != 30:
        raise ValueError("expected 30 main lessons and seven beginner alternatives")
    for name in ASSETS:
        shutil.copyfile(ROOT / name, output / name)
    (output / ".nojekyll").touch()
    all_links = "".join(
        f'<li><a href="{baseurl}{p["url"]}">Week {p["week"]}: {escape(p["title"])}{" (beginner)" if p["beginner"] else ""}</a></li>'
        for p in pages
    )
    (output / "all-weeks").mkdir()
    (output / "all-weeks/index.html").write_text(
        f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>All lessons</title><link rel="stylesheet" href="{baseurl}/styles.css"><main><h1>All lessons</h1><ol>{all_links}</ol></main></html>',
        encoding="utf-8",
    )
    # Existing lessons may link runnable source or SQL. Preserve only explicit teaching trees.
    for directory in ("labs", "document_service", "llm_comparison"):
        if (ROOT / directory).exists():
            shutil.copytree(
                ROOT / directory,
                output / directory,
                ignore=shutil.ignore_patterns(
                    "__pycache__", "*.pyc", ".env", "*.sqlite*"
                ),
            )
    manifest: BuildManifest = {
        "baseurl": baseurl,
        "pages": pages,
        "publication": "All weeks included at owner request; reconstructed content is identified in the source review.",
    }
    (output / "build-manifest.json").write_text(json.dumps(manifest, indent=2))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("_site"))
    parser.add_argument("--baseurl", default="/Prep")
    args = parser.parse_args()
    result = build(args.output, args.baseurl)
    print(
        f"Built {len(result['pages'])} lesson pages at {args.output}; base URL {args.baseurl or '/'}"
    )


if __name__ == "__main__":
    main()
