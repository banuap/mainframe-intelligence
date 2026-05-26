"""API routes for agent tools and ingestion."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AskRequest(BaseModel):
    question: str


class IngestPathRequest(BaseModel):
    path: str


class EvidenceSearchRequest(BaseModel):
    query: str
    filters: dict[str, str] | None = None


@router.post("/ingest/path")
def ingest_path(request: IngestPathRequest) -> dict[str, str]:
    """Placeholder endpoint for ingesting a local path."""
    return {"status": "not_implemented", "path": request.path}


@router.get("/program/{program_name}/summary")
def get_program_summary(program_name: str) -> dict[str, str]:
    return {"program": program_name, "summary": "Not implemented yet."}


@router.get("/program/{program_name}/dependencies")
def get_program_dependencies(program_name: str) -> dict[str, object]:
    return {"program": program_name, "dependencies": []}


@router.get("/program/{program_name}/business-rules")
def get_program_business_rules(program_name: str) -> dict[str, object]:
    return {"program": program_name, "business_rules": []}


@router.get("/job/{job_name}/flow")
def get_job_flow(job_name: str) -> dict[str, object]:
    return {"job": job_name, "flow": []}


@router.get("/impact/program/{program_name}")
def impact_program(program_name: str) -> dict[str, object]:
    return {"program": program_name, "impacted_assets": []}


@router.get("/impact/rule/{rule_name}")
def impact_rule(rule_name: str) -> dict[str, object]:
    return {"rule": rule_name, "impacted_assets": []}


@router.get("/impact/data-element/{data_element_name}")
def impact_data_element(data_element_name: str) -> dict[str, object]:
    return {"data_element": data_element_name, "impacted_assets": []}


@router.post("/search/evidence")
def search_evidence(request: EvidenceSearchRequest) -> dict[str, object]:
    return {"query": request.query, "filters": request.filters or {}, "results": []}


@router.post("/modernization/candidates")
def modernization_candidates() -> dict[str, object]:
    return {"candidates": []}


@router.post("/agent/ask")
def agent_ask(request: AskRequest) -> dict[str, str]:
    return {
        "question": request.question,
        "answer": "Agent orchestration is not implemented yet. This endpoint is reserved for Step 4.",
    }
