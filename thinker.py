import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""

def btn1_isclicked():
    global val
    val=val+"1"
    data.set(val)

def btn2_isclicked():
    global val
    val=val+"2"
    data.set(val)

def btn3_isclicked():
    global val
    val=val+"3"
    data.set(val)

def btn4_isclicked():
    global val
    val=val+"4"
    data.set(val)

def btn5_isclicked():
    global val
    val=val+"5"
    data.set(val)

def btn6_isclicked():
    global val
    val=val+"6"
    data.set(val)

def btn7_isclicked():
    global val
    val=val+"7"
    data.set(val)

def btn8_isclicked():
    global val
    val=val+"8"
    data.set(val)

def btn9_isclicked():
    global val
    val=val+"9"
    data.set(val)

def btn0_isclicked():
    global val
    val=val+"0"
    data.set(val)

def btn_plus_clicked():
    global A
    global operator
    global val
    A = int (val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_sub_clicked():
    global A
    global operator
    global val
    A = int (val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_multiply_clicked():
    global A
    global operator
    global val
    A = int (val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_divide_clicked():
    global A
    global operator
    global val
    A = int (val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_clicked():
    global A
    global operator
    global val
    val = ""
    operator = ""
    A = 0
    data.set(val)

def result_clicked():
    global A
    global operator
    global val
    val2=val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
         x = int((val2.split("/")[1]))
         if x == 0:
             messagebox. showerror("ERROR","division by 0 not supported")
             A = ""
             val = ""
             data.set(val)
         else:
             c = int(A / x)
             data.set(c)
             val =str(c)



root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("CALCULATOR")

data = StringVar()
lbl=Label(
    root,
    text="lable",
    anchor = SE,
    font =("verdana",22),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand =True , fill="both")

row1=Frame (root,bg="#000000")
row1.pack(expand=True, fill="both")

row2=Frame (root)
row2.pack(expand=True, fill="both")

row3=Frame (root)
row3.pack(expand=True, fill="both")

row4=Frame (root)
row4.pack(expand=True, fill="both")



btn1= Button(
    row1,
    text="1",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn1_isclicked,
)
btn1.pack(side=LEFT , expand=True, fill="both")

btn2= Button(
    row1,
    text="2",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn2_isclicked,
)
btn2.pack(side=LEFT , expand=True, fill="both")

btn3= Button(
    row1,
    text="3",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn3_isclicked,
)
btn3.pack(side=LEFT , expand=True, fill="both")

btnplus= Button(
    row1,
    text="+",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command= btn_plus_clicked
)
btnplus.pack(side=LEFT , expand=True, fill="both")

btn5= Button(
    row2,
    text="4",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn4_isclicked,
)
btn5.pack(side=LEFT , expand=True, fill="both")

btn6= Button(
    row2,
    text="5",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn5_isclicked,
)
btn6.pack(side=LEFT , expand=True, fill="both")

btn7= Button(
    row2,
    text="6",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn6_isclicked,
)
btn7.pack(side=LEFT , expand=True, fill="both")

btn8= Button(
    row2,
    text="-",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command= btn_sub_clicked
)
btn8.pack(side=LEFT , expand=True, fill="both")

btn9= Button(
    row3,
    text="7",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn7_isclicked,
)
btn9.pack(side=LEFT , expand=True, fill="both")

btn0= Button(
    row3,
    text="8",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn8_isclicked,
)
btn0.pack(side=LEFT , expand=True, fill="both")

btn3= Button(
    row3,
    text="9",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn9_isclicked,
)
btn3.pack(side=LEFT , expand=True, fill="both")

btn4= Button(
    row3,
    text="*",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command= btn_multiply_clicked
)
btn4.pack(side=LEFT , expand=True, fill="both")

btnc= Button(
    row4,
    text="C",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0, 
    command = btn_c_clicked
)
btnc.pack(side=LEFT , expand=True, fill="both")

btn2= Button(
    row4,
    text="0",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = btn0_isclicked,
)
btn2.pack(side=LEFT , expand=True, fill="both")

btnequal= Button(
    row4,
    text="=",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command = result_clicked
)
btnequal.pack(side=LEFT , expand=True, fill="both")

btn4= Button(
    row4,
    text="/",
    font = ("verdana",20),
    relief = GROOVE,
    border = 0,
    command= btn_divide_clicked
)
btn4.pack(side=LEFT , expand=True, fill="both")




root.mainloop()
