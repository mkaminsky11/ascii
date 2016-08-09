from pixel import Pixel
import math
pixels = ".,:;i1tfLCG08@"

import colorize

def asciify(r,g,b,a):
	pix = Pixel(r,g,b,a)

	#
	value = pix.intensity()
	precision = 255 * 3 / (len(pixels) -1)
	rawChar = pixels[int(round(value / precision))]
	#

	return colorize.colorize(rawChar, (r,g,b))