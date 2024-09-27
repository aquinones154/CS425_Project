-- file has temproary tables

-- sample table that creates table with data, only where the year = 2024
CREATE TEMPORARY TABLE Temp_2024_Matches AS
SELECT * FROM Match
WHERE YEAR(MData) = 2024;

-- sample table that will create a table showing only teams that have more that 2 wins
CREATE TEMPORARY TABLE Temp_Top_Winning_Teams AS
SELECT Team.TID, Team.Country, COUNT(*) AS Win_Count
FROM Team
JOIN Match ON Team.TID = Match.Winner
GROUP BY Team.TID
HAVING Win_Count > 2;