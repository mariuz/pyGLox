"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from pyglet.gl import *

from sandbox.meshquad import MeshQuad
from sandbox.texture import Texture
from sandbox.shader import Shader

class Overlay:
	def __init__(self):
		self.quad = MeshQuad()
		self.texture = Texture("media/textures/border4.png")
		#self.texture = Texture("media/textures/flare.png")
		self.shader = Shader("media/shaders/overlay.vert", "media/shaders/overlay.frag", isFile=True)

	def on_beat(self, dt):
		pass

	def update(self, dt):
		pass

	def draw(self):
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		#glBlendFunc(GL_SRC_ALPHA, GL_ONE)
		#glDepthMask(GL_FALSE)
		#glDisable(GL_DEPTH_TEST)
		self.texture.bind()
		self.shader.bind()
		glPushMatrix()
		glLoadIdentity()
		self.quad.draw()
		glPopMatrix()
		self.shader.release()
		self.texture.release()
		#glEnable(GL_DEPTH_TEST)
		#glDepthMask(GL_TRUE)
		glDisable(GL_BLEND)
