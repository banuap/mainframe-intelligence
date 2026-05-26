"""JCL parser placeholder."""

from dataclasses import dataclass


@dataclass
class JclParseResult:
    job_name: str | None
    executed_programs: list[str]


def parse_jcl(source: str) -> JclParseResult:
    """Parse JCL source. Step 2 will implement heuristics."""
    return JclParseResult(job_name=None, executed_programs=[])
