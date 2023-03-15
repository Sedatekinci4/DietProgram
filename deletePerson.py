from tkinter import *
import sqlite3
from tkinter import messagebox


def delete_user_ui():
    root = Tk()
    root.title("SEDAT HOTEL CHECK OUT")
    root.geometry("500x500")

    def close_it():
        root.destroy()

    # Creating the boxes
    delete_box = Entry(root, width=40, borderwidth=10)
    delete_box.grid(row=0, column=1)

    # Creating the box label
    delete_box_label = Label(root, text="Delete ID")
    delete_box_label.grid(row=0, column=0)

    # CREATE a query button
    query_btn = Button(root, text="Show OID's", command=None)
    query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # create a delete button
    delete_btn = Button(root, text="Delete Record", command=None)
    delete_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close_it)
    exit_button.grid(row=4, column=3, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    delete_user_ui()
