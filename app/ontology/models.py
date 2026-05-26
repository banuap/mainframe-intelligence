"""Ontology model DTOs."""

from pydantic import BaseModel, Field


class OntologyObject(BaseModel):
    object_name: str
    class_name: str
    description: str | None = None
    confidence_score: float | None = Field(default=None, ge=0, le=1)


class OntologyRelationship(BaseModel):
    source_object_name: str
    relationship_type: str
    target_object_name: str
    confidence_score: float | None = Field(default=None, ge=0, le=1)
    evidence_uri: str | None = None
