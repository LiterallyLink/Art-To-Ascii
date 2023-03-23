import os
from PIL import Image
from tkinter import filedialog

def main():
    filepath = select_file()

    if filepath is not None:
        image = Image.open(filepath)
        image = resize(image)
        image = greyscale(image)
    
        # greyscaling makes the pixels have a value between 0 (black) to 255 (white), dividing by 25 makes it 0-10.
        # making it equal to the lowest (0) and highest (10) array index for the ascii table.
        ascii_table = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
        pixel_value_divider = 25

        ascii_art_str = ''

        for pixel in image.getdata():
            ascii_art_str += ascii_table[int(pixel / pixel_value_divider)]

        new_width = image.size[0]
        
        ascii_art = '\n'.join(
            [ascii_art_str[i:i+new_width] for i in range(0, len(ascii_art_str), new_width)]
        )

        save_ascii_art(ascii_art)
        os.startfile('ascii_art.txt')

def select_file():
    file_path = filedialog.askopenfilename()

    if file_path: return file_path
    else: return None

def resize(image, new_width = 200):
    old_width, old_height = image.size
    aspect_ratio = old_height / old_width
    new_height = int(aspect_ratio * new_width * 0.55)

    return image.resize((new_width, new_height))

def greyscale(image):
    return image.convert("L")

def save_ascii_art(ascii_art):
    with open('ascii_art.txt', 'w') as file:
        file.write(ascii_art)

main()