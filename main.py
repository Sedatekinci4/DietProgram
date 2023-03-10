from tkinter import *
from PIL import ImageTk, Image


def home_ui():
    root = Tk()
    root.title("RUDIYET PROGRAMI")
    root.geometry("1280x1080")

    top = Frame(root)
    top.pack(side="top")

    bottom = Frame(root)
    bottom.pack(side="top")

    # Frames
    frame1 = Frame(root, width=50, height=50)
    frame1.pack()
    frame1.place(anchor='sw', relx=0.05, rely=0.2)

    frame2 = Frame(root, width=50, height=50)
    frame2.pack()
    frame2.place(anchor='sw', relx=0.05, rely=0.4)

    frame3 = Frame(root, width=50, height=50)
    frame3.pack()
    frame3.place(anchor='sw', relx=0.05, rely=0.6)

    frame4 = Frame(root, width=50, height=50)
    frame4.pack()
    frame4.place(anchor='sw', relx=0.05, rely=0.8)

    # Title
    label = Label(top, font=("Helvetica", "18", "bold italic"), text="---------- HOSGELDINIZ ----------", fg="#DF01A5",
                  anchor="center")
    label.grid(row=0, column=1)

    img1 = ImageTk.PhotoImage(Image.open("tomatoe.jpg"))
    label1 = Label(frame1, image=img1)
    label1.pack()

    img2 = ImageTk.PhotoImage(Image.open("tomatoe.jpg"))
    label2 = Label(frame2, image=img2)
    label2.pack()

    img3 = ImageTk.PhotoImage(Image.open("tomatoe.jpg"))
    label3 = Label(frame3, image=img3)
    label3.pack()

    img4 = ImageTk.PhotoImage(Image.open("tomatoe.jpg"))
    label4 = Label(frame4, image=img4)
    label4.pack()

    # Buttons
    # Show person
    show_persons = Button(bottom, text="Kişileri Göster", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                          relief=RIDGE,
                          height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    show_persons.grid(row=0, column=2, padx=10, pady=10)

    # select person
    select_person = Button(bottom, text="Kişi Seç", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                           relief=RIDGE,
                           height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    select_person.grid(row=1, column=2, padx=10, pady=10)

    # add person
    add_person = Button(bottom, text="Kişi Ekle", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                        relief=RIDGE,
                        height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    add_person.grid(row=2, column=2, padx=10, pady=10)

    # edit person
    edit_person = Button(bottom, text="Kişi Düzenle", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                         relief=RIDGE,
                         height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    edit_person.grid(row=3, column=2, padx=10, pady=10)

    # delete person
    delete_person = Button(bottom, text="Kişi Sil", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                           relief=RIDGE,
                           height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    delete_person.grid(row=4, column=2, padx=10, pady=10)

    # enter meal
    enter_meal = Button(bottom, text="Öğün Girişi Yap", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                        relief=RIDGE,
                        height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    enter_meal.grid(row=5, column=2, padx=10, pady=10)

    # enter cal burnt
    cal_burned = Button(bottom, text="Yakılan Kalori Girişi Yap", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                        relief=RIDGE,
                        height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    cal_burned.grid(row=6, column=2, padx=10, pady=10)

    # information
    program_info = Button(bottom, text="BİLGİ", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                          relief=RIDGE,
                          height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    program_info.grid(row=7, column=2, padx=10, pady=10)

    # exit
    exit_program = Button(bottom, text="Çıkış", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                          relief=RIDGE,
                          height=2, width=35, fg="#F4F4A4", anchor="center", command=exit)
    exit_program.grid(row=8, column=2, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    home_ui()
