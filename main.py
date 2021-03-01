from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import openpyxl
import math as M

# ====== initialisation=========
root = Tk()
root.title("Student Registration Form")
root.geometry("1350x700+0+0")
root.config(bg="teal")

# filepath = "C:\Users\Mousumi\Documents\Python\GUI-Group-Project"

Wb = openpyxl.Workbook()
Wb.save('data.xlsx')
sheet = Wb.active

# ======== functions============


def excel():
    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C'].width = 30
    sheet.column_dimensions['D'].width = 60
    sheet.column_dimensions['E'].width = 20
    sheet.column_dimensions['F'].width = 50
    sheet.column_dimensions['G'].width = 50
    sheet.column_dimensions['H'].width = 50
    sheet.column_dimensions['I'].width = 30
    sheet.column_dimensions['J'].width = 30
    sheet.column_dimensions['K'].width = 30
    sheet.column_dimensions['L'].width = 30
    sheet.column_dimensions['M'].width = 30
    sheet.column_dimensions['N'].width = 30
    sheet.column_dimensions['O'].width = 30


    sheet.cell(row=1, column=1).value = "Student Name"
    sheet.cell(row=1, column=2).value = "Father's Name"
    sheet.cell(row=1, column=3).value = "Mother Name"
    sheet.cell(row=1, column=4).value = "Email"
    sheet.cell(row=1, column=5).value = "Gender"
    sheet.cell(row=1, column=6).value = "Contact Number"
    sheet.cell(row=1, column=7).value = "Present Address"
    sheet.cell(row=1, column=8).value = "Permanent Address"
    sheet.cell(row=1, column=9).value = "X Marks"
    sheet.cell(row=1, column=10).value = "XII Marks"
    sheet.cell(row=1, column=11).value = "Board"
    sheet.cell(row=1, column=12).value = "Physics Marks"
    sheet.cell(row=1, column=13).value = "Chemistry Marks"
    sheet.cell(row=1, column=14).value = "Maths Marks"
    sheet.cell(row=1,column=15).value = "Percentage Marks"

def removeData():
    ck = chk_var.get()
    if(ck != 0):
        student_name.delete(0, END)
        fname.delete(0, END)
        mname.delete(0, END)
        mail.delete(0, END)
        phone.delete(0, END)
        present_address.delete(0, END)
        permanent_address.delete(0, END)
        ten.delete(0, END)
        twelve.delete(0, END)
        phy.delete(0, END)
        chem.delete(0, END)
        math.delete(0, END)
        cmb_board.delete(0,END)


def getData():
    chk = chk_var.get()

    if (chk == 0):
        messagebox.showerror('Error', 'Please check the checkbutton')
    else:
        currentRow = sheet.max_row
        currentColumn = sheet.max_column

        sheet.cell(row=currentRow+1, column=1).value = studentName.get()
        sheet.cell(row=currentRow+1, column=2).value = fatherName.get()
        sheet.cell(row=currentRow+1, column=3).value = motherName.get()
        sheet.cell(row=currentRow+1, column=4).value = email.get()
        sheet.cell(row=currentRow+1, column=5).value = gender.get()
        sheet.cell(row=currentRow+1, column=6).value = phoneNumber.get()
        sheet.cell(row=currentRow+1, column=7).value = presentAddress.get()
        sheet.cell(row=currentRow+1, column=8).value = permanentAddress.get()
        sheet.cell(row=currentRow+1, column=9).value = tenMarks.get()
        sheet.cell(row=currentRow+1, column=10).value = twelveMarks.get()
        sheet.cell(row=currentRow+1, column=11).value = cmb_board.get()
        sheet.cell(row=currentRow+1, column=12).value = phyMarks.get()
        sheet.cell(row=currentRow+1, column=13).value = chemMarks.get()
        sheet.cell(row=currentRow+1, column=14).value = mathMarks.get()
        Percentage = round((int(phyMarks.get()) + int(chemMarks.get()) + int(mathMarks.get()))/3)
        sheet.cell(row=currentRow+1, column=15).value = Percentage
        

        Wb.save('data.xlsx')
        removeData()


def show():
    excel()
    getData()


# ==================== Declarations =========================
studentName = StringVar()
fatherName = StringVar()
motherName = StringVar()
email = StringVar()
gender = StringVar()
phoneNumber = IntVar()
presentAddress = StringVar()
permanentAddress = StringVar()
tenMarks = IntVar()
twelveMarks = IntVar()
otherBoard = StringVar()
phyMarks = IntVar()
chemMarks = IntVar()
mathMarks = IntVar()
chk_var = IntVar()

# ======================== Form ==============================

