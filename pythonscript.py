import mysql.connector

host="localhost",  
user="root",  # Database username
password="password",  # Database password
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
    
except:
    print("ERROR: COULD NOT CONNECT TO MYSQL DATABASE")