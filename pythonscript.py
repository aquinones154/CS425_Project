import mysql.connector

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
        userChoice= input('1. Read Data \n 2. Write Data \n 3. Insert Data \n 4. Update Data \n 5. Exit \n Enter which on you would like to do:  ')
        

        #READ DATA
        if (userChoice == '1'):
            def read_data():
                try:
                # Read data from table
                    select_query = "SELECT * FROM Player"  # selects everything from player table
                    cursor.execute(select_query)
                    player_data = cursor.fetchall()  # Fe
                    return player_data
                except:
                    print("ERROR COULD NOT READ DATA")
                    return None

            player_data = read_data()
            if player_data:
                print(player_data)  #prints data
                print("\n READ DATA COMPLETE \n") #print message to show it worked
            else:
                print("ERROR COULD NOT READ DATA") #if it didnt work then print error message


        #WRITE DATA
        elif(userChoice == '2'):
            def write_data():
                try: 
                    insert_query = "INSERT INTO `Stadium` (SID, Sname, Capacity, City) VALUES (%s,%s,%s,%s)"
                    stadium_data = (52 ,"COTA",50000, "Austin") #once running once change SID, if not then error will pop up saying error-> duplicate entry
                    cursor.execute(insert_query,stadium_data)
                    connection.commit()
                except Exception as e:
                    print(f"ERROR COULD NOT WRITE DATA: {e}")

            write_data()
            print("\n WRITE DATA COMPLETE \n")
            


        elif(userChoice == '3'):
            #Insert data
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