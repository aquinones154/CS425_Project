-- file for test queries for deliverable #3

-- simple queries

-- gets everyting from player table
SELECT * 
FROM Player;

-- gets capactiy from stadium table and sorts it by ascending order
SELECT Capacity, Sname
FROM Stadium
ORDER BY Capacity ASC; 

-- Inserts data into gameMatch table 
INSERT INTO GameMatch (MID,MData,Winner,Home_team_score,Away_team_score) VALUES (46,2004-10-09,'Team1', 3, 2, 15);

-- Inserts data into TeamGroup table
INSERT INTO TeamGroup (GID, Gname, Teams, Matches) VALUES (24, 'NorthEast', 'TeamsA-D', 'test');

-- outputs the goals scored after halftime  
SELECT Time_of_Goal
FROM Goals
WHERE Time_of_Goal > 45; 