# BG IMAGE #
bg_image = Image.open("images\stcet.png")
bg = ImageTk.PhotoImage(bg_image)
bg_label = Label(image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#COLLEGE LOGO #
logo_image = Image.open("images\logo.png")
logo = ImageTk.PhotoImage(logo_image)
logo_label = Label(image=logo)
logo_label.place(x=80, y=100, width=280, height=380)

#  REGISTRATION FRAME #

# we are making the frame in the root window
frame1 = Frame(root, bg="white")
frame1.place(x=360, y=100, width=730, height=380)

# title
title = Label(frame1, text="PLEASE ENTER YOUR DETAILS HERE", font=(
    "times new roman", 15, "bold"), bg="white", fg="green")
title.place(x=50, y=5)

# STUDENT NAME #
student_Label = Label(frame1, text="NAME  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
student_Label.place(x=10, y=50)

student_name = Entry(frame1, font=("verdana", 10),
                     textvariable=studentName, bg="lightgray")
student_name.place(x=150, y=50)

#PARENT'S NAME #
fname_label = Label(frame1, text="FATHER'S NAME  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
fname_label.place(x=10, y=70)

fname = Entry(frame1, font=("verdana", 10),
              bg="lightgray", textvariable=fatherName)
fname.place(x=150, y=70)

mname_label = Label(frame1, text="MOTHER'S NAME  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
mname_label.place(x=320, y=70)

mname = Entry(frame1, font=("verdana", 10),
              bg="lightgray", textvariable=motherName)
mname.place(x=500, y=70)


# MAIL ID #
mail_label = Label(frame1, text="EMAIL ID  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
mail_label.place(x=10, y=90)

mail = Entry(frame1, font=("verdana", 10),
             bg="lightgray", textvariable=email)
mail.place(x=150, y=90)


# SEX #
sex_label = Label(frame1, text="SEX  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
sex_label.place(x=10, y=110)

# RADIOBUTTON
Radiobutton(frame1, text="MALE", value="male",
            variable=gender).place(x="150", y="110")

Radiobutton(frame1, text="FEMALE", value="female",
            variable=gender).place(x="230", y="110")

Radiobutton(frame1, text="OTHER", value="other",
            variable=gender).place(x="310", y="110")


# CONTACT NUMBER #
phone_label = Label(frame1, text="PHONE NUMBER  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
phone_label.place(x=10, y=130)

phone = Entry(frame1, font=("verdana", 10),
              bg="lightgray", textvariable=phoneNumber)
phone.place(x=150, y=130)

# ADDRESS #
present_address_label = Label(frame1, text="PRESENT ADDRESS  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
present_address_label.place(x=10, y=150)

present_address = Entry(frame1, font=("verdana", 10),
                        bg="lightgray", textvariable=presentAddress)
present_address.place(x=150, y=150)

permanent_address_label = Label(frame1, text="PERMANENT ADDRESS  ", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
permanent_address_label.place(x=320, y=150)

permanent_address = Entry(frame1, font=("verdana", 10),
                          bg="lightgray", textvariable=permanentAddress)
permanent_address.place(x=500, y=150)


# CLASS 10 #
ten_label = Label(frame1, text="X BOARD MARKS", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
ten_label.place(x=10, y=170)

ten = Entry(frame1, font=("verdana", 10),
            bg="lightgray", textvariable=tenMarks)
ten.place(x=150, y=170)


# CLASS 12 #
twelve_label = Label(frame1, text="XII BOARD MARKS", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
twelve_label.place(x=320, y=170)

twelve = Entry(frame1, font=("verdana", 10),
               bg="lightgray", textvariable=twelveMarks)
twelve.place(x=500, y=170)


# BOARD NAME #
board_label = Label(frame1, text="BOARD", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
board_label.place(x=10, y=190)

cmb_board = ttk.Combobox(frame1, font=(
    "verdane", 10, "bold"), values=("ISC", "STATE BOARD", "CBSE", "OTHER"))
cmb_board.place(x=150, y=190)


# PCM MARKS #
phy_label = Label(frame1, text="MARKS IN PHY", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
phy_label.place(x=10, y=210)

phy = Entry(frame1, font=("verdana", 10),
            bg="lightgray", textvariable=phyMarks)
phy.place(x=150, y=210)

chem_label = Label(frame1, text="MARKS IN CHEM", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
chem_label.place(x=10, y=230)

chem = Entry(frame1, font=("verdana", 10),
             bg="lightgray", textvariable=chemMarks)
chem.place(x=150, y=230)

math_label = Label(frame1, text="MARKS IN MATH", font=(
    "verdana", 10, "bold"), bg="white", fg="black")
math_label.place(x=10, y=250)

math = Entry(frame1, font=("verdana", 10),
             bg="lightgray", textvariable=mathMarks)
math.place(x=150, y=250)

# checkbox
chk_1 = Checkbutton(frame1,
                    text="I do hereby declare that all the information given above is true to the best of my knowledge and belief.",
                    bg="LightBlue1", activebackground="#80c1ff", font=("bold", 11), bd=15, variable=chk_var)
chk_1.place(x=10, y=280)

# SUBMIT BUTTON
Button(frame1, font=("verdana", 12), text="Submit",
       command=show).place(x=260, y=340)


root.mainloop()
