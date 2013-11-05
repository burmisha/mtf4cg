#!/usr/bin/python
import os,sys
from PIL import Image

def calcMTF():
	 return 0

def main():
	filename="_MG_0324.JPG"
	image = Image.open(filename)
	xsize, ysize = image.size
	print xsize, ysize
	box = (xsize / 2, ysize / 2, xsize / 2 + 1000, ysize / 2 + 1) # (left, upper, right, lower).	
	line = image.crop(box)
	line.save("tmp.png", 'png')
	list(line.getdata())

if __name__ == "__main__":
	main()
