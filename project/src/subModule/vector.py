# coding: utf-8

class Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "Vector(" + str(self.x) + ", " + str(self.y) + ")"

