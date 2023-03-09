from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import date
import datetime


def add_person_ui():
    root = Tk()
    root.title("Add Person")
    root.geometry("500x500")

    label = Label(root, font=("Helvetica", "18", "bold italic"), text="---------- KİŞİ EKLEYİN ----------", fg="#DF01A5",
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
    submit_btn = Button(root, text="Add record to Database", command=None)
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=exit)
    exit_button.grid(row=8, column=2, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    add_person_ui()
