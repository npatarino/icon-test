# !/usr/bin/python

import os
import sys

PIPE = "|"
SLASH = "/"
PNG_FOLDER = "PNG"
SVG_FOLDER = "SVG"
PDF_FOLDER = "PDF"
PNG_EXTENSION = ".png"
SVG_EXTENSION = ".svg"
PDF_EXTENSION = ".pdf"
BREAK = "\n"

if __name__ == '__main__':
    path = sys.argv[1]
    files = os.listdir(path)
    root = os.path.basename(path)
    dictionary = {}
    file_content = "| global | name | SVG | PDF | | O2 | name | SVG | PDF |" + BREAK + "| :-: | :- | :-: | :-: | - | :-: | :- | :-: | :-: |" + BREAK
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
        row = ""
        counter = 0
        dictionary[icon].sort()
        for brand in dictionary[icon]:
            path_icon = root + SLASH + brand + SLASH + icon + SLASH + PNG_FOLDER + SLASH + icon + PNG_EXTENSION
            svg_icon = root + SLASH + brand + SLASH + icon + SLASH + SVG_FOLDER + SLASH + icon + SVG_EXTENSION
            pdf_icon = root + SLASH + brand + SLASH + icon + SLASH + PDF_FOLDER + SLASH + icon + PDF_EXTENSION
            row = row + "| ![" + icon + "](" + path_icon + ") | `" + icon + "`  |  [.svg](" + svg_icon + ") | [.pdf](" + pdf_icon + ") |  "
        file_content += row + BREAK

    output_file_path = os.path.dirname(path) + SLASH + "README.md"
    print(output_file_path)
    print(file_content)
    file = open(output_file_path, "w+")
    file.write(file_content)
    file.close()
