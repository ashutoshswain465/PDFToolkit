from PyPDF2 import PdfReader, PdfWriter
import os

print("PDF Toolkit")
print("===========\n")


def split_pdf():
    pdf_file = input("Enter PDF file: ")

    if not os.path.exists(pdf_file):
        print("Error: File not found!")
        return

    reader = PdfReader(pdf_file)
    total_pages = len(reader.pages)

    print(f"\nSplitting PDF into pages...")

    for page_num in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])

        output_file = f"page_{page_num + 1:03d}.pdf"
        with open(output_file, 'wb') as f:
            writer.write(f)

        print(f"✓ Created {output_file}")

    print(f"\nSuccessfully split into {total_pages} pages!")


def extract_pages():
    pdf_file = input("Enter PDF file: ")

    if not os.path.exists(pdf_file):
        print("Error: File not found!")
        return

    start_page = int(input("Start page: "))
    end_page = int(input("End page: "))
    output_file = input("Output filename: ")

    if not output_file.endswith('.pdf'):
        output_file += '.pdf'

    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    print(f"\nExtracting pages {start_page}-{end_page}...")

    for page_num in range(start_page - 1, end_page):
        if page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num])

    with open(output_file, 'wb') as f:
        writer.write(f)

    pages_extracted = end_page - start_page + 1
    print(f"✓ Extracted {pages_extracted} pages to {output_file}")


def rotate_pages():
    pdf_file = input("Enter PDF file: ")

    if not os.path.exists(pdf_file):
        print("Error: File not found!")
        return

    angle = int(input("Rotation angle (90, 180, 270): "))
    output_file = input("Output filename: ")

    if not output_file.endswith('.pdf'):
        output_file += '.pdf'

    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    print(f"\nRotating all pages by {angle} degrees...")

    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)

    with open(output_file, 'wb') as f:
        writer.write(f)

    print(f"✓ Rotated {len(reader.pages)} pages")
    print(f"✓ Saved to {output_file}")


def compress_pdf():
    pdf_file = input("Enter PDF file: ")

    if not os.path.exists(pdf_file):
        print("Error: File not found!")
        return

    output_file = input("Output filename: ")

    if not output_file.endswith('.pdf'):
        output_file += '.pdf'

    print("\nCompressing PDF...")

    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    with open(output_file, 'wb') as f:
        writer.write(f)

    original_size = os.path.getsize(pdf_file)
    compressed_size = os.path.getsize(output_file)
    reduction = ((original_size - compressed_size) / original_size) * 100

    print(f"Original size: {original_size / 1024 / 1024:.1f} MB")
    print(f"Compressed size: {compressed_size / 1024 / 1024:.1f} MB")
    print(f"Compression ratio: {reduction:.0f}% smaller\n")
    print(f"✓ Saved to {output_file}")


while True:
    print("\n1. Split PDF into individual pages")
    print("2. Extract page range")
    print("3. Rotate pages")
    print("4. Compress PDF")
    print("5. Exit\n")

    choice = input("Choose option: ")
    print()

    if choice == '1':
        split_pdf()
    elif choice == '2':
        extract_pages()
    elif choice == '3':
        rotate_pages()
    elif choice == '4':
        compress_pdf()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
