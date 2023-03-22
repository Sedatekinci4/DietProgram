from tkinter import *
import sqlite3
from tkinter import messagebox


def select_person_ui():
    root = Tk()
    root.geometry("700x700")
    root.title("Select Person")

    def close_it():
        root.destroy()

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
                             + "Oid:" + '\t' + str(record[5]) + '\n'
        query_label = Label(root, text=print_records, anchor='center')
        query_label.grid(row=4, column=0)

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    def select():
        pass

    # Title
    label = Label(root, font=("Helvetica", "14", "bold italic"), text="----- KİŞİ SEÇ -----", fg="#DF01A5",
                  anchor="center")
    label.grid(row=0, column=1)

    # CREATE a query button
    query_btn = Button(root, text="KAYITLARI GÖSTER", command=query)
    query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # Exit button
    exit_button = Button(root, text="ÇIKIŞ", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close_it)
    exit_button.grid(row=2, column=2)

    # Selcet box
    select_box = Entry(root, width=40, borderwidth=10)
    select_box.grid(row=2, column=0)

    # Select button
    select_button = Button(root, text="SEÇ", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=None)
    select_button.grid(row=2, column=3, padx=5)


    root.mainloop()


if __name__ == '__main__':
    select_person_ui()
