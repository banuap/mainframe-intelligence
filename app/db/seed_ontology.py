"""Seed ontology classes and relationship types."""

from sqlalchemy import text

from app.db.connection import get_engine

ONTOLOGY_CLASSES = [
    ("Application", "A business or technical application boundary."),
    ("Program", "A COBOL or other executable program."),
    ("JCLJob", "A JCL job."),
    ("JCLStep", "A step within a JCL job."),
    ("Copybook", "A COBOL copybook."),
    ("DataElement", "A field or logical data element."),
    ("DB2Table", "A DB2 table."),
    ("VSAMFile", "A VSAM file or dataset."),
    ("CICSMap", "A CICS screen map."),
    ("Transaction", "A transaction or user/system interaction."),
    ("BusinessRule", "A business rule extracted or inferred from code/documentation."),
    ("BusinessCapability", "A business capability supported by legacy assets."),
    ("BatchFlow", "A batch process flow."),
    ("Interface", "An external or internal interface."),
    ("Report", "A generated report or statement."),
    ("TestCase", "A test case or regression scenario."),
    ("TargetService", "A target-state service/API/domain component."),
    ("ModernizationCandidate", "A candidate asset or domain for modernization."),
]

RELATIONSHIP_TYPES = [
    ("CALLS", "Program", "Program", "A program calls another program."),
    ("EXECUTES", "JCLJob", "Program", "A job executes a program."),
    ("HAS_STEP", "JCLJob", "JCLStep", "A job contains a step."),
    ("USES_COPYBOOK", "Program", "Copybook", "A program uses a copybook."),
    ("DEFINES", "Copybook", "DataElement", "A copybook defines a data element."),
    ("READS", "Program", "DB2Table|VSAMFile", "A program reads a data source."),
    ("WRITES", "Program", "DB2Table|VSAMFile", "A program writes a data source."),
    ("IMPLEMENTS", "Program", "BusinessRule", "A program implements a business rule."),
    ("SUPPORTS", "BusinessRule|Program", "BusinessCapability", "An object supports a business capability."),
    ("PART_OF", "Program|JCLJob", "BatchFlow|Application", "An object is part of a larger flow or application."),
    ("PRODUCES", "Program|JCLJob", "Report|Interface", "An object produces an output."),
    ("CONSUMES", "Program|JCLJob", "Interface", "An object consumes an input."),
    ("MAPS_TO", "DataElement|BusinessRule", "DataElement|TargetService", "An object maps to another object."),
    ("MODERNIZES_TO", "Program|BusinessCapability", "TargetService", "An object modernizes to a target service."),
    ("TESTED_BY", "Program|BusinessRule", "TestCase", "An object is tested by a test case."),
    ("IMPACTS", "Program|BusinessRule|DataElement", "Program|Job|DataElement", "An object impacts another object."),
    ("DEPENDS_ON", "Program|JCLJob|BusinessCapability", "Program|JCLJob|DataElement", "An object depends on another object."),
]


def seed() -> None:
    """Seed the database with core ontology types."""
    engine = get_engine()
    with engine.begin() as conn:
        for class_name, description in ONTOLOGY_CLASSES:
            conn.execute(
                text("""
                INSERT INTO ontology_class (class_name, description)
                VALUES (:class_name, :description)
                ON CONFLICT (class_name) DO UPDATE SET description = EXCLUDED.description
                """),
                {"class_name": class_name, "description": description},
            )

        for relationship_name, source_class, target_class, description in RELATIONSHIP_TYPES:
            conn.execute(
                text("""
                INSERT INTO relationship_type (
                    relationship_name, source_class, target_class, description
                )
                VALUES (
                    :relationship_name, :source_class, :target_class, :description
                )
                ON CONFLICT (relationship_name) DO UPDATE SET
                    source_class = EXCLUDED.source_class,
                    target_class = EXCLUDED.target_class,
                    description = EXCLUDED.description
                """),
                {
                    "relationship_name": relationship_name,
                    "source_class": source_class,
                    "target_class": target_class,
                    "description": description,
                },
            )


if __name__ == "__main__":
    seed()
    print("Seeded ontology classes and relationship types.")
