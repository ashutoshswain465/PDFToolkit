from PyPDF2 import PdfMerger, PdfReader
import os

print("PDF Merger")
print("==========\n")

folder_path = input("Enter folder path (or press Enter for current directory): ").strip()

if not folder_path:
    folder_path = "."

if not os.path.exists(folder_path):
    print(f"Error: Folder '{folder_path}' not found!")
    exit()

pdf_files = []
for file in os.listdir(folder_path):
    if file.lower().endswith('.pdf'):
        pdf_files.append(os.path.join(folder_path, file))

pdf_files.sort()

if not pdf_files:
    print(f"No PDF files found in '{folder_path}'")
    exit()

print(f"\nFound {len(pdf_files)} PDF files:")
for i, pdf in enumerate(pdf_files, 1):
    print(f"{i}. {os.path.basename(pdf)}")

output_file = input("\nOutput filename: ").strip()

if not output_file.endswith('.pdf'):
    output_file += '.pdf'

print("\nMerging PDFs...")

merger = PdfMerger()
total_pages = 0

for pdf_file in pdf_files:
    merger.append(pdf_file)

    reader = PdfReader(pdf_file)
    page_count = len(reader.pages)
    total_pages += page_count

    print(f"✓ Added {os.path.basename(pdf_file)} ({page_count} pages)")

merger.write(output_file)
merger.close()

print(f"\nSuccessfully merged {len(pdf_files)} PDFs into {output_file}")
print(f"Total pages: {total_pages}")
