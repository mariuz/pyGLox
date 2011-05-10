"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from ctypes import *
from pyglet.gl import *
from sandbox.texture import Texture

class RenderTarget:
	def __init__(self, w, h, multisample=False, samples=4):
		self.w = w
		self.h = h
		self.texture = Texture(w=w, h=h)
		self.id = GLuint()
		self.depth_id = GLuint()

		if multisample:
			self.mid = GLuint()
			self.mcolor_id = GLuint()
			self.mdepth_id = GLuint()

			glGenFramebuffersEXT(1, byref(self.mid)) 
			glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, self.mid)
	
			glGenRenderbuffersEXT(1, byref(self.mcolor_id))
			glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, self.mcolor_id);
			glRenderbufferStorageMultisampleEXT(GL_RENDERBUFFER_EXT, samples, GL_RGBA, w, h);
			glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, GL_COLOR_ATTACHMENT0_EXT, GL_RENDERBUFFER_EXT, self.mcolor_id); 

			glGenRenderbuffersEXT(1, byref(self.mdepth_id))
			glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, self.mdepth_id);
			glRenderbufferStorageMultisampleEXT(GL_RENDERBUFFER_EXT, samples, GL_DEPTH_COMPONENT, w, h);
			glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, GL_DEPTH_ATTACHMENT_EXT, GL_RENDERBUFFER_EXT, self.mdepth_id); 

			glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, 0)
			glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0)

		else:
			self.mid = None
			self.mcolor_id = None
			self.mdepth_id = None

		glBindTexture(GL_TEXTURE_2D, self.texture.id) 

		glGenFramebuffersEXT(1, byref(self.id)) 
		glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, self.id)
		# FIXME: add support for other (or multiple) "attachment" types
		# FIXME: add support for glDrawBuffers
		# FIXME: add GL_DEPTH_COMPONENT support
		glFramebufferTexture2DEXT(GL_FRAMEBUFFER_EXT, GL_COLOR_ATTACHMENT0_EXT, GL_TEXTURE_RECTANGLE, self.texture.id, 0) 

		glGenRenderbuffersEXT(1, byref(self.depth_id))
		glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, self.depth_id);
		glRenderbufferStorageEXT(GL_RENDERBUFFER_EXT ,GL_DEPTH_COMPONENT24, w, h);
		glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, GL_DEPTH_ATTACHMENT_EXT, GL_RENDERBUFFER_EXT, self.depth_id); 

		glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, 0)
		glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0)

		glBindTexture(GL_TEXTURE_2D, 0)

	def __del__(self):
		pass

	def bind(self):
		if self.mid != None:
			glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, self.mid)
		else:
			glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, self.id)
		glPushMatrix()
		glPushAttrib(GL_VIEWPORT_BIT)                                                                                 
		glViewport(0, 0, self.w, self.h)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	def release(self):
		if self.mid != None:
			glBindFramebufferEXT(GL_READ_FRAMEBUFFER_EXT, self.mid)
			glBindFramebufferEXT(GL_DRAW_FRAMEBUFFER_EXT, self.id)
			glBlitFramebufferEXT(0, 0, self.w, self.h, 0, 0, self.w, self.h, GL_COLOR_BUFFER_BIT, GL_NEAREST)

		glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0)
		glPopAttrib()
		glPopMatrix()
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
