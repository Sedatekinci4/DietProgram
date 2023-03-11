from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import date
from sqlite3 import Error


def add_person_ui():
    root = Tk()
    root.title("Add Person")
    root.geometry("500x500")

    def create_table(conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                            name text PRIMARY KEY,
                                            surname text NOT NULL,
                                            height integer,
                                            weight float,
                                            day text
                                        ); """

    # Destroy the window
    def close_it():
        root.destroy()

    def submit():
        if not f_name.get() or not l_name.get() or not height.get() or not weight.get():
            messagebox.showwarning("Warning", "Please fill all the information")
            root.destroy()
            return

        # database = r"C:\Users\tades\PycharmProjects\RuDiyet\Users.db"

        # Create a db or connect to one
        conn = sqlite3.connect("Users.db")

        # Create table
        if conn is not None:
            # create users table
            create_table(conn, sql_create_users_table)
        else:
            print("Error! cannot create the database connection.")

        today = date.today()
        day_str = str(today)

        # Create a cursor
        c = conn.cursor()
        # Insert into table
        c.execute("INSERT INTO users VALUES (:f_name, :l_name, :height, :weight, :day)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'height': height.get(),
                      'weight': weight.get(),
                      'day': day_str
                  })

        # Commit change
        conn.commit()

        # Close connection
        conn.close()

        # Clear the text boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        height.delete(0, END)
        weight.delete(0, END)

        messagebox.showinfo("information", "Check in done successfully")
        root.destroy()

    label = Label(root, font=("Helvetica", "18", "bold italic"), text="---------- KİŞİ EKLEYİN ----------",
                  fg="#DF01A5",
                  anchor="center")
    label.grid(row=0, column=1)

    # Create tet boxes
    f_name = Entry(root, width=40, borderwidth=10)
    f_name.grid(row=2, column=1, padx=20)
    l_name = Entry(root, width=40, borderwidth=10)
    l_name.grid(row=3, column=1)
    height = Entry(root, width=40, borderwidth=10)
    height.grid(row=4, column=1)
    weight = Entry(root, width=40, borderwidth=10)
    weight.grid(row=5, column=1)

    # Create Box labels
    f_name_label = Label(root, text="İsim")
    f_name_label.grid(row=2, column=0)
    l_name_label = Label(root, text="Soyisim")
    l_name_label.grid(row=3, column=0)
    height_label = Label(root, text="Boy")
    height_label.grid(row=4, column=0)
    weight_label = Label(root, text="Kilo")
    weight_label.grid(row=5, column=0)

    # Create a submit button
    submit_btn = Button(root, text="Add record to Database", command=submit)
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close_it)
    exit_button.grid(row=8, column=2, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    add_person_ui()
