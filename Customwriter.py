import Buddy, test

from docx import Document

# # Open an existing document
# document = Document('path/to/your/document.docx')

# # Accessing document content
# for paragraph in document.paragraphs:
#     print(paragraph.text)

fonts=["LettersFont\Lettersv1-Regular (8).ttf","LettersFont\Lettersv2-Regular (2).ttf"]
Numbers=['NumberFont\Digits1-Regular.ttf']
slate=Buddy.Handwriting()

text11='''Ashu Chaurasiya '''
# Text corpus division
slate.write(text=test.text12,fontsize=72,fontpath=fonts)
slate.write("ty is completed")
