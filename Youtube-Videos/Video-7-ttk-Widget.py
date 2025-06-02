import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x400")

image = Image.open("Jill.jpg")
photo = ImageTk.PhotoImage(image)

label1 =ttk.Label(root, image=photo)
label1.pack()

label1.configure(text="Hello World")

root.mainloop()