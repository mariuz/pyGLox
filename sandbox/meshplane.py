"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from sandbox.mesh import Mesh

class MeshPlane(Mesh):
	def __init__(self, w=10, h=10, vertical=False):
		self.vertices = []
		self.indices = []
		self.texcoords = []
		self.normals = []

		nv = 0
		if vertical:
			for y in range(h):
				y2 = -h + (y * 2)
				for x in range(w):
					x2 = -w + (x * 2)

					self.vertices.extend([-1 + x2, 1 + y2, 0,
										   1 + x2, 1 + y2, 0,
										   1 + x2,-1 + y2, 0,
										  -1 + x2,-1 + y2, 0])

					self.normals.extend([0,0,1,
										 0,0,1,
										 0,0,1,
										 0,0,1])
			
					self.texcoords.extend([0,1,
										   1,1,
										   1,0,
										   0,0])

					self.indices.extend([nv + 0, nv + 1, nv + 2,
										 nv + 0, nv + 2, nv + 3])

					nv += 4
		else:
			for z in range(h):
				z2 = -h + (z * 2)
				for x in range(w):
					x2 = -w + (x * 2)

					self.vertices.extend([-1 + x2, 0,  1 + z2,
										   1 + x2, 0,  1 + z2,
										   1 + x2, 0, -1 + z2,
										  -1 + x2, 0, -1 + z2 ])
	
					self.normals.extend([0,1,0,
										 0,1,0,
										 0,1,0,
										 0,1,0])
			
					self.texcoords.extend([0,0,
										   1,0,
										   1,1,
										   0,1])

					self.indices.extend([nv + 0, nv + 1, nv + 2,
										 nv + 0, nv + 2, nv + 3])

					nv += 4

		super(MeshPlane, self).__init__()
