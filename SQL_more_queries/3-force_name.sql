-- Creates the table 'force_name' in the current database.
-- The 'name' column is explicitly set to NOT NULL, preventing empty/null values.
-- The IF NOT EXISTS clause ensures the script does not fail if the table already exists.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
