# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Settings
W, H = (2048, 2048)
font_color = "black"
truetype_size = 100
elems = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"
etc_elems = "1234567890‘?’“!”(%)[#]{@}/&\<-+÷×=>®©$€£¥¢:;,.*"


def ttf2png():
  for filename in os.listdir("fonts/"):
    if os.path.isfile("fonts/"+filename):
      font_file = os.path.join("fonts/", filename)
      # Font
      font = ImageFont.truetype(font_file, truetype_size, encoding='utf-8')
      # Image
      image = Image.new('RGB', (W, H), "white")
      draw = ImageDraw.Draw(image)

      file_path=f"fontpng/{filename[:-4]}.png"
      # line splitting
      lines = textwrap.wrap(elems+etc_elems, width=16)  # width - number of characters
      y_text = 64  # upper edge
      for line in lines:
        _, _, w, h = draw.textbbox((0, 0), line, font=font)
        draw.text(((5), y_text), line, font=font, fill=font_color, align ="right")
        y_text += 1.3*h
        try:  
          image.save(file_path)
        except:
          error_text = f"[-] Couldn't Save: {filename}"
          print(error_text.encode("utf-8"))


def ttf2pngfile(filename):  # for one file
  font_file = os.path.join("fonts/", filename)
  # Font
  font = ImageFont.truetype(font_file, truetype_size, encoding='utf-8')
  # Image
  image = Image.new('RGB', (W, H), "white")
  draw = ImageDraw.Draw(image)
  
  file_path=f"fontpng-file/{filename[:-4]}.png"
  # line splitting
  lines = textwrap.wrap(elems+etc_elems, width=16)  # width - number of characters
  y_text = 64  # upper edge

  for line in lines:
    _, _, w, h = draw.textbbox((0, 0), line, font=font)
    draw.text(((5), y_text), line, font=font, fill=font_color, align ="right")
    y_text += 1.3*h
    try:  
      image.save(file_path)
    except:
      error_text = f"[-] Couldn't Save: {filename}"
      print(error_text.encode("utf-8"))

ttf2png()
#ttf2pngfile("ofont.ru_FatGrot.ttf")

