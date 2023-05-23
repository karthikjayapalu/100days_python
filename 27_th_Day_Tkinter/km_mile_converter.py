import tkinter
from tkinter import *

window = tkinter.Tk()

window.title("KM to Mile Converter")

window.minsize(width=300,height=150)
window.config(padx=20,pady=20)

#text box to get the input in KM
input=Entry(width=15)
input.grid(column=1,row=0)


lbl_km=tkinter.Label(text="Km/s",font=("Arial"))
lbl_km.grid(column=2,row=0)


# label to print the result

lbl_mile=tkinter.Label(text="is equal to",font=("Arial"))
lbl_mile.grid(column=0,row=1)

lbl_result=tkinter.Label(text=" ",font=("Arial"))
lbl_result.grid(column=1,row=1)

lbl_km=tkinter.Label(text="Mile/S",font=("Arial"))
lbl_km.grid(column=2,row=1)

# Button - to calculate the conversion
def calculate_km_to_mile():
    km = float(input.get())
    mile=round(km*0.621371,2)
    lbl_result.config(text=mile)
    return mile
button=Button(text="Calculate",command=calculate_km_to_mile)
button.grid(column=1,row=2)







window.mainloop()