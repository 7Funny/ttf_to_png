from aspose.imaging import Image
from aspose.imaging.fileformats.png import PngImage
from aspose.imaging.imageoptions import SvgOptions, SvgRasterizationOptions
import os


if 'TEMPLATE_DIR' in os.environ:
	templates_folder = os.environ['TEMPLATE_DIR']
else:
	templates_folder = r"result0/"

delete_output = 'SAVE_OUTPUT' not in os.environ
data_dir = templates_folder
with Image.load(os.path.join(data_dir, "OpenGostTypeA-Regular.png")) as image:
	svg_options = SvgOptions()
	svg_rasterization_options = SvgRasterizationOptions()
	svg_rasterization_options.page_width = float(image.width)
	svg_rasterization_options.page_height = float(image.height)
	svg_options.vector_rasterization_options = svg_rasterization_options
	image.save(os.path.join(data_dir, "result.svg"), svg_options)

"""
if delete_output:
	os.remove(os.path.join(data_dir, "result.svg"))
	"""