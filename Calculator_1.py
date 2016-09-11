from tkinter import *

root = Tk()

# Stops the window from being resized by the user
root.resizable(0, 0)
root.title("calculator")

# _______________________________________ #
# ******* (* CALCULATOR ENGINE *) ******* #


string = StringVar()  # String Var that contains what is displayed on the screen


def clear():
    string.set("")


def equals():
    # Tries this line
    try:
        # Evaluates the string
        result = eval(string.get())
    # But if it doesn't work out, tries this line so it doesn't break the code
    except:
        result = "Error"

    string.set(result)


def add_char(char):
    if string.get() == "Error":
        string.set("")

    string.set(string.get() + str(char))
    screen.focus()


def delete():
    string.set(string.get()[0:-1])  # Will delete the last char of the string

# ____________________________________ #
# ******* (* CALCULATOR GUI *) ******* #


# ( * The Number Button Images * ) #
ci_1 = PhotoImage(file="CalcIcons\ci_1.png")
ci_2 = PhotoImage(file="CalcIcons\ci_2.png")
ci_3 = PhotoImage(file="CalcIcons\ci_3.png")
ci_4 = PhotoImage(file="CalcIcons\ci_4.png")
ci_5 = PhotoImage(file="CalcIcons\ci_5.png")
ci_6 = PhotoImage(file="CalcIcons\ci_6.png")
ci_7 = PhotoImage(file="CalcIcons\ci_7.png")
ci_8 = PhotoImage(file="CalcIcons\ci_8.png")
ci_9 = PhotoImage(file="CalcIcons\ci_9.png")
ci_0 = PhotoImage(file="CalcIcons\ci_0.png")

# ( * The Operator Button Images * ) #
ci_plus = PhotoImage(file="CalcIcons\ci_plus.png")
ci_minus = PhotoImage(file="CalcIcons\ci_minus.png")
ci_divide = PhotoImage(file="CalcIcons\ci_divide.png")
ci_equals = PhotoImage(file="CalcIcons\ci_equals.png")
ci_period = PhotoImage(file="CalcIcons\ci_period.png")
ci_clear = PhotoImage(file="CalcIcons\ci_clear.png")
ci_delete = PhotoImage(file="CalcIcons\ci_erase.png")
ci_multiply = PhotoImage(file="CalcIcons\ci_multiply.png")

# ( * The Number Buttons * ) #

cb_1 = Button(root, image=ci_1, relief=FLAT, command=lambda x=1: add_char(x))
cb_2 = Button(root, image=ci_2, relief=FLAT, command=lambda x=2: add_char(x))
cb_3 = Button(root, image=ci_3, relief=FLAT, command=lambda x=3: add_char(x))
cb_4 = Button(root, image=ci_4, relief=FLAT, command=lambda x=4: add_char(x))
cb_5 = Button(root, image=ci_5, relief=FLAT, command=lambda x=5: add_char(x))
cb_6 = Button(root, image=ci_6, relief=FLAT, command=lambda x=6: add_char(x))
cb_7 = Button(root, image=ci_7, relief=FLAT, command=lambda x=7: add_char(x))
cb_8 = Button(root, image=ci_8, relief=FLAT, command=lambda x=8: add_char(x))
cb_9 = Button(root, image=ci_9, relief=FLAT, command=lambda x=9: add_char(x))
cb_0 = Button(root, image=ci_0, relief=FLAT, command=lambda x=0: add_char(x))

cb_1.grid(row=1, column=0, padx=1, pady=1)
cb_2.grid(row=1, column=1, padx=1, pady=1)
cb_3.grid(row=1, column=2, padx=1, pady=1)
cb_4.grid(row=2, column=0, padx=1, pady=1)
cb_5.grid(row=2, column=1, padx=1, pady=1)
cb_6.grid(row=2, column=2, padx=1, pady=1)
cb_7.grid(row=3, column=0, padx=1, pady=1)
cb_8.grid(row=3, column=1, padx=1, pady=1)
cb_9.grid(row=3, column=2, padx=1, pady=1)
cb_0.grid(row=4, column=1, padx=1, pady=1)


# ( * The Operator Buttons * ) #
cb_equals = Button(root, image=ci_equals, relief=FLAT, command=equals).grid(row=5, column=3)
cb_plus = Button(root, image=ci_plus, relief=FLAT, command=lambda x=' + ': add_char(x)).grid(row=3, column=3)
cb_minus = Button(root, image=ci_minus, relief=FLAT, command=lambda x=' - ': add_char(x)).grid(row=2, column=3)
cb_divide = Button(root, image=ci_divide, relief=FLAT, command=lambda x=' / ': add_char(x)).grid(row=1, column=3)
cb_period = Button(root, image=ci_period, relief=FLAT, command=lambda x=' . ': add_char(x)).grid(row=4, column=2)
cb_clear = Button(root, image=ci_clear, relief=FLAT, command=clear).grid(row=4, column=0)
cb_delete = Button(root, image=ci_delete, relief=FLAT, command=delete).grid(row=5, column=2)
cb_multiply = Button(root, image=ci_multiply, relief=FLAT, command=lambda x=' * ': add_char(x)).grid(row=4, column=3)


# Screen where the results show up in
screen = Entry(textvariable=string, bd=1, relief=SUNKEN)
screen.grid(row=0, column=0, columnspan=4, sticky=E+W, pady=5)
screen.focus()


# End~
root.mainloop()
