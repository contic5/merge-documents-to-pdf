import tkinter as tk
from tkinter import ttk  # Import themed widgets
from tkinter import filedialog

from pathlib import Path
from docx2pdf import convert
from docx import Document
from docxcompose.composer import Composer
import shutil

class Merge_Documents_GUI(tk.Tk):
    def __init__(self):
            super().__init__(className="Merge Documents to PDF")  # Initialize the base tk.Tk class
            self.geometry("500x400")
            self.label = ttk.Label(self, text="Merge Word Documents to PDF",wraplength=300,font=("Arial",24),justify="center")
            self.label.pack()

            self.results_label=ttk.Label(self,text="Ready to merge documents",font=("Arial",18),wraplength=300,justify="center")
            self.results_label.pack()

            self.current_file_label=ttk.Label(self,text="")
            self.current_file_label.pack()
    
            self.button = ttk.Button(self, text="Select Folder", width=25, command=self.select_folder)
            self.button.pack()
    
    def select_folder(self):
        #self.withdraw()  # Hides the main small root window
        folder_location = filedialog.askdirectory(title="Select Folder")
        
        if folder_location:
            student=folder_location.split("/")[-1]
            print("Selected folder:", folder_location)
            self.merge_student_files(folder_location,student)
        else:
            print("No folder selected.")

    def merge_student_files(self,folder_location,student):
        # Set the directory path
        dir_path = Path(folder_location)
        parent_path=dir_path.parent
        total_pdfs=0
        total_docx=0
        composer = Composer(Document())

        # Recursively iterate through all files and folders
        for path in dir_path.rglob("*"):
            depth = len(path.relative_to(dir_path).parts) - 1
            if path.is_file():
                if path.suffix==".docx":
                    print(f"Reading: {path}")
                    self.current_file_label.config(text=f"Reading {path}")
                    doc_to_append = Document(path)
                    composer.append(doc_to_append)
                    total_docx+=1
                elif path.suffix==".pdf":
                    total_pdfs+=1

        output_file_name=f"{student} Documents Merged"
        composer.save(f"output/{output_file_name}.docx")
        self.current_file_label.config(text=f"")

        self.results_label.config(text=f"Merged all Microsoft Word Documents for {student}")
        convert(f"output/{output_file_name}.docx")

        self.results_label.config(text=f"Converted Merged {student} Documents to PDF")

        if not "input" in str(parent_path):
            shutil.copy2(f"output/{output_file_name}.docx", f"{parent_path}/{output_file_name}.docx")        
            shutil.copy2(f"output/{output_file_name}.pdf", f"{parent_path}/{output_file_name}.pdf")        

if __name__ == "__main__":
    root=Merge_Documents_GUI()
    root.mainloop()