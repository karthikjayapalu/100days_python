from tkinter import *
import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

window.config(padx=200,pady=200)

#Label
my_label=tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.config(text="New Text")
my_label.grid(column=0,row=0)

#button
def button_clicked():
    print("Button got clicked")
    my_label.config(text=input.get())

button=Button(text='Click Me', command=button_clicked)
button.grid(column=1,row=1)

button1=Button(text='New Button', command=button_clicked)
button1.grid(column=2,row=0)
#Entry
input=Entry(width=15)
input.grid(column=3,row=2)
my_label.config(text=input.get())

window.mainloop()