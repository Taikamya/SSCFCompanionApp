from tkinter import *
from tkinter.ttk import *
import modules.database as mdb
import sys
# class WindowExec(object):


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in mdb.view():
        return list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in mdb.search(username_text.get()):
        return list1.insert(END, row)


def add_command():
    mdb.insert(username_text.get(), password_text.get, premium_bool.get())
    list1.delete(0, END)
    return list1.insert(END, (username_text.get(), password_text.get, premium_bool.get()))


def update_command():
    return mdb.update(selected_tuple[0], username_text.get(), password_text.get())


def delete_command():
    return mdb.delete(selected_tuple[0])


window = Tk()
window.title("SSCF Companion App")

l1 = Label(window, text="Username")
l1.grid(column=0, row=0)

l2 = Label(window, text="Password")
l2.grid(column=0, row=1)

l3 = Label(window, text="Ok!")
l3.grid(column=2, row=1)

bar = Progressbar(window, length=200)
bar.grid(column=3, row=8)

username_text = StringVar()
e1 = Entry(window, textvariable=username_text)
e1.grid(column=1, row=0)

password_text = StringVar()
e2 = Entry(window, textvariable=password_text)
e2.grid(column=1, row=1)

premium_bool = BooleanVar()
premium_bool.set(False)
chk1 = Checkbutton(window, text="Premium", var=premium_bool)
chk1.grid(column=2, row=0)

list1 = Listbox(window, height=6, width=35)
list1.grid(column=0, row=2, columnspan=2, rowspan=6)
sb1 = Scrollbar(window)
sb1.grid(column=2, row=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<Listbox>>', get_selected_row)

b1 = Button(window, text="View All", width=14, command=view_command)
b1.grid(column=3, row=2)

b2 = Button(window, text="Search", width=14, command=search_command)
b2.grid(column=3, row=3)

b3 = Button(window, text="Add", width=14, command=add_command)
b3.grid(column=3, row=4)

b4 = Button(window, text="Update Selected", width=14,
            command=update_command)
b4.grid(column=3, row=5)

b5 = Button(window, text="Delete Selected", width=14,
            command=delete_command)
b5.grid(column=3, row=6)

b6 = Button(window, text="Close", width=14, command=sys.exit)
b6.grid(column=3, row=7)

window.mainloop()
