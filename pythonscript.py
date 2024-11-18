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
            password="Boba2021",
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
        return cursor.fetchall(), [desc[0] for desc in cursor.description] #read the data 
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
        data, columns = read_data(cursor, table_name) # gets the data to be displayed in gui
        if data:
            result_window = Toplevel(root)
            result_window.title(f"Data from {table_name}")
            table = ttk.Treeview(result_window, columns=columns, show="headings") #displays the table
            for col in columns:
                table.heading(col, text=col)
            for row in data:
                table.insert("", "end", values=row)
            table.pack(fill=BOTH, expand=True)

    read_window = Toplevel(root) #creates new windwo for the read data 
    read_window.title("Read Data")
    Label(read_window, text="Select Table:").pack(pady=5)
    read_table_choice = ttk.Combobox(
        read_window,
        values=list(table_mapping.keys()) #drop down menu stuff
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


def create_data_gui(cursor, connection):
    def setup_form():
        for widget in form_frame.winfo_children():
            widget.destroy()
        input_fields.clear()  

        table_name = create_table_choice.get()

        if table_name == "Team": #creates input boxes to but in a name from country
            Label(form_frame, text="Country:").grid(row=0, column=0, padx=5, pady=5)
            input_fields["Country"] = Entry(form_frame)
            input_fields["Country"].grid(row=0, column=1, padx=5, pady=5)

            #create input field to put name of coach
            Label(form_frame, text="Coach:").grid(row=1, column=0, padx=5, pady=5)
            input_fields["Coach"] = Entry(form_frame)
            input_fields["Coach"].grid(row=1, column=1, padx=5, pady=5)

        #
        elif table_name == "Stadium": #creates field to put stamdium name
            Label(form_frame, text="Stadium Name:").grid(row=0, column=0, padx=5, pady=5)
            input_fields["Stadium Name"] = Entry(form_frame)
            input_fields["Stadium Name"].grid(row=0, column=1, padx=5, pady=5)

            #input field for capactiy
            Label(form_frame, text="Capacity:").grid(row=1, column=0, padx=5, pady=5)
            input_fields["Capacity"] = Entry(form_frame)
            input_fields["Capacity"].grid(row=1, column=1, padx=5, pady=5)

            #input field for city
            Label(form_frame, text="City:").grid(row=2, column=0, padx=5, pady=5)
            input_fields["City"] = Entry(form_frame)
            input_fields["City"].grid(row=2, column=1, padx=5, pady=5)

        elif table_name == "Player": # input field for player name
            Label(form_frame, text="Player Name:").grid(row=0, column=0, padx=5, pady=5)
            input_fields["Player Name"] = Entry(form_frame)
            input_fields["Player Name"].grid(row=0, column=1, padx=5, pady=5)

            #input field for position
            Label(form_frame, text="Position:").grid(row=1, column=0, padx=5, pady=5)
            input_fields["Position"] = Entry(form_frame)
            input_fields["Position"].grid(row=1, column=1, padx=5, pady=5)

            #input field for DOB
            Label(form_frame, text="DOB (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
            input_fields["DOB"] = Entry(form_frame)
            input_fields["DOB"].grid(row=2, column=1, padx=5, pady=5)


            #input field for AGE
            Label(form_frame, text="Age:").grid(row=3, column=0, padx=5, pady=5)
            input_fields["Age"] = Entry(form_frame)
            input_fields["Age"].grid(row=3, column=1, padx=5, pady=5)

            Label(form_frame, text="Team ID:").grid(row=4, column=0, padx=5, pady=5)
            input_fields["Team ID"] = Entry(form_frame)
            input_fields["Team ID"].grid(row=4, column=1, padx=5, pady=5)

    def submit_data(): #actual creation of the data and genreating the ID's randomly
        table_name = create_table_choice.get()
        if not table_name:
            messagebox.showerror("Error", "Please select a valid table!")
            return

        try:
            if table_name == "Team":
                data = (
                    random.randint(1, 1000),  # creating a new TID
                    input_fields["Country"].get(),
                    input_fields["Coach"].get(),
                )
            elif table_name == "Stadium":
                capacity = int(input_fields["Capacity"].get())
                data = (
                    random.randint(1, 1000), #creating a new SID
                    input_fields["Stadium Name"].get(),
                    capacity,
                    input_fields["City"].get(),
                )
            elif table_name == "Player":
                age = int(input_fields["Age"].get())
                dob = input_fields["DOB"].get()
                data = (
                    random.randint(1, 1000), #creating a new PID
                    input_fields["Player Name"].get(),
                    input_fields["Position"].get(),
                    dob,
                    age,
                    input_fields["Team ID"].get(),
                )
            else:
                messagebox.showerror("Error", "Unsupported table!") #error handling
                return

            create_data(cursor, connection, table_name, data)
            create_window.destroy()

        except ValueError as ve:
            messagebox.showerror("Validation Error", f"Invalid input: {ve}")

    # creates a new windown for the create operation
    create_window = Toplevel(root)
    create_window.title("Create Data")
    Label(create_window, text="Select Table:").pack(pady=5)
    create_table_choice = ttk.Combobox(create_window, values=["Team", "Stadium", "Player"])
    create_table_choice.pack(pady=5)
    create_table_choice.bind("<<ComboboxSelected>>", lambda _: setup_form())

    form_frame = Frame(create_window)
    form_frame.pack(pady=10)

    Button(create_window, text="Submit", command=submit_data).pack(pady=10)

    input_fields = {}

       
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


def delete_data_gui(cursor, connection):
    def submit_delete():
        table_name = table_mapping[delete_table_choice.get()]
        identifier = delete_id_input.get()
        if not table_name or not identifier:
            messagebox.showerror("Error", "Please select a table and enter an ID!") #error handling
            return
        delete_data(cursor, connection, table_name, identifier)
        delete_window.destroy()

    delete_window = Toplevel(root)
    delete_window.title("Delete Data")
    Label(delete_window, text="Select Table:").grid(row=0, column=0, padx=5, pady=5) #creates the main delete
    delete_table_choice = ttk.Combobox(delete_window, values=list(table_mapping.keys()))
    delete_table_choice.grid(row=0, column=1, padx=5, pady=5)
    Label(delete_window, text="Enter ID to Delete:").grid(row=1, column=0, padx=5, pady=5)
    delete_id_input = Entry(delete_window)
    delete_id_input.grid(row=1, column=1, padx=5, pady=5)
    Button(delete_window, text="Delete", command=submit_delete).grid(row=2, column=0, columnspan=2, pady=10)

def update_data_gui(cursor, connection):
    def setup_form():
        for widget in form_frame.winfo_children():
            widget.destroy()
        input_fields.clear()

        table_name = update_table_choice.get() 

        # add input field to get id
        Label(form_frame, text="Record ID to Update:").pack(anchor="w", padx=5, pady=5)
        input_fields["Record ID"] = Entry(form_frame)
        input_fields["Record ID"].pack(fill="x", padx=5, pady=5)

        # add input field for team
        if table_name == "Team":
            Label(form_frame, text="Country:").pack(anchor="w", padx=5, pady=5)
            input_fields["Country"] = Entry(form_frame)
            input_fields["Country"].pack(fill="x", padx=5, pady=5)

            Label(form_frame, text="Coach:").pack(anchor="w", padx=5, pady=5)
            input_fields["Coach"] = Entry(form_frame)
            input_fields["Coach"].pack(fill="x", padx=5, pady=5)

        elif table_name == "Stadium":
            Label(form_frame, text="Stadium Name:").pack(anchor="w", padx=5, pady=5)
            input_fields["Stadium Name"] = Entry(form_frame)
            input_fields["Stadium Name"].pack(fill="x", padx=5, pady=5)

            Label(form_frame, text="Capacity:").pack(anchor="w", padx=5, pady=5)
            input_fields["Capacity"] = Entry(form_frame)
            input_fields["Capacity"].pack(fill="x", padx=5, pady=5)

            Label(form_frame, text="City:").pack(anchor="w", padx=5, pady=5)
            input_fields["City"] = Entry(form_frame)
            input_fields["City"].pack(fill="x", padx=5, pady=5)

        elif table_name == "Player":
            Label(form_frame, text="Player Name:").pack(anchor="w", padx=5, pady=5)
            input_fields["Player Name"] = Entry(form_frame)
            input_fields["Player Name"].pack(fill="x", padx=5, pady=5)

            Label(form_frame, text="Position:").pack(anchor="w", padx=5, pady=5)
            input_fields["Position"] = Entry(form_frame)
            input_fields["Position"].pack(fill="x", padx=5, pady=5)

            Label(form_frame, text="DOB (YYYY-MM-DD):").pack(anchor="w", padx=5, pady=5)
            input_fields["DOB"] = Entry(form_frame)
            input_fields["DOB"].pack(fill="x", padx=5, pady=5)

            Label(form_frame, text="Age:").pack(anchor="w", padx=5, pady=5)
            input_fields["Age"] = Entry(form_frame)
            input_fields["Age"].pack(fill="x", padx=5, pady=5)

    def submit_update():
        table_name = update_table_choice.get()
        if not table_name:
            messagebox.showerror("Error", "Please select a valid table!") #error handling
            return
        record_id = input_fields["Record ID"].get()
        if not record_id:
            messagebox.showerror("Error", "Please enter the Record ID!")
            return

        try: #sql queries 
            if table_name == "Team":
                data = (input_fields["Country"].get(), input_fields["Coach"].get())
                update_query = "UPDATE Team SET Country = %s, Coach = %s WHERE TID = %s"
            elif table_name == "Stadium":
                data = (
                    input_fields["Stadium Name"].get(),
                    input_fields["Capacity"].get(),
                    input_fields["City"].get(),
                )
                update_query = "UPDATE Stadium SET Sname = %s, Capacity = %s, City = %s WHERE SID = %s"
            elif table_name == "Player":
                data = (
                    input_fields["Player Name"].get(),
                    input_fields["Position"].get(),
                    input_fields["DOB"].get(),
                    input_fields["Age"].get(),
                )
                update_query = "UPDATE Player SET Pname = %s, Position = %s, DOB = %s, Age = %s WHERE PID = %s"
            else:
                return

            cursor.execute(update_query, data + (record_id,))
            connection.commit()
            messagebox.showinfo("Success", f"Record in {table_name} updated successfully!")
            update_window.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Update Error", f"Error updating data: {e}")

    # crates new windwos for the update operation
    update_window = Toplevel(root)
    update_window.title("Update Data")
    update_window.geometry("400x400")

    Label(update_window, text="Select Table:").pack(pady=5)
    update_table_choice = ttk.Combobox(update_window, values=["Team", "Stadium", "Player"])
    update_table_choice.pack(pady=5)
    update_table_choice.bind("<<ComboboxSelected>>", lambda _: setup_form())

    form_frame = Frame(update_window)
    form_frame.pack(fill="both", expand=True, padx=10, pady=10)

    Button(update_window, text="Submit", command=submit_update).pack(pady=10)

    input_fields = {}


# advanced queries option
def advanced_queries(cursor, query):
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return rows, columns
    except mysql.connector.Error as e:
        messagebox.showerror("Query Error", f"Error executing query: {e}") #error handling
        return None, None


# creates user interface for advance queries
def show_query_results(rows, columns):
    if not rows or not columns:
        return
    
    result_window = Toplevel(root)
    result_window.title("Query Results")

    table = ttk.Treeview(result_window, columns=columns, show="headings")
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=120, anchor=CENTER)

    for row in rows:
        table.insert("", "end", values=row)

    table.pack(fill=BOTH, expand=True)

# GUI for selecting and executing advanced queries
def advanced_query_gui(cursor):
    def execute_selected_query():
        query = query_mapping[query_choice.get()]
        rows, columns = advanced_queries(cursor, query)
        show_query_results(rows, columns)

    advanced_window = Toplevel(root)
    advanced_window.title("Advanced Queries")

    Label(advanced_window, text="Select Advanced Query:").pack(pady=5)
    query_choice = ttk.Combobox(advanced_window, values=list(query_mapping.keys()))
    query_choice.pack(pady=5)

    Button(advanced_window, text="Execute Query", command=execute_selected_query).pack(pady=10)


# Advanced SQL Queries
query_mapping = {
    "Teams with Oldest Players": """
        SELECT T.Country
        FROM Team T
        WHERE NOT EXISTS (
            SELECT 1
            FROM Player P
            WHERE P.TID != T.TID AND P.Age > (
                SELECT MAX(Age) FROM Player WHERE TID = T.TID
            )
        );
    """,
    "Selects all the goals and shows player, country, time of goak, and ranks over fastest scored goals": """
        SELECT p.pname, p.position, t.country, g.Time_of_Goal,
        RANK() OVER (ORDER BY Time_of_Goal ASC) AS fastest_goal_rank
        FROM Player AS p
        LEFT JOIN goals AS g
        ON p.pid = g.pid
        LEFT JOIN team AS t
        ON g.tid = t.tid;
    """,
    "Counts the total number of players per team": """
        SELECT T.Country, COUNT(P.PID) AS Total_Players
        FROM Player P
        JOIN Team T ON P.TID = T.TID
        GROUP BY T.Country;
    """,
    "Display the IDs of teams that have earned at least 7 points in a home game": """
        SELECT DISTINCT t.TID FROM team_match AS t, gamematch AS g
        WHERE t.MID = g.MID AND t.Home_match = "yes" AND Home_team_score > 7;
    """,
    "List all players above the average age, as well as how much older they are than the average sorted from youngest to oldest": """
        SELECT Pname, (Age - (SELECT AVG(Age) FROM Player)) AS distance_from_avg_age FROM Player
    WHERE Age > (SELECT AVG(Age) FROM Player)
    ORDER BY Age ASC
    """,
    "List all past world champion team countries along with the year they won the championship, in chronological order": """
        SELECT t.Country, w.Year FROM team AS t, world_champions AS w
        WHERE t.TID = w.TID
        ORDER BY w.Year;
    """,
    "Find Average Player Age Per Team": """
        WITH TeamPlayerAges AS (
        SELECT 
            T.Country AS Team,
            P.Age AS PlayerAge
        FROM Team T
        JOIN Player P ON T.TID = P.TID
    )
    SELECT 
        Team,
        AVG(PlayerAge) AS AverageAge
    FROM TeamPlayerAges
    GROUP BY Team;
    """

}
# table mapping to be used in some of the operations
table_mapping = {
    "Team": "Team",
    "Stadium": "Stadium",
    "Player": "Player",
    "GameMatch": "GameMatch",
    "Goals" : "Goals",
    "team_match" : "team_match",
    "World_Champions" : "World_Champions",
    "TeamGroup" : "TeamGroup"
}

#tikner initalization
root = Tk()
root.title("CS425 Database Project")
root.geometry("400x300")

connection = connect_to_database()
if connection:
    cursor = connection.cursor()
    Button(root, text="Read Data", command=lambda: read_data_gui(cursor), width=20).pack(pady=10)
    Button(root, text="Create Data", command=lambda: create_data_gui(cursor, connection), width=20).pack(pady=10)
    Button(root, text="Delete Data", command=lambda: delete_data_gui(cursor, connection), width=20).pack(pady=10)
    Button(root, text="Update Data", command=lambda: update_data_gui(cursor, connection), width=20).pack(pady=10)
    Button(root, text="Advanced Queries", command=lambda: advanced_query_gui(cursor), width=20).pack(pady=10)
    Button(root, text="Exit", command=root.destroy, width=20).pack(pady=10)
    
root.mainloop()