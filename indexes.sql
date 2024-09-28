-- file has Indexes

-- index for Player's table to look up name faster
CREATE INDEX idx_player_pname ON Player(Pname);

-- index for Match table to look up winner faster
CREATE INDEX idx_match_winner ON GameMatch(Winner);

-- index for Goals table to look up time of goal faster
CREATE INDEX idx_goals_time_of_goal ON Goals(Time_of_Goal);

-- index for goals table to look up group name
CREATE INDEX idx_group_gname ON TeamGroup(Gname);

-- compound index for team_match table on MID and TID
CREATE INDEX idx_team_match_mid_tid ON team_match(MID, TID);