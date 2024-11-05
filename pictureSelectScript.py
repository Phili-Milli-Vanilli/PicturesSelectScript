import os
import shutil
from tkinter import Tk, filedialog, messagebox

def copy_files(src_folder, dest_folder, extensions):
    """Kopiert Dateien mit den angegebenen Erweiterungen aus den direkten Unterordnern in den Zielordner."""
    for subdir in os.listdir(src_folder):
        subdir_path = os.path.join(src_folder, subdir)
        if os.path.isdir(subdir_path):
            for file in os.listdir(subdir_path):
                if file.lower().endswith(extensions):
                    src_file = os.path.join(subdir_path, file)
                    dest_file = os.path.join(dest_folder, file)
                    if not os.path.exists(dest_file):  # Vermeide das Überschreiben von Dateien
                        try:
                            shutil.copy2(src_file, dest_file)
                            print(f"Kopiere: {src_file} -> {dest_file}")  # Protokollierung
                        except Exception as e:
                            print(f"Fehler beim Kopieren von {src_file} nach {dest_file}: {e}")
                    else:
                        print(f"Überspringe {src_file}, da es bereits im Zielordner existiert.")

def main():
    try:
        # Erstellen der Tkinter-Hauptanwendung
        root = Tk()
        root.withdraw()  # Fenster verstecken

        # Auswahl des obersten Ordners
        src_folder = filedialog.askdirectory(title="Wähle den obersten Ordner aus")
        if not src_folder:
            messagebox.showerror("Fehler", "Kein Quellordner ausgewählt.")
            return

        # Zielordner auf dem Desktop erstellen
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        dest_folder = filedialog.askdirectory(title="Wähle ein Zielverzeichnis auf dem Desktop aus", initialdir=desktop_path)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Dateitypen definieren
        extensions = ('.jpg', '.jpeg', '.cr2')

        # Kopieren der Dateien
        copy_files(src_folder, dest_folder, extensions)

        # Erfolgsnachricht anzeigen
        messagebox.showinfo("Erfolg", "Dateien wurden erfolgreich kopiert.")
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
