# This code example demonstrates how to convert PNG to SVG
import os
import aspose.words as aw

#  Create document object
doc = aw.Document()

# Create a document builder object
builder = aw.DocumentBuilder(doc)

for dirs, folder, files in os.walk("fontpng/"):
    for file in files:
        # Load and insert PNG image
        shape = builder.insert_image(os.path.join(dirs, file))

        # Specify image save format as SVG
        saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)

        # Save image as SVG
        shape.get_shape_renderer().save(f"svg/{os.path.splitext(file)[0]}.svg", saveOptions)