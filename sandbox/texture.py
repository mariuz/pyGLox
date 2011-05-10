"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from ctypes import *
from pyglet.gl import *
from pyglet import image

# FIXME: this needs to be re-factored
class Texture(object):
	def __init__(self,filename=None,w=None,h=None,hint=GL_LINEAR,wrap=GL_CLAMP_TO_EDGE,mipmaps=False):

		if filename != None:
			w, h, frm, img = self.load_image(filename)
		elif w != None and h != None:
			frm = "RGBA"
			l = w * h * len(frm)
			img = (GLubyte * l)(*([GLubyte(255)] * l))
		else:
			raise Exception("Cannot create texture")

		self.id = GLuint()
		glGenTextures(1, byref(self.id))
		
		glBindTexture(GL_TEXTURE_2D, self.id)
		self[GL_TEXTURE_MIN_FILTER] = hint
		self[GL_TEXTURE_MAG_FILTER] = hint
		self[GL_TEXTURE_WRAP_S] = wrap
		self[GL_TEXTURE_WRAP_T] = wrap
		glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
		
		if len(frm) == 4:
			frm = GL_RGBA
		else:
			frm = GL_RGB

		if mipmaps == True:
			self[GL_TEXTURE_MIN_FILTER] = GL_LINEAR_MIPMAP_NEAREST
			gluBuild2DMipmaps(GL_TEXTURE_2D, frm, w, h, frm, GL_UNSIGNED_BYTE, img)
		else:
			glTexImage2D(GL_TEXTURE_2D, 0, frm, w, h, 0, frm, GL_UNSIGNED_BYTE, img)

		glBindTexture(GL_TEXTURE_2D, 0)
		self.tu = 0

	def __del__(self):
		pass

	def __setitem__(self, name, value):
		glTexParameteri(GL_TEXTURE_2D, name, value)

	def load_image(self, filename):
		img = image.load(filename)
		return (img.width, img.height, img.format, img.get_image_data().get_data(img.format, img.width * len(img.format)))

	def set_texture_unit(self, i = None):
		if i != None:
			self.tu = i
		glActiveTexture(GL_TEXTURE0 + self.tu)

	def bind(self, i = 0):
		self.set_texture_unit(i)
		glBindTexture(GL_TEXTURE_2D, self.id)

	def release(self):
		self.set_texture_unit()
		glBindTexture(GL_TEXTURE_2D, 0)

