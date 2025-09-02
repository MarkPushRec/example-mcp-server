"""Core conversion and verification logic for Premiere-to-Resolve workflows."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List


class VerificationError(Exception):
    """Raised when a converted project fails verification checks."""


@dataclass
class PremiereResolveConverter:
    """Convert Premiere project data into Resolve-compatible form.

    This is an early skeleton focused on validating clip placement.
    """

    def load_premiere_project(self, path: str) -> Dict[str, Any]:
        """Load a simplified Premiere project represented as JSON."""
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def translate(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """Translate a Premiere project into Resolve form.

        The initial implementation simply returns the provided structure.
        """
        return project

    def verify(self, project: Dict[str, Any]) -> None:
        """Verify that clip timing information is preserved."""
        clips: List[Dict[str, Any]] = project.get("clips", [])
        if not clips:
            raise VerificationError("No clips found in project")

        first = clips[0]
        if first.get("start") != 0:
            raise VerificationError("First clip does not start at timecode 0")
