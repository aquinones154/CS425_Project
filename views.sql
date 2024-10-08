
-- Shows player with team info
CREATE VIEW Player_Team_Info AS
SELECT Player.PID, Player.Pname, Player.Position, Team.Country, Team.Coach
FROM Player
JOIN Team ON Player.TID = Team.TID;

-- shows goals scored by each player 
CREATE VIEW Player_Goal_Summary AS
SELECT Player.PID, Player.Pname, COUNT(Goals.PID) AS Total_Goals
FROM Player
JOIN Goals ON Player.PID = Goals.PID
GROUP BY Player.PID, Player.Pname;

-- shows match results including away and home matches
CREATE VIEW Match_Score_Info AS
SELECT GameMatch.MID, GameMatch.MData, GameMatch.Winner, GameMatch.Home_team_score, GameMatch.Away_team_score, Stadium.Sname AS Stadium
FROM GameMatch
JOIN Stadium ON GameMatch.SID = Stadium.SID;
