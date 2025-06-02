import tkinter as tk
from PIL import Image, ImageTk
import os
 

bildpfad = r"C:\Users\Scriptsprache\Desktop\TKinter\Tkinter\Youtube-Videos\Jill_Valentine.png"
 

print("Aktuelles Arbeitsverzeichnis:", os.getcwd())
 

root = tk.Tk()
root.title("Bildanzeige-Test")
root.geometry("400x400")
 

try:
    image = Image.open(bildpfad)
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
 
    
    label = tk.Label(root, image=photo)
    label.pack()
    print("Bild erfolgreich geöffnet und angezeigt!")
 
except FileNotFoundError:
    print("Bild nicht gefunden! Bitte Pfad prüfen.")
    label = tk.Label(root, text="Bild nicht gefunden!", bg="red", fg="white")
    label.pack(padx=10, pady=10)
 
except Exception as e:
    print("Ein anderer Fehler ist aufgetreten:", e)
    label = tk.Label(root, text="Fehler beim Laden!", bg="red", fg="white")
    label.pack(padx=10, pady=10)
 

root.mainloop()