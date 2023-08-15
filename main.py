import tkinter as tk
from tkinter import *

root = Tk()

def showthis():
    Label(root, text="job is done!").grid(row=13, column=1)


btton = Button(root, text="Download", padx=30, pady=30, command=showthis).grid(row=1, column=1)


root.mainloop()