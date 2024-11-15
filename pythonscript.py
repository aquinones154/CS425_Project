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
        messagebox.showerror("Database Connection Error", f"Error: {e}") #error message in case connnection to database cannt be made
        return None
    
    # read opeartion
def read_data(cursor, table_name):
    try:
        select_query = f"SELECT * FROM {table_name}" #select query
        cursor.execute(select_query)
        return cursor.fetchall(), [desc[0] for desc in cursor.description]
    except mysql.connector.Error as e: #error handling
        messagebox.showerror("Read Error", f"Error reading data: {e}") #error handling in case data cannot be read 
        return None, None
    
#user interface for read
def read_data_gui(cursor):
    def fetch_data():
        table_name = table_mapping[read_table_choice.get()]
        if not table_name:
            messagebox.showerror("Error", "Please select a valid table!")
            return
        data, columns = read_data(cursor, table_name)
        if data:
            result_window = Toplevel(root)
            result_window.title(f"Data from {table_name}")
            table = ttk.Treeview(result_window, columns=columns, show="headings")
            for col in columns:
                table.heading(col, text=col)
            for row in data:
                table.insert("", "end", values=row)
            table.pack(fill=BOTH, expand=True)

    read_window = Toplevel(root)
    read_window.title("Read Data")
    Label(read_window, text="Select Table:").pack(pady=5)
    read_table_choice = ttk.Combobox(
        read_window,
        values=list(table_mapping.keys())
    )
    read_table_choice.pack(pady=5)
    Button(read_window, text="Fetch Data", command=fetch_data).pack(pady=10)

#create data operation
def create_data(cursor, connection, table_name, data):
    try:
        if table_name == "Team": 
            insert_query = "INSERT INTO Team (TID, Country, Coach) VALUES (%s, %s, %s)" #create data for Team table
        elif table_name == "Stadium":
            insert_query = "INSERT INTO Stadium (SID, Sname, Capacity, City) VALUES (%s, %s, %s, %s)" #create data fro stadium table
        elif table_name == "Player":
            insert_query = "INSERT INTO Player (PID, Pname, Position, DOB, Age, TID) VALUES (%s, %s, %s, %s, %s, %s)" #create data for player table
        cursor.execute(insert_query, data)
        connection.commit()
        messagebox.showinfo("Success", f"Data inserted into {table_name}!")
    except mysql.connector.Error as e:
        messagebox.showerror("Insert Error", f"Error inserting data: {e}") #error handling incase inserting of data is not valid or succesfful



       
def delete_data(cursor, connection, table_name, identifier):
    try:
        if table_name == "Team":
            delete_query = "DELETE FROM Team WHERE TID = %s" #delete query for team
        elif table_name == "Stadium":
            delete_query = "DELETE FROM Stadium WHERE SID = %s" #delete query for Stadium 
        elif table_name == "Player":
            delete_query = "DELETE FROM Player WHERE PID = %s" #delete query for Player
        cursor.execute(delete_query, (identifier,))
        connection.commit()
        messagebox.showinfo("Success", f"Data deleted from {table_name}!")
    except mysql.connector.Error as e:
        messagebox.showerror("Delete Error", f"Error deleting data: {e}") #error handling in case delete is not successful



#         UPDATE DATA     
#         elif(userChoice == '4'):
#             def update_data():
#                 try:
#                     #ask user which table to update
#                     userChoice_update = input('Choose which table to update data in: \n 1. Team \n 2. Stadium \n 3. Player\n Please choose one: ') 

#                     # map user choice to a table
#                     table_mapping = {
#                         '1': 'Team',
#                         '2': 'Stadium',
#                         '3': 'Player',
#                     }
                    
#                      # Fetch the table name based on the user's choice
#                     table_name = table_mapping.get(userChoice_update)

#                     if not table_name:
#                         print("Invalid choice")
#                         return
                    
#                     if table_name == 'Team' : 
#                         team_id = input("Enter the TID of the team you want to update: ")
#                         check_query = "SELECT * FROM Team WHERE TID = %s"
#                         cursor.execute(check_query,(team_id,))
#                         team_data = cursor.fetchone()

#                         if team_data:
#                             print(f"Current team data: {team_data}")
#                             new_country = input("Enter updated country: ")
#                             new_coach = input("Enter updated coach: ")

#                             update_query = """
#                             UPDATE Team
#                             SET Country = %s, Coach = %s
#                             WHERE TID = %s
#                             """

#                             cursor.execute(update_query, (new_country,new_coach, team_id))
#                             connection.commit()
#                             print(f"Team with TID {team_id} updated successfully.")

#                         else:
#                             print(f"No Team found with TID {team_id}")                            

#                     elif table_name == 'Stadium':
#                         stadium_id = input("Enter the SID of the stadium you want to update: ")
#                         check_query = "SELECT * FROM Stadium WHERE SID = %s"
#                         cursor.execute(check_query,(stadium_id,))
#                         stadium_data = cursor.fetchone()

#                         if stadium_data:
#                             print(f"Current stadium data: {stadium_data}")
#                             new_sname = input("Enter updated stadium name: ")
#                             new_capacity = input("Enter updated capacity: ")
#                             new_city = input("Enter updated city: ")

#                             update_query = """
#                             UPDATE Stadium
#                             SET Sname = %s, Capacity = %s, City = %s
#                             WHERE SID = %s
#                             """

#                             cursor.execute(update_query, (new_sname, new_capacity, new_city, stadium_id))
#                             connection.commit()
#                             print(f"Stadium with SID {stadium_id} updated successfully.")
#                         else:
#                             print(f"No STADIUM found with SID {stadium_id}.")


#                     if table_name == 'Player':
#                         player_id = input("Enter the PID of the player you want to update: ")
#                         check_query = "SELECT * FROM Player WHERE PID = %s"
#                         cursor.execute(check_query,(player_id,))
#                         player_data = cursor.fetchone()

#                         if player_data:
#                             print(f"Current Player data:  {player_data}")
#                             new_pname = input("Enter updated Player name: ")
#                             new_pPosition = input("Enter updates Player position: ")
#                             new_DOB = input("Enter new DOB for player(YYYY-MM-DD): ")
#                             new_age = input("Enter new Player age: ")

#                             update_query = """
#                             UPDATE Player
#                             SET Pname = %s, Position = %s, DOB = %s, Age = %s
#                             WHERE PID = %s
#                             """
#                             cursor.execute(update_query, (new_pname, new_pPosition,new_DOB, new_age, player_id))
#                             connection.commit()
#                             print(f"Player with PID {player_id} updated successfully.")
#                         else:
#                             print(f"No PLAYER found with PID {player_id}.")
        
#                 except Exception as e:
#                     print(f"ERROR: Could not update data: {e}")

#             update_data()
#         #EXIT
#         elif(userChoice == '5'):
          
#           #if user choose to exit, then check if connection is still openend, if it is then close it
#           if connection.is_connected():
#                 cursor.close()
#                 connection.close()
#                 print("\n Database connection closed. \n") #print message for the user

#         else:
#             print("NOT A VALID CHOICE") #print message if user picks an option that is not valid 

# # except:
# #    print("ERROR: COULD NOT CONNECT TO MYSQL DATABASE") #message to print if no connection could be made with MYSQL database

# table mapping to be used in some of the operations
table_mapping = {
    "Team": "Team",
    "Stadium": "Stadium",
    "Player": "Player"
}

#tikner initalization
root = Tk()
root.title("CS425 Database Project")
root.geometry("400x300")