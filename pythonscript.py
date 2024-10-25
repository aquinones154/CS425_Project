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
        

        if(userChoice == '1' ):
            #read data
            print("read data")
        elif(userChoice == '2'):
            #write data
            print("write data")
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