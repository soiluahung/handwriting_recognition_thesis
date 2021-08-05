import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--name")
args = vars(parser.parse_args())

import pdf2image
import os

path, file = os.path.split(args["file"])
pages = pdf2image.convert_from_path(args["file"])

for page in pages:
	page.save(args["name"], "png")
	break;