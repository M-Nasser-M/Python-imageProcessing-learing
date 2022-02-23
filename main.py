from filter_to_grayscale import turn_to_grayscale
import os
directory = './assets'
list = os.listdir(directory)
print(list)
for item in list:
    turn_to_grayscale(f'{directory}/{item}', './out')
