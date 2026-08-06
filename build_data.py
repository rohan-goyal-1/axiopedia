#!/usr/bin/env python3
"""Split a public export into a small index and lazy-loaded article files."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Full public_export.json file")
    parser.add_argument("--output", type=Path, default=Path("data"))
    args = parser.parse_args()

    articles = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(articles, list):
        raise SystemExit("Expected the export to contain a JSON array")

    output = args.output
    entries = output / "entries"
    if entries.exists():
        shutil.rmtree(entries)
    entries.mkdir(parents=True)

    index = []
    for article in articles:
        slug = article.get("sep_slug")
        title = article.get("title")
        if not slug or not title or "/" in slug or "\\" in slug:
            raise SystemExit(f"Invalid article slug/title: {slug!r}")
        index.append({"sep_slug": slug, "title": title})
        (entries / f"{slug}.json").write_text(
            json.dumps(article, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

    index.sort(key=lambda entry: entry["title"].casefold())
    output.mkdir(parents=True, exist_ok=True)
    (output / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"Built {len(index)} entries in {output}")


if __name__ == "__main__":
    main()
