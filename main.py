from tkinter import *
from PIL import ImageTk, Image
import addPerson
import showPerson
import deletePerson
import selectPerson

def home_ui():
    root = Tk()
    root.title("RUDIYET PROGRAMI")
    root.geometry("1280x1080")
    root.resizable()
    # root.configure(bg="white")

    top = Frame(root)
    top.pack(side="top")

    bottom = Frame(root)
    bottom.pack(side="top")

    # Frames
    frame1 = Frame(root, width=50, height=50)
    frame1.pack()
    frame1.place(anchor='sw', relx=0.03, rely=0.3)

    frame2 = Frame(root, width=50, height=50)
    frame2.pack()
    frame2.place(anchor='sw', relx=0.05, rely=0.5)

    frame3 = Frame(root, width=10, height=10)
    frame3.pack()
    frame3.place(anchor='sw', relx=0.05, rely=0.7)

    frame4 = Frame(root, width=50, height=50)
    frame4.pack()
    frame4.place(anchor='sw', relx=0.07, rely=0.9)

    frame5 = Frame(root, width=50, height=50)
    frame5.pack()
    frame5.place(anchor='center', relx=0.85, rely=0.15)

    frame6 = Frame(root, width=10, height=10)
    frame6.pack()
    frame6.place(anchor='center', relx=0.85, rely=0.5)

    frame7 = Frame(root, width=50, height=50)
    frame7.pack()
    frame7.place(anchor='center', relx=0.87, rely=0.8)

    # Title
    label = Label(top, font=("Helvetica", "25", "bold italic"), text="---------- HOSGELDINIZ ----------", fg="#DF01A5",
                  anchor="center")
    label.grid(row=0, column=1)

    # Showing the frames and attaching images to them
    img1 = ImageTk.PhotoImage(Image.open("meal3.png"))
    label1 = Label(frame1, image=img1)
    label1.pack()

    img2 = ImageTk.PhotoImage(Image.open("meal2.png"))
    label2 = Label(frame2, image=img2)
    label2.pack()

    img3 = ImageTk.PhotoImage(Image.open("meal1.png"))
    label3 = Label(frame3, image=img3)
    label3.pack()

    img4 = ImageTk.PhotoImage(Image.open("tomato.png"))
    label4 = Label(frame4, image=img4)
    label4.pack()

    img5 = ImageTk.PhotoImage(Image.open("meal4.png"))
    label5 = Label(frame5, image=img5)
    label5.pack()

    img6 = ImageTk.PhotoImage(Image.open("meal5.png"))
    label6 = Label(frame6, image=img6)
    label6.pack()

    img7 = ImageTk.PhotoImage(Image.open("meal6.png"))
    label7 = Label(frame7, image=img7)
    label7.pack()

    # Buttons
    # Show person
    show_persons = Button(bottom, text="Kişileri Göster / Düzenle", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                          relief=RIDGE,
                          height=2, width=35, fg="#F4F4A4", anchor="center", command=showPerson.person_info_ui)
    show_persons.grid(row=0, column=2, padx=10, pady=20)

    # Select person
    select_person = Button(bottom, text="Kişi Seç", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                           relief=RIDGE,
                           height=2, width=35, fg="#F4F4A4", anchor="center", command=selectPerson.select_person_ui)
    select_person.grid(row=1, column=2, padx=10, pady=20)

    # Add person
    add_person = Button(bottom, text="Kişi Ekle", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                        relief=RIDGE,
                        height=2, width=35, fg="#F4F4A4", anchor="center", command=addPerson.add_person_ui)
    add_person.grid(row=2, column=2, padx=10, pady=20)

    # Edit person
    # edit_person = Button(bottom, text="Kişi Düzenle", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
    #                      relief=RIDGE,
    #                      height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    # edit_person.grid(row=3, column=2, padx=10, pady=10)

    # Delete person
    delete_person = Button(bottom, text="Kişi Sil", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                           relief=RIDGE,
                           height=2, width=35, fg="#F4F4A4", anchor="center", command=deletePerson.delete_user_ui)
    delete_person.grid(row=4, column=2, padx=10, pady=20)

    # Enter meal
    enter_meal = Button(bottom, text="Öğün Girişi Yap", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                        relief=RIDGE,
                        height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    enter_meal.grid(row=5, column=2, padx=10, pady=20)

    # Enter cal burnt
    cal_burned = Button(bottom, text="Yakılan Kalori Girişi Yap", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                        relief=RIDGE,
                        height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    cal_burned.grid(row=6, column=2, padx=10, pady=20)

    # Information
    program_info = Button(bottom, text="BİLGİ", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                          relief=RIDGE,
                          height=2, width=35, fg="#F4F4A4", anchor="center", command=None)
    program_info.grid(row=7, column=2, padx=10, pady=20)

    # Exit
    exit_program = Button(bottom, text="Çıkış", font=("Helvetica", "18", "bold italic"), bg="#6E6E6E",
                          relief=RIDGE,
                          height=2, width=35, fg="#F4F4A4", anchor="center", command=exit)
    exit_program.grid(row=8, column=2, padx=10, pady=20)

    root.mainloop()


if __name__ == '__main__':
    home_ui()
