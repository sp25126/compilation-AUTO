-- Migration 001_schema.sql
-- Enables UUID generation extension if not present
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table 1: clips
CREATE TABLE IF NOT EXISTS clips (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category TEXT,
    title TEXT,
    storage_path TEXT,
    duration_sec NUMERIC,
    apex_sec NUMERIC,
    used_count INT DEFAULT 0
);

-- Table 2: sfx_library
CREATE TABLE IF NOT EXISTS sfx_library (
    id TEXT PRIMARY KEY,
    file_url TEXT,
    category TEXT
);

-- Table 3: compilation_jobs
CREATE TABLE IF NOT EXISTS compilation_jobs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    status TEXT,
    theme TEXT,
    cue_sheet_json JSONB,
    output_url TEXT
);

