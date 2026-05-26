"""Chunking utilities for source artifacts."""

from dataclasses import dataclass


@dataclass
class TextChunk:
    text: str
    start_line: int
    end_line: int
    chunk_type: str = "text"


def chunk_by_lines(source: str, max_lines: int = 80) -> list[TextChunk]:
    """Split text into line-based chunks."""
    lines = source.splitlines()
    chunks: list[TextChunk] = []
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        chunks.append(
            TextChunk(
                text="\n".join(lines[start:end]),
                start_line=start + 1,
                end_line=end,
            )
        )
    return chunks
