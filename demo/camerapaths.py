"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import math
from demo.camera import CameraPath

class CameraPathOne(CameraPath):
	def __init__(self):
		super(CameraPathOne, self).__init__(tx=2,ty=3,tz=-19,rx=-37,ry=160)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(-dt * 20.0)
		camera.move(-dt * 0.5)
		camera.strafe(-dt * 1.5)

		if(self.dt > 6 and self.dt < 10):
			camera.rotateX(dt * 10.0)

		if(self.dt > 10 and self.dt < 13):
			camera.rotateX(-dt * 5.0)

		if(self.dt > 20 and self.dt < 30):
			camera.rotateX(dt * 2.0)

		if(self.dt > 30):
			camera.rotateX(-dt * 2.0)

	def finished(self):
		return self.dt > 40

class CameraPathTwo(CameraPath):
	def __init__(self):
		super(CameraPathTwo, self).__init__(tx=3,ty=0,tz=-13,rx=-5,ry=52)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(-dt * 20.0)
		camera.strafe(-dt * 1.5)

	def finished(self):
		return self.dt > 40

class CameraPathThree(CameraPath):
	def __init__(self):
		super(CameraPathThree, self).__init__(tx=2,ty=2,tz=-13,rx=-35,ry=52)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(math.sin(dt * 20.0)*2)
		camera.strafe(math.sin(dt * 1.2)*2)

	def finished(self):
		return self.dt > 30

class CameraPathFour(CameraPath):
	def __init__(self):
		super(CameraPathFour, self).__init__(tx=3,ty=-2.2,tz=-19,rx=20,ry=138)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(dt * 30.0)
		camera.strafe(dt * 1.6)
		camera.move(-dt * 0.5)

		if(self.dt > 10 and self.dt < 11):
			camera.rotateX(-dt * 15.0)

	def finished(self):
		return self.dt > 25

class CameraPathFive(CameraPath):
	def __init__(self):
		super(CameraPathFive, self).__init__(tx=0,ty=0,tz=-22,rx=-4,ry=177)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(dt * 25.0)
		camera.strafe(dt * 1.5)
		
		if(self.dt < 2):
			camera.move(-dt * 2.0)

	def finished(self):
		return self.dt > 25

class CameraPathSix(CameraPath):
	def __init__(self):
		super(CameraPathSix, self).__init__(tx=2,ty=3,tz=-14,rx=-49,ry=421)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(dt * 20.0)
		camera.strafe(dt * 1.5)

		camera.move(math.sin(-dt * 1.2)*0.2)
		
		if(self.dt > 10 and self.dt < 13):
			camera.rotateX(dt * 10)

	def finished(self):
		return self.dt > 20

class CameraPathSeven(CameraPath):
	def __init__(self):
		super(CameraPathSeven, self).__init__(tx=2,ty=-1,tz=-16,rx=18,ry=84)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(dt * 20.0)
		camera.strafe(dt * 1.5)

		if(self.dt < 2):
			camera.move(dt * 1.5)

		if(self.dt > 5 and self.dt < 7):
			camera.move(-dt * 1.0)

	def finished(self):
		return self.dt > 30

class CameraPathEight(CameraPath):
	def __init__(self):
		super(CameraPathEight, self).__init__(tx=2,ty=-1,tz=-16,rx=18,ry=84)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(-dt * 20.0)
		camera.strafe(-dt * 1.5)

		if(self.dt < 2):
			camera.move(dt * 1.5)

		if(self.dt > 5 and self.dt < 7):
			camera.move(-dt * 1.0)

	def finished(self):
		return self.dt > 30

class CameraPathNine(CameraPath):
	def __init__(self):
		super(CameraPathNine, self).__init__(tx=1,ty=1,tz=-13,rx=-20,ry=-360)

	def update(self, dt, camera):
		self.dt += dt
		camera.rotateY(-dt * 20.0)
		camera.strafe(-dt * 1.5)

		camera.move(math.sin(-dt * 1.1)*0.1)
		
		if(self.dt > 10 and self.dt < 13):
			camera.rotateX(dt * 6)

	def finished(self):
		return self.dt > 25

