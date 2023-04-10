import tkinter as tk
import mysql.connector

pw=input('Enter password to database')

# Create a connection to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pw,
    database="library"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

class User:

    def __init__(self) -> None:
        # Create a cursor object to execute SQL queries
        self.cursor = conn.cursor()


    def dashboard(self):
        root = tk.Tk()
        add_user_button = tk.Button(root, text="Add new user", command=self.add_user_driver)
        add_user_button.pack()

        delete_user_button = tk.Button(root, text="Delete existing user", command=self.delete_user_driver)
        delete_user_button.pack()

        root.mainloop()


    # Create a function to add a new user to the database
    def add_user(self):
        # Get the user's information from the input boxes
        firstname = self.firstname_box.get()
        middlename = self.middlename_box.get()
        lastname = self.lastname_box.get()
        city = self.city_box.get()
        street = self.street_box.get()
        postalCode = self.postalCode_box.get()
        userID=self.userID_box.get()
        contact=self.contact_box.get()
        phoneID=contact+userID

        # Execute the SQL query to insert the new user into the database
        query1 = f"INSERT INTO userInfo (userID,firstname, middlename, lastname, city, street, postalCode) VALUES ('{userID}','{firstname}', '{middlename}', '{lastname}', '{city}', '{street}', '{postalCode}')"
        self.cursor.execute(query1)

        query2=f"INSERT INTO usercontact(phoneID,userID,phoneNum) VALUES ('{phoneID}','{userID}','{contact}')"
        self.cursor.execute(query2)
        conn.commit()

        # Clear the input boxes
        self.userID_box.delete(0, tk.END)
        self.firstname_box.delete(0, tk.END)
        self.middlename_box.delete(0, tk.END)
        self.lastname_box.delete(0, tk.END)
        self.city_box.delete(0, tk.END)
        self.street_box.delete(0, tk.END)
        self.postalCode_box.delete(0, tk.END)
        self.contact_box.delete(0, tk.END)

        # Display a message to the user
        self.message_label.config(text="User added successfully!")

    def add_user_driver(self):
        
        # Create the main window
        window = tk.Tk()
        window.title("SQL Project Frontend")

        # Create input boxes for adding a new user
        firstname_label = tk.Label(window, text="First Name:")
        firstname_label.pack()
        self.firstname_box = tk.Entry(window)
        self.firstname_box.pack()

        middlename_label = tk.Label(window, text="Middle Name:")
        middlename_label.pack()
        self.middlename_box = tk.Entry(window)
        self.middlename_box.pack()

        lastname_label = tk.Label(window, text="Last Name:")
        lastname_label.pack()
        self.lastname_box = tk.Entry(window)
        self.lastname_box.pack()

        city_label = tk.Label(window, text="City:")
        city_label.pack()
        self.city_box = tk.Entry(window)
        self.city_box.pack()

        street_label = tk.Label(window, text="Street:")
        street_label.pack()
        self.street_box = tk.Entry(window)
        self.street_box.pack()

        postalCode_label = tk.Label(window, text="Postal Code:")
        postalCode_label.pack()
        self.postalCode_box = tk.Entry(window)
        self.postalCode_box.pack()

        contact_label = tk.Label(window, text="Phone number:")
        contact_label.pack()
        self.contact_box = tk.Entry(window)
        self.contact_box.pack()

        userID_label = tk.Label(window, text="Password:")
        userID_label.pack()
        self.userID_box = tk.Entry(window)
        self.userID_box.pack()

        # Create the button to add a new user
        add_button = tk.Button(window, text="Add User", command=self.add_user)
        add_button.pack()

        # Create a label to display messages to the user
        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        # Start the main event loop
        window.mainloop()

    def delete_user(self):
        # Get the user's information from the input boxes
        userID=self.delete_userID_box.get()

        query1=f"DELETE FROM usercontact where userID='{userID}'"
        self.cursor.execute(query1)

        query2 = f"DELETE FROM userinfo where userID='{userID}'"
        self.cursor.execute(query2)

        
        conn.commit()

        # Display a message to the user
        self.message_label.config(text="User deleted successfully!")

        # Clear the input boxes
        self.delete_userID_box.delete(0, tk.END)


    def delete_user_driver(self):
        # Create the main window
        window = tk.Tk()
        window.title("SQL Project Frontend")

        # Create input boxes for adding a new user
        userID_label = tk.Label(window, text="UserID:")
        userID_label.pack()
        self.delete_userID_box = tk.Entry(window)
        self.delete_userID_box.pack()

        # Create the button to add a new user
        add_button = tk.Button(window, text="Delete User", command=self.delete_user)
        add_button.pack()

        # Create a label to display messages to the user
        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        # Start the main event loop
        window.mainloop()



user=User()
user.dashboard()
# Close the connection to the MySQL database
conn.close()

