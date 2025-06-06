import PyPDF2
import os

def scale_pdf_in_place(pdf_file, scale_factor):
    temp_file = pdf_file + '.tmp.pdf'
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()

    for page in reader.pages:
        page.scale_by(scale_factor)
        writer.add_page(page)

    with open(temp_file, 'wb') as f:
        writer.write(f)

    # Replace original PDF with the scaled version
    os.replace(temp_file, pdf_file)