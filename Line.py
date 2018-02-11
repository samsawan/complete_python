class Line(object):

	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return ((self.horizontal_distance() ** 2) + (self.vertical_distance() ** 2)) ** 0.5

	def slope(self):
		return (float(self.vertical_distance()) / float(self.horizontal_distance()))

	def vertical_distance(self):
		y1, y2 = self.coor2
		return y2 - y1

	def horizontal_distance(self):
		x1, x2 = self.coor2
		return x2 - x1
