import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x400")

image = Image.open("C:\Users\Scriptsprache\Desktop\TKinter\Tkinter\Main")

label1 =ttk.Label(root)
label1.pack()

label1.configure(text="Hello World")

root.mainloop()