-- Creates a table called 'first_table' in the current database.
-- The IF NOT EXISTS clause prevents the script from failing if the table already exists.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
