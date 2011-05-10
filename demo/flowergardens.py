"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import random
from pyglet.gl import *

from sandbox.meshcube import MeshCube
from sandbox.shader import Shader
from sandbox.texture import Texture

class FlowerGardens:
	def __init__(self, n=32, f=6):
		self.n = n # number of floating platforms (a.k.a gardens)
		self.f = f # maximum number of flowers per platform

		self.platforms = []
		self.flowers = []

		for i in range(self.n):
			nx = (random.random() * 5) - random.random() * 1
			ny = (random.random() * 5)
			nz = (random.random() * 5) - random.random() * 1
			self.platforms.append(MeshCube(0.1,0.02,0.1,tx=nx,ty=ny,tz=nz))
			self.flowers.extend(self.create_flowers(nx, ny+0.02, nz))

		self.flowertexture = Texture("media/textures/flare2.png")

		self.flowerlistid = glGenLists(1)
		glNewList(self.flowerlistid, GL_COMPILE)
		glColor4f(0.0,0.4,0.8,1)
		for f in self.flowers:
			i = 0
			glLineWidth(1.5)
			glBegin(GL_LINE_STRIP)
			for s in range(f['n']):
				glNormal3f(f['n'],float(i),float(f['d']))
				glVertex3f(f['x'],f['y']+(s*0.1),f['z'])
				i+=1
			glEnd()
		glColor4f(1,1,1,1)
		glEndList()

		self.flowerlistid2 = glGenLists(1)
		glNewList(self.flowerlistid2, GL_COMPILE)
		glColor4f(1,1,1,1)
		for f in self.flowers:
			i = 0
			glPointSize(20.0)
			glBegin(GL_POINTS)
			for s in range(f['n']):
				glNormal3f(f['n'],float(i),float(f['d']))
				glVertex3f(f['x'],f['y']+(s*0.1),f['z'])					
				i+=1
			glEnd()
		glEndList()

		self.platformshader = Shader("media/shaders/spherecubes.vert", "media/shaders/spherecubes.frag", isFile=True)
		self.flowershader = Shader("media/shaders/flowers.vert", None, isFile=True)

		self.dt = 0

	def create_flowers(self, x, y, z):
		flowers = []
		dx = x
		dy = y
		dz = z
		
		dn = random.random() * self.f
		while dn < 3:
			dn = random.random() * self.f

		d = random.random() - 0.5

		flowers.append({'x':dx-0.05,'y':dy,'z':dz-0.05,'n':int(dn),'d':d})

		dn = random.random() * self.f
		while dn < 3:
			dn = random.random() * self.f

		d = random.random() - 0.5

		flowers.append({'x':dx-0.05,'y':dy,'z':dz+0.05,'n':int(dn),'d':d})

		dn = random.random() * self.f
		while dn < 3:
			dn = random.random() * self.f

		d = random.random() - 0.5

		flowers.append({'x':dx,'y':dy,'z':dz,'n':int(dn),'d':d})
		
		dn = random.random() * self.f
		while dn < 3:
			dn = random.random() * self.f

		d = random.random() - 0.5

		flowers.append({'x':dx+0.05,'y':dy,'z':dz-0.05,'n':int(dn),'d':d})
		
		dn = random.random() * self.f
		while dn < 3:
			dn = random.random() * self.f

		d = random.random() - 0.5

		flowers.append({'x':dx+0.05,'y':dy,'z':dz+0.05,'n':int(dn),'d':d})

		return flowers

	def on_beat(self, beat):
		self.dt += (beat.confidence / 3)

	def update(self, dt):
		self.dt += dt

	def draw(self):
		glPushMatrix()
		glTranslatef(-2,-3,-2)

		self.platformshader.bind()
		self.platformshader["lightPos"] = [10,10,0]

		for p in self.platforms:
			p.draw()

		self.platformshader.release()

		self.flowershader.bind()
		self.flowershader["time"] = float(self.dt)

		glCallList(self.flowerlistid)
	
		glEnable(GL_POINT_SPRITE)
		glPointSize(50.0)
		glTexEnvi(GL_POINT_SPRITE, GL_COORD_REPLACE, GL_TRUE);

		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE)
		glDepthMask(GL_FALSE)
		self.flowertexture.bind()
		glCallList(self.flowerlistid2)
		self.flowertexture.release()
		glDepthMask(GL_TRUE)
		glDisable(GL_BLEND)
		glDisable(GL_POINT_SPRITE)

		self.flowershader.release()

		glPopMatrix()
