import tkinter as tk
import mysql.connector

# Create a connection to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sidshan2003!!",
    database="library"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a function to execute the SQL query and display the results in a listbox
def execute_query():
    # Get the SQL query from the input box
    query = input_box.get()

    # Execute the SQL query
    cursor.execute(query)

    # Get the results of the query
    results = cursor.fetchall()

    # Clear the listbox
    result_listbox.delete(0, tk.END)

    # Display the results in the listbox
    for row in results:
        result_listbox.insert(tk.END, row)

class Dashboard:

    def __init__(self) -> None:
        window = tk.Tk()
        window.title("SQL Project Frontend")

# Create a function to add a new user to the database
def add_user():
    # Get the user's information from the input boxes
    userID=userID_box.get()
    firstname = firstname_box.get()
    middlename = middlename_box.get()
    lastname = lastname_box.get()
    city = city_box.get()
    street = street_box.get()
    postalCode = postalCode_box.get()

    # Execute the SQL query to insert the new user into the database
    query = f"INSERT INTO userInfo (userID,firstname, middlename, lastname, city, street, postalCode) VALUES ('{userID}','{firstname}', '{middlename}', '{lastname}', '{city}', '{street}', '{postalCode}')"
    cursor.execute(query)
    conn.commit()

    # Clear the input boxes
    userID_box.delete(0, tk.END)
    firstname_box.delete(0, tk.END)
    middlename_box.delete(0, tk.END)
    lastname_box.delete(0, tk.END)
    city_box.delete(0, tk.END)
    street_box.delete(0, tk.END)
    postalCode_box.delete(0, tk.END)

    # Display a message to the user
    message_label.config(text="User added successfully!")

# Create the main window
window = tk.Tk()
window.title("SQL Project Frontend")

# Create the input box for the SQL query
input_box = tk.Entry(window)
input_box.pack()

# Create the button to execute the SQL query
execute_button = tk.Button(window, text="Execute", command=execute_query)
execute_button.pack()

# Create input boxes for adding a new user
userID_label = tk.Label(window, text="UserID:")
userID_label.pack()
userID_box = tk.Entry(window)
userID_box.pack()

firstname_label = tk.Label(window, text="First Name:")
firstname_label.pack()
firstname_box = tk.Entry(window)
firstname_box.pack()

middlename_label = tk.Label(window, text="Middle Name:")
middlename_label.pack()
middlename_box = tk.Entry(window)
middlename_box.pack()

lastname_label = tk.Label(window, text="Last Name:")
lastname_label.pack()
lastname_box = tk.Entry(window)
lastname_box.pack()

city_label = tk.Label(window, text="City:")
city_label.pack()
city_box = tk.Entry(window)
city_box.pack()

street_label = tk.Label(window, text="Street:")
street_label.pack()
street_box = tk.Entry(window)
street_box.pack()

postalCode_label = tk.Label(window, text="Postal Code:")
postalCode_label.pack()
postalCode_box = tk.Entry(window)
postalCode_box.pack()

# Create the button to add a new user
add_button = tk.Button(window, text="Add User", command=add_user)
add_button.pack()

# Create a label to display messages to the user
message_label = tk.Label(window, text="")
message_label.pack()

# Create the listbox to display the results
result_listbox = tk.Listbox(window)
result_listbox.pack()

# Start the main event loop
window.mainloop()

# Close the connection to the MySQL database
conn.close()
