import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter.messagebox import showinfo

# Importiere die ausgelagerten Funktionen
from file_operations import open_file_dialog, save_file_dialog
from sound_player import play_sound_placeholder, play_all_sounds_placeholder

class SoundboardApp:
    def __init__(self, master):
        self.master = master
        master.title("Soundboard")
        master.geometry("700x400")
        master.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="15 15 15 15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Steuerungs-Buttons ---
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(pady=10)

        self.open_button = ttk.Button(
            control_frame,
            text='📁 Datei öffnen',
            command=self._handle_open_file # Ruft die interne Handler-Methode auf
        )
        self.open_button.grid(row=0, column=0, padx=5)

        self.save_button = ttk.Button(
            control_frame,
            text='💾 Datei speichern',
            command=self._handle_save_file # Ruft die interne Handler-Methode auf
        )
        self.save_button.grid(row=0, column=1, padx=5)

        self.exit_button = ttk.Button(
            control_frame,
            text='❌ Beenden',
            command=self._quit_application
        )
        self.exit_button.grid(row=0, column=2, padx=5)

        # --- Sound-Buttons ---
        sound_buttons_frame = ttk.Frame(main_frame, padding="10 20 10 0")
        sound_buttons_frame.pack(pady=20, fill=tk.X)

        self.sound_names = ['Jingle 1 🎶', 'Effect 2 🥁', 'Voice 3 🗣️', 'Loop 4 🔁']
        self.sound_buttons = []

        for i, name in enumerate(self.sound_names):
            button = ttk.Button(
                sound_buttons_frame,
                text=name,
                width=20,
                command=lambda n=name: self._handle_play_sound(n) # Ruft die interne Handler-Methode auf
            )
            button.grid(row=0, column=i, padx=8, pady=8)
            self.sound_buttons.append(button)

        # --- Separater Play-Button ---
        self.play_all_button = ttk.Button(
            main_frame,
            text="▶ Alles abspielen",
            command=self._handle_play_all_sounds # Ruft die interne Handler-Methode auf
        )
        self.play_all_button.pack(pady=15)

        # --- Status-Label ---
        self.status_label = ttk.Label(main_frame, text="Soundboard bereit.")
        self.status_label.pack(side=tk.BOTTOM, pady=10)

    # --- Interne Handler-Methoden, die die externen Funktionen aufrufen ---

    def _handle_open_file(self):
        """Behandelt das Öffnen eines Dateidialogs und aktualisiert den Status."""
        self.status_label.config(text="Dateidialog wird geöffnet...")
        selected_file = open_file_dialog() # Aufruf der ausgelagerten Funktion
        if selected_file:
            showinfo(title='Ausgewählte Datei', message=f"Du hast ausgewählt: {selected_file}")
            self.status_label.config(text=f"Datei geladen: {selected_file.split('/')[-1]}")
        else:
            self.status_label.config(text="Keine Datei ausgewählt.")

    def _handle_save_file(self):
        """Behandelt das Speichern eines Dateidialogs und aktualisiert den Status."""
        self.status_label.config(text="Speicherdialog wird geöffnet...")
        saved_file = save_file_dialog() # Aufruf der ausgelagerten Funktion
        if saved_file:
            self.status_label.config(text=f"Datei gespeichert: {saved_file.split('/')[-1]}")
        else:
            self.status_label.config(text="Speichern abgebrochen.")

    def _handle_play_sound(self, sound_name):
        """Behandelt das Abspielen eines einzelnen Sounds und aktualisiert den Status."""
        self.status_label.config(text=f"Spiele ab: {sound_name}...")
        play_sound_placeholder(sound_name) # Aufruf der ausgelagerten Funktion
        # Hier könntest du prüfen, ob das Abspielen erfolgreich war und den Status entsprechend anpassen

    def _handle_play_all_sounds(self):
        """Behandelt das Abspielen aller Sounds und aktualisiert den Status."""
        self.status_label.config(text="Spiele alle Sounds ab...")
        play_all_sounds_placeholder() # Aufruf der ausgelagerten Funktion

    def _quit_application(self):
        """Fragt nach Bestätigung und beendet die Anwendung."""
        if mb.askyesno("Soundboard beenden", "Bist du sicher, dass du das Soundboard beenden möchtest?"):
            self.master.quit()