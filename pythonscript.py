import mysql.connector
import random

host="localhost" # host name
user="root"  # Database username
password="Boba2021"  # Database password
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
                    userChoice_Create = input('Choose which table to Create data in: \n 1. Team \n 2. Stadium \n 3. Player \n 4. GameMatch \n 5. Goals \n 6. Team_match \n 7. World_Champions \n 8. TeamGroup \n 9. Team_tournament \n Please choose one: ') #asking user to pick a table to create data in 

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
                  
                except Exception as e:
                    print(f"ERROR COULD NOT CREATE DATA: {e}")


        elif(userChoice == '3'):
            #Delete data
            print("delete data")


        #UPDATE DATA     
        elif(userChoice == '4'):
            def update_data():
                try:
                     #ask user for TID they want to modify
                    team_id = input("Enter the TEAM ID (TID) of the Team you want to update: ")
            
                    # verifying whether it is a valid TID or not
                    check_query = "SELECT * FROM Team WHERE TID = %s"
                    cursor.execute(check_query, (team_id,))
                    team_data = cursor.fetchone()
            
                    if team_data:
                        print(f"Current team data: {team_data}")
                
                        # asking for updated data to be put into table
                        new_country = input("Enter updated country: ")
                        new_coach = input("Enter updated coach: ")
                
                        # Update the team data
                        update_query = """
                        UPDATE Team
                        SET Country = %s, Coach = %s
                        WHERE TID = %s
                        """
                
                        # Execute the update query with new data
                        cursor.execute(update_query, (new_country, new_coach,team_id))
                        connection.commit()  # commit the changes
                
                        print(f"TEAM with TID {team_id} updated successfully.") #print messsage to user that successfull update of data
            
                    else:
                        print(f"No TEAM found with TID {team_id}.") #if not able to update data then let user know
        
                except Exception as e: 
                    print(f"ERROR COULD NOT UPDATE DATA: {e}") #error message for user

            # call the update function
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