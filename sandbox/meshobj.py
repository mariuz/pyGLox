"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import re
from sandbox.mesh import Mesh
from sandbox.math import Vec3

class MeshObj(Mesh):
	def __init__(self, filename):
		"""
			Original source:
				http://www.vivahate.com/2009/10/15/obj-loader/

			Added:
				+ masturbate with "generators"
				+ handle faces "f i/n/t i/n/t i/n/t"
				+ triangulate quads
				+ calculate per-vertex normals
		"""
		self.vertices = []
		self.indices = []
		self.normals = None
		
		fp = open(filename, 'r')
		regexp = re.compile(r'([^\s]+)')
		for line in fp.readlines():
			if line[0] == '#': continue # skip comments
			tokens = regexp.findall(line)
			if tokens:
				if tokens[0] == 'v':
					v = tokens[1:]
					self.vertices.extend([float(v[i]) for i in range(len(v))])
				if tokens[0] == 'f':
					if self.normals == None:
						self.normals = [float(0)] * len(self.vertices)

					f = tokens[1:]
					# 0..N-1
					f = [int(f[i].split("/")[0])-1 for i in range(len(f))]
				
					if len(f) == 4:
						self.indices.extend([f[0], f[1], f[2], f[0], f[2], f[3]])
						self.process_normal(f[0], f[1], f[2])
						self.process_normal(f[0], f[2], f[3])
					else:
						self.indices.extend(f)
						self.process_normal(f[0], f[1], f[2])

		fp.close()

		for n in range(len(self.normals) / 3):
			self.normalize(n)

		# TODO: read tex-coords
		self.texcoords = [float(0)] * len(self.vertices)

		super(MeshObj, self).__init__()

	# FIXME: these should be part of the base Mesh class
	def indice(self, idx):
		""" Returns the indice at the specified index """
		offset = idx * 3
		return [self.indices[offset + 0],
				self.indices[offset + 1],
				self.indices[offset + 2]]

	def vertex(self, idx):
		""" Returns the vertex at the specified index """
		offset = idx * 3
		return [self.vertices[offset + 0],
				self.vertices[offset + 1],
				self.vertices[offset + 2]]

	def normal(self, idx):
		""" Returns the normal at the specified index """
		offset = idx * 3
		return [self.normals[offset + 0],
				self.normals[offset + 1],
				self.normals[offset + 2]]

	def process_normal(self, f1, f2, f3):
		""" Generate and process per-vertex normals for a given face """
		n = self.gen_normal(f1,f2,f3)
		self.add_normal(f1, n)
		self.add_normal(f2, n)
		self.add_normal(f3, n)

	def gen_normal(self, f1, f2, f3):
		""" Calculate the normal vector for a face """
		v1 = self.vertex(f1)
		v2 = self.vertex(f2)
		v3 = self.vertex(f3)

		vv1 = Vec3.sub(v2,v1)
		vv2 = Vec3.sub(v3,v1)

		return Vec3.cross(vv1,vv2)

	def add_normal(self, idx, n):
		""" Adds another normal to this normal """
		offset = idx * 3
		self.normals[offset + 0] += n[0]
		self.normals[offset + 1] += n[1]
		self.normals[offset + 2] += n[2]

	def normalize(self, idx):
		""" Normalizes a normal """
		n = Vec3.normalize(self.normal(idx))

		offset = idx * 3
		self.normals[offset + 0] = n[0]
		self.normals[offset + 1] = n[1]
		self.normals[offset + 2] = n[2]
