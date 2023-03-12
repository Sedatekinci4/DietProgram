from tkinter import *


def person_info_ui():
    root = Tk()
    root.title("Show Persons")
    root.geometry("600x600")

    # CREATE a query button
    query_btn = Button(root, text="Show Records", command=None)
    query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=None)
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