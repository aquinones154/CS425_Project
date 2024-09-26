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

CREATE TABLE Match (
    MID INT, 
    MData Date, 
    Winner VARCHAR(15),
    PRIMARY KEY (MID);
    FOREGIN KEY REFERENCES Stadium(SID);
)

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

