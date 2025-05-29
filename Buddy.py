from PIL import Image, ImageDraw, ImageFont
import textwrap,random

class Handwriting:
    def __init__(self,savepath="./Pages",width=2480,height=2408):
        self.width =width
        self.height =height
        self.savepath=savepath
        self.current_imgset=Image.new("RGB", (self.width, self.height), "white")
        self.current_img=ImageDraw.Draw(self.current_imgset)
        self.current_page=1
        self.current_y=100
        self.set=False
        self.fontsize=72
        self.wrap_width=150

    def __write(self,text,fontsize,font_path,offset = 100,numbers_path=['NumberFont\Digits1-Regular.ttf','NumberFont\Myfont-Regular.otf'],page_number=1,Line_index=0,first=True):
        #iterate to fontpath array to create fonts array
       
        # print(text)
        print(Line_index)
        if(not first):
            imgsets = Image.new("RGB", (self.width, self.height), "white")
            img = ImageDraw.Draw(imgsets)
        else:
            imgsets=self.current_imgset
            img=self.current_img
            page_number=self.current_page
            offset=self.current_y
            first=False
        print(page_number)
        fonts=self.__pathtottf(font_path,fontsize)
        nfonts=self.__pathtottf(numbers_path,fontsize)
        margin = 110
    
        numbers=['1','2','3','4','5','6','7','8','9','0']
        remaining=['&','-','_','*','@','~']
        nonexisting=['-','_']
        for line in textwrap.wrap(text,self.wrap_width):
            # print(line)
            x=margin
            for char in line:
                rint=random.randint(0,len(fonts)-1)
                if (char in nonexisting):
                    img.text((x, offset), " ", font=nfonts[0], fill="black")
                    x+=nfonts[0].getmask(char).size[0]
                elif(char in numbers):
                    img.text((x, offset), char, font=nfonts[0], fill="black")
                    x+=nfonts[0].getmask(char).size[0]
                elif(char in remaining):
                    # print(char)
                    img.text((x, offset), char, font=nfonts[1], fill="black")
                    x+=nfonts[1].getmask(char).size[0]
                else:
                    img.text((x, offset), char, font=fonts[rint], fill="black")
                    x+=fonts[rint].getmask(char).size[0]
            
                # print(i,char)
            Line_index+=1
            offset += fontsize + random.randint(9,10)
            # New Page
            if(offset>=self.height-80):
                
                self.__write(self.slice_txt(text,Line_index),fontsize,font_path,100,numbers_path,page_number+1,Line_index,False)
                break
        if(not self.set):
            self.current_imgset=imgsets
            self.current_img=img
            self.current_page=page_number
            self.current_y=offset
            print(f"offset{offset}")
            self.set=True
        imgsets.save(f'''{self.savepath}/handwritten_note{page_number}.jpg''')
        print(f"✅ Handwritten note created locally: handwritten_note{page_number}.jpg")
    def __randomSpaces(self, text):
        count=0
        new_text=""
        for i in text:
            if i==".":
                new_text+=" "
                count+=1
            elif (i==" " and random.randint(1,200)<20):
                new_text+="   "
                count+=3
            elif (i==" " and random.randint(1,200)<40):
                new_text+="  "
                count+=2
            elif(i==" " and random.randint(1,100)<60):
                new_text+=" "
                count+=1
            new_text+=i
        return new_text
    
    def __pathtottf(self,patharray,fontsize):
        ttfarray=[]
        for i in patharray:
            ttfarray.append (ImageFont.truetype(i, fontsize))
        return ttfarray
    def write(self, text, fontsize=72,fontpath=["LettersFont\Lettersv2-Regular (2).ttf"]):
        self.set=False
        self.fontsize=fontsize
        text=self.__randomSpaces(text)
        self.__write(text,fontsize,fontpath)
    def slice_txt(self,text,line_number):
        new_text=""
        index=1
        wrapobject=textwrap.wrap(text,self.wrap_width)[line_number:]
        for line in wrapobject:
                new_text+=line
        return new_text




