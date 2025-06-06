from PIL import Image,ImageEnhance,ImageDraw
import random

# def random_color(opacity=255):
#     return (0, 0, 0, opacity) if random.random() < 0.5 else (255, 255, 255, opacity)

# def draw_noise_splatter(draw, width, height, splatters=100, min_r=3, max_r=15):
#     for _ in range(splatters):
#         x = random.randint(0, width)
#         y = random.randint(0, height)
#         r = random.randint(min_r, max_r)
#         aspect = random.uniform(0.5, 1.5)  # Some splatters are ovals
#         opacity = random.randint(120, 255)
#         color = random_color(opacity)

#         # Draw ellipse (splatter shape)
#         x0 = x - r
#         y0 = int(y - r * aspect)
#         x1 = x + r
#         y1 = int(y + r * aspect)
#         draw.ellipse([x0, y0, x1, y1], fill=color)


# Load your scanned page or create a blank one for this example
width, height = 2480, 3508
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))  # Alpha=0 for transparency

draw = ImageDraw.Draw(image)

# Simulate noise: density = percentage of affected pixels
noise_density = 0.04  # 1% of the pixels
num_noise_pixels = int(width * height * noise_density)

for _ in range(num_noise_pixels):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    color = 0 if random.random() < 0.5 else 255  # black or white noise
    draw.point((x, y), fill=color)
# draw_noise_splatter(draw, width, height, splatters=10)
# Save or show the noisy image
image.save("scanned_page_with_noise.png")





def overlay(x,y,img2_path,bg_Img_path,outfolder,outname,masking=False,show=True):
    # Opening the primary image (used in background) 
    img1 = Image.open(bg_Img_path) 

    # Opening the secondary image (overlay image) 
    img2 = Image.open(img2_path) 

    #copying the image
    img_copy = img1.copy()

    # Pasting img2 image on top of img1 's copy
    # starting at coordinates (x, y) 
    if(not masking):
        img_copy.paste(img2, (x,y)) 
    else:
        img_copy.paste(img2, (x,y),mask=img2)

    # saving the image
    outpath2=outfolder+outname+".JPG"
    brightness_enhancer = ImageEnhance.Brightness(img_copy)
    image_darker = brightness_enhancer.enhance(0.5)  # 0.7 = 70% brightness (reduce exposure)
    color_enhancer = ImageEnhance.Color(img_copy)
    warmer_image = color_enhancer.enhance(1.4)  # e.g., 1.2 means 20% more color
    img_copy.save(outpath2)
    # Displaying the image 
    if(show):
        img_copy.show()
overlay(0,0,'scanned_page_with_noise.png','Pages/2.jpg','./','test',masking=True,show=False)