"""Check actual generated pages and all local page/asset links before publication."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(str(values["id"]))
        if tag == "title":
            self.title = True
        if tag in {"a", "script", "link", "img"}:
            target = values.get("href") or values.get("src")
            if target:
                self.links.append(target)


def check(directory: Path) -> None:
    directory = directory.resolve()
    manifest = json.loads(
        (directory / "build-manifest.json").read_text(encoding="utf-8")
    )
    prefix = manifest["baseurl"]
    assert len(manifest["pages"]) == 37
    assert {p["week"] for p in manifest["pages"] if not p["beginner"]} == set(
        range(1, 31)
    )
    parsed: dict[Path, Page] = {}
    for file in directory.rglob("*.html"):
        parser = Page()
        text = file.read_text(encoding="utf-8")
        parser.feed(text)
        assert parser.title, f"No title: {file}"
        assert "{{ page." not in text and "{% if" not in text, (
            f"Unrendered template: {file}"
        )
        parsed[file] = parser
    errors = []
    for file, parser in parsed.items():
        address = (
            "https://local.invalid"
            + prefix
            + "/"
            + file.relative_to(directory).as_posix()
        )
        for link in parser.links:
            absolute = urlsplit(urljoin(address, link))
            if absolute.netloc != "local.invalid" or absolute.scheme not in {
                "http",
                "https",
            }:
                continue
            path = unquote(absolute.path)
            if prefix and not path.startswith(prefix + "/"):
                errors.append(f"{file.relative_to(directory)}: outside baseurl {link}")
                continue
            target = directory / path[len(prefix) :].lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                errors.append(f"{file.relative_to(directory)}: missing {link}")
            elif (
                absolute.fragment
                and target in parsed
                and unquote(absolute.fragment) not in parsed[target].ids
            ):
                # Dashboard cards are created from Path.md at runtime.
                if not (
                    target == directory / "index.html"
                    and absolute.fragment.startswith("week-")
                ):
                    errors.append(
                        f"{file.relative_to(directory)}: missing anchor {link}"
                    )
    if errors:
        raise ValueError("\n".join(errors))
    print(
        f"PASS: {len(parsed)} HTML pages; 30 weeks, seven alternatives, local links/assets and anchors"
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--directory", type=Path, default=Path("_site"))
    check(p.parse_args().directory)
