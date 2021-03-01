from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def form(root):
    root.title("Student Registration Form")
    root.geometry("1350x700+0+0")
    root.config(bg="teal")

    # BG IMAGE #
    bg_image = Image.open("images\stcet.png")
    bg = ImageTk.PhotoImage(bg_image)
    bg_label = Label(image=bg)
    bg_label.place(x=250, y=0, relwidth=1, relheight=1)

    #COLLEGE LOGO #
    logo_image = Image.open("images\logo.png")
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(image=logo)
    logo_label.place(x=80, y=100, width=280, height=360)

    #  REGISTRATION FRAME #

    # we are making the frame in the root window
    frame1 = Frame(root, bg="white")
    frame1.place(x=360, y=100, width=700, height=360)

    # title
    title = Label(frame1, text="PLEASE ENTER YOUR DETAILS HERE", font=(
        "times new roman", 15, "bold"), bg="white", fg="green").place(x=50, y=5)

    # STUDENT NAME #
    studentName = StringVar()

    student_Label = Label(frame1, text="NAME  ", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=50)
    student_name = Entry(frame1, font=(
        "verdana", 10), textvariable=studentName, bg="lightgray").place(x=150, y=50)

    #PARENT'S NAME #
    fname_label = Label(frame1, text="FATHER'S NAME  ", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=70)
    fname = Entry(frame1, font=("verdana", 10),
                  bg="lightgray").place(x=150, y=70)
    mname_label = Label(frame1, text="MOTHER'S NAME  ", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=70)
    mname = Entry(frame1, font=("verdana", 10),
                  bg="lightgray").place(x=500, y=70)

    # MAIL ID #

    mail_label = Label(frame1, text="EMAIL ID  ", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=90)
    mail = Entry(frame1, font=("verdana", 10),
                 bg="lightgray").place(x=150, y=90)

    # SEX #
    sex_label = Label(frame1, text="SEX  ", font=("verdana", 10, "bold"),
                      bg="white", fg="black").place(x=10, y=110)

    # RADIOBUTTON #
    male = Radiobutton(frame1, text="MALE", value=1)
    female = Radiobutton(frame1, text="FEMALE", value=2)

    male.place(x="150", y=110)
    female.place(x="230", y=110)

    # CONTACT NUMBER #
    phone_label = Label(frame1, text="PHONE NUMBER  ", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=130)
    phone = Entry(frame1, font=("verdana", 10),
                  bg="lightgray").place(x=150, y=130)

    # ADDRESS #
    present_address_label = Label(frame1, text="PRESENT ADDRESS  ", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=150)
    present_address = Entry(frame1, font=("verdana", 10),
                            bg="lightgray").place(x=150, y=150)

    permanent_address_label = Label(frame1, text="PERMANENT ADDRESS  ", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=150)
    permanent_address = Entry(frame1, font=("verdana", 10),
                              bg="lightgray").place(x=500, y=150)

    # CLASS 10 #
    ten_label = Label(frame1, text="X BOARD MARKS", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=170)
    ten = Entry(frame1, font=("verdana", 10),
                bg="lightgray").place(x=150, y=170)
    # CLASS 12 #
    twelve_label = Label(frame1, text="XII BOARD MARKS", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=170)
    twelve = Entry(frame1, font=("verdana", 10),
                   bg="lightgray").place(x=500, y=170)

    # BOARD NAME #
    board_label = Label(frame1, text="BOARD", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=190)
    cmb_board = ttk.Combobox(frame1, font=("verdane", 10, "bold"))
    cmb_board['values'] = ("ISC", "WBBSE", "CBSE", "OTHER")
    cmb_board.place(x=150, y=190)
    other_board_label = Label(frame1, text="SPECIFY IF OTHER", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=190)
    other_board = Entry(frame1, font=("verdana", 10),
                        bg="lightgray").place(x=500, y=190)

    # PCM MARKS #
    phy_label = Label(frame1, text="MARKS IN PHY", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=210)
    phy = Entry(frame1, font=("verdana", 10),
                bg="lightgray").place(x=150, y=210)

    chem_label = Label(frame1, text="MARKS IN CHEM", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=230)
    chem = Entry(frame1, font=("verdana", 10),
                 bg="lightgray").place(x=150, y=230)

    math_label = Label(frame1, text="MARKS IN MATH", font=(
        "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=250)
    math = Entry(frame1, font=("verdana", 10),
                 bg="lightgray").place(x=150, y=250)

    # Button Function
    def getData():
       # print('hello')
        print(student_name.get())

    # SUBMIT BUTTON
    submit_button = Button(root, font=("verdana", 14),
                           text="Submit", command=getData)
    submit_button.place(x=600, y=390)

    root.mainloop()

root = Tk()
form(root)
