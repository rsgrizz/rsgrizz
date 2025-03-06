import os
import sys
import subprocess

try:
    from pdf2docx import Converter
except ImportError:
    print("[INFO] pdf2docx module not found. Installing it now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pdf2docx"])
    from pdf2docx import Converter

def convert_pdf_to_word(pdf_file, docx_file):
    """Converts a PDF file to a Word document."""
    print(f"[INFO] Starting conversion: {pdf_file} -> {docx_file}")
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        print(f"[INFO] Successfully converted to {docx_file}")
    except Exception as e:
        print(f"[ERROR] Conversion failed: {e}")
        return

def main():
    if len(sys.argv) < 2:
        print("[ERROR] No PDF file provided! Please run the script with the PDF file as an argument.")
        print("Usage: python script.py <path_to_pdf>")
        return
    
    pdf_file = sys.argv[1]
    print(f"[INFO] Received file path: {pdf_file}")
    
    if not os.path.isfile(pdf_file):
        print(f"[ERROR] The provided file does not exist: {pdf_file}")
        return
    
    try:
        docx_file = os.path.splitext(pdf_file)[0] + ".docx"
        print(f"[INFO] Preparing to convert {pdf_file} to {docx_file}")
        convert_pdf_to_word(pdf_file, docx_file)
        print(f"[INFO] Conversion complete: {docx_file}")
        
        if sys.platform == "win32":
            print(f"[INFO] Opening Word document: {docx_file}")
            os.startfile(docx_file)  # Open the converted file on Windows
        else:
            print(f"[INFO] Please open the file manually: {docx_file}")
    except OSError as e:
        print(f"[ERROR] File processing error: {e}")

if __name__ == "__main__":
    main()
