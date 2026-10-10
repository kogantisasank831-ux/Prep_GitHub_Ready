"""Regression checks for portable deployment and destructive-output protection."""

from pathlib import Path

import pytest

from scripts.build_site import ROOT, build
from scripts.check_built_site import check


def test_builder_refuses_source_root() -> None:
    with pytest.raises(ValueError, match="new build directory"):
        build(ROOT, "/Prep")


def test_builder_preserves_existing_directory(tmp_path: Path) -> None:
    valuable = tmp_path / "notes.txt"
    valuable.write_text("keep this")
    with pytest.raises(ValueError, match="refusing to overwrite"):
        build(tmp_path, "/Prep")
    assert valuable.read_text() == "keep this"


@pytest.mark.parametrize("prefix", ["", "/RenamedRepo"])
def test_portable_build_and_broken_link_detection(tmp_path: Path, prefix: str) -> None:
    output = tmp_path / "site"
    manifest = build(output, prefix)
    assert len(manifest["pages"]) == 37
    check(output)
    (output / "reader.js").unlink()
    with pytest.raises(ValueError, match="missing .*reader.js"):
        check(output)
