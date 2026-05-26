"""Copybook parser placeholder."""

from dataclasses import dataclass


@dataclass
class CopybookParseResult:
    record_names: list[str]
    data_elements: list[str]


def parse_copybook(source: str) -> CopybookParseResult:
    """Parse copybook source. Step 2 will implement heuristics."""
    return CopybookParseResult(record_names=[], data_elements=[])
