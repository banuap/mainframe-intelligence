"""COBOL parser placeholder."""

from dataclasses import dataclass


@dataclass
class CobolParseResult:
    program_name: str | None
    calls: list[str]
    copybooks: list[str]


def parse_cobol(source: str) -> CobolParseResult:
    """Parse COBOL source. Step 2 will implement heuristics."""
    return CobolParseResult(program_name=None, calls=[], copybooks=[])
