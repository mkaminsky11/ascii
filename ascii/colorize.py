from ascii import convert

def colorize(rawChar, px):
	r = px[0]
	g = px[1]
	b = px[2]
	rgb = [r,g,b]
	code = convert.convert["rgb"]["ansi256"](rgb)
	color = wrapAnsi256(code, 0)
	reset = '\x1b[0m'
	
	return color + rawChar + reset

def wrapAnsi16(code, offset):
	return '\x1b[' + str(code) + 'm'

def wrapAnsi256(code, offset):
	return '\x1b[38;5;' + str(code) + 'm'