from ascii import convert

def colorize(rawChar, px):
	r = px[0]
	g = px[1]
	b = px[2]
	rgb = [r,g,b]
	code = convert.convert["rgb"]["ansi256"](px)
	color = wrapAnsi256(code, 0)
	reset = '\x1b[0m'
	
	return color + rawChar + reset

def wrapAnsi16(code, offset):
	code = int(code)
	offset = int(offset)
	return '\x1b[' + str(code + offset) + 'm'

def wrapAnsi256(code, offset):
	code = int(code)
	offset = int(offset)
	return '\x1b[38;5;' + str(code + offset) + 'm'