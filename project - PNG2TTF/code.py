from PIL import Image
import fontforge


def png2ttf():
    output = "_output.ttf"
    image = Image.open("y0.png")
    width = 8
    height = 8

    factor = 10 # size factor so that coords are in range [16, 65536]
    private_range = 0xe000 # starting codepoint of private copy
    background = (0, 0, 0) # background RGB color

    font = fontforge.font() 
    font.ascent = height * factor
    font.descent = 0 * factor
    font.encoding = 'UnicodeFull' # required encoding to access private range

    pixels = image.load()

    for j in range(image.height // height):
        print(f"j = {j}")
        for i in range(image.width // width):
            offset = i + j * (image.width // width)
            print(f"i = {i}; offset = {offset}")

            # generate two copies of char, in 0-256 and in private range
            for codepoint in [offset, private_range + offset]:
                char = font.createChar(codepoint)
                char.width = width * factor
                pen = char.glyphPen()

                # draw each non-background pixel as a square
                for y in range(height):
                    for x in range(width):
                        pixel = pixels[i * width + x, j * height + y]
                        if pixel != background:
                            pen.moveTo((x * factor, (height - y) * factor)) # draw a pixel
                            pen.lineTo(((x + 1) * factor, (height - y) * factor))
                            pen.lineTo(((x + 1) * factor, (height - y - 1) * factor))
                            pen.lineTo((x * factor, (height - y - 1) * factor))
                            pen.closePath()
    # export to font 
    font.generate(output, flags=('opentype'))


def png2ttfinfo():
    output = "output.ttf"
    image = Image.open("OpenGostTypeA-Regular.png")
    width = 128
    height = 128

    factor = 10 # size factor so that coords are in range [16, 65536]
    private_range = 0xe000 # starting codepoint of private copy
    background = (0, 0, 0) # background RGB color - black

    font = fontforge.font() 
    font.ascent = height * factor
    font.descent = 0 * factor
    font.encoding = 'UnicodeFull' # required encoding to access private range
    
    pixels = image.load()

    for j in range(image.height // height):
        print(f"j = {j}")
        for i in range(image.width // width):
            offset = i + j * (image.width // width)
            print(f"i = {i}; offset = {offset}")

            # generate two copies of char, in 0-256 and in private range
            for codepoint in [offset, private_range + offset]:
                print(f"codepoint: {codepoint}, arr=[{offset}, {private_range+offset}]")
                char = font.createChar(codepoint)
                char.width = width * factor
                #print(f"width * factor = {width * factor}")
                pen = char.glyphPen()

                # draw each non-background pixel as a square
                for y in range(height):
                    #print(f"y = {y}")
                    for x in range(width):
                        pixel = pixels[i * width + x, j * height + y]
                        #print(f"x = {x}")
                        #print(f"pixel = {pixel}")
                        if pixel != background:
                            pen.moveTo((x * factor, (height - y) * factor)) # draw a pixel
                            pen.lineTo(((x + 1) * factor, (height - y) * factor))
                            pen.lineTo(((x + 1) * factor, (height - y - 1) * factor))
                            pen.lineTo((x * factor, (height - y - 1) * factor))
                            pen.closePath()
    # export to font 
    font.generate(output, flags=('opentype'))
    

#png2ttf()
png2ttfinfo()
