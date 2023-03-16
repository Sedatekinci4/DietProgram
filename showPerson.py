from tkinter import *
import sqlite3
from tkinter import messagebox


def person_info_ui():
    root = Tk()
    root.title("Show Persons")
    root.geometry("650x600")

    def close_it():
        root.destroy()

        # Create query function

    def update():
        # Create a db or connect to one
        conn = sqlite3.connect("Users.db")
        # Create a cursor
        c = conn.cursor()

        record_id = edit_box.get()
        c.execute("""UPDATE users SET
            name = :first,
            surname = :last,
            height = :height,
            weight = :weight,
            day = :day

            WHERE oid = :oid""",
                  {
                      'first': f_name_editor.get(),
                      'last': l_name_editor.get(),
                      'height': height_editor.get(),
                      'weight': weight_editor.get(),
                      'day': day_editor.get(),

                      'oid': record_id
                  })

        # Commit change
        conn.commit()
        # close connection
        conn.close()

        # Clear the text boxes
        f_name_editor.delete(0, END)
        l_name_editor.delete(0, END)
        height_editor.delete(0, END)
        weight_editor.delete(0, END)
        day_editor.delete(0, END)

        messagebox.showinfo("TAMAMLANDI", "KULLANICI BİLGİLERİ DÜZENLENDİ")
        editor.destroy()
        root.destroy()

    def edit():
        def close_editor():
            editor.destroy()

        global editor
        editor = Tk()
        editor.title("EDIT CUSTOMERS")
        editor.geometry("400x400")

        global f_name_editor
        global l_name_editor
        global height_editor
        global weight_editor
        global day_editor

        # Create tet boxes
        f_name_editor = Entry(editor, width=40, borderwidth=10)
        f_name_editor.grid(row=0, column=1, padx=20)
        l_name_editor = Entry(editor, width=40, borderwidth=10)
        l_name_editor.grid(row=1, column=1)
        height_editor = Entry(editor, width=40, borderwidth=10)
        height_editor.grid(row=2, column=1)
        weight_editor = Entry(editor, width=40, borderwidth=10)
        weight_editor.grid(row=3, column=1)
        day_editor = Entry(editor, width=40, borderwidth=10)
        day_editor.grid(row=4, column=1)

        # Create Box labels
        f_name_label = Label(editor, text="First Name")
        f_name_label.grid(row=0, column=0)
        l_name_label = Label(editor, text="Last Name")
        l_name_label.grid(row=1, column=0)
        height_label = Label(editor, text="Height")
        height_label.grid(row=2, column=0)
        weight_label = Label(editor, text="Weight")
        weight_label.grid(row=3, column=0)
        day_label = Label(editor, text="Day")
        day_label.grid(row=4, column=0)

        # Save button
        save_button = Button(editor, text="SAVE", font=('', 10), bg="#15d3ba",
                             relief=RIDGE,
                             height=1, width=15, fg="red", anchor="center", command=update)
        save_button.grid(row=6, column=1, padx=50)

        # Exit button
        exit_editor_button = Button(editor, text="EXIT", font=('', 10), bg="#15d3ba",
                                    relief=RIDGE,
                                    height=1, width=15, fg="red", anchor="center", command=close_editor)
        exit_editor_button.grid(row=8, column=1, pady=10)

        # Create a db or connect to one
        conn = sqlite3.connect("Users.db")
        # Create a cursor
        c = conn.cursor()

        record_id = edit_box.get()
        if record_id == '' or not record_id.isnumeric():
            messagebox.showerror("HATA", "BU ID İLE BİR KULLANICI BULUNAMADI")
            close_editor()
            root.destroy()
        c.execute("SELECT * FROM users WHERE oid = " + record_id)
        records = c.fetchall()
        if not records:
            print("empty")
            messagebox.showerror("HATA", "BU ID İLE BİR KULLANICI BULUNAMADI")
            close_editor()
            root.destroy()

        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            height_editor.insert(0, record[2])
            weight_editor.insert(0, record[3])
            day_editor.insert(0, record[4])

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
                             + "Day:      " + '\t' + str(record[4]) + '\n' + "Oid:" + '\t' + str(record[5]) + '\n'
        query_label = Label(root, text=print_records, anchor='center')
        query_label.grid(row=4, column=0)

        # Commit change
        conn.commit()

        # close connection
        conn.close()

    # CREATE a query button
    query_btn = Button(root, text="KAYITLARI GÖSTER", command=query)
    query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

    # Exit button
    exit_button = Button(root, text="ÇIKIŞ", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close_it)
    exit_button.grid(row=2, column=2)

    # Edit box
    edit_box = Entry(root, width=40, borderwidth=10)
    edit_box.grid(row=2, column=0)

    # Edit button
    edit_button = Button(root, text="DÜZENLE", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=edit)
    edit_button.grid(row=2, column=3, padx=5)

    root.mainloop()


if __name__ == '__main__':
    person_info_ui()
