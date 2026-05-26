@workspace Read AGENTS.md, README.md, and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Issue 1: PostgreSQL Ontology Repository.

Goal:
Make PostgreSQL the persistent ontology store.

Implement:
1. SQLAlchemy session handling in app/db/connection.py
2. Repository functions in app/ontology/repository.py:
   - get_class_id(class_name)
   - get_relationship_type_id(relationship_name)
   - upsert_object(class_name, object_name, description=None, metadata=None, confidence_score=None)
   - upsert_relationship(source_object_name, relationship_type, target_object_name, confidence_score=None, evidence_uri=None, metadata=None)
   - get_object_by_name(object_name)
   - get_relationships_for_object(object_name)
   - list_objects(class_name=None)
3. Improve app/db/seed_ontology.py if needed
4. Add tests for repository behavior

Constraints:
- Do not add Neo4j.
- Do not add Kafka.
- Do not require production database credentials.
- Tests should use a test database, mocks, or clearly isolated setup.
- Preserve the existing schema unless changes are necessary.

After implementing:
- Run pytest
- Explain changed files
- Explain how to seed the ontology