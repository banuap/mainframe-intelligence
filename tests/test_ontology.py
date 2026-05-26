"""Ontology DTO tests."""

from app.ontology.models import OntologyObject


def test_ontology_object_model():
    obj = OntologyObject(object_name="SETL001", class_name="Program", confidence_score=0.9)
    assert obj.object_name == "SETL001"
    assert obj.class_name == "Program"
