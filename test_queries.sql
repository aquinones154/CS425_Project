-- file for test queries for deliverable #3

-- select query

-- gets everyting from player table
SELECT * 
FROM Player;

-- gets capactiy from stadium table and sorts it by ascending order
SELECT Capacity, Sname
FROM Stadium
ORDER BY Capacity ASC; 

-- outputs the goals scored after halftime  
SELECT Time_of_Goal,MID,TID
FROM Goals
WHERE Time_of_Goal > 45; 

-- insert query

-- inserts data into team table
INSERT INTO Team (TID, Country, Coach) VALUES (2, 'Germany', 'Martina');

-- inserts dat into stadium table
INSERT INTO Stadium (SID, Sname, Capacity, City) VALUES (1, 'Stadium A', 50000, 'New York');

-- include advance window features
-- olap query

-- Selects all the goals and shows player, country, time of goak, and ranks over fastest scored goals
SELECT p.pname, p.position, t.country, g.Time_of_Goal,
RANK() OVER (ORDER BY Time_of_Goal ASC) AS fastest_goal_rank
FROM Player AS p
LEFT JOIN goals AS g
ON p.pid = g.pid
LEFT JOIN team AS t
ON g.tid = t.tid;


-- counts the total number of players per team
SELECT T.Country, COUNT(P.PID) AS Total_Players
FROM Player P
JOIN Team T ON P.TID = T.TID
GROUP BY T.Country;




