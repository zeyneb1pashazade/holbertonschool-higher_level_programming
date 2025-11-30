-- Lists all records from the table 'second_table' that have a name value (name is NOT NULL).
-- Results display the score and the name, ordered by score (highest first).
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
