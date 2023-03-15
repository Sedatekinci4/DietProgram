from tkinter import *
import sqlite3


def person_info_ui():
    root = Tk()
    root.title("Show Persons")
    root.geometry("600x600")

    def close_it():
        root.destroy()

        # Create query function

    def query():
        # Create a db or connect to one
        conn = sqlite3.connect("Users.db")
        # Create a cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *,oid FROM users")
        records = c.fetchall()
        print(records)

        # Loop through records
        print_records = ''
        for record in records:
            print_records += '\n' + "First Name:" + '\t' + str(record[0]) + '\n' \
                             + "Last Name:" + '\t' + str(record[1]) + '\n' \
                             + "Height:     " + '\t' + str(record[2]) + '\n' \
                             + "Weight:     " + '\t' + str(record[3]) + '\n' \
                             + "Day:      " + '\t' + str(record[4]) + '\n\n'
        query_label = Label(root, text=print_records, anchor='center')
        query_label.grid(row=4, column=0)

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    # CREATE a query button
    query_btn = Button(root, text="Show Records", command=query)
    query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close_it)
    exit_button.grid(row=2, column=2)

    # Edit box
    edit_box = Entry(root, width=40, borderwidth=10)
    edit_box.grid(row=2, column=0)

    # Edit button
    edit_button = Button(root, text="EDIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=None)
    edit_button.grid(row=2, column=3, padx=5)

    root.mainloop()


if __name__ == '__main__':
    person_info_ui()
