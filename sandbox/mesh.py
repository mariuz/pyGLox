"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from pyglet.gl import *

# FIXME: this is not very DRY but it does the job for now :P

class Mesh(object):
	def __init__(self, hint=GL_TRIANGLES, do_list=True):
		self.vertices = (GLfloat * len(self.vertices))(*self.vertices)
		self.normals = (GLfloat * len(self.normals))(*self.normals)
		self.texcoords = (GLfloat * len(self.texcoords))(*self.texcoords)
		self.indices = (GLuint * len(self.indices))(*self.indices)
		self.numindices = len(self.indices)

		self.hint = hint

		if do_list == True:
			self.id = self.create_list()
		else:
			self.id = 0

	def __del__(self):
		pass

	def draw(self):
		glCallList(self.id)

	def draw_instance(self, x=0, y=0, z=0):
		glPushMatrix()
		glTranslatef(x,y,z)
		glDrawElements(self.hint, self.numindices, GL_UNSIGNED_INT, self.indices)
		glPopMatrix()

	def bind(self):
		glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
		glEnableClientState(GL_VERTEX_ARRAY)
		glEnableClientState(GL_TEXTURE_COORD_ARRAY)
		glEnableClientState(GL_NORMAL_ARRAY)
		glVertexPointer(3, GL_FLOAT, 0, self.vertices)
		glTexCoordPointer(2, GL_FLOAT, 0, self.texcoords)
		glNormalPointer(GL_FLOAT, 0, self.normals)

	def release(self):
		glPopClientAttrib()

	def create_list(self, indices=None):
		id = glGenLists(1)                                                                                     
		glNewList(id, GL_COMPILE)
		self.bind()
		if indices == None:
			glDrawElements(self.hint, self.numindices, GL_UNSIGNED_INT, self.indices)
		else:
			glDrawElements(self.hint, len(indices), GL_UNSIGNED_INT, indices)
		self.release()
		glEndList()
		
		return id

	def create_indices(self, indices):
		return (GLuint * len(indices))(*indices)
