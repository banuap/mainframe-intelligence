"""Ingestion pipeline placeholder."""

from pathlib import Path


def ingest_path(path: str) -> dict[str, object]:
    """Ingest a file or directory path. Step 2 will implement persistence."""
    target = Path(path)
    return {
        "path": str(target),
        "exists": target.exists(),
        "status": "not_implemented",
    }
