from tkinter import *
from tkinter.ttk import *


window = Tk(screenName='main')


def func():
    pass


e1 = Label(window, text="Say Whaaaaaaaat?")
e1.grid(row=0, column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

b1 = Button(window, text="Login", command='')
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
