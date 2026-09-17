import tkinter as tk
from tkinter import filedialog
import time

from pathlib import Path
from docx2pdf import convert
from docx import Document
from docxcompose.composer import Composer

def merge_student_files(folder_location,student):
    # Set the directory path
    dir_path = Path(folder_location)
    total_pdfs=0
    total_docx=0
    composer = Composer(Document())

    # Recursively iterate through all files and folders
    for path in dir_path.rglob("*"):
        depth = len(path.relative_to(dir_path).parts) - 1
        if path.is_file():
            if path.suffix==".docx":
                print(f"Reading: {path}")
                doc_to_append = Document(path)
                composer.append(doc_to_append)
                total_docx+=1
            elif path.suffix==".pdf":
                total_pdfs+=1

    print(f"Total Docxs: {total_docx}")
    print(f"Total PDFs: {total_pdfs}")
    composer.save(f"output/{student} Documents Merged.docx")
    print(f"Merged all Microsoft Word Documents for {student}")

    convert(f"output/{student} Documents Merged.docx")
    print("Converted Merged Document to PDF")

def select_folder():
    print("Merge Student Documents to PDF")
    print("Select a Student Folder to Scan")
    time.sleep(1)
    
    root = tk.Tk()
    root.withdraw()  # Hides the main small root window
    folder_location = filedialog.askdirectory(title="Select Folder")
    
    if folder_location:
        student=folder_location.split("/")[-1]
        print("Selected folder:", folder_location)
        merge_student_files(folder_location,student)
    else:
        print("No folder selected.")

if __name__ == "__main__":
    select_folder()