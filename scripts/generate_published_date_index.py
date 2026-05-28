#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate exact-date indexes for published WeChat articles."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = REPO_ROOT / "articles" / "published"
DEFAULT_MARKDOWN_OUTPUT = ARTICLES_DIR / "README.md"
DEFAULT_CSV_OUTPUT = ARTICLES_DIR / "published-date-index.csv"
FRONTMATTER_DATE_KEYS = ("date", "publish_date", "published_at", "published")
DATE_PATTERN = re.compile(r"(?<!\d)(20\d{2})[-_/年.]?([01]\d)[-_/月.]?([0-3]\d)(?!\d)")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)


@dataclass(frozen=True)
class ArticleRecord:
    published_date: str
    month_day: str
    date_source: str
    last_changed_date: str
    title: str
    author: str
    path: str


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip()


def parse_frontmatter(markdown: str) -> dict[str, str]:
    match = FRONTMATTER_PATTERN.match(markdown)
    if not match:
        return {}

    metadata: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key:
            metadata[key] = value
    return metadata


def normalize_date(value: str) -> str | None:
    match = DATE_PATTERN.search(value)
    if not match:
        return None

    year, month, day = match.groups()
    try:
        parsed = datetime(int(year), int(month), int(day))
    except ValueError:
        return None
    return parsed.strftime("%Y-%m-%d")


def find_frontmatter_date(metadata: dict[str, str]) -> tuple[str, str] | None:
    for key in FRONTMATTER_DATE_KEYS:
        value = metadata.get(key)
        if not value:
            continue
        normalized = normalize_date(value)
        if normalized:
            return normalized, f"frontmatter:{key}"
    return None


def find_filename_date(path: Path) -> str | None:
    return normalize_date(path.stem)


def git_dates(path: Path) -> tuple[str, str]:
    relative_path = path.relative_to(REPO_ROOT).as_posix()
    latest = run_git(["log", "-1", "--format=%ad", "--date=short", "--", relative_path])
    first = run_git(["log", "--follow", "--format=%ad", "--date=short", "--", relative_path])
    first_date = first.splitlines()[-1] if first else ""
    return first_date, latest


def display_month_day(date_value: str) -> str:
    parsed = datetime.strptime(date_value, "%Y-%m-%d")
    return f"{parsed.month}月{parsed.day}日"


def collect_article(path: Path) -> ArticleRecord:
    markdown = path.read_text(encoding="utf-8-sig", errors="replace")
    metadata = parse_frontmatter(markdown)
    git_first_date, git_last_date = git_dates(path)

    date_info = find_frontmatter_date(metadata)
    if date_info:
        published_date, date_source = date_info
    else:
        filename_date = find_filename_date(path)
        if filename_date:
            published_date = filename_date
            date_source = "filename"
        else:
            published_date = git_first_date or git_last_date
            date_source = "git:first_commit"

    title = metadata.get("title") or path.stem
    author = metadata.get("author") or ""
    relative_path = path.relative_to(REPO_ROOT).as_posix()
    return ArticleRecord(
        published_date=published_date,
        month_day=display_month_day(published_date),
        date_source=date_source,
        last_changed_date=git_last_date,
        title=title,
        author=author,
        path=relative_path,
    )


def collect_articles() -> list[ArticleRecord]:
    records = [collect_article(path) for path in sorted(ARTICLES_DIR.glob("*.md")) if path.name != "README.md"]
    return sorted(records, key=lambda item: (item.published_date, item.title), reverse=True)


def write_csv(records: list[ArticleRecord], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "published_date",
                "month_day",
                "date_source",
                "last_changed_date",
                "title",
                "author",
                "path",
            ],
        )
        writer.writeheader()
        for record in records:
            writer.writerow(record.__dict__)


def markdown_link(record: ArticleRecord) -> str:
    name = Path(record.path).name
    safe_title = record.title.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
    return f"[{safe_title}]({quote(name)})"


def table_cell(value: str) -> str:
    return value.replace("\n", " ").replace("|", "\\|")


def write_markdown(records: list[ArticleRecord], output_path: Path, csv_output: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    relative_csv = csv_output.relative_to(output_path.parent).as_posix()

    lines: list[str] = [
        "# Published Articles By Date",
        "",
        "本页由 `scripts/generate_published_date_index.py` 生成，用于弥补 GitHub 目录页只显示 `last week` / `last month` 等相对时间的问题。",
        "",
        f"- Article count: {len(records)}",
        f"- Machine-readable CSV: [{relative_csv}]({relative_csv})",
        "- Published date priority: frontmatter date -> filename date -> git first commit date",
        "- Last changed date comes from the latest git commit that touched the article",
        "",
    ]

    current_date = ""
    for record in records:
        if record.published_date != current_date:
            current_date = record.published_date
            lines.extend(["", f"## {record.published_date} ({record.month_day})", ""])
            lines.append("| Article | Author | Date Source | Last Changed |")
            lines.append("| --- | --- | --- | --- |")
        lines.append(
            f"| {table_cell(markdown_link(record))} | {table_cell(record.author)} | {record.date_source} | {record.last_changed_date} |"
        )

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown-output", type=Path, default=DEFAULT_MARKDOWN_OUTPUT)
    parser.add_argument("--csv-output", type=Path, default=DEFAULT_CSV_OUTPUT)
    args = parser.parse_args()

    records = collect_articles()
    write_csv(records, args.csv_output)
    write_markdown(records, args.markdown_output, args.csv_output)
    print(f"Indexed {len(records)} published articles")
    print(f"Markdown: {args.markdown_output.relative_to(REPO_ROOT).as_posix()}")
    print(f"CSV: {args.csv_output.relative_to(REPO_ROOT).as_posix()}")


if __name__ == "__main__":
    main()
