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
        if userChoice == '1': 
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
        

        #WRITE DATA
        elif(userChoice == '2'):
            def create_data():
                try: 
                    random_int = random.randint(1, 1000)
                    insert_query = "INSERT INTO `Stadium` (SID, Sname, Capacity, City) VALUES (%s,%s,%s,%s)"  
                    stadium_data = (random_int ,"COTA",50000, "Austin") # added random int just so everytime its run, hopefully a different unqiue SID and no errors
                    cursor.execute(insert_query,stadium_data)
                    connection.commit()
                except Exception as e:
                    print(f"ERROR COULD NOT CREATE DATA: {e}")

            create_data()
            print("\n CREATE DATA COMPLETE \n")
            


        elif(userChoice == '3'):
            #Delete data
            print("insert data")
        elif(userChoice == '4'):
             #Update data
            print("update data")
        elif(userChoice == '5'):
         #exit
            print("exit")

        else:
            print("NOT A VALID CHOICE")

        

except:
    print("ERROR: COULD NOT CONNECT TO MYSQL DATABASE")