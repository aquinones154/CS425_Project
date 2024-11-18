# CS425_Project

## Table of Contents
-[About the Project](#about-the-project)

-[Features](#features)

-[How to use](#how-to-use)


# About the Project

This program allows you to interface with the database for the women's World Cup. You may access and update information about players, teams, and stadiums. You may additionally read but not edit information about matches that have occurred, the world champions of a particular season, team groups, and tournaments.

This program uses a user interface created with tkinter, which is already native to python library. Tkinter is a good tool for building simple grahical user interfaces(GUIs) as it provides easy to create a user interface and is cross-platform. Using the gui is pretty simple and straight forward, allowing the user to perform many operation such as CRUD(Create, Read, Update,and Delete) operations as well as some more advanced SQL queries. 

The project is part of the CS425 course, database organization. The goal with completing the project is to build a simple application that uses a database backend, for each group there was a different topic of interest, for this project specically the topic was the Women's World Cup. 

# Features

The database application supports CRUD(Create, Read, Update, Delete) opeartions

Create
- When selecting to create data, the application will ask the user to input the data for the newly created data. To ensure no duplicate ID's are created for the data, there is a random generator to create the ID for the data minimizing errors with duplicate ID's

Read
- When selecting to read data, the application will ask which table to read data from and opens up a new window and displays the user's selected table

Update
- When selecting to update data, the application will ask the user for the table and the corresponding ID for the data to be updated. At each step there is validation to ensure there does exist an entry for that data, if not then and error will be printed to the user. Otherwise, the user can continue and update the data, at the end a message is printed to let the user know the data was updated successfully. 

Delete
- When selecting to delete data, similar to the update operation, the application will validate the table and ID to make sure an entry exist, if so then the data will be deleted along with a sucess message. If not, then an error will be printed to the user. 

Advanced SQL Queries

- Although having CRUD operations is useful, in the read world users want and will ask for more comlex queries. For this reason, the application also supports a number of more complex queries such as displaying teams who have scored more than 7 points in a home game, displaying players who have scored a number of goals in a home match etc.. 

# How to use
Follow these steps to get the database application running:

### Make sure to have the following
- Python 
- MySQL server
- Make sure mysql-connector is installed and running
- Make sure tkinter is installed and working

## Install commands for mysql-connector && Tkinter
```bash
pip install mysql-connector
``` 

```bash
pip install tk
```

To test out if Tkinter was installed right, use test function
```bash 
import tkinter
tkinter._test()
```





