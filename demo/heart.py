"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import math

from pyglet.gl import *
from sandbox.meshobj import MeshObj
from sandbox.shader import Shader

class Heart:
	def __init__(self):
		self.heart = MeshObj("media/geometry/heart.obj")
		#self.heart = MeshObj("media/geometry/apricot.obj")
		self.shader = Shader("media/shaders/heart.vert","media/shaders/heart.frag",isFile=True)
		self.shader2 = Shader("media/shaders/heart.vert",None,isFile=True)
		
		self.dt = 0
		self.beat = 0

	def on_beat(self, beat):
		self.beat += (beat.confidence / 2)
		self.dt += (beat.confidence / 3)
	
	def update(self, dt):
		self.beat += dt
		self.dt += dt

	def draw(self):
		glPushMatrix()
		glTranslatef(0,-2,0)
		glRotatef(math.sin(self.beat)*160, 0, 1, 0)

		self.shader.bind()
		self.shader["lightPos"] = [10,10,0]
		self.shader["time"] = float(self.dt)
		self.shader["beat"] = float(self.beat)
		self.heart.draw()
		self.shader.release()

		self.shader2.bind()
		self.shader2["time"] = float(self.dt)
		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
		glLineWidth(2.0)
		self.heart.draw()
		glLineWidth(1.0)
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
		self.shader2.release()

		glPopMatrix()

