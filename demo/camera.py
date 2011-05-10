"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
class CameraPath(object):
	def __init__(self, tx = 0, ty = 0, tz = 0, rx = 0, ry = 0):
		self.tx = tx
		self.ty = ty
		self.tz = tz

		self.rx = rx
		self.ry = ry
		
		self.dt = 0

	def update(self, dt, camera):
		pass

	def finished(self):
		return False

class Camera:
	def __init__(self, camera):
		self.paths = []
		self.active = None
		self.camera = camera

	def add(self, p):
		self.paths.append(p)

	def switch(self, p):
		self.active = self.paths[p]
		self.active.dt = 0
		self.camera.position(self.active.tx, self.active.ty, self.active.tz)
		self.camera.rotation(self.active.rx, self.active.ry)

	def num(self):
		return len(self.paths)

	def update(self, dt):
		if self.active != None and not self.active.finished():
			self.active.update(dt, self.camera)

	def finished(self):
		if self.active != None:
			return self.active.finished()

		return False
