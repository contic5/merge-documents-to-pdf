from pathlib import Path
from docx2pdf import convert
from docx import Document
from docxcompose.composer import Composer

def merge_word_documents():
    pass

def get_all_files_for_student(student):
    # Set the directory path
    dir_path = Path(f"input/{student}")
    total_pdfs=0
    total_docx=0
    composer = Composer(Document())

    # Recursively iterate through all files and folders
    for path in dir_path.rglob("*"):
        if path.is_file():
            print(f"File: {path}")
            if path.suffix==".pdf":
                total_pdfs+=1
            elif path.suffix==".docx":
                doc_to_append = Document(path)
                composer.append(doc_to_append)
                total_docx+=1
        elif path.is_dir():
            print(f"Directory: {path}")
            
    print(f"Total PDFs: {total_pdfs}")
    print(f"Total Docxs: {total_docx}")
    composer.save(f"output/{student} Documents Merged.docx")
    print(f"Merged all Microsoft Word Documents for {student}")

    convert(f"output/{student} Documents Merged.docx")
    print("Converted Merged Document to PDF")

def main():
    get_all_files_for_student("Nicholas Popailo")

if __name__=="__main__":
    main()