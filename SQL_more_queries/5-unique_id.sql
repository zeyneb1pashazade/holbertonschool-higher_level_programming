-- Creates the table 'unique_id' in the current database.
-- The 'id' column has a default value of 1 and must be unique across all records.
-- The IF NOT EXISTS clause ensures the script does not fail if the table already exists.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
