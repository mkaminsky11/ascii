#!/usr/bin/env python
import terminal
import math
import asciify

def rgb_to_hex(rgb):
	return '%02x%02x%02x' % rgb

# import image stuff
from PIL import Image
import urllib3
http = urllib3.PoolManager()
import io

# load images
URL = "http://mkaminsky11.github.io/img/profile.jpeg"
fd = http.request('GET', URL)
image_file = io.BytesIO(fd.data)
im = Image.open(image_file)

size = im.size
columns = terminal.get_terminal_size()[0]
rows = round(size[1]/size[0] * columns)	
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
		output = output + asciify.asciify(_px[0], _px[1], _px[2], 1)
	output = output

print(output)