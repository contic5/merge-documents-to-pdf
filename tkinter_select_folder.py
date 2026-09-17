import tkinter as tk
from tkinter import filedialog

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hides the main small root window
    folder_path = filedialog.askdirectory(title="Select Folder")
    
    if folder_path:
        print("Selected folder:", folder_path)
    else:
        print("No folder selected.")

if __name__ == "__main__":
    select_folder()