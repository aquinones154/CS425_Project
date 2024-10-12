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

-- update winner of a match
UPDATE GameMatch
SET Winner = 'Germany'
WHERE MID = 65;

-- counts total matches played at a stadium 
SELECT Sname, TotalMatches
FROM (
    SELECT S.Sname, COUNT(GM.MID) AS TotalMatches
    FROM GameMatch GM
    JOIN Stadium S ON GM.SID = S.SID
    GROUP BY S.Sname
) AS StadiumMatchCount;

-- display the IDs of teams that have earned at least 7 points in a home game
SELECT DISTINCT t.TID FROM team_match AS t, gamematch AS g
WHERE t.MID = g.MID AND t.Home_match = "yes" AND Home_team_score > 7;

-- display how many countries were eliminated in the first 5 tourney rounds (from 0 to 4)
SELECT Round_Eliminated, COUNT(TID) AS Teams_Eliminated FROM team_tournament
WHERE Round_Eliminated <= 4
GROUP BY Round_Eliminated
ORDER BY Round_Eliminated ASC;

-- list all past world champion team countries along with the year they won the championship, in
-- chronological order
SELECT t.Country, w.Year FROM team AS t, world_champions AS w
WHERE t.TID = w.TID
ORDER BY w.Year;

-- list all players above the average age, as well as how much older they are than the average
-- sorted from youngest to oldest
SELECT Pname, (Age - (SELECT AVG(Age) FROM Player)) AS distance_from_avg_age FROM Player
WHERE Age > (SELECT AVG(Age) FROM Player)
ORDER BY Age ASC