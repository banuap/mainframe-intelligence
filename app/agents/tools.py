"""Agent tool placeholders."""

def get_program_summary(program_name: str) -> dict[str, object]:
    return {"program": program_name, "summary": "Not implemented yet."}


def get_impacted_assets(object_name: str, depth: int = 3) -> dict[str, object]:
    return {"object": object_name, "depth": depth, "impacted_assets": []}
