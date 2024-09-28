CREATE DATABASE womensWrlCUP;
USE womensWrlCUP;

CREATE TABLE Team (
    TID INT,
    Country VARCHAR(15),
    Coach VARCHAR(15),
    PRIMARY KEY (TID)
);

CREATE TABLE Stadium(
    SID INT,
    Sname VARCHAR(15),
    Capacity INT,
    City VARCHAR(15),
    PRIMARY KEY(SID)
);

CREATE TABLE Player(
    PID INT,
    Pname VARCHAR(15),
    Position VARCHAR(15),
    DOB Date,
    Age INT,
    TID INT,
    PRIMARY KEY (PID),
    FOREIGN KEY (TID) REFERENCES Team(TID)
);

CREATE TABLE GameMatch (
    MID INT, 
    MData Date, 
    Winner VARCHAR(15),
    Home_team_score INT,
    Away_team_score INT,
	SID INT,
    PRIMARY KEY (MID),
    FOREIGN KEY (SID) REFERENCES Stadium(SID)
);

-- Bridge entity
CREATE TABLE Goals (
    PID INT,
    TID INT,
    MID INT,
    Time_of_Goal INT, -- could just be the minute when the goal was scored at
    FOREIGN KEY (PID) REFERENCES Player (PID),
    FOREIGN KEY (TID) REFERENCES Team(TID),
    FOREIGN KEY (MID) REFERENCES GameMatch(MID)
);

-- Bridge entity 
CREATE TABLE team_match(
    MID INT,
    TID INT,
    Goal_scored INT,
    Home_match VARCHAR(15),
    FOREIGN KEY (MID) REFERENCES GameMatch (MID),
    FOREIGN KEY (TID) REFERENCES Team (TID)
);

CREATE TABLE World_Champions (
    WID INT, 
    Year INT,
    TID INT,
    PRIMARY KEY(WID),
    FOREIGN KEY (TID) REFERENCES Team(TID)
);

CREATE TABLE TeamGroup (
    GID INT,
    Gname VARCHAR(15),
    Teams VARCHAR(15),
    Matches VARCHAR(15), 
    PRIMARY KEY (GID)
);

-- Bridge entity
CREATE TABLE Team_tournament(
    TID INT,
    GID INT,
    Match_played INT, 
    Ranking INT,
    Round_Eliminated INT,
    FOREIGN KEY (TID) REFERENCES Team (TID),
    FOREIGN KEY (GID) REFERENCES TeamGroup (GID)
);