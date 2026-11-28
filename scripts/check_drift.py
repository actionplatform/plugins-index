"""Fail when a plugin's `latest` differs from the newest GitHub release of its repository."""

import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def newest(repo: str) -> str:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/releases/latest",
        headers={"Accept": "application/vnd.github+json"},
    )

    if token := os.environ.get("GITHUB_TOKEN"):
        request.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["tag_name"].removeprefix("v")


failed = False

for path in sorted((ROOT / "plugins").glob("*.json")):
    row = json.loads(path.read_text())
    repo = row["repo"].removeprefix("https://github.com/")
    released = newest(repo)

    if released != row["latest"]:
        failed = True
        print(f"::error file={path.relative_to(ROOT)}::{row['name']} latest is {row['latest']}, {repo} released {released}")

sys.exit(1 if failed else 0)
