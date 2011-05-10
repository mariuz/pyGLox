"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import numpy

class Vec3:
	@classmethod	
	def mul(self,a,b):
		return [a[0] * b, a[1] * b, a[2] * b]

	@classmethod
	def add(self,a,b):
		return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
	
	@classmethod
	def sub(self,a,b):
		return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

	@classmethod
	def cross(self,a,b):
		return numpy.cross(a,b)
	
	@classmethod
	def dot(self,a,b):
		return (a[0] * b[0] + a[1] * b[1] + a[2] * b[2])

	@classmethod
	def length(self,a):
		return numpy.sqrt(Vec3.dot(a,a))

	@classmethod
	def normalize(self,a):
		l = 1 / Vec3.length(a)
		return [a[0] * l, a[1] * l, a[2] * l]

	@classmethod
	def dist(self,a,b):
		return Vec3.length(Vec3.sub(a,b))
