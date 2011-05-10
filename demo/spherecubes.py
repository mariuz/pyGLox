"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import math
from sandbox.shader import Shader
from sandbox.meshcube import MeshCube

# Source: http://stackoverflow.com/questions/477486/python-decimal-range-step-value
def frange(start,end,step):
	return map(lambda x: x*step, range(int(start*1./step),int(end*1./step)))

class SphereCubes:
	def __init__(self):
		self.cubes = []
		
		alpha_inc = math.pi / 20.0
		theta_inc = math.pi / 20.0
		pip2 = math.pi / 2.0
		pi2 = math.pi * 2

		for alpha in frange(-pip2, pip2, alpha_inc):
			for theta in frange(0, pi2, theta_inc):
				nx =  math.cos(alpha) * math.sin(theta) * 6.0;  
				ny =  math.cos(alpha) * math.cos(theta) * 6.0;
				nz = -math.sin(alpha) * 6.0
				self.cubes.append(MeshCube(0.275,0.275,0.275,tx=nx,ty=ny,tz=nz))

		self.shader = Shader("media/shaders/spherecubes.vert","media/shaders/spherecubes.frag",isFile=True)

	def draw(self):
		self.shader.bind()
		self.shader["lightPos"] = [1,1,0]
		
		for cube in self.cubes:
			cube.draw()

		self.shader.release()

	def on_beat(self, dt):
		pass

	def update(self, dt):
		pass
