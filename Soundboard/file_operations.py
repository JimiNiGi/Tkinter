from tkinter import filedialog as fd

def open_file_dialog():
    """
    Öffnet einen Dateiauswahldialog und gibt den Pfad der ausgewählten Datei zurück.
    Gibt None zurück, wenn der Dialog abgebrochen wird.
    """
    filetypes = (
        ('Audio Dateien', '*.mp3 *.wav *.ogg'),
        ('Alle Dateien', '*.*')
    )
    filename = fd.askopenfilename(
        title='Wähle eine Audiodatei',
        initialdir='./',
        filetypes=filetypes
    )
    return filename

def save_file_dialog():
    """
    Öffnet einen "Speichern unter"-Dialog und gibt den Pfad der ausgewählten Datei zurück.
    Gibt None zurück, wenn der Dialog abgebrochen wird.
    """
    filetypes = (
        ('Text Dateien', '*.txt'), # Beispiel: Wenn du Einstellungen speichern willst
        ('Alle Dateien', '*.*')
    )
    filename = fd.asksaveasfilename(
        title='Speichern unter',
        initialdir='./',
        filetypes=filetypes
    )
    return filename

# Du könntest hier auch Funktionen für das tatsächliche Laden/Speichern von Daten hinzufügen
# def load_soundboard_settings(filepath):
#     pass
#
# def save_soundboard_settings(filepath, settings_data):
#     pass