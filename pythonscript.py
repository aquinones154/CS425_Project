import mysql.connector
import random

host="localhost" # host name
user="root"  # Database username
password="password"  # Database password
database="womensWrlCUP"  # Name of the database to use


try: 
# Connect to the MySQL database
    connection = mysql.connector.connect(
    host=host,
    user=user,  
    password=password, 
    database=database
)
    
    if connection.is_connected():
        print("Connected to MYSQL database successfully")

        cursor = connection.cursor()

        #print statemnts for user to select what they want to do
        userChoice= input(' 1. Read Data \n 2. Create Data \n 3. Delete Data \n 4. Update Data \n 5. Exit \n Enter which on you would like to do:  ')
        
        #function to read data
        def read_data(table_name):
            try:
                select_query = f"SELECT * FROM {table_name}" #default query is select all from a table
                cursor.execute(select_query)
                return cursor.fetchall()
            except Exception as e: #exception handling
                print(f"ERROR COULD NOT READ DATA FROM: {table_name}: {e}") #if there is an expcetion, then tell user the table name and what the exception is
                return None #end

        # READ DATA
        if (userChoice == '1'): 
            userChoice_read = input('Choose which table to read from: \n 1. Team \n 2. Stadium \n 3. Player \n 4. GameMatch \n 5. Goals \n 6. Team_match \n 7. World_Champions \n 8. TeamGroup \n 9. Team_tournament \n Please choose one: ') #asking user to pick a table to read from
            
            #map a number to a table name
            table_mapping = {
                '1': 'Team',
                '2': 'Stadium',
                '3': 'Player',
                '4': 'GameMatch',
                '5': 'Goals',
                '6': 'Team_match',
                '7': 'World_Champions',
                '8': 'TeamGroup',
                '9': 'Team_tournament'
            }
            
            if userChoice_read in table_mapping: #if a valid choice then read data
                table_name = table_mapping[userChoice_read]
                data = read_data(table_name)
                if data:
                    print(f"\n Data from {table_name}: \n") #printing data
                    for row in data:
                        print(row)
                    print("\n READ DATA COMPLETE \n") #print for sucessful completion of data read
                else:
                    print("ERROR COULD NOT READ DATA") #print if data could not be read
            else:
                print("INVALID CHOICE") #print message only if choice is not valid
        

        #CREATE DATA
        elif(userChoice == '2'):
            
            def create_data():
                try:
                    # Ask the user which table they want to insert data into
                    userChoice_create = input(
                        'Choose which table to create data in: \n' #pick from the following 
                        '1. Team \n'
                        '2. Stadium \n'
                        '3. Player \n'
                        'Please choose one: '
                    )

                    # map user choice to a table
                    table_mapping = {
                        '1': 'Team',
                        '2': 'Stadium',
                        '3': 'Player',
                    }

                    # get table based off of user choice
                    table_name = table_mapping.get(userChoice_create)

                    if not table_name:
                        print("Invalid choice") #making sure chocie is valid
                        return
                    
                    # if team table then get the new data to be created
                    if table_name == 'Team':
                        tid = random.randint(1, 1000) #creating random TID for team
                        country = input("Enter team country: ") #asking user for country name
                        coach = input("Enter coach name: ") #asking user for coach name
                        insert_query = "INSERT INTO Team (TID, Country, Coach) VALUES (%s, %s, %s)" #query to insert data into team table
                        data = (tid, country, coach) #save it into data to be used at end of function

                    #if Stadium table then get the new data to be created
                    elif table_name == 'Stadium':
                        sid = random.randint(1, 1000) #creating random SID 
                        sname = input("Enter stadium name: ") #ask user for stadium name
                        capacity = input("Enter capacity: ") #ask user for capacity
                        city = input("Enter city: ") #ask user for city 
                        insert_query = "INSERT INTO Stadium (SID, Sname, Capacity, City) VALUES (%s, %s, %s, %s)" #query to inser data into stadium table
                        data = (sid, sname, capacity, city) #save it into data to be used at the end of function


                    elif table_name == 'Player': #if player table then get new data to be created
                        pid = random.randint(1, 1000) #create new random PID
                        pname = input("Enter player name: ") # enter name for new player
                        position = input("Enter player position: ") #enter postiion for player
                        dob = input("Enter date of birth (YYYY-MM-DD): ") #etner date of birth for new player
                        age = input("Enter player age: ") #enter age for player
                        tid = input("Enter team ID: ") #enter team ID for player
                        insert_query = "INSERT INTO Player (PID, Pname, Position, DOB, Age, TID) VALUES (%s, %s, %s, %s, %s, %s)"
                        data = (pid, pname, position, dob, age, tid)

                    # Execute the insert query
                    cursor.execute(insert_query, data)
                    connection.commit()

                    print(f"\nData inserted successfully into {table_name}.\n")
                
                except Exception as e:
                    print(f"ERROR COULD NOT CREATE DATA: {e}")

            create_data()

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

        

except:
    print("ERROR: COULD NOT CONNECT TO MYSQL DATABASE") #message to print if no connection could be made with MYSQL database