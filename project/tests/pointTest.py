# coding: utf-8

import unittest
from project.src.point import Point

class PointTestCase(unittest.TestCase):
	def setUp(self):
		self.point = Point(2.4, 6.3)

	def testToString(self):
		self.assertEquals("(2.4, 6.3)", self.point.toString())

if __name__ == "__main__":
	unittest.main()

