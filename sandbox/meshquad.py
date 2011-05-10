"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from sandbox.mesh import Mesh

class MeshQuad(Mesh):
	def __init__(self, x=1, y=1):
		self.vertices = [
			-x, -y, 0,
			 x, -y, 0,
			 x,  y, 0,
			-x,  y, 0 ]

		self.normals = [
			 0, 0, 1,
			 0, 0, 1,
			 0, 0, 1,
			 0, 0, 1 ]
	
		self.texcoords = [
			 0, 0,
			 1, 0,
			 1, 1,
			 0, 1 ]

		self.indices = [
			 3, 2, 1,
			 3, 1, 0 ]
		
		super(MeshQuad, self).__init__()
