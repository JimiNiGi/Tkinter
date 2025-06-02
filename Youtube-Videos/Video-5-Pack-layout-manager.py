import tkinter as tk

root = tk.Tk()
root.title("Hier steht der Titel")
root.geometry("400x400") # legt eine Größe fest die aber veränderbar ist


label1 = tk.Label(root, text="Label 1 beansprucht nun mehr Platz", bg="green")
label1.pack(side="top", expand=True, fill="both") #both ersetzt "x" oder "y"

label2 =tk.Label(root, text="Label 2", bg="red")
label2.pack(side="top", expand=True, fill="both")

root.mainloop()

print("Testausgabe")