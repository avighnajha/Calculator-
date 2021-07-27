from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))

        equation_label.set(total)
        equation_text=total
    except ZeroDivisionError:
        equation_label.set("Arithematic Error")
    except SyntaxError:
        equation_label.set("Syntax Error")
def clear():
    global equation_text
    equation_label.set("")

    equation_text = ""
window=Tk()

window.title("Calculator")
window.geometry("280x370")
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, bg="white", width=24, height=2)
label.grid(row=0, column=0, columnspan=4)

frame = Frame(window)
frame.grid()

button1 = Button(window, text=1, height=2, width=5, font=20,
                 command= lambda:button_press(1))
button1.grid(row=1, column=0)

button2 = Button(window, text=2, height=2, width=5, font=20,
                 command= lambda:button_press(2))
button2.grid(row=1, column=1)

button3 = Button(window, text=3, height=2, width=5, font=20,
                 command= lambda:button_press(3))
button3.grid(row=1, column=2)

button4 = Button(window, text=4, height=2, width=5, font=20,
                 command= lambda:button_press(4))
button4.grid(row=2, column=0)

button5 = Button(window, text=5, height=2, width=5, font=20,
                 command= lambda:button_press(5))
button5.grid(row=2, column=1)

button6 = Button(window, text=6, height=2, width=5, font=20,
                 command= lambda:button_press(6))
button6.grid(row=2, column=2)

button7 = Button(window, text=7, height=2, width=5, font=20,
                 command= lambda:button_press(7))
button7.grid(row=3, column=0)

button8 = Button(window, text=8, height=2, width=5, font=20,
                 command= lambda:button_press(8))
button8.grid(row=3, column=1)

button9 = Button(window, text=9, height=2, width=5, font=20,
                 command= lambda:button_press(9))
button9.grid(row=3, column=2)

button0 = Button(window, text=0, height=2, width=5, font=20,
                 command= lambda:button_press(0))
button0.grid(row=4, column=0)

plus = Button(window, text="+", height=2, width=5, font=20,
                 command= lambda:button_press("+"))
plus.grid(row=1, column=3)

minus = Button(window, text="-", height=2, width=5, font=20,
                 command= lambda:button_press("-"))
minus.grid(row=2, column=3)

times = Button(window, text="*", height=2, width=5, font=20,
                 command= lambda:button_press("*"))
times.grid(row=3, column=3)

divide = Button(window, text="/", height=2, width=5, font=20,
                 command= lambda:button_press("/"))
divide.grid(row=4, column=3)

equals = Button(window, text="=", height=2, width=5, font=20,
                 command= equals)
equals.grid(row=4, column=2)

decimal = Button(window, text=".", height=2, width=5, font=20,
                 command= lambda:button_press("."))
decimal.grid(row=4, column=1)

clear = Button(window, text="Clear", height=2, width=10, font=20,
                 command= clear)
clear.grid(row=5, column=0, columnspan=4)
window.mainloop()
