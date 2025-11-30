-- Creates the table 'id_not_null' in the current database.
-- The 'id' column is set to default to 1 if no value is provided.
-- The IF NOT EXISTS clause ensures the script does not fail if the table already exists.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
