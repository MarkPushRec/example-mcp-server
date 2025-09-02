"""Tests for the Premiere-to-Resolve converter."""

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from premiere_resolve_tool import PremiereResolveConverter


def test_verify_sample_project() -> None:
    converter = PremiereResolveConverter()
    project = converter.load_premiere_project("tests/sample_premiere_project.json")
    resolve_project = converter.translate(project)
    converter.verify(resolve_project)
