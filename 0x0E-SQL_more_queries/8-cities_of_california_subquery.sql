-- script that list all the cities of california present in the database.
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'california'
)
ORDER BY id ASC;