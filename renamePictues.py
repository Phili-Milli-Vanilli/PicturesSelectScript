import os
from tkinter import Tk, filedialog, messagebox, Label, Entry, Button, StringVar

def rename_images(directory, base_name):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Initialize a counter for naming
    counter = 1
    
    # Loop through each file in the directory
    for filename in files:
        # Check if the file is a JPEG or CR2
        if filename.lower().endswith(('.jpeg', '.jpg', '.cr2')):
            # Determine the file extension
            _, extension = os.path.splitext(filename)
            
            # Create a new file name
            new_name = f"{base_name}{counter}{extension}"
            
            # Define full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            
            print(f"Renamed '{filename}' to '{new_name}'")
            
            # Increment the counter
            counter += 1

def select_directory():
    # Set an initial directory
    initial_dir = "E:/Bilder"
    directory = filedialog.askdirectory(title="Wähle den Ordner mit den Bildern aus", initialdir=initial_dir)
    if directory:
        directory_var.set(directory)

def on_rename():
    # Get the directory and base name from the user
    directory = directory_var.get()
    base_name = base_name_entry.get().strip()
    
    if not directory:
        messagebox.showwarning("Fehler", "Bitte wählen Sie ein Verzeichnis aus.")
        return
    
    if not base_name:
        messagebox.showwarning("Fehler", "Bitte geben Sie einen Basisnamen ein.")
        return
    
    # Call the function to rename images
    rename_images(directory, base_name)
    
    # Show a success message
    messagebox.showinfo("Erfolg", f"Alle Bilder wurden erfolgreich umbenannt mit dem Basisnamen '{base_name}'.")

# Initialize Tkinter root widget
root = Tk()
root.title("Bild Umbenennung")

# Create a StringVar to hold the directory path
directory_var = StringVar()

# Create and place widgets
directory_label = Label(root, textvariable=directory_var, width=50, anchor='w')
directory_label.pack(pady=10)

select_directory_button = Button(root, text="Ordner auswählen", command=select_directory)
select_directory_button.pack(pady=5)

Label(root, text="Geben Sie den Basisnamen ein:").pack(pady=10)

base_name_entry = Entry(root, width=30)
base_name_entry.pack(pady=5)

rename_button = Button(root, text="Bilder umbenennen", command=on_rename)
rename_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
