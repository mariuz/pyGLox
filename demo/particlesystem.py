"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import random
import math
from pyglet.gl import *

class Particle(object):
	def __init__(self):
		self.p = [0,0,0]
		self.a = 1

		self.dx = (random.random() - 0.5)
		self.dy = (random.random() - 0.5)
		
	def update(self, dt):
		self.p[0] += self.dx * dt
		self.p[1] += math.fabs(self.dy / 3 * dt)
		
		self.a -= math.fabs(self.dx * 4) * dt
		self.a -= math.fabs(self.dy / 2) * dt
		if self.a <= 0:
			self.p = [0,0,0]
			self.a = 1
			self.dx = (random.random() - 0.5)
			self.dy = (random.random() - 0.5)

	def draw(self):
		#glColor4f(1, 0.6, 0.0, self.a)
		glColor4f(0.65, 0.0, 0.15, self.a)
		glVertex3f(self.p[0], self.p[1], self.p[2])

class ParticleSystem(object):
	def __init__(self, texture, n=512, p=Particle):
		self.texture = texture		
		self.n = n
		self.particles = []

		for i in range(n):
			self.particles.append(p())

	def update(self, dt):
		for i in range(self.n):
			self.particles[i].update(dt)

	def draw(self):
		self.texture.bind()
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE)

		glEnable(GL_POINT_SPRITE)
		glPointSize(60.0)
		glTexEnvi(GL_POINT_SPRITE, GL_COORD_REPLACE, GL_TRUE);
		#glPointParameterf(GL_POINT_FADE_THRESHOLD_SIZE, 60.0);
		#glPointParameterf(GL_POINT_SIZE_MIN, 30.0);
		#glPointParameterf(GL_POINT_SIZE_MAX, 40.0);
		
		glDisable(GL_DEPTH_TEST)
		glDepthMask(GL_FALSE)
		for i in range(self.n):
			glBegin(GL_POINTS)
			self.particles[i].draw()
			glEnd()

		glDepthMask(GL_TRUE)
		glEnable(GL_DEPTH_TEST)
		glDisable(GL_POINT_SPRITE)
		glDisable(GL_BLEND)
		self.texture.release()
		glColor4f(1,1,1,1)
