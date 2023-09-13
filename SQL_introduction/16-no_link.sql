-- display list by order high level to low level
SELECT score,name 
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
