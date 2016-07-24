# coding: utf-8

from project.src.point import Point
from project.src.subModule.vector import Vector

if __name__ == "__main__":
	point = Point(3.2, 6.4)
	vector = Vector(4.2, 6.9)
	print(str(point) + ", " + str(vector))

