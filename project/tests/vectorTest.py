# coding: utf-8

from project.src.subModule.vector import Vector
import unittest

class VectorTestCase(unittest.TestCase):
	def setUp(self):
		self.vector = Vector(2.49, 4.21)

	def testStr(self):
		self.assertEquals("Vector(2.49, 4.21)", str(self.vector))

if __name__ == "__main__":
	unittest.main()

