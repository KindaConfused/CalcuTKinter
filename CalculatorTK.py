from tkinter import *

def calc_button(num):
    global equation_text
    if len(equation_text) <= 30:
        if equation_text == "" and num == 0:
            pass
        else:
            equation_text = equation_text + str(num)
            label.config(text=equation_text)
    else:
        pass


def equals():
    global equation_text
    try:
        equation = eval(equation_text)
    except ZeroDivisionError:
        equation_text = ""
        label.config(text="no dividing by 0")
    except SyntaxError:
        equation_text = ""
        label.config(text="dont do that")
    else:
        equation_text = str(equation)
        if equation_text[-2:] == ".0":
            equation_text = equation_text[:-2]
        label.config(text=equation_text)


def clear():
    global equation_text
    equation_text = ""
    label.config(text="")

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    label.config(text=equation_text)


window = Tk() # Creating the Window
#window.config(bg="light gray")

equation_text = ""

label = Label(window, width=32, height=3, bg="white")
label.pack()

frame = Frame(window)
frame.pack(pady=50)

# Nunber Buttona:
#1
button1 = Button(frame,
                            text="1",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(1))
button1.grid(row=0,column=0)
#a

# 2
button2 = Button(frame,
                            text="2",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(2))
button2.grid(row=0,column=1)
#

#  3
button3 = Button(frame,
                            text="3",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(3))
button3.grid(row=0,column=2)
#

#    4
button4 = Button(frame,
                            text="4",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(4))
button4.grid(row=1,column=0)
#

#    5
button5 = Button(frame,
                            text="5",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(5))
button5.grid(row=1,column=1)
#

#    6
button6 = Button(frame,
                            text="6",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(6))
button6.grid(row=1,column=2)
#

#    7
button7 = Button(frame,
                            text="7",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(7))
button7.grid(row=2,column=0)
#

#   8
button8 = Button(frame,
                            text="8",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(8))
button8.grid(row=2,column=1)
#

#     9
button9 = Button(frame,
                            text="9",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(9))
button9.grid(row=2,column=2)
#

#0
button0 = Button(frame,
                            text="0",
                            font=("Arial",30),
                            command= lambda:
                                calc_button(0))
button0.grid(row=3,column=0)
#
# End of Number Buttons
#
# Operations:
plus = Button(frame,
                            width=1,
                            text="+",
                            font=("Arial",30),
                            command= lambda:
                                calc_button('+'))
plus.grid(row=0,column=4)

minus = Button(frame,
                            text="-",
                            width=1,
                            font=("Arial",30),
                            command= lambda:
                                calc_button('-'))
minus.grid(row=1,column=4)

multiply = Button(frame,
                            text="x",
                            width=1,
                            font=("Arial",30),
                            command= lambda:
                                calc_button('*'))
multiply.grid(row=2,column=4)

divide = Button(frame,
                            text="÷",
                            width=1,
                            font=("Arial",30),
                            command= lambda:
                                calc_button('/'))
divide.grid(row=3,column=4)
#

point = Button(frame,
                            text="•",
                            width=1,
                            font=("Arial",30),
                            command= lambda:
                                calc_button("."))
point.grid(row=3,column=1)

equal = Button(frame,
                            text="=",
                            width=1,
                            font=("Arial",30),
                            command=equals)
equal.grid(row=3,column=2)

clearB = Button(window,text="Clear",width=7,command=clear)
clearB.pack()

back = Button(window,text="Backspace",width=7,command=backspace)
back.pack()

labelWisdom = Label(window,font=("Arial", 5),text='// = division but always rounded down\n** = "To the power of"\n')
labelWisdom.pack()

window.mainloop() # End of the Window