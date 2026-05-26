"""Ingestion placeholder tests."""

from app.ingestion.chunker import chunk_by_lines


def test_chunk_by_lines():
    source = "\n".join([f"line {i}" for i in range(1, 6)])
    chunks = chunk_by_lines(source, max_lines=2)
    assert len(chunks) == 3
    assert chunks[0].start_line == 1
    assert chunks[0].end_line == 2
