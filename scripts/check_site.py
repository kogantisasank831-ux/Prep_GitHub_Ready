"""Exercise the built curriculum in a real browser, including saved-state failures."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import threading
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path("_site"))
    parser.add_argument("--screenshots", type=Path, default=Path(".qa/screenshots"))
    args = parser.parse_args()
    manifest = json.loads(
        (args.directory / "build-manifest.json").read_text(encoding="utf-8")
    )
    prefix = manifest["baseurl"]

    class Handler(SimpleHTTPRequestHandler):
        def log_message(self, *args: object) -> None:
            pass

        def translate_path(self, path: str) -> str:
            if prefix and (path == prefix or path.startswith(prefix + "/")):
                path = path[len(prefix) :] or "/"
            return super().translate_path(path)

    server = ThreadingHTTPServer(
        ("127.0.0.1", 0), partial(Handler, directory=str(args.directory.resolve()))
    )
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}{prefix}/"
    args.screenshots.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    failed: list[str] = []
    launch = {}
    config = os.environ.get("PREP_BROWSER_CONFIG")
    if config:
        settings = json.loads(Path(config).read_text(encoding="utf-8"))
        launch = {
            "executable_path": settings["path"],
            "args": settings["args"],
            "env": dict(os.environ, LD_LIBRARY_PATH=settings.get("library") or ""),
        }
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(**launch)
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            page = context.new_page()
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.on(
                "response",
                lambda r: (
                    failed.append(r.url)
                    if r.status >= 400 and urlsplit(r.url).hostname == "127.0.0.1"
                    else None
                ),
            )
            page.goto(base)
            page.wait_for_selector(".week-card")
            assert page.locator(".week-card").count() == 30
            assert page.locator(".week-direct-link:visible").count() == 30
            page.screenshot(
                animations="disabled",
                path=str(args.screenshots / "dashboard-desktop.png"),
            )
            page.locator("#search").fill("LoRA")
            assert page.locator(".week-card").count() > 0
            page.locator("#search").fill("no-such-topic-xyz")
            assert page.locator("#empty-state").is_visible()
            page.locator("#search").fill("")
            page.get_by_role("button", name="Phase 2", exact=True).click()
            assert page.locator(".week-card").count() == 4
            page.get_by_role("button", name="All phases", exact=True).click()
            for entry in manifest["pages"]:
                page.goto(base.rstrip("/") + entry["url"])
                page.wait_for_selector(".lesson-chapter:visible")
                assert page.locator(".app-week-link").count() == 30
                assert page.locator(".lesson-chapter:visible").count() == 1
                assert page.locator("h1").first.inner_text().strip()
                assert page.evaluate(
                    "document.documentElement.scrollWidth <= innerWidth+1"
                ), entry["url"]
                page.get_by_role("button", name="Next section →", exact=True).click()
                assert page.locator(".lesson-chapter:visible").count() == 1
                page.get_by_role("button", name="Show full lesson", exact=True).click()
                assert page.locator(".lesson-chapter:visible").count() > 1
                page.get_by_role(
                    "button", name="Read section by section", exact=True
                ).click()
            for n in [8, 15, 30]:
                page.goto(base + f"weeks/week-{n:02}/#knowledge-check")
                assert (
                    page.locator(".lesson-chapter:visible h2").inner_text()
                    == "Knowledge check"
                )
                page.get_by_text("Reveal answer key", exact=True).click()
                assert (
                    page.locator(".lesson-chapter:visible details[open]").count() == 1
                )
                page.set_viewport_size({"width": 390, "height": 844})
                page.wait_for_function("document.querySelector('#app-sidebar').inert")
                assert page.evaluate(
                    "document.documentElement.scrollWidth <= innerWidth+1"
                )
                page.screenshot(
                    animations="disabled",
                    path=str(args.screenshots / f"week-{n}-mobile.png"),
                )
                page.get_by_role("button", name="Menu", exact=True).click()
                assert not page.locator("#app-sidebar").evaluate("e=>e.inert")
                page.keyboard.press("Escape")
                assert page.locator("#app-sidebar").evaluate("e=>e.inert")
                page.set_viewport_size({"width": 1440, "height": 1000})
            page.goto(base + "weeks/week-08/#walk-through-one-case")
            page.screenshot(
                animations="disabled", path=str(args.screenshots / "week-8-desktop.png")
            )
            page.locator("#lesson-complete").check()
            page.locator("#lesson-notes").fill("Test: preserve inspection condition.")
            page.reload()
            assert page.locator("#lesson-complete").is_checked()
            assert (
                page.locator("#lesson-notes").input_value()
                == "Test: preserve inspection condition."
            )
            page.goto(base)
            page.wait_for_selector(".week-card")
            assert page.locator("#week-8 input[type=checkbox]").is_checked()
            assert (
                page.locator("#week-8 textarea").input_value()
                == "Test: preserve inspection condition."
            )
            assert (
                page.locator("#continue-learning").get_attribute("href")
                == "weeks/week-08/"
            )
            page.get_by_role("button", name="Switch to dark mode").click()
            page.reload()
            assert page.locator("html").get_attribute("data-theme") == "dark"
            nojs = browser.new_context(java_script_enabled=False)
            raw = nojs.new_page()
            raw.goto(base + "weeks/week-30/")
            assert raw.get_by_role(
                "heading", name="Knowledge check", exact=True
            ).is_visible()
            blocked = browser.new_context()
            blocked.add_init_script(
                "Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError')}})"
            )
            blocked_page = blocked.new_page()
            blocked_page.on("pageerror", lambda e: errors.append(str(e)))
            blocked_page.goto(base)
            blocked_page.wait_for_selector(".week-card")
            assert blocked_page.locator(".storage-notice").is_visible()
            blocked_page.goto(base + "weeks/week-30/")
            blocked_page.wait_for_selector(".lesson-chapter:visible")
            assert blocked_page.locator(".storage-notice").is_visible()
            assert not errors, errors
            assert not failed, failed
            browser.close()
        report = {
            "lesson_pages": 37,
            "all_weeks": 30,
            "javascript_errors": errors,
            "failed_local_requests": failed,
            "screenshots": 5,
            "checks": [
                "search",
                "phase filters",
                "every lesson",
                "guided/full reading",
                "deep links",
                "answer reveal",
                "mobile menu",
                "no overflow",
                "progress/notes persistence",
                "continue link",
                "theme persistence",
                "no JavaScript",
                "blocked storage",
            ],
        }
        Path(".qa/browser-checks.json").write_text(json.dumps(report, indent=2))
        print(json.dumps(report))
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
