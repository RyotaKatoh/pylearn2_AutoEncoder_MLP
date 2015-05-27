import numpy
from PIL import Image
import sys
import os
import glob
from PIL import ImageOps
import random
import cv2

def gs(path):
	im = Image.open(path)
	im = ImageOps.grayscale(im)
	return im

def resize(im, x, y):
	return im.resize((x, y))

def img2text(path):
	im = resize(gs(path), 64, 64)

	l = (numpy.asarray(im).flatten() / 255.0).tolist()

	l = [str(e) for e in l]
	return " ".join(l)

def img2csv(imgPath, csvPath, start, end):
	import csv
	f = open(csvPath, "w")
	writer = csv.writer(f)
	writer.writerow([1,1])

	for e in glob.glob(imgPath):
		print e
		l = img2text(e)
		writer.writerow([1, l])

	f.close()


def createDogCatData(DOG_PATH, CAT_PATH, OTH_PATH, csvPath):
	import csv
	f = open(csvPath, "w")
	writer = csv.writer(f)
	writer.writerow([1,1])

	doglist = glob.glob(DOG_PATH)
	catlist = glob.glob(CAT_PATH)
	othlist = glob.glob(OTH_PATH)

	for i in range(len(doglist)):
		dogimage = doglist[i]
		catimage = catlist[i]
		othimage = othlist[i]

		dl = img2text(dogimage)
		cl = img2text(catimage)
		ol = img2text(othimage)

		writer.writerow([0, dl])
		writer.writerow([1, cl])
		writer.writerow([2, ol])

	f.close()


if __name__ == "__main__":

	if len(sys.argv) == 5:
		dog_dir_path = sys.argv[1] + "/*"
		cat_dir_path = sys.argv[2] + "/*"
		oth_dir_path = sys.argv[3] + "/*"
		output_path  = sys.argv[4]

	else:
		sys.exit("Need 4 args. Dog, Cat, Other Image Dir Path and Output Path")

	createDogCatData(dog_dir_path, cat_dir_path, oth_dir_path, output_path)
