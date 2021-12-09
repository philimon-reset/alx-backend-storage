-- query through a list and search non unique values

SELECT origin, SUM(fans) AS 'nb_fans'
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;