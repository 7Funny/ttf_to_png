# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import uuid
import textwrap
import os

# Settings
W, H = (2048, 2048)
font_color = "black"
truetype_size = 128
lower_elems = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
upper_elems = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"
etc_elems = "1234567890‘?’“!”(%)[#]{@}/&\<-+÷×=>®©$€£¥¢:;,.*"

# for example
etc_elems="f"

def create_image(word, font):
  image = Image.new('RGB', (W, H), "white")
  draw = ImageDraw.Draw(image)
  _, _, w, h = draw.textbbox((0, 0), word, font=font)
  draw.text(((W-w)/2, (H-h)/2), word, font=font, fill=font_color)
  return image


def dir_path(isupper, elem):
  dir_path=f"fontpng-elems/({elem})/"
  if not isupper and not os.path.exists(dir_path): 
    os.makedirs(dir_path)
  elif isupper and not os.path.exists(f"result/({elem})upper/"):
    dir_path = f"fontpng-elems/({elem})upper/"
    os.makedirs(dir_path)
  elif isupper and os.path.exists(f"result/({elem})upper/"):
    dir_path = f"fontpng-elems/({elem})upper/"
  return dir_path


def ttf_TO_png(list_elems, isupper):
  index = 0

  for filename in os.listdir("fonts/"):
    print(filename)
    if os.path.isfile("fonts/"+filename):
      font_file = os.path.join("fonts/", filename)
      # Font
      font = ImageFont.truetype(font_file, truetype_size, encoding='utf-8')
      for elem in list_elems:
        # Image
        image = create_image(elem, font)
        # Save png file
        if elem == "/": elem = "!slash"
        if elem == "?": elem = "!question"
        if elem == "<": elem = "!less"
        if elem == ">": elem = "!more"
        if elem == ":": elem = "!colon"
        if elem == "*": elem = "!multiply"

        file_path=f"{dir_path(isupper, elem)}({filename}){str(uuid.uuid4())}.png"
        try:  
          image.save(file_path)
          index+=1
        except:
          error_text = f"[-] Couldn't Save: {elem} [{filename}]"
          print(error_text.encode("utf-8"))
    print(f"result: {index}")
  print(f"RESULT: {index}")


#ttf_TO_png(upper_elems, True)
#ttf_TO_png(lower_elems, False)
#ttf_TO_png(etc_elems, False)