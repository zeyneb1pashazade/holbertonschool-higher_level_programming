-- Lists the number of records with the same score in the table 'second_table'.
-- The results display the score and the count (labeled 'number').
-- The list is sorted by the count (number of records) in descending order (highest count first).
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
