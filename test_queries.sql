-- file for test queries for deliverable #3

-- simple queries

-- gets everyting from player table
SELECT * 
FROM Player;


-- gets everyting from goals table
SELECT * 
FROM Goals; 

-- gets capactiy from stadium table and sorts it by ascending order

SELECT Capacity, Sname
FROM Stadium
ORDER BY Capacity ASC; 

