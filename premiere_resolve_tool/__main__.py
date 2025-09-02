"""Command-line interface for the Premiere-to-Resolve converter."""

from __future__ import annotations

import sys

import click

from .converter import PremiereResolveConverter, VerificationError


@click.command()
@click.argument("project_file")
def main(project_file: str) -> None:
    """Convert a Premiere project file and verify the result."""
    converter = PremiereResolveConverter()
    project = converter.load_premiere_project(project_file)
    resolve_project = converter.translate(project)
    try:
        converter.verify(resolve_project)
    except VerificationError as exc:
        click.echo(f"Verification failed: {exc}", err=True)
        sys.exit(1)
    click.echo("Project verified successfully")


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()
