from filter_functions import turn_to_grayscale, apply_blur_filter, apply_crop, apply_thumbnail
import os
directory = './assets'
list = os.listdir(directory)

# for item in list:
#     turn_to_grayscale(f'{directory}/{item}', './out')

# for item in list:
#     apply_blur_filter(f'{directory}/{item}', './out')

# for item in list:
#     apply_crop(f'{directory}/{item}', './out', (100, 100, 400, 400))

for item in list:
    apply_thumbnail(f'{directory}/{item}', './out', (400, 400))
