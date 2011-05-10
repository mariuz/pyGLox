"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from pyglet.gl import *
from sandbox.texture import Texture
from sandbox.meshcube import MeshCube

class Skybox(MeshCube):
	def __init__(self, x=16, y=16, z=16):
		super(Skybox, self).__init__(x,y,z)

		self.faces = [
		[0,2,1,0,3,2],			# 0
		[4,6,5,4,7,6],			# 1
		[8,10,9,8,11,10],		# 2
		[12,14,13,12,15,14],	# 3
		[16,18,17,16,19,18],	# 4
		[20,22,21,20,23,22]]	# 5

		for f in range(len(self.faces)):
			self.faces[f] = self.create_list(self.create_indices(self.faces[f]))

		self.textures = {}

	def draw(self):
		self.textures['front'].bind()
		glCallList(self.faces[0])
		self.textures['back'].bind()
		glCallList(self.faces[1])
		self.textures['left'].bind()
		glCallList(self.faces[2])
		self.textures['right'].bind()
		glCallList(self.faces[3])
		self.textures['top'].bind()
		glCallList(self.faces[4])
		self.textures['bottom'].bind()
		glCallList(self.faces[5])
		self.textures['bottom'].release()

	def __setitem__(self, name, value):
		if isinstance(value, Texture):
			self.textures[name] = value
		elif isinstance(value, str):
			if name == 'init':
				for f in ['back','front','left','right','top','bottom']:
					self[f] = value % f
			else:
				self.textures[name] = Texture(value)
		else:
			raise TypeError('Trying to set a non-texture')
