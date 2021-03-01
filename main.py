from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="teal")
        # BG IMAGE #

        # this bg is object of class
        self.bg = ImageTk.PhotoImage(file="images\stcet.png")
        bg = Label(self.root, image=self.bg).place(
            x=250, y=0, relwidth=1, relheight=1)  # this bg is object of root window

        # LEFT IMAGE which shows COLLEGE LOGO #

        self.left = ImageTk.PhotoImage(file="images/1.png")
        left = Label(self.root, image=self.left).place(
            x=80, y=100, width=280, height=360)

        #  REGISTRATION FRAME #
        # we are making the frame in the root window
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=360, y=100, width=700, height=360)

        title = Label(frame1, text="PLEASE ENTER YOUR DETAILS HERE", font=(
            "times new roman", 15, "bold"), bg="white", fg="green").place(x=50, y=5)
        # STUDENT NAME #

        name = Label(frame1, text="NAME  ", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=50)
        # making the entry field #
        txt_name = Entry(frame1, font=("verdana", 10),
                         bg="lightgray").place(x=150, y=50)

        # PARENT'S NAME #

        fname = Label(frame1, text="FATHER'S NAME  ", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=70)
        txt_fname = Entry(frame1, font=("verdana", 10),
                          bg="lightgray").place(x=150, y=70)
        mname = Label(frame1, text="MOTHER'S NAME  ", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=70)
        txt_mname = Entry(frame1, font=("verdana", 10),
                          bg="lightgray").place(x=500, y=70)

        # MAIL ID #

        mail = Label(frame1, text="EMAIL ID  ", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=90)
        txt_mail = Entry(frame1, font=("verdana", 10),
                         bg="lightgray").place(x=150, y=90)

        # SEX #
        sex = Label(frame1, text="SEX  ", font=("verdana", 10, "bold"),
                    bg="white", fg="black").place(x=10, y=110)
        # RADIOBUTTON #
        rad1 = Radiobutton(frame1, text="MALE", value=1)
        rad2 = Radiobutton(frame1, text="FEMALE", value=2)

        rad1.place(x="150", y=110)
        rad2.place(x="230", y=110)

        # CONTACT NUMBER #
        num = Label(frame1, text="PHONE NUMBER  ", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=130)
        txt_num = Entry(frame1, font=("verdana", 10),
                        bg="lightgray").place(x=150, y=130)

        # ADDRESS #

        add1 = Label(frame1, text="PRESENT ADDRESS  ", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=150)
        txt_add1 = Entry(frame1, font=("verdana", 10),
                         bg="lightgray").place(x=150, y=150)

        add2 = Label(frame1, text="PERMANENT ADDRESS  ", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=150)
        txt_add2 = Entry(frame1, font=("verdana", 10),
                         bg="lightgray").place(x=500, y=150)

        # CLASS 10 #
        ten = Label(frame1, text="X BOARD MARKS", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=170)
        txt_ten = Entry(frame1, font=("verdana", 10),
                        bg="lightgray").place(x=150, y=170)
        # CLASS 12 #
        twelve = Label(frame1, text="XII BOARD MARKS", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=170)
        txt_twelve = Entry(frame1, font=("verdana", 10),
                           bg="lightgray").place(x=500, y=170)

        # BOARD NAME #

        board = Label(frame1, text="BOARD", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=190)
        cmb_board = ttk.Combobox(frame1, font=("verdane", 10, "bold"))
        cmb_board['values'] = ("ISC", "WBBSE", "CBSE", "OTHER")
        cmb_board.place(x=150, y=190)
        other = Label(frame1, text="SPECIFY IF OTHER", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=320, y=190)
        txt_other = Entry(frame1, font=("verdana", 10),
                          bg="lightgray").place(x=500, y=190)

        # PCM MARKS #
        phy = Label(frame1, text="MARKS IN PHY", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=210)
        txt_phy = Entry(frame1, font=("verdana", 10),
                        bg="lightgray").place(x=150, y=210)

        chem = Label(frame1, text="MARKS IN CHEM", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=230)
        txt_chem = Entry(frame1, font=("verdana", 10),
                         bg="lightgray").place(x=150, y=230)

        math = Label(frame1, text="MARKS IN MATH", font=(
            "verdana", 10, "bold"), bg="white", fg="black").place(x=10, y=250)
        txt_math = Entry(frame1, font=("verdana", 10),
                         bg="lightgray").place(x=150, y=250)


root = Tk()
obj = Register(root)
root.mainloop()
