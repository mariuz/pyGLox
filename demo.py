#!/usr/bin/env python
"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import sys
import math
import random
from pyglet.gl import *
from pyglet.window import key

from sandbox.window import Window
from sandbox import main
from sandbox.audio import AudioDevice, AudioStream

from demo.spherecubes import SphereCubes
from demo.lightbeams import LightBeams
from demo.heart import Heart
from demo.flowergardens import FlowerGardens
from demo.gears import Gears
from demo.overlay import Overlay
from demo.postprocess import PostProcess
from demo.camera import Camera
from demo.camerapaths import *

class Demo(Window):
	def __init__(self, argv):
		super(Demo, self).__init__(caption="-== Demo ==-", argv=argv, multisample=True, it=False,w=1280,h=464)
		glClearColor(0.7,0.1,0.1,1)

		self.audiodevice = AudioDevice()
		#self.audio = AudioStream("media/music/grapes_-_I_dunno.mp3")
		#self.audio = AudioStream("media/music/vincenzo_-_compofiller_94.ogg")
		self.audio = AudioStream("media/music/sinatra-electric_gumpop.mp3")

		self.cam = Camera(self.camera)
		self.cam.add(CameraPathOne())
		self.cam.add(CameraPathTwo())
		self.cam.add(CameraPathThree())
		self.cam.add(CameraPathFour())
		self.cam.add(CameraPathFive())
		self.cam.add(CameraPathSix())
		self.cam.add(CameraPathSeven())
		self.cam.add(CameraPathEight())
		self.cam.add(CameraPathNine())

		self.pp = PostProcess(self.width, self.height)
		self.ss = SphereCubes()
		self.lb = LightBeams()

		self.ht = Heart()
		self.audio.subscribe(self.ht.on_beat)
		
		self.fg = FlowerGardens()
		self.audio.subscribe(self.fg.on_beat)

		self.gs = Gears()
		self.audio.subscribe(self.gs.on_beat)

		self.ov = Overlay()

		self.cam.switch(0)
		self.audio.play()
		
	def __del__(self):
		self.audio.__del__()
		self.audiodevice.__del__()
		super(Demo, self).__del__()

	def random_cam(self):
		self.cam.switch(int(random.random() * self.cam.num()))

	def random_post(self):
		self.pp.switch(int(random.random() * self.pp.num()))

	def update(self, dt):
		self.audio.update(dt, 0.85)
		
		self.pp.update(dt)
		self.update_scene(dt)

		if self.keys[key._0]:
			self.random_post()
		elif self.keys[key._1]:
			self.pp.switch(0)
		elif self.keys[key._2]:
			self.pp.switch(1)
		elif self.keys[key._3]:
			self.pp.switch(2)
		elif self.keys[key._4]:
			self.pp.switch(3)
		elif self.keys[key._5]:
			self.pp.switch(4)

		if self.keys[key.NUM_0]:
			self.random_cam()
		elif self.keys[key.NUM_1]:
			self.cam.switch(0)
		elif self.keys[key.NUM_2]:
			self.cam.switch(1)
		elif self.keys[key.NUM_3]:
			self.cam.switch(2)
		elif self.keys[key.NUM_4]:
			self.cam.switch(3)
		elif self.keys[key.NUM_5]:
			self.cam.switch(4)
		elif self.keys[key.NUM_6]:
			self.cam.switch(5)
		elif self.keys[key.NUM_7]:
			self.cam.switch(6)
		elif self.keys[key.NUM_8]:
			self.cam.switch(7)
		elif self.keys[key.NUM_9]:
			self.cam.switch(8)

		if not self.interactive:
			self.cam.update(dt)
			if self.cam.finished():
				self.random_cam()
				#self.random_post()

	def update_scene(self, dt):
		self.ht.update(dt)
		self.ss.update(dt)
		self.gs.update(dt)
		self.fg.update(dt)
		self.lb.update(dt)

	def draw_scene(self):
		glTranslatef(0,0,-16)
		self.ht.draw()
		self.ss.draw()
		self.gs.draw()
		self.fg.draw()
		self.lb.draw()

	def draw_overlay(self):
		self.ov.draw()

	def draw(self):
		self.pp.bind()
		self.draw_scene()
		if self.pp.current() == 3:
			self.draw_overlay()
		self.pp.release()
		self.pp.draw()

		if self.pp.current() != 3:
			self.draw_overlay()

if __name__ == "__main__":
	main.run(sys.argv, Demo)
