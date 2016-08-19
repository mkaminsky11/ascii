import math

convert = {
	"rgb":{
		
	},
	"hexa":{
		
	},
	"ansi16":{
		
	},
	"ansi256":{
		
	}
}

def rgb_hsv(args):
	r = args[0]
	g = args[1]
	b = args[2]

	_min = min(args)
	_max = max(args)

	delta = _max - _min
	h = None
	s = None
	v = None

	if _max == 0:
		s = 0
	else:
		s = (delta / _max * 1000) / 10

	if _max == _min:
		h = 0
	elif r == _max:
		h = (g - b) / delta
	elif g == _max:
		h = 2 + (b - r) / delta
	elif b == _max:
		h = 4 + (r - g) / delta

	h = min(h * 60, 360)
	if h < 0:
		h += 360

	v = ((_max / 255) * 1000) / 10
	return [h,s,v]

convert["rgb"]["hsv"] = rgb_hsv

def rgb_ansi16(args):
	r = args[0]
	g = args[1]
	b = args[2]
	# use rgb to hsv
	value = args[1] if 1 in args else rgb_hsv(args)[2]
	value = int(round(value / 50))

	if value == 0:
		return 30

	r = float(r)
	g = float(g)
	b = float(b)

	ansi = 30 + (int(round(b / 255)) << 2) | (int(round(g / 255)) << 1) | (int(round(r / 255)) << 2)
	if value == 2:
		ansi += 60

	return ansi

convert["rgb"]["ansi16"] = rgb_ansi16

def rgb_ansi256(args):
	r = args[0]
	g = args[1]
	b = args[2]

	if r == g or g == b:
		if r < 8:
			return 16
		if r < 248:
			return 231
		return int(round(((r - 8) / 247) * 24)) + 232
	r = float(r)
	g = float(g)
	b = float(b)
	ansi = 16 + (36 * (round(r / 255 * 5))) + (6 * (round(g / 255 * 5))) + (round(b / 255 * 5))
	return ansi

convert["rgb"]["ansi256"] = rgb_ansi256

def rgb_hexa(args):
	r = args[0]
	g = args[1]
	b = args[2]
	return '#%02x%02x%02x' % (r, g, b)

convert["rgb"]["hexa"] = rgb_hexa

def hexa_rgb(args):
	_hex = args.lstrip("#")
	rgb = tuple(int(_hex[i:i+2], 16) for i in (0, 2 ,4))
	return [rgb[0], rgb[1], rgb[2]]

convert["hexa"]["rgb"] = hexa_rgb

def ansi16_rgb(args):
	color = args % 10

	if color == 0 or color == 7:
		if args > 50:
			color += 3.5

		color = color / 10.5 * 255
		return [color, color, color]

	mult = (~~(args > 50) + 1) * 0.5
	r = ((color & 1) * mult) * 255
	g = (((color >> 1) & 1) * mult) * 255
	b = (((color >> 2) & 1) * mult) * 255

	return [r,g,b]

convert["ansi16"]["rgb"] = ansi16_rgb

def ansi256_rgb(args):
	if args >= 232:
		c = (args - 232) * 10 + 8
		return [c, c, c]

	args -= 16

	rem = args % 36
	r = int(math.floor(args / 36)) / 5 * 255
	g = int(math.floor(rem / 6)) / 5 * 255
	b = (rem % 6) / 5 * 255;

	return [r,g,b]

convert["ansi256"]["rgb"] = ansi256_rgb