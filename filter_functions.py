from PIL import Image, ImageFilter
import re


def turn_to_grayscale(img_path: str, out_path):
    name = re.search("(?:.(?!\/))+$", img_path)
    new_name = name.group().replace('/', 'grayscale_').replace('jpg', 'png')

    img = Image.open(img_path)
    img = img.convert('L')
    img.save(f'{out_path}/{new_name}', 'png')
    return img


def apply_blur_filter(img_path: str, out_path):
    name = re.search("(?:.(?!\/))+$", img_path)
    new_name = name.group().replace('/', 'blurred_').replace('jpg', 'png')

    img = Image.open(img_path)
    img = img.filter(ImageFilter.BLUR)
    img.save(f'{out_path}/{new_name}' 'png')
    return img


def apply_crop(img_path, out_path, crop_size):
    name = re.search("(?:.(?!\/))+$", img_path)
    new_name = name.group().replace('/', 'cropped_').replace('jpg', 'png')

    img = Image.open(img_path)
    img = img.crop(crop_size)
    img.save(f'{out_path}/{new_name}', 'png')
    return img


def apply_thumbnail(img_path, out_path, thumbnail_size):
    name = re.search("(?:.(?!\/))+$", img_path)
    new_name = name.group().replace('/', 'thumbnail_').replace('jpg', 'png')

    img = Image.open(img_path)
    img.thumbnail(thumbnail_size)
    img.save(f'{out_path}/{new_name}', 'png')
    return img
