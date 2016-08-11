from ascii import convert

def colorize(rawChar, px):
	r = px[0]
	g = px[1]
	b = px[2]
	rgb = [r,g,b]
	code = convert.convert["rgb"]["ansi256"](rgb)
	color = wrapAnsi256(code, 0)
	reset = '\u001b[39m'
	
	return color + rawChar + reset

def wrapAnsi16(code, offset):
	return '\u001b[' + str(code + offset) + 'm'

def wrapAnsi256(code, offset):
	return '\u001b[' + str(38 + offset) + ';5;' + str(code) + 'm'