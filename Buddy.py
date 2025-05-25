from PIL import Image, ImageDraw, ImageFont
import textwrap,random

class Handwriting:
    def __init__(self,savepath="C:/Users/ashup/Downloads",width=2480,height=3508):
        self.imgsets = Image.new("RGB", (width, height), "white")
        self.img = ImageDraw.Draw(self.imgsets)
        self.savepath=savepath
    def write(self,text,fontsize=36,font_path=["LettersFont\Lettersv2-Regular (2).ttf"],offset = 100,wrap_width=150,weights=[]):
        #iterate to fontpath array to create fonts array
        fonts=[]
        times=[]
        
        for i in font_path:
            fonts.append (ImageFont.truetype(i, fontsize))
            times.append(0)
        margin = 110
        text=self.__randomSpaces(text)
        for line in textwrap.wrap(text,wrap_width):
            print(len(line))
            # Random font index 
            rint=random.randint(0,len(fonts)-1)
            self.img.text((margin, offset), line, font=fonts[rint], fill="black")
            offset += fontsize + random.randint(8,10)
        self.imgsets.save(self.savepath+"/handwritten_note1.jpg")
        print("✅ Handwritten note created locally: handwritten_note1.jpg")
    def __randomSpaces(self, text):
        new_text=""
        for i in text:
            if (i==" " and random.randint(1,200)<20):
                new_text+="   "
            elif (i==" " and random.randint(1,200)<40):
                new_text+="  "
            elif(i==" " and random.randint(1,100)<60):
                new_text+=" "
            new_text+=i
        return new_text

