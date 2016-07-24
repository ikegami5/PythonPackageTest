# coding: utf-8

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "Point(" + str(self.x) + ", " + str(self.y) + ")"

