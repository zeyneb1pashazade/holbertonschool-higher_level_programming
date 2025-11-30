-- Updates the score of the record where the name is 'Bob' to 10.
-- This uses the name field to target the specific row, as required.
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
