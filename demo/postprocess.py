"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from sandbox.rendertarget import RenderTarget
from sandbox.shader import Shader
from sandbox.texture import Texture
from sandbox.meshquad import MeshQuad

class PostProcess:
	def __init__(self, w=1024, h=1024):
		self.quad = MeshQuad()
		self.shader = Shader("media/shaders/postprocess.vert", "media/shaders/postprocess.frag", isFile=True)
		self.rt = RenderTarget(w,h,multisample=True)
		self.dt = 0
		self.mode = 0
		self.texture = Texture("media/textures/gradient.png")

	def on_beat(self, beat):
		pass

	def switch(self, n):
		self.mode = n

	def current(self):
		return self.mode

	def num(self):
		return 6

	def bind(self):
		if self.mode == 0:
			return

		self.rt.bind()

	def release(self):
		if self.mode == 0:
			return

		self.rt.release()

	def update(self, dt):
		self.dt += dt

	def draw(self):
		if self.mode == 0:
			return

		self.rt.texture.bind()
		self.shader.bind()
		self.shader["time"] = float(self.dt)
		self.shader["rt_w"] = float(self.rt.w)
		self.shader["rt_h"] = float(self.rt.h)
		self.shader["mode"] = float(self.mode)
		self.shader["texture2"] = int(1)
		self.texture.bind(1)
		self.quad.draw()
		self.texture.release()
		self.shader.release()
		self.rt.texture.release()
