"""Writes the FastAPI app's OpenAPI schema to disk, so the frontend can
generate TypeScript types from it without the server needing to be running.
Run via `make types` from the repo root.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app  # noqa: E402

OUT = Path(__file__).resolve().parents[2] / "frontend" / "openapi.json"

if __name__ == "__main__":
    OUT.write_text(json.dumps(app.openapi(), indent=2))
    print(f"wrote {OUT}")
