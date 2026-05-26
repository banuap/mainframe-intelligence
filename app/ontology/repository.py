"""Repository layer placeholder for ontology persistence."""

class OntologyRepository:
    """Repository facade for ontology objects and relationships."""

    def upsert_object(self, *args, **kwargs):
        raise NotImplementedError("Step 2 will implement object persistence.")

    def upsert_relationship(self, *args, **kwargs):
        raise NotImplementedError("Step 2 will implement relationship persistence.")
