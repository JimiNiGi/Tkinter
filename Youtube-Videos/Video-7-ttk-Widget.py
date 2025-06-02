import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")

label1 =ttk.Label(root)
label1.pack()

label1.configure(text="Hello World")

root.mainloop()