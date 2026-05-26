-- PostgreSQL schema for Mainframe Application Intelligence Platform.
-- Step 1 scaffold. Step 2 will harden indexes, constraints, and repository usage.

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS ontology_class (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS ontology_object (
    object_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    class_id INT NOT NULL REFERENCES ontology_class(class_id),
    object_name VARCHAR(255) NOT NULL,
    description TEXT,
    source_system VARCHAR(100),
    confidence_score NUMERIC(5,2),
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now(),
    UNIQUE(class_id, object_name)
);

CREATE TABLE IF NOT EXISTS relationship_type (
    relationship_type_id SERIAL PRIMARY KEY,
    relationship_name VARCHAR(100) UNIQUE NOT NULL,
    source_class VARCHAR(100),
    target_class VARCHAR(100),
    description TEXT
);

CREATE TABLE IF NOT EXISTS ontology_relationship (
    relationship_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_object_id UUID NOT NULL REFERENCES ontology_object(object_id),
    relationship_type_id INT NOT NULL REFERENCES relationship_type(relationship_type_id),
    target_object_id UUID NOT NULL REFERENCES ontology_object(object_id),
    confidence_score NUMERIC(5,2),
    evidence_uri TEXT,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(source_object_id, relationship_type_id, target_object_id)
);

CREATE TABLE IF NOT EXISTS source_artifact (
    artifact_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    artifact_type VARCHAR(50) NOT NULL,
    artifact_name VARCHAR(255) NOT NULL,
    storage_uri TEXT,
    checksum TEXT,
    version VARCHAR(100),
    metadata JSONB DEFAULT '{}'::jsonb,
    ingested_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS artifact_chunk (
    chunk_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    artifact_id UUID NOT NULL REFERENCES source_artifact(artifact_id),
    chunk_type VARCHAR(50),
    chunk_text TEXT NOT NULL,
    start_line INT,
    end_line INT,
    vector_doc_id VARCHAR(255),
    related_object_id UUID REFERENCES ontology_object(object_id),
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS modernization_score (
    score_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    object_id UUID NOT NULL REFERENCES ontology_object(object_id),
    business_value_score NUMERIC(5,2),
    complexity_score NUMERIC(5,2),
    risk_score NUMERIC(5,2),
    reuse_potential_score NUMERIC(5,2),
    recommended_disposition VARCHAR(100),
    rationale TEXT,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS agent_query_log (
    query_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    question TEXT NOT NULL,
    route VARCHAR(100),
    answer TEXT,
    evidence JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_ontology_object_name ON ontology_object(object_name);
CREATE INDEX IF NOT EXISTS idx_ontology_object_class ON ontology_object(class_id);
CREATE INDEX IF NOT EXISTS idx_relationship_source ON ontology_relationship(source_object_id);
CREATE INDEX IF NOT EXISTS idx_relationship_target ON ontology_relationship(target_object_id);
CREATE INDEX IF NOT EXISTS idx_artifact_name ON source_artifact(artifact_name);
