"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from pyglet.gl import *

class Camera:
	def __init__(self):
		self.m = (GLfloat*16)()
		self.vx = self.vy = self.vz = 1
		self.tx = self.ty = self.tz = 0
		self.rx = self.ry = self.rz = 0

	def position(self, x, y, z):
		self.tx = x
		self.ty = y
		self.tz = z

	def rotation(self, x, y, z = 0):
		self.rx = x
		self.ry = y
		self.rz = z

	def move(self, dist):
		self.tx += ( self.vx * dist )
		self.ty += ( self.vy * dist )
		self.tz += ( self.vz * dist )
	
	def strafe(self, dist, d=0):
		if d == 1:
			self.ty += ( self.vy * dist )
		else:
			self.tx += ( self.vz * dist )
			self.tz -= ( self.vx * dist )

	def rotateX(self, rot):
		self.rx += rot

	def rotateY(self, rot):
		self.ry += rot

	def update(self):
		glRotatef(-self.rx, 1.0, 0.0, 0.0)
		glRotatef(-self.ry, 0.0, 1.0, 0.0)
		glRotatef(-self.rz, 0.0, 0.0, 1.0)
		glTranslatef(-self.tx, -self.ty, -self.tz)

		# Update View Dir 
		glGetFloatv(GL_MODELVIEW_MATRIX, self.m)
		self.vx = self.m[2]
		self.vy = self.m[6]
		self.vz = self.m[10]
