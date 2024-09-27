CREATE DATABASE womensWrlCUP;
USE womensWrlCUP;

CREATE TABLE Player(
    PID INT,
    Pname VARCHAR(15),
    Position VARCHAR(15),
    DOB DATE,
    PRIMARY KEY (PID),
    FOREGIN KEY (TID) REFERENCES Team(TID);
)

-- Bridge entity
CREATE TABLE Goals (
    PID INT,
    TID INT,
    MID INT,
    Time_of_Goal INT, --could just be the minute when the goal was scored at
    FOREGIN KEY (PID) REFERENCES Player (PID),
    FOREGIN KEY (TID) REFERENCES Team(TID),
    FOREGIN KEY (MID) REFERENCES Match(MID);
)

CREATE TABLE Match (
    MID INT, 
    MData Date, 
    Winner VARCHAR(15),
    Home_team_score INT,
    Away_tema_score INT,
    PRIMARY KEY (MID),
    FOREGIN KEY REFERENCES Stadium(SID);
)

--Bridge entity 
CREATE TABLE team_match(
    MID INT,
    TID INT,
    Goal_scored INT,
    Home_match VARCHAR(15),
    FOREGIN KEY (MID) REFERENCES Match (MID),
    FOREGIN KEY (TID) REFERENCES Team (TID);
)

--Bridge entity

CREATE TABLE Team_Tournament()

CREATE TABLE Stadium(
    SID INT,
    Sname VARCHAR(15),
    Capacity INT,
    City VARCHAR(15),
    PRIMARY KEY(SID);
)

CREATE TABLE World_Champions (
    WID INT, 
    Year INT,
    PRIMARY KEY(WID);
)

CREATE TABLE Team (
    TID INT,
    Country VARCHAR(15),
    Coach VARCHAR(15),
    PRIMARY KEY (TID);
)

CREATE TABLE Group (
    GID INT,
    Gname VARCHAR(15),
    Teams VARCHAR(15),
    Matches VARCHAR(15), 
    PRIMARY KEY (GID); 
)

