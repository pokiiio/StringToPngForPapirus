# coding=utf-8

import sys
import math
import argparse
from os import path
from PIL import Image, ImageDraw, ImageFont

# color settings
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# display size of PaPiRus e-paper (Default : LARGE)
DISPLAY_WIDTH = 264
DISPLAY_HEIGHT = 176

# max chars/row (approx)
MAX_TEXT_LENGTH = 15

# font path
FONT_PATH = path.dirname(path.abspath(__file__)) + '/ipaexg.ttf'

# string to show
text = u""

# string split
text_list = []

# column
num_text_column = 0

# size of row
text_width = 0
text_height = 0

# font config (font size is tentative)
font = ImageFont.truetype(FONT_PATH, 200, encoding='unic')


def parse_arguments():
    global text, DISPLAY_WIDTH, DISPLAY_HEIGHT, BACKGROUND_COLOR, TEXT_COLOR

    parser = argparse.ArgumentParser(description='This command creates a PNG image file for PaPiRus e-papers.')
    parser.add_argument("-s", type=str, help = "set string to show on PaPiRus e-papers.", required=True)
    parser.add_argument("-i", action="store_true", default=False, help = "invert color. (white text with black background)", required=False)

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-L", action="store_true", default=False, help = "create a large image. (264 x 176)", required=False)
    group.add_argument("-M", action="store_true", default=False, help = "create a medium image. (200 x 96)", required=False)
    group.add_argument("-S", action="store_true", default=False, help = "create a small image. (128 x 96)", required=False)

    command_arguments = parser.parse_args()
    text = command_arguments.s.decode('utf-8')

    if command_arguments.L:
        DISPLAY_WIDTH, DISPLAY_HEIGHT = (264, 176)
    elif command_arguments.M:
        DISPLAY_WIDTH, DISPLAY_HEIGHT = (200, 96)
    elif command_arguments.S:
        DISPLAY_WIDTH, DISPLAY_HEIGHT = (128, 96)

    if command_arguments.i:
        TEXT_COLOR = (255, 255, 255)
        BACKGROUND_COLOR = (0, 0, 0)


def split_text_to_show():
    global text_list, num_text_column

    max_text = "";
    for i in range(MAX_TEXT_LENGTH):
        max_text = max_text + u"あ"

    max_length, max_height = font.getsize(max_text)
    actual_length, actual_height = font.getsize(text)

    num_text_column = int(math.ceil(float(actual_length)/float(max_length)))
    max_length = int(math.ceil(float(actual_length)/float(num_text_column)))

    temp_text = ""
    for c in text:
        temp_text = temp_text + c
        temp_length, temp_height = font.getsize(temp_text)

        if temp_length > max_length:
            text_list.append(temp_text)
            temp_text = ""

    if len(temp_text) > 0:
        text_list.append(temp_text)


def determine_font_size():
    global font, text_width, text_height

    font_size = DISPLAY_HEIGHT
    font = ImageFont.truetype(FONT_PATH, font_size, encoding='unic')
    longest_text = text_list[0]

    for text in text_list:
        while 1:
            w, h = font.getsize(text)
            if w < DISPLAY_WIDTH and h < DISPLAY_HEIGHT:
                break
            font_size = font_size - 2
            font = ImageFont.truetype(FONT_PATH, font_size, encoding='unic')
            longest_text = text

    text_width, text_height = font.getsize(longest_text)


def create_image_file():
    im = Image.new("RGB", (DISPLAY_WIDTH, DISPLAY_HEIGHT), BACKGROUND_COLOR)
    d = ImageDraw.Draw(im)

    column = 0
    while column < num_text_column:
        d.text(((DISPLAY_WIDTH - text_width) / 2, (DISPLAY_HEIGHT - text_height * num_text_column) / 2 + text_height * column),
               text_list[column], font=font, fill=TEXT_COLOR)
        column = column + 1

    im.save("output.png", "PNG")


if __name__ == '__main__':
    parse_arguments()
    split_text_to_show()
    determine_font_size()
    create_image_file()
