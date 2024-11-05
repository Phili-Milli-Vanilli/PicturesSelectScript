import os
from tkinter import Tk, filedialog, messagebox, Label, Button, StringVar

def rename_images_in_subfolders(root_directory):
    # Loop through each direct subdirectory in the root directory
    for subdir in os.listdir(root_directory):
        subdir_path = os.path.join(root_directory, subdir)
        if os.path.isdir(subdir_path):
            # Initialize a counter for naming files in this subdirectory
            counter = 1

            # List all files in the subdirectory
            for filename in os.listdir(subdir_path):
                # Check if the file is a JPEG or CR2
                if filename.lower().endswith(('.jpeg', '.jpg', '.cr2')):
                    # Determine the file extension
                    _, extension = os.path.splitext(filename)

                    # Create a new file name based on the subdirectory name
                    new_name = f"{subdir}_{counter}{extension}"

                    # Define full file paths
                    old_file = os.path.join(subdir_path, filename)
                    new_file = os.path.join(subdir_path, new_name)

                    # Rename the file
                    os.rename(old_file, new_file)

                    print(f"Renamed '{filename}' to '{new_name}' in '{subdir_path}'")

                    # Increment the counter
                    counter += 1

    # Show a success message after processing all subdirectories
    messagebox.showinfo("Erfolg", "Alle Bilder in den Unterordnern wurden erfolgreich umbenannt.")

def select_directory():
    # Set an initial directory
    initial_dir = "/Pfad/zum/Standardverzeichnis"  # Beispielpfad
    root_directory = filedialog.askdirectory(title="Wähle das Stammverzeichnis aus", initialdir=initial_dir)
    if root_directory:
        directory_var.set(root_directory)

def on_rename():
    # Get the root directory from the user
    root_directory = directory_var.get()
    
    if not root_directory:
        messagebox.showwarning("Fehler", "Bitte wählen Sie ein Stammverzeichnis aus.")
        return
    
    # Call the function to rename images
    rename_images_in_subfolders(root_directory)

# Initialize Tkinter root widget
root = Tk()
root.title("Bild Umbenennung in Unterordnern")

# Create a StringVar to hold the directory path
directory_var = StringVar()

# Create and place widgets
directory_label = Label(root, textvariable=directory_var, width=50, anchor='w')
directory_label.pack(pady=10)

select_directory_button = Button(root, text="Stammverzeichnis auswählen", command=select_directory)
select_directory_button.pack(pady=5)

rename_button = Button(root, text="Bilder umbenennen", command=on_rename)
rename_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
