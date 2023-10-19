-- diplay top 3 cities ranked by temperatures
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
