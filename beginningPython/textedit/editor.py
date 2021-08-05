from tkinter import *
from tkinter.scrolledtext import ScrolledText

def load():
    with open(filename.get()) as file:
        contents.delete('1.0',END)
        contents.insert(INSERT, file.read())

def save():
    with open(filename.get()) as file:
        contents.write('1.0', END)

top = Tk()
top.title("Simple editor")

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, file=BOTH)

filename = Entry()
filename.pack(side=BOTTOM, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save,).pack(side=LEFT)

mainloop()