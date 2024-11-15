import mysql.connector
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# connection to database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="womensWrlCUP"
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        messagebox.showerror("Database Connection Error", f"Error: {e}")
        return None
    
    # read opeartion
def read_data(cursor, table_name):
    try:
        select_query = f"SELECT * FROM {table_name}" #select query
        cursor.execute(select_query)
        return cursor.fetchall(), [desc[0] for desc in cursor.description]
    except mysql.connector.Error as e: #error handling
        messagebox.showerror("Read Error", f"Error reading data: {e}")
        return None, None
#
       
def create_data(cursor, connection, table_name, data):
    try:
        if table_name == "Team":
            insert_query = "INSERT INTO Team (TID, Country, Coach) VALUES (%s, %s, %s)"
        elif table_name == "Stadium":
            insert_query = "INSERT INTO Stadium (SID, Sname, Capacity, City) VALUES (%s, %s, %s, %s)"
        elif table_name == "Player":
            insert_query = "INSERT INTO Player (PID, Pname, Position, DOB, Age, TID) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, data)
        connection.commit()
        messagebox.showinfo("Success", f"Data inserted into {table_name}!")
    except mysql.connector.Error as e:
        messagebox.showerror("Insert Error", f"Error inserting data: {e}")

       
        # DELETE DATA
        elif(userChoice == '3'):
            def delete_data():
                try:
                    # ask user which table to delete data from
                    userChoice_delete = input('Choose which table to delete data from:\n1. Team\n2. Stadium\n3. Player\nPlease choose one: ')

                    # map user choice to a table
                    table_mapping = {
                        '1': 'Team',
                        '2': 'Stadium',
                        '3': 'Player',
                    }
                    
                     # Fetch the table name based on the user's choice
                    table_name = table_mapping.get(userChoice_delete)

                    if not table_name:
                        print("Invalid choice")
                        return
                    
                    if table_name == 'Team' : 
                        team_id = input("Enter the TID of the team you want to delete: ")
                        check_query = "SELECT * FROM Team WHERE TID = %s"
                        cursor.execute(check_query,(team_id,))
                        team_data = cursor.fetchone()
                        

                        if team_data:
                            print(f"Team data: {team_data}\n")
                            delete_confirm = input("Really delete this team? (y/n) ")
                            if delete_confirm == "y" or delete_confirm == "Y":
                                cursor.execute("DELETE FROM Team WHERE TID = %s",(team_id,))
                                connection.commit()
                                print(f"Team {team_id} deleted.")
                            else:
                                print("Deletion aborted.")
                        else:
                            print(f"No Team found with TID {team_id}") 
                    elif table_name == "Stadium":
                        stadium_id = input("Enter the SID of the stadium you want to delete: ")
                        check_query = "SELECT * FROM Stadium WHERE SID = %s"
                        cursor.execute(check_query,(stadium_id,))
                        stadium_data = cursor.fetchone()

                        if stadium_data:
                            print(f"Stadium data: {stadium_data}")
                            delete_confirm = input("Really delete this stadium? (y/n) ")
                            if delete_confirm == "y" or delete_confirm == "Y":
                                cursor.execute("DELETE FROM Stadium WHERE SID = %s",(stadium_id,))
                                connection.commit()
                                print(f"Stadium {stadium_id} deleted.")
                            else:
                                print("Deletion aborted.")
                        else:
                            print(f"No Stadium found with SID {stadium_id}") 
                    elif table_name == 'Player':
                        player_id = input("Enter the PID of the player you want to delete: ")
                        check_query = "SELECT * FROM Player WHERE PID = %s"
                        cursor.execute(check_query,(player_id,))
                        player_data = cursor.fetchone()

                        if player_data:
                            print(f"Player data: {player_data}")
                            delete_confirm = input("Really delete this player? (y/n) ")
                            if delete_confirm == "y" or delete_confirm == "Y":
                                cursor.execute("DELETE FROM Player WHERE PID = %s",(player_id,))
                                connection.commit()
                                print(f"Player {player_id} deleted.")
                            else:
                                print("Deletion aborted.")
                        else:
                            print(f"No Player found with PID {player_id}")
                except Exception as e:
                    print(f"ERROR: Could not delete data: {e}")
            delete_data()


        #UPDATE DATA     
        elif(userChoice == '4'):
            def update_data():
                try:
                    #ask user which table to update
                    userChoice_update = input('Choose which table to update data in: \n 1. Team \n 2. Stadium \n 3. Player\n Please choose one: ') 

                    # map user choice to a table
                    table_mapping = {
                        '1': 'Team',
                        '2': 'Stadium',
                        '3': 'Player',
                    }
                    
                     # Fetch the table name based on the user's choice
                    table_name = table_mapping.get(userChoice_update)

                    if not table_name:
                        print("Invalid choice")
                        return
                    
                    if table_name == 'Team' : 
                        team_id = input("Enter the TID of the team you want to update: ")
                        check_query = "SELECT * FROM Team WHERE TID = %s"
                        cursor.execute(check_query,(team_id,))
                        team_data = cursor.fetchone()

                        if team_data:
                            print(f"Current team data: {team_data}")
                            new_country = input("Enter updated country: ")
                            new_coach = input("Enter updated coach: ")

                            update_query = """
                            UPDATE Team
                            SET Country = %s, Coach = %s
                            WHERE TID = %s
                            """

                            cursor.execute(update_query, (new_country,new_coach, team_id))
                            connection.commit()
                            print(f"Team with TID {team_id} updated successfully.")

                        else:
                            print(f"No Team found with TID {team_id}")                            

                    elif table_name == 'Stadium':
                        stadium_id = input("Enter the SID of the stadium you want to update: ")
                        check_query = "SELECT * FROM Stadium WHERE SID = %s"
                        cursor.execute(check_query,(stadium_id,))
                        stadium_data = cursor.fetchone()

                        if stadium_data:
                            print(f"Current stadium data: {stadium_data}")
                            new_sname = input("Enter updated stadium name: ")
                            new_capacity = input("Enter updated capacity: ")
                            new_city = input("Enter updated city: ")

                            update_query = """
                            UPDATE Stadium
                            SET Sname = %s, Capacity = %s, City = %s
                            WHERE SID = %s
                            """

                            cursor.execute(update_query, (new_sname, new_capacity, new_city, stadium_id))
                            connection.commit()
                            print(f"Stadium with SID {stadium_id} updated successfully.")
                        else:
                            print(f"No STADIUM found with SID {stadium_id}.")


                    if table_name == 'Player':
                        player_id = input("Enter the PID of the player you want to update: ")
                        check_query = "SELECT * FROM Player WHERE PID = %s"
                        cursor.execute(check_query,(player_id,))
                        player_data = cursor.fetchone()

                        if player_data:
                            print(f"Current Player data:  {player_data}")
                            new_pname = input("Enter updated Player name: ")
                            new_pPosition = input("Enter updates Player position: ")
                            new_DOB = input("Enter new DOB for player(YYYY-MM-DD): ")
                            new_age = input("Enter new Player age: ")

                            update_query = """
                            UPDATE Player
                            SET Pname = %s, Position = %s, DOB = %s, Age = %s
                            WHERE PID = %s
                            """
                            cursor.execute(update_query, (new_pname, new_pPosition,new_DOB, new_age, player_id))
                            connection.commit()
                            print(f"Player with PID {player_id} updated successfully.")
                        else:
                            print(f"No PLAYER found with PID {player_id}.")
        
                except Exception as e:
                    print(f"ERROR: Could not update data: {e}")

            update_data()
        #EXIT
        elif(userChoice == '5'):
          
          #if user choose to exit, then check if connection is still openend, if it is then close it
          if connection.is_connected():
                cursor.close()
                connection.close()
                print("\n Database connection closed. \n") #print message for the user

        else:
            print("NOT A VALID CHOICE") #print message if user picks an option that is not valid 

# except:
#    print("ERROR: COULD NOT CONNECT TO MYSQL DATABASE") #message to print if no connection could be made with MYSQL database