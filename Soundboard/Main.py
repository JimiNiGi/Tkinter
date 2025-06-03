import tkinter as tk
from gui import SoundboardApp # Importiere die Haupt-GUI-Klasse

if __name__ == "__main__":
    root = tk.Tk()
    app = SoundboardApp(root)
    root.mainloop()