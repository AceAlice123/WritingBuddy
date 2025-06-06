import Buddy, os
from Buddy import Image
from docx import Document
from PyPDF2 import PdfMerger

from PDFScaler import scale_pdf_in_place
from Noise_tools import noise
fonts=["LettersFont/Lettersv1-Regular.otf","LettersFont/Lettersv2-Regular.otf"]
Numbers=['NumberFont/Digits1-Regular.ttf']

# Open an existing document
names=[201,208,211,212,213,214,215,216,217]
path=f"C:/Users/ashup/OneDrive/Desktop/{names[8]}.docx"
document = Document(path)
Name =f'2501321326_MCA_New_MCS{path[-8:-5]}'
# slate=Buddy.Handwriting(BackImg="Page (1).jpg",wrap_width=130,top_margin=380,side_margin=365)

slate=Buddy.Handwriting(wrap_width=86,fontsize=135,top_margin=140)

# slate.write(";",fontpath=fonts)
# Accessing document content
answer = True
for paragraph in document.paragraphs:
    st=paragraph.text[:8]
    if(st=="Question"):
        answer=False
    elif(st[:6]=="Answer"):
        answer = True
    slate.write(text=paragraph.text,fontpath=fonts,Answer=answer)
    

# save PDF 

pages=os.listdir("./Pages")
def sort_key(s):
    return int(s[:-4])

pages.sort(key=sort_key)

images = [
    Image.open("./Pages/" + f)
    for f in pages
]
# Id= Image.open("C:/Users/ashup/OneDrive/Desktop/1.jpg")
# Id.resize((1240,1754))
pdf_path = f"./{Name}.pdf"
for i in images:
    noise(i)
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)


# Delete all Pages
dir_path="./Pages"
[os.remove(os.path.join(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]


merger = PdfMerger()

path_for_pdfs="C:/Users/ashup/OneDrive/Desktop/IGNOU"

merger.append(f'{path_for_pdfs}/{path[-8:-5]}.pdf')
merger.append(f"C:/Users/ashup/OneDrive/Desktop/id_Scanned.pdf")
merger.append(f'{path_for_pdfs}/{path[-8:-5]}_.pdf')
scale_pdf_in_place(f'C:/Users/ashup/OneDrive/Desktop/Personal_Pro/WritingBuddy/{Name}.pdf',0.32 )

merger.append(f'C:/Users/ashup/OneDrive/Desktop/Personal_Pro/WritingBuddy/{Name}.pdf')
merger.write(f'2501321326_MCA_New_MCS{path[-8:-5]}.pdf')
print(f"PDF Sucessfully Created! C:/Users/ashup/OneDrive/Desktop/Personal_Pro/WritingBuddy/2501321326_MCA_New_MCS{path[-8:-5]}.pdf")
merger.close()

