import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3'],
    'Archives': ['.zip', '.rar']
}

def organize_files(source, destination):
    if not os.path.exists(source) or not os.path.exists(destination):
        messagebox.showerror("❌ Error", "Please select valid folders.")
        return

    for filename in os.listdir(source):
        file_path = os.path.join(source, filename)

        if os.path.isdir(file_path):
            continue  # Skip folders

        _, ext = os.path.splitext(filename)

        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                dest_folder = os.path.join(destination, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                break

    messagebox.showinfo("✅ Done", "Files organized successfully!")

def browse_source():
    folder = filedialog.askdirectory()
    if folder:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, folder)

def browse_destination():
    folder = filedialog.askdirectory()
    if folder:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder)

# GUI setup
root = tk.Tk()
root.title("🗂 File Organizer")
root.geometry("480x300")
root.resizable(False, False)

tk.Label(root, text="Select Source Folder:", font=("Arial", 12)).pack(pady=5)
source_entry = tk.Entry(root, width=60)
source_entry.pack(pady=5)
tk.Button(root, text="Browse Source", command=browse_source).pack()

tk.Label(root, text="Select Destination Folder:", font=("Arial", 12)).pack(pady=10)
destination_entry = tk.Entry(root, width=60)
destination_entry.pack(pady=5)
tk.Button(root, text="Browse Destination", command=browse_destination).pack()

tk.Button(root, text="🧹 Organize Files", font=("Arial", 12), bg="#4CAF50", fg="white",
          command=lambda: organize_files(source_entry.get(), destination_entry.get())).pack(pady=20)

root.mainloop()
