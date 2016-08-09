#!/usr/bin/env python
def colorize(rawChar, px):
	color = ""
	reset = ""
	
	return color + rawChar + reset

colors = {
	"modifiers": {
		"reset": [0,0]
	},
	"colors": {
			"black": [30, 39],
			"red": [31, 39],
			"green": [32, 39],
			"yellow": [33, 39],
			"blue": [34, 39],
			"magenta": [35, 39],
			"cyan": [36, 39],
			"white": [37, 39],
			"gray": [90, 39],
			"grey": [90, 39]
	}
}
for groupKey in colors:
	group = colors[groupKey]
	for key in group:
		style = group[key]
		colors[groupKey][key] = {
			"open": '\u001b[' + str(style[0]) + 'm',
			"close": '\u001b[' + str(style[1]) + 'm'
		}

colors["colors"]["close"] = '\u001b[39m'
colors["colors"]["ansi"] = {}
colors["colors"]["ansi256"] = {}

