# coding: utf-8

import unittest
from project.src.point import Point

class PointTestCase(unittest.TestCase):
	def setUp(self):
		self.point = Point(2.4, 6.3)

	def testStr(self):
		self.assertEquals("Point(2.4, 6.3)", str(self.point))

if __name__ == "__main__":
	unittest.main()

