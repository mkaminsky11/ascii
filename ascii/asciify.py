import math
pixels = ".,:;i1tfLCG08@"

from ascii import colorize
from ascii import terminal

def asciify(r,g,b,a):

	#
	value = intensity(r,g,b,a)
	precision = 255 * 3 / (len(pixels) -1)
	rawChar = pixels[int(round(value / precision))]
	#

	return colorize.colorize(rawChar, (r,g,b))

def intensity(r,g,b,a):
	return (r+g+b) * a