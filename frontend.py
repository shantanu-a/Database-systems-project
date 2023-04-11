import tkinter as tk
import mysql.connector
import time
import datetime
import getpass
from tkinter import *
 

pw = getpass.getpass(prompt='Enter password to database:')

# Create a connection to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pw,
    database="library"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

class Library:

    def __init__(self) -> None:
        # Create a cursor object to execute SQL queries
        self.cursor = conn.cursor()


    def dashboard(self):
        root = tk.Tk()
        add_user_button = tk.Button(root, text="Add new user", command=self.add_user_driver)
        add_user_button.pack()

        delete_user_button = tk.Button(root, text="Delete existing user", command=self.delete_user_driver)
        delete_user_button.pack()

        issue_book_button = tk.Button(root, text="Issue a book", command=self.issue_book_driver)
        issue_book_button.pack()

        return_book_button = tk.Button(root, text="Return a book", command=self.return_book_driver)
        return_book_button.pack()

        add_book_button = tk.Button(root, text="Add new book", command=self.add_book_driver)
        add_book_button.pack()

        delete_book_button = tk.Button(root, text="Delete existing book", command=self.delete_book_driver)
        delete_book_button.pack()

        show_fine_button = tk.Button(root, text="User fine", command=self.show_fine_driver)
        show_fine_button.pack()

        show_fine_by_all_button = tk.Button(root, text="Total fine paid", command=self.show_fine_by_all_driver)
        show_fine_by_all_button.pack()

        update_book_copies_button = tk.Button(root, text="Update no. of copies of book", command=self.update_book_copies_driver)
        update_book_copies_button.pack()

        checked_out_books_button = tk.Button(root, text="List of checked out books", command=self.checked_out_books_driver)
        checked_out_books_button.pack()

        overdue_button = tk.Button(root, text="Overdue items", command=self.overdue_items_driver)
        overdue_button.pack()
        

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


    def issue_book(self):
        issueDate = datetime.datetime.now()
        
        # ts store timestamp of current time
        ts = issueDate.timestamp()

        due_ts=int(ts)-864000
        # dueDate=datetime.fromtimestamp(due_ts)

        returnDate=1.1

        # Get the user's information from the input boxes
        userID=self.issue_userID_box.get()
        ISBN=self.issue_ISBN.get()
        circulationID=userID+ISBN

        # query1 = f"INSERT INTO userInfo (userID,firstname, middlename, lastname, city, street, postalCode) VALUES ('{userID}','{firstname}', '{middlename}', '{lastname}', '{city}', '{street}', '{postalCode}')"

        query1=f"INSERT INTO circulationrecord (circulationID,userID,ISBN,dueDate,returnDate) VALUES ('{circulationID}','{userID}','{ISBN}','{due_ts}','{returnDate}')"
        self.cursor.execute(query1)

        # query2 = f"INSERT INTO issues(userID,ISBN,issueDate) VALUES ('{userID}','{ISBN}','{issueDate}')"
        # self.cursor.execute(query2)

        
        conn.commit()

        # Display a message to the user
        self.message_label.config(text="Book issued!")

        # Clear the input boxes
        self.issue_userID_box.delete(0, tk.END)
        self.issue_ISBN.delete(0, tk.END)

    def issue_book_driver(self):
        # Create the main window
        window = tk.Tk()
        window.title("SQL Project Frontend")

        # Create input boxes for adding a new user
        issue_userID_label = tk.Label(window, text="UserID:")
        issue_userID_label.pack()
        self.issue_userID_box = tk.Entry(window)
        self.issue_userID_box.pack()

        issue_ISBN_label = tk.Label(window, text="ISBN:")
        issue_ISBN_label.pack()
        self.issue_ISBN = tk.Entry(window)
        self.issue_ISBN.pack()

        # Create the button to add a new user
        add_button = tk.Button(window, text="Issue book", command=self.issue_book)
        add_button.pack()

        # Create a label to display messages to the user
        self.message_label = tk.Label(window, text="")
        self.message_label.pack()


    def return_book(self):
        returnDate = datetime.datetime.now()
        
        # ts store timestamp of current time
        ts = returnDate.timestamp()

        # Get the user's information from the input boxes
        userID=self.return_userID_box.get()
        ISBN=self.return_ISBN_box.get()
        circulationID=userID+ISBN

        self.cursor.execute(f"SELECT dueDate FROM circulationrecord WHERE circulationID='{circulationID}'")
        dueDate=self.cursor.fetchone()

        if(dueDate[0]<ts):
            fineID=str(dueDate[0])+str(userID)
            self.cursor.execute(f"INSERT INTO finerecord (fineID,userID,reason,ISBN,amount) VALUES ('{fineID}','{userID}','{'late'}','{ISBN}','{'100'}')")
            self.message_label.config(text="Late! Fine issued.")

        query2=f"DELETE FROM circulationrecord WHERE circulationID='{circulationID}' "
        self.cursor.execute(query2)

        
        conn.commit()

        # Display a message to the user
        self.message_label.config(text="Book returned!")

        # Clear the input boxes
        self.return_userID_box.delete(0, tk.END)
        self.return_ISBN_box.delete(0, tk.END)

    def return_book_driver(self):
        window=tk.Tk()
        window.title('Return book')

        userID_label = tk.Label(window, text="UserID:")
        userID_label.pack()
        self.return_userID_box = tk.Entry(window)
        self.return_userID_box.pack()

        return_ISBN_label = tk.Label(window, text="ISBN:")
        return_ISBN_label.pack()
        self.return_ISBN_box = tk.Entry(window)
        self.return_ISBN_box.pack()

        add_button = tk.Button(window, text="Return book", command=self.return_book)
        add_button.pack()

        # Create a label to display messages to the user
        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        # Start the main event loop
        window.mainloop()

    def show_fine(self):
        # Get the user's information from the input boxes
        userID=self.fine_userID_box.get()

        query1=f"SELECT SUM(AMOUNT) FROM finerecord where userID='{userID}'"
        self.cursor.execute(query1)

        fine_amount=self.cursor.fetchone()

        fine_window=tk.Tk()
        fine_window.title('Fine')

        userID_label = tk.Label(fine_window, text=f"Fine uptil now is: {fine_amount[0]}")
        userID_label.pack()
        
        conn.commit()

        # Clear the input boxes
        self.fine_userID_box.delete(0, tk.END)

    def show_fine_driver(self):
        window=tk.Tk()
        window.title('Show fine')

        userID_label = tk.Label(window, text="UserID:")
        userID_label.pack()
        self.fine_userID_box = tk.Entry(window)
        self.fine_userID_box.pack()

        add_button = tk.Button(window, text="Show fine", command=self.show_fine)
        add_button.pack()

        # Create a label to display messages to the user
        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        # Start the main event loop
        window.mainloop()


    def show_fine_by_all_driver(self):
        query1=f"SELECT SUM(AMOUNT) FROM finerecord"
        self.cursor.execute(query1)

        fine_amount=self.cursor.fetchone()

        window=tk.Tk()
        window.title('Show fine')

        userID_label = tk.Label(window, text=f"Fine paid by all users is: {fine_amount[0]}")
        userID_label.pack()

        # Start the main event loop
        window.mainloop()


    # Create a function to add a new book to the database
    def add_book(self):
        # Get the book's information from the input boxes
        ISBN = self.ISBN_box.get()
        title = self.title_box.get()
        publisher = self.publisher_box.get()
        authorFirstName = self.authorFirstName_box.get()
        authorMiddleName = self.authorMiddleName_box.get()
        authorLastName = self.authorLastName_box.get()
        numCopy = self.numCopy_box.get()

        # Execute the SQL query to insert the new user into the database
        query1 = f"INSERT INTO bookInfo (ISBN, title, publisher, numCopy) VALUES ('{ISBN}','{title}', '{publisher}', '{numCopy}')"
        self.cursor.execute(query1)

        query2=f"INSERT INTO bookAuthor(ISBN, authorFirstName, authorMiddleName, authorLastName) VALUES ('{ISBN}', '{authorFirstName}', '{authorMiddleName}', '{authorLastName}')"
        self.cursor.execute(query2)
        conn.commit()

        # Clear the input boxes
        self.ISBN_box.delete(0, tk.END)
        self.title_box.delete(0, tk.END)
        self.publisher_box.delete(0, tk.END)
        self.numCopy_box.delete(0, tk.END)
        self.authorFirstName_box.delete(0, tk.END)
        self.authorMiddleName_box.delete(0, tk.END)
        self.authorLastName_box.delete(0, tk.END)

        # Display a message to the user
        self.message_label.config(text="Book added successfully!")
        
    def add_book_driver(self):
        
        # Create the main window
        window = tk.Tk()
        window.title("SQL Project Frontend")

        # Create input boxes for adding a new user
        ISBN_label = tk.Label(window, text="ISBN:")
        ISBN_label.pack()
        self.ISBN_box = tk.Entry(window)
        self.ISBN_box.pack()

        title_label = tk.Label(window, text="Title:")
        title_label.pack()
        self.title_box = tk.Entry(window)
        self.title_box.pack()

        publisher_label = tk.Label(window, text="Publisher:")
        publisher_label.pack()
        self.publisher_box = tk.Entry(window)
        self.publisher_box.pack()

        numCopy_label = tk.Label(window, text="Number of copies:")
        numCopy_label.pack()
        self.numCopy_box = tk.Entry(window)
        self.numCopy_box.pack()

        authorFirstName_label = tk.Label(window, text="Author's first name:")
        authorFirstName_label.pack()
        self.authorFirstName_box = tk.Entry(window)
        self.authorFirstName_box.pack()

        authorMiddleName_label = tk.Label(window, text="Author's middle name:")
        authorMiddleName_label.pack()
        self.authorMiddleName_box = tk.Entry(window)
        self.authorMiddleName_box.pack()

        authorLasteName_label = tk.Label(window, text="Author's last name:")
        authorLasteName_label.pack()
        self.authorLastName_box = tk.Entry(window)
        self.authorLastName_box.pack()

        # Create the button to add a new user
        add_button = tk.Button(window, text="Add Book", command=self.add_book)
        add_button.pack()

        # Create a label to display messages to the user
        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        # Start the main event loop
        window.mainloop()

    def delete_book(self):
        # Get the user's information from the input boxes
        ISBN=self.delete_ISBN_box.get()

        query2 = f"DELETE FROM bookAuthor where ISBN='{ISBN}'"
        self.cursor.execute(query2)

        query1=f"DELETE FROM bookInfo where ISBN='{ISBN}'"
        self.cursor.execute(query1)
  
        conn.commit()

        # Display a message to the user
        self.message_label.config(text="Book deleted successfully!")

        # Clear the input boxes
        self.delete_ISBN_box.delete(0, tk.END)


    def delete_book_driver(self):
        # Create the main window
        window = tk.Tk()
        window.title("SQL Project Frontend")

        # Create input boxes for adding a new user
        ISBN_label = tk.Label(window, text="ISBN:")
        ISBN_label.pack()
        self.delete_ISBN_box = tk.Entry(window)
        self.delete_ISBN_box.pack()

        # Create the button to add a new user
        add_button = tk.Button(window, text="Delete Book", command=self.delete_book)
        add_button.pack()

        # Create a label to display messages to the user
        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        # Start the main event loop
        window.mainloop()

    def update_book_copies(self):
        # Get the user's information from the input boxes
        ISBN=self.update_copies_ISBN_box.get()
        copies=self.num_copies_box.get()

        query1 = f"UPDATE bookinfo set numCopy={copies} where ISBN='{ISBN}'"
        self.cursor.execute(query1)
  
        conn.commit()

        # Display a message to the user
        self.message_label.config(text=f"Number of copies updated to {copies}")

        # Clear the input boxes
        self.update_copies_ISBN_box.delete(0, tk.END)
        self.num_copies_box.delete(0, tk.END)


    def update_book_copies_driver(self):
        # Create the main window
        window = tk.Tk()
        window.title("Book copies")

        ISBN_label = tk.Label(window, text="ISBN:")
        ISBN_label.pack()
        self.update_copies_ISBN_box = tk.Entry(window)
        self.update_copies_ISBN_box.pack()

        num_copies_label = tk.Label(window, text="Copies:")
        num_copies_label.pack()
        self.num_copies_box = tk.Entry(window)
        self.num_copies_box.pack()

        add_button = tk.Button(window, text="Update copies", command=self.update_book_copies)
        add_button.pack()

        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        # Start the main event loop
        window.mainloop()

    def checked_out_books_driver(self):
        window=tk.Tk()
        window.title('Checked out books')

        self.cursor.execute("SELECT title FROM bookinfo,circulationrecord where bookinfo.ISBN=circulationrecord.ISBN")

        i=0 
        for book in self.cursor: 
            for j in range(len(book)):
                e = Entry(window, width=100, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, book[j])
            i=i+1

        # Start the main event loop
        window.mainloop()

    def overdue_items_driver(self):
        window=tk.Tk()
        window.title('Overdue books')
        
        currentDate = datetime.datetime.now() 
        # ts store timestamp of current time
        ts = currentDate.timestamp()

        self.cursor.execute(f"SELECT firstName,middleName,lastName,title FROM bookinfo,circulationrecord,userinfo where circulationrecord.dueDate<{ts} AND userinfo.userID=circulationrecord.userID AND bookinfo.ISBN=circulationrecord.ISBN")

        # self.message_label = tk.Label(window, text="")
        # self.message_label.pack()

        # self.message_label.config(text="The names of overdue users and corresponding books are:")

        i=0
        for book in self.cursor: 
            for j in range(len(book)):
                e = Entry(window, width=20, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, book[j])
            i=i+1

        # Start the main event loop
        window.mainloop()


library=Library()
library.dashboard()


# Close the connection to the MySQL database
conn.close()
