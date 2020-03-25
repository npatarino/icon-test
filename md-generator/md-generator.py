# !/usr/bin/python

import os
import sys

PIPE = "|"
SLASH = "/"
PNG_FOLDER = "PNG"
PNG_EXTENSION = ".png"
BREAK = "\n"


class Icon:
    def __init__(self, image, name):
        self.image = image
        self.name = name


if __name__ == '__main__':
    path = sys.argv[1]
    files = os.listdir(path)
    root = os.path.basename(path)
    dictionary = {}
    file_content = ""
    for brand in files:
        brand_folder = path + SLASH + brand
        if os.path.isdir(brand_folder) and brand != ".DS_Store":
            for icon in os.listdir(brand_folder):
                if icon != ".DS_Store":
                    if icon in dictionary:
                        brands = dictionary[icon]
                        brands.append(brand)
                    else:
                        dictionary[icon] = [brand]
    for icon in dictionary:
        line_image = PIPE
        line_separator = BREAK + PIPE
        line_name = BREAK + PIPE
        for brand in dictionary[icon]:
            image = "[![" + icon + "](" + root + SLASH + brand + SLASH + icon + SLASH + PNG_FOLDER + SLASH + icon + PNG_EXTENSION + ")](" + root + SLASH + brand + SLASH + icon + SLASH + ")"
            line_image = line_image + image + PIPE
            line_separator = line_separator + " :----------: " + PIPE
            line_name = line_name + icon + PIPE
        line = line_image + line_separator + line_name + BREAK + BREAK
        file_content += line

    output_file_path = os.path.dirname(path) + SLASH + "README.md"
    print(output_file_path)
    print(file_content)
    file = open(output_file_path, "w+")
    file.write(file_content)
    file.close()
