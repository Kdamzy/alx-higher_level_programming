-- script that display the top 3 cities temperature 
SELECT city, avg(value) AS avg_temp FROM temperatures 
WHERE month IN ('July', 'August')
GROUP BY city 
ORDER BY avg_temp DESC
LIMIT 3;