"""FastAPI entrypoint for the Mainframe Application Intelligence Platform."""

from fastapi import FastAPI

from app.api.routes import router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Ontology-driven application intelligence for mainframe relearning and modernization.",
)

app.include_router(router)


@app.get("/health")
def health() -> dict[str, str]:
    """Simple health check endpoint."""
    return {"status": "ok", "app": settings.app_name, "env": settings.app_env}
