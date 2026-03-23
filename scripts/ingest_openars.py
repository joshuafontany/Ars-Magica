#!/usr/bin/env python3
"""Scaffold-oriented ingestion helper for the Ars Magica vault."""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.yml"
BOOKS_DIR = ROOT / "_books"
WORK_DIR = ROOT / "work"


def load_catalog() -> dict:
    with CATALOG.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def extract_book_stub(entry: dict) -> pathlib.Path:
    source = BOOKS_DIR / entry["source_pdf"]
    output = WORK_DIR / f"{entry['slug']}.txt"
    WORK_DIR.mkdir(exist_ok=True)
    if not source.exists():
        raise FileNotFoundError(f"Missing source PDF: {source}")
    output.write_text(
        "Extraction placeholder. Install pdftotext and replace this stub with real extraction.\n",
        encoding="utf-8",
    )
    return output


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", nargs="?", help="Book slug from catalog.yml")
    args = parser.parse_args(argv)

    catalog = load_catalog()
    books = {entry["slug"]: entry for entry in catalog.get("books", [])}

    if args.slug:
        targets = [books[args.slug]]
    else:
        targets = [entry for entry in catalog.get("books", []) if entry.get("status") == "pilot"]

    for entry in targets:
        out = extract_book_stub(entry)
        print(f"Prepared {entry['slug']} -> {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
