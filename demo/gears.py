"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import math

from pyglet.gl import *

from sandbox.meshcube import MeshCube
from sandbox.shader import Shader

class Gears:
	def __init__(self,r=10):
		self.cubes = []

		for i in range(100):
			nx = math.sin(180*i)
			ny = math.cos(180*i)
			nz = 0
			self.cubes.append(MeshCube(0.02,0.02,0.02,tx=nx,ty=ny,tz=nz))

		self.dt = 0
		self.beat_dt = 0
		self.r = 0
		self.r2=0

		self.shader = Shader("media/shaders/gears.vert","media/shaders/gears.frag",isFile=True)

	def on_beat(self, beat):
		self.beat_dt += beat.confidence

	def update(self, dt):
		self.r += dt * 60
		self.r2-= dt * 80
		self.dt+= dt

	def draw(self):
		self.shader.bind()
		self.shader["lightPos"] = [5,2,0]
		self.shader["time"] = float(self.dt)
		self.shader["beat"] = float(self.beat_dt)
		glPushMatrix()
		glScalef(2.8,2.8,2.8)
		glRotatef(self.r, 1, 1, 1)
		for c in self.cubes:
			c.draw()
		glPopMatrix()
		glPushMatrix()
		glScalef(2.5,2.5,2.5)
		glRotatef(self.r2, 1, 1, 1)
		for c in self.cubes:
			c.draw()
		glPopMatrix()
		self.shader.release()
