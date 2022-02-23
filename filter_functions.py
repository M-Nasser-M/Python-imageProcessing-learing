from PIL import Image,ImageFilter
import re


def turn_to_grayscale(img_path: str, out_path):
    name = re.search("(?:.(?!\/))+$", img_path)
    new_name = name.group().replace('/', 'grayscale_').replace('jpg', 'png')

    img = Image.open(img_path)
    img = img.convert('L')
    img.save(f'{out_path}/{new_name}')
