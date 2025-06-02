import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x800")

image = Image.open("Youtube-Videos/Jill.jpg") # Unterordner mit angeben falls Bild dort liegt
image = image.resize((500, 500))
photo = ImageTk.PhotoImage(image)


label1 =ttk.Label(root, image=photo, text="Hallo ich bin Jill", compound="top")
label1.pack()

#label1.configure(text="Hello World")

root.mainloop()