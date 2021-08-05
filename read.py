import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--path")
parser.add_argument("--border")
args = vars(parser.parse_args())

import fitz
import json
import cv2
import os

# pdf = fitz.open("sample.pdf")
# for i, page in enumerate(pdf):
# 	pix = page.getPixmap()
# 	pix.writePNG("output"+str(i)+".png")
# args["path"] = r"C:\Users\Admin\source\repos\LVTN\LVTN\bin\Debug\sample"
# args["border"] = r"C:\Users\Admin\source\repos\LVTN\LVTN\bin\Debug\sample\box.json"

bbox = dict()
with open(args["border"], 'r', encoding='utf-8') as f:
	bbox = json.load(f) # x1 y1 x2 y2

for file in os.listdir(args["path"]):
	if (file[-4:] != ".png" and file[-4:] != ".pdf"): continue
	img = ""
	print(file)
	filePath = os.path.join(args["path"], file)
	if (file[-4:] == ".pdf"):
		pdf = fitz.open(filePath)
		pix = pdf[0].getPixmap()
		pix.writePNG(file[:-4]+".png")
		img = cv2.imread(file[:-4]+".png")
	elif (file[-4:] == ".png"):
		img = cv2.imread(filePath)
	rect = img.copy()
	height, width, c = img.shape
	for key in bbox.keys():
		start_point = (int(bbox[key][0]*width), int(bbox[key][1]*height)) # x1 y1
		end_point = (int(bbox[key][2]*width), int(bbox[key][3]*height)) # x2 y2
		color = (255,0,0)
		thickness = 2
		rect = cv2.rectangle(rect, start_point, end_point, color, thickness)
		crop_img = img[start_point[1]:end_point[1], start_point[0]:end_point[0]].copy() # y1:y2, x1:x2
		output = cv2.resize(crop_img, (2560,160), interpolation=cv2.INTER_CUBIC)
		cv2.imwrite("images/" + file[:-4] + "_" + key + ".png", output)

with open("src.txt", 'w', newline="") as f:
	for file in os.listdir("images"):
		if (file[-4:] != ".png"): continue
		f.write(file + "\n")