import math
pixels = ".,:;i1tfLCG08@"

from ascii import colorize

def asciify(r,g,b,a):
	rawChar = getRawChar(r,g,b,a)

	return colorize.colorize(rawChar, (r,g,b))

def getRawChar(r,g,b,a):
	value = intensity(r,g,b,a)
	precision = 255 * 3 / (len(pixels) -1)
	rawChar = pixels[int(round(value / precision))]

	return rawChar

def intensity(r,g,b,a):
	return (r+g+b) * a