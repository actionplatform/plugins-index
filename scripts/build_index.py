"""Collect plugins/<slug>.json into index.json — the one file the hosted platform reads. Run after editing any plugin file."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
rows = sorted(
    (json.loads(p.read_text()) for p in (ROOT / "plugins").glob("*.json")),
    key=lambda r: r["name"],
)
(ROOT / "index.json").write_text(json.dumps({"plugins": rows}, indent=2) + "\n")
print(f"{len(rows)} plugin(s)")
