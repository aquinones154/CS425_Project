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

#create_data user interface
def create_data_gui(cursor, connection):
    def submit_data():
        table_name = table_mapping[create_table_choice.get()]
        if not table_name:
            messagebox.showerror("Error", "Please select a valid table!")
            return

        if table_name == "Team":
            data = (random.randint(1, 1000), country_input.get(), coach_input.get())
        elif table_name == "Stadium":
            data = (
                random.randint(1, 1000),
                stadium_name_input.get(),
                capacity_input.get(),
                city_input.get(),
            )
        elif table_name == "Player":
            data = (
                random.randint(1, 1000),
                player_name_input.get(),
                position_input.get(),
                dob_input.get(),
                age_input.get(),
                tid_input.get(),
            )
        create_data(cursor, connection, table_name, data)
        create_window.destroy()

       
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
            messagebox.showerror("Error", "Please select a table and enter an ID!")
            return
        delete_data(cursor, connection, table_name, identifier)
        delete_window.destroy()

    delete_window = Toplevel(root)
    delete_window.title("Delete Data")
    Label(delete_window, text="Select Table:").grid(row=0, column=0, padx=5, pady=5)
    delete_table_choice = ttk.Combobox(delete_window, values=list(table_mapping.keys()))
    delete_table_choice.grid(row=0, column=1, padx=5, pady=5)
    Label(delete_window, text="Enter ID to Delete:").grid(row=1, column=0, padx=5, pady=5)
    delete_id_input = Entry(delete_window)
    delete_id_input.grid(row=1, column=1, padx=5, pady=5)
    Button(delete_window, text="Delete", command=submit_delete).grid(row=2, column=0, columnspan=2, pady=10)

