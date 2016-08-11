#!/usr/bin/env python
import math
from ascii import asciify

def rgb_to_hex(rgb):
	return '%02x%02x%02x' % rgb

# import image stuff
from PIL import Image
import urllib3
http = urllib3.PoolManager()
import io

# load images
def loadFromUrl(URL):
	fd = http.request('GET', URL)
	image_file = io.BytesIO(fd.data)
	im = Image.open(image_file)

	size = im.size
	columns = 60
	rows = columns * size[1] / size[0]
	rows = int(round(rows))
	"""
	rows/columns = height/width
	"""
	im = im.resize((columns, rows))
	px = im.load()
	size = im.size

	output = ""

	for y in range(0, size[1]):
		for x in range(0, size[0]):
			_px = px[x,y]
			_a = asciify.asciify(_px[0], _px[1], _px[2], 1)

			output = output + _a
		output = output + "\n"
	return output

def onePixel(r, g, b):
	return asciify.asciify(r,g,b, 1)