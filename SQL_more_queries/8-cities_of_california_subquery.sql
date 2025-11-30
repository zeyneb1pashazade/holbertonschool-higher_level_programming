-- Lists all cities belonging to the state of California using a subquery.
-- Results are sorted by the city ID in ascending order.
SELECT id, name
FROM cities
WHERE state_id = (
    -- Subquery: Selects the 'id' of the state named 'California'
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
