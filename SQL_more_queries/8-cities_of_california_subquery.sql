-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.name,cities.id
FROM cities,states
WHERE cities.state_id = states.id 
AND cities.name = 'California'
ORDER BY cities.id ASC;
