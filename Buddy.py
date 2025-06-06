from PIL import Image, ImageDraw, ImageFont
import textwrap,random
from fontTools.ttLib import TTFont

class Handwriting:
    def __init__(self,numbers_path=[],fontpath=[],fontsize=140,savepath="./Pages",width=2480,height=3508,BackImg=' ',wrap_width=150,side_margin=150,top_margin=150):
        self.BackImg=BackImg
        numbers_path=['NumberFont/Digits1-Regular.ttf','NumberFont/Myfont-Regular.otf',"NumberFont/mathilde.otf","NumberFont/Lasts-Regular.otf"]
        fontpath=["LettersFont/Lettersv1-Regular.otf","LettersFont/Lettersv2-Regular.otf"]
        self.width =width
        self.height =height
        self.savepath=savepath
        self.fontsize=fontsize
        if BackImg==' ':
            self.current_imgset=Image.new("RGB", (self.width, self.height), "white")
        else:
            self.BackImg=Image.open(BackImg).convert('RGB')
            self.current_imgset=self.BackImg.copy()
        numbers_path=['NumberFont/Digits1-Regular.ttf','NumberFont/Myfont-Regular (3).otf',"NumberFont/mathilde.otf","NumberFont/Lasts-Regular.otf"]
        self.fonts=self.__pathtottf(fontpath,fontsize)
        self.nfonts=self.__pathtottf(numbers_path,fontsize)
        self.current_img=ImageDraw.Draw(self.current_imgset)
        enr_x=850+random.randint(20,100)
        self.current_img.text((enr_x, 10), "Enrollment No.", font=self.fonts[random.randint(0,1)], fill='black')
        self.current_img.text((enr_x+410+random.randint(7,14), 10), "2501321326", font=self.nfonts[0], fill='black')
        self.current_page=1
        self.current_y=top_margin
        self.top_margin =top_margin
        self.set=False
        self.side_margin=side_margin
        self.wrap_width=wrap_width

    def __write(self,text,fontsize,Answer,page_number=1,Line_index=0,first=True):
        #iterate to fontpath array to create self.fonts array
       
        # print(text)
        if(not first):
            imgsets = Image.new("RGB", (self.width, self.height), "white") if self.BackImg==' ' else self.BackImg.copy()
            img = ImageDraw.Draw(imgsets)
            
            # img.line([(0, self.fontsize-20), (2480, self.fontsize-20)], fill='black', width=5)
            offset=self.top_margin-random.randint(0,15)
        else:
            imgsets=self.current_imgset
            img=self.current_img
            page_number=self.current_page
            offset=self.current_y
            first=False
        margin = self.side_margin
        Characters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',';','!','"','(',')','[',']','<','>',',','∑','\\','=','#','%','^']
        numbers=['1','2','3','4','5','6','7','8','9','0']
        remaining=['&','~']
        Last=['{','}','-']
        Ink="#252724" if not Answer else "#0b2a84"
        for line in textwrap.wrap(text,self.wrap_width, drop_whitespace=False):
            # print(line)
            Random_side=random.randint(4,11)+random.randint(0,12) if Answer else random.randint(0,4)
            x=margin+Random_side
            for char in line:
                off_R=random.randint(0,3)
                if (char in Characters):
                    rint=random.randint(0,len(self.fonts)-1)
                    img.text((x, offset+off_R), char, font=self.fonts[rint], fill=Ink)
                    x+=self.fonts[rint].getmask(char).size[0]
                elif(char in numbers):
                    img.text((x, offset+off_R), char, font=self.nfonts[0], fill=Ink)
                    x+=self.fonts[0].getmask(char).size[0]-random.randint(13,15)
                elif(char in remaining):
                    # print(char)
                    img.text((x, offset+off_R), char, font=self.nfonts[1], fill=Ink)
                    x+=self.fonts[0].getmask(char).size[0]-random.randint(9,11)
                elif(char in Last):
                    # print(char)
                    img.text((x, offset+off_R), char, font=self.nfonts[3], fill=Ink)
                    x+=self.fonts[0].getmask(char).size[0]-random.randint(9,11)
                else:
                    # print(self.fonts[0].getmask(char).size[0])
                    if self.__font_has_char("NumberFont/mathilde.otf",char):
                        img.text((x, offset+off_R), char, font=self.nfonts[2], fill=Ink)
                        x+=self.fonts[0].getmask(char).size[0]-random.randint(7,8)
                # print(i,char)
            Line_index+=1
            offset += self.fontsize + random.randint(8,11)
            # New Page
            if(offset>=self.height-138):
                print(f"✅ Completed {page_number}-{page_number+1}")
                self.__write(self.slice_txt(text,Line_index),fontsize,Answer,page_number+1,Line_index,False)
                break
        if(not self.set):
            self.current_imgset=imgsets
            self.current_img=img
            self.current_page=page_number
            self.current_y=offset
            # print(f"offset{offset}")
            self.set=True
        imgsets.save(f'''{self.savepath}/{page_number+1}.jpg''')
        
    def __randomSpaces(self, text):
        
        new_text=""
        for i in text:
            if i==".":
                new_text+=" "
            elif (i==" " and random.randint(1,200)<20):
                new_text+="   "
                
            elif (i==" " and random.randint(1,200)<40):
                new_text+="  "
                
            elif(i==" " ):
                new_text+=" "
                
            new_text+=i
        return new_text
    
    def __pathtottf(self,patharray,fontsize):
        ttfarray=[]
        for i in patharray:
            ttfarray.append (ImageFont.truetype(i, fontsize))
        return ttfarray
    def write(self, text, fontsize=' ',fontpath=["LettersFont/Lettersv2-Regular.otf"],Answer=True):
        self.set=False
        if not fontsize==' ':
            self.fontsize=fontsize
            self.fonts=self.__pathtottf(fontpath,fontsize)
            self.nfonts=self.__pathtottf(numbers_path,fontsize)
        text=self.__randomSpaces(text)
        numbers_path=['NumberFont/Digits1-Regular.ttf','NumberFont/Myfont-Regular.otf',"NumberFont/mathilde.otf","NumberFont/Lasts-Regular.otf"]
        self.__write(text,self.fontsize,Answer)
    def slice_txt(self,text,line_number):
        new_text=""

        wrapobject=textwrap.wrap(text,self.wrap_width)[line_number:]
        for line in wrapobject:
                new_text+=line
        return new_text
    
    def __font_has_char(self,font_path, char):
        font = TTFont(font_path)
        for table in font['cmap'].tables:
            if ord(char) in table.cmap:
                return True
        return False




