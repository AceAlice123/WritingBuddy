from PIL import ImageEnhance,ImageDraw
import random

def noise(image):
    draw = ImageDraw.Draw(image)
    width,height =2480,3508
    # Simulate noise: density = percentage of affected pixels
    noise_density = 0.2 # 1% of the pixels
    num_noise_pixels = int(height * noise_density)

    for _ in range(num_noise_pixels):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        color = 0 if random.random() < 0.5 else 255  # black or white noise
        draw.point((x, y), fill=color)
    brightness_enhancer = ImageEnhance.Brightness(image)
    image = brightness_enhancer.enhance(0.5)  # 0.7 = 70% brightness (reduce exposure)
    color_enhancer = ImageEnhance.Color(image)
    image = color_enhancer.enhance(1.5)
    print('Page_Noised')
