-- query and list all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, IF(split is NULL , year(curdate()) - formed, (split - formed))  AS 'lifespan'
FROM metal_bands
WHERE `style` LIKE '%Glam rock%'
ORDER BY lifespan DESC;