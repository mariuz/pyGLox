"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import random
from pyglet.gl import *

from sandbox.texture import Texture
from sandbox.shader import Shader

class LightBeams:
	def __init__(self,n=512):
		self.texture = Texture("media/textures/flare3.png")
		#self.texture = Texture("media/textures/heart.tga")
		self.shader = Shader("media/shaders/beams.vert",fs=None,isFile=True)

		self.beams = []
		self.n = n

		for i in range(self.n):
			self.beams.append([random.random() * 10, random.random() * 10, random.random() * 10])

		self.beamlistid = glGenLists(1)
		glNewList(self.beamlistid, GL_COMPILE)
		glBegin(GL_POINTS)
		for i in range(self.n):
			glVertex3f(	self.beams[i][0],
						self.beams[i][1],
						self.beams[i][2] )
		glEnd()
		glEndList()

		self.dt = 0

	def on_beat(self, beat):
		pass

	def update(self, dt):
		self.dt += dt
		
	def draw(self):
		#glColor4f(0.9,0.1,0.1,1)
		self.texture.bind()
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE)

		glEnable(GL_POINT_SPRITE)
		glPointSize(60.0)
		glTexEnvi(GL_POINT_SPRITE, GL_COORD_REPLACE, GL_TRUE);
		#glPointParameterf(GL_POINT_FADE_THRESHOLD_SIZE, 60.0);
		#glPointParameterf(GL_POINT_SIZE_MIN, 30.0);
		#glPointParameterf(GL_POINT_SIZE_MAX, 40.0);
		
		glDepthMask(GL_FALSE)
		glPushMatrix()
		glTranslatef(-5,-5,-5)
		self.shader.bind()
		self.shader["time"] = float(self.dt)
		glCallList(self.beamlistid)
		self.shader.release()
		glPopMatrix()
		glDepthMask(GL_TRUE)
		glDisable(GL_POINT_SPRITE)
		glDisable(GL_BLEND)
		self.texture.release()
		glColor4f(1,1,1,1)

		self.beat = False