# main menu for gui
def setup_form():
    for widget in form_frame.winfo_children():
        widget.destroy()
    table_name = table_mapping[create_table_choice.get()]
    if table_name == "Team":
        Label(form_frame, text="Country:").grid(row=0, column=0, padx=5, pady=5)
        global country_input, coach_input
        country_input = Entry(form_frame)
        country_input.grid(row=0, column=1, padx=5, pady=5)
        Label(form_frame, text="Coach:").grid(row=1, column=0, padx=5, pady=5)
        coach_input = Entry(form_frame)
        coach_input.grid(row=1, column=1, padx=5, pady=5)
    elif table_name == "Stadium":
        Label(form_frame, text="Stadium Name:").grid(row=0, column=0, padx=5, pady=5)
        global stadium_name_input, capacity_input, city_input
        stadium_name_input = Entry(form_frame)
        stadium_name_input.grid(row=0, column=1, padx=5, pady=5)
        Label(form_frame, text="Capacity:").grid(row=1, column=0, padx=5, pady=5)
        capacity_input = Entry(form_frame)
        capacity_input.grid(row=1, column=1, padx=5, pady=5)
        Label(form_frame, text="City:").grid(row=2, column=0, padx=5, pady=5)
        city_input = Entry(form_frame)
        city_input.grid(row=2, column=1, padx=5, pady=5)
    elif table_name == "Player":
        Label(form_frame, text="Player Name:").grid(row=0, column=0, padx=5, pady=5)
        global player_name_input, position_input, dob_input, age_input, tid_input
        player_name_input = Entry(form_frame)
        player_name_input.grid(row=0, column=1, padx=5, pady=5)
        Label(form_frame, text="Position:").grid(row=1, column=0, padx=5, pady=5)
        position_input = Entry(form_frame)
        position_input.grid(row=1, column=1, padx=5, pady=5)
        Label(form_frame, text="DOB (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        dob_input = Entry(form_frame)
        dob_input.grid(row=2, column=1, padx=5, pady=5)
        Label(form_frame, text="Age:").grid(row=3, column=0, padx=5, pady=5)
        age_input = Entry(form_frame)
        age_input.grid(row=3, column=1, padx=5, pady=5)
        Label(form_frame, text="Team ID:").grid(row=4, column=0, padx=5, pady=5)
        tid_input = Entry(form_frame)
        tid_input.grid(row=4, column=1, padx=5, pady=5)

        create_window = Toplevel(root)
        create_window.title("Add Data")
        Label(create_window, text="Select Table:").pack(pady=5)
        create_table_choice = ttk.Combobox(
        create_window,
        values=list(table_mapping.keys())
        )
        create_table_choice.pack(pady=5)
        create_table_choice.bind("<<ComboboxSelected>>", lambda _: setup_form())
        form_frame = Frame(create_window)
        form_frame.pack(pady=10)
        Button(create_window, text="Submit", command=submit_data).pack(pady=10)


def update_data():
        table_name = table_mapping[update_table_choice.get()]
        identifier = record_id_input.get()
        if not identifier:
            messagebox.showerror("Error", "Please enter the Record ID!")
            return
        if table_name == "Team":
            data = (country_input.get(), coach_input.get())
        elif table_name == "Stadium":
            data = (stadium_name_input.get(), capacity_input.get(), city_input.get())
        elif table_name == "Player":
            data = (player_name_input.get(), position_input.get(), dob_input.get(), age_input.get())
        else:
            return
        update_data(cursor, connection, table_name, identifier, data)
        update_window.destroy()

        update_window = Toplevel(root)
        update_window.title("Update Data")
        Label(update_window, text="Select Table:").pack(pady=5)
        update_table_choice = ttk.Combobox(
        update_window,
        values=list(table_mapping.keys())
        )
        update_table_choice.pack(pady=5)
        update_table_choice.bind("<<ComboboxSelected>>", lambda _: setup_update_form())
        form_frame = Frame(update_window)
        form_frame.pack(pady=10)
        Button(update_window, text="Submit", command=submit_update).pack(pady=10)


# GUI Functions
def update_data_gui(cursor, connection):
    def setup_update_form():
            for widget in form_frame.winfo_children():
                widget.destroy()
            table_name = table_mapping[update_table_choice.get()]
            Label(form_frame, text="Enter Record ID to Update:").grid(row=0, column=0, padx=5, pady=5)
            global record_id_input
            record_id_input = Entry(form_frame)
            record_id_input.grid(row=0, column=1, padx=5, pady=5)

            if table_name == "Team":
                Label(form_frame, text="Country:").grid(row=1, column=0, padx=5, pady=5)
                global country_input, coach_input
                country_input = Entry(form_frame)
                country_input.grid(row=1, column=1, padx=5, pady=5)
                Label(form_frame, text="Coach:").grid(row=2, column=0, padx=5, pady=5)
                coach_input = Entry(form_frame)
                coach_input.grid(row=2, column=1, padx=5, pady=5)
            elif table_name == "Stadium":
                Label(form_frame, text="Stadium Name:").grid(row=1, column=0, padx=5, pady=5)
                global stadium_name_input, capacity_input, city_input
                stadium_name_input = Entry(form_frame)
                stadium_name_input.grid(row=1, column=1, padx=5, pady=5)
                Label(form_frame, text="Capacity:").grid(row=2, column=0, padx=5, pady=5)
                capacity_input = Entry(form_frame)
                capacity_input.grid(row=2, column=1, padx=5, pady=5)
                Label(form_frame, text="City:").grid(row=3, column=0, padx=5, pady=5)
                city_input = Entry(form_frame)
                city_input.grid(row=3, column=1, padx=5, pady=5)
            elif table_name == "Player":
                Label(form_frame, text="Player Name:").grid(row=1, column=0, padx=5, pady=5)
                global player_name_input, position_input, dob_input, age_input
                player_name_input = Entry(form_frame)
                player_name_input.grid(row=1, column=1, padx=5, pady=5)
                Label(form_frame, text="Position:").grid(row=2, column=0, padx=5, pady=5)
                position_input = Entry(form_frame)
                position_input.grid(row=2, column=1, padx=5, pady=5)
                Label(form_frame, text="DOB (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
                dob_input = Entry(form_frame)
                dob_input.grid(row=3, column=1, padx=5, pady=5)
                Label(form_frame, text="Age:").grid(row=4, column=0, padx=5, pady=5)
                age_input = Entry(form_frame)
                age_input.grid(row=4, column=1, padx=5, pady=5)

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

connection = connect_to_database()
if connection:
    cursor = connection.cursor()
    Button(root, text="Read Data", command=lambda: read_data_gui(cursor), width=20).pack(pady=10)
    Button(root, text="Add Data", command=lambda: create_data_gui(cursor, connection), width=20).pack(pady=10)
    Button(root, text="Delete Data", command=lambda: delete_data_gui(cursor, connection), width=20).pack(pady=10)
    Button(root, text="Update Data", command=lambda: update_data_gui(cursor, connection), width=20).pack(pady=10)
    Button(root, text="Exit", command=root.destroy, width=20).pack(pady=10)
    
root.mainloop()