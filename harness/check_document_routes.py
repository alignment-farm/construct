"""Check local Markdown routes in the current documentation surface.

The archive, previous lab, generated evidence, and substrate transcripts are
lineage rather than the current read-in path. Their historical links are not
silently promoted into live routing obligations by this check.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
SKIP_TOP_LEVEL = {".archive", ".git", ".substrate", "corpus", "runs"}
SKIP_PREFIXES = {Path("notes/previous")}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SCHEMES = ("http://", "https://", "mailto:", "data:")


def _is_skipped(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if relative.parts and relative.parts[0] in SKIP_TOP_LEVEL:
        return True
    return any(relative == prefix or prefix in relative.parents for prefix in SKIP_PREFIXES)


def _target(raw: str) -> str | None:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        value = value[1:value.index(">")]
    else:
        value = value.split(maxsplit=1)[0]
    if not value or value.startswith("#") or value.startswith(SCHEMES):
        return None
    return unquote(value.split("#", 1)[0].split("?", 1)[0])


def main() -> int:
    failures: list[str] = []
    checked_files = 0
    checked_links = 0

    for source in sorted(ROOT.rglob("*.md")):
        if _is_skipped(source):
            continue
        checked_files += 1
        for line_number, line in enumerate(source.read_text().splitlines(), 1):
            for match in MARKDOWN_LINK.finditer(line):
                target = _target(match.group(1))
                if target is None:
                    continue
                checked_links += 1
                candidate = (source.parent / target).resolve()
                try:
                    candidate.relative_to(ROOT)
                except ValueError:
                    failures.append(
                        f"{source.relative_to(ROOT)}:{line_number}: "
                        f"route escapes repository: {target}"
                    )
                    continue
                if not candidate.exists():
                    failures.append(
                        f"{source.relative_to(ROOT)}:{line_number}: missing local target: {target}"
                    )

    if failures:
        print("\n".join(failures))
        print(f"DOCUMENT ROUTES: FAIL ({len(failures)} missing or escaped targets)")
        return 1

    print(
        f"document routes: {checked_links} local links across "
        f"{checked_files} live Markdown files"
    )
    print("DOCUMENT ROUTES: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
