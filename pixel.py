class Pixel:
	def __init__(self, r, g, b, a):
		self.r = r
		self.g = g
		self.b = b
		self.a = a

	def intensity(self):
		return (self.r + self.g + self.b) * self.a

	def hex(self):
		return '#%02x%02x%02x' % (self.r, self.g, self.b)