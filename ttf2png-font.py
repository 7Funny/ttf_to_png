# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import time

# Settings
W, H = (2048, 2048)
font_color = "black"
truetype_size = 100

elems = "!\"#&$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
ru_elems = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def ttf2png():
  for filename in os.listdir("fonts/"):
    if os.path.isfile("fonts/"+filename):
      # font's file path
      font_file = os.path.join("fonts/", filename)
      # Font
      font = ImageFont.truetype(font_file, truetype_size, encoding='utf-8')
      # Image
      image = Image.new('RGB', (W, H), "white")
      draw = ImageDraw.Draw(image)
      # font's png file path
      file_path=f"fontpng/{filename[:-4]}.png"
      # line splitting
      lines = textwrap.wrap(elems+ru_elems, width=16)  # width - number of characters
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


def resize(image_path):
  #image_path = 'F:/hello.png'

  img = Image.open(image_path)
  pixels = img.load()
  # изменяем размер
  #new_image = img.resize((2048, 2048), Image.BILINEAR)
  # сохранение картинки
  for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i,j] != (0,0,0):
            pixels[i,j] = (255,255,255)
  img.save('_resize/111.png')
  #new_image.save('_resize/000.png')


def ttf2pngfile(filename):  # for one file
  # Settings
  W, H = (2048, 2048)
  font_color = "white"
  truetype_size = 100
  # font's file path
  font_file = os.path.join("fonts/", filename)
  # Font
  font = ImageFont.truetype(font_file, truetype_size, encoding='utf-8')

  # Image
  image = Image.new('RGB', (W, H), "black")
  draw = ImageDraw.Draw(image)
  # font's png file path
  file_path=f"fontpng-file/{filename[:-4]}.png"
  # line splitting
  lines = textwrap.wrap(elems+ru_elems, width=13)  # width - number of characters
  y_text = 0  # upper edge
  x_text = 36  # left edge
  index = 0  # characters

  for elem in elems+ru_elems:
    index += 1  
    _, _, w, h = draw.textbbox((0, 0), elem, font=font)
    print(w, h)
    draw.text(((x_text), y_text), elem, font=font, fill=font_color, align ="right")
    x_text += 128
    if index % 16 == 0: 
      y_text += 128
      x_text = 36
    try:
      image.save(file_path)
    except:
      error_text = f"[-] Couldn't Save: {filename}"
      print(error_text.encode("utf-8"))


def ttf2pngelems():
  start_time = time.time()
  # Settings
  W, H = (2048, 2048)
  font_color = "white"
  truetype_size = 128
  # font's file path
  for filename in os.listdir("fonts/"):
    if os.path.isfile("fonts/"+filename):
      # font's file path
      font_file = os.path.join("fonts/", filename)
      # Font
      font = ImageFont.truetype(font_file, truetype_size, encoding='utf-8')

      # Image
      image = Image.new('RGB', (W, H), "black")
      draw = ImageDraw.Draw(image)
      # font's png file path
      file_path=f"fontpngelems/{filename[:-4]}.png"
      # line splitting
      lines = textwrap.wrap(elems+ru_elems, width=13)  # width - number of characters
      y_text = 0  # upper edge
      x_text = 36  # left edge
      index = 0  # characters

      for elem in elems+ru_elems:
        index += 1  
        _, _, w, h = draw.textbbox((0, 0), elem, font=font)
        print(w, h)
        draw.text(((x_text), y_text), elem, font=font, fill=font_color, align ="right")
        x_text += 128
        if index % 16 == 0: 
          y_text += 128
          x_text = 36
        try:
          image.save(file_path)
        except:
          error_text = f"[-] Couldn't Save: {filename}"
          print(error_text.encode("utf-8"))
  print("--- %s seconds ---" % (time.time() - start_time))


#ttf2png()
#ttf2pngfile("OpenGostTypeA-Regular.ttf")
resize("fontpng-file/OpenGostTypeA-Regular.png")
#ttf2pngelems()

