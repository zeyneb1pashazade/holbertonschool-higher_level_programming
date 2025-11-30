-- Lists all cities in the database hbtn_0d_usa, showing their city ID, city name, and corresponding state name.
-- Uses an INNER JOIN to link the cities and states tables based on state_id = id.
-- Results are sorted by city ID (cities.id) in ascending order.
SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities
JOIN
    states ON cities.state_id = states.id
ORDER BY
    cities.id ASC;
