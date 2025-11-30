-- Creates the table 'second_table' in the current database and adds multiple rows.
-- The database name is passed as an argument to the mysql command.

-- 1. Create the table 'second_table' with IF NOT EXISTS
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- 2. Insert the specified records into 'second_table'
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
