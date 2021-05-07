import tkinter as tk
from tkinter import *
root = Tk()


root.geometry("900x600")
root.title("Temperature Converter")


numberInput = StringVar()
var = StringVar()
input_label = Label(root, text="Enter temperature")
input_entry = Entry(root, textvariable=numberInput)
input_label.grid(row=0)
input_entry.grid(row=0, column=1)

result_button = Button(root, text="Convert")
result_button.grid(row=1, columnspan=4)

rLabel1 = tk.Label(root, text="Result1")
rLabel2 = Label(root, text="Result2")
rLabel.grid(row=3, columnspan=4)
dropdownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = OptionMenu(root, var, *dropdownList)
var.set(dropdownList[0])
dropdown.grid(row=0, column=2)

root.mainloop()
