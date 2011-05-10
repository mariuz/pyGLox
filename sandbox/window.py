"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import sys
import datetime
import pyglet
from pyglet.gl import *
from pyglet.window import mouse
from pyglet.window import key
from ctypes import *

from sandbox.camera import Camera

class Window(pyglet.window.Window):
	def __init__(self, w = 1280, h = 720, caption = "Sandbox", multisample=False, argv=[], vsync=True, it=True):
		self.multisample = multisample
		if self.multisample:
			config = Config(sample_buffers=1,samples=4,double_buffer=True)
		else:
			config = Config(double_buffer=True)
		super(Window, self).__init__(w,h,caption,config=config)
		self.fps = pyglet.window.FPSDisplay(self)
		self.fps.label.color = (255,255,255,255)
		self.initialize()
		self.camera = Camera()
		self.keys = key.KeyStateHandler()
		self.push_handlers(self.keys)
		self.perf = False
		self.interactive = it

		self.set_exclusive_mouse(self.interactive)
		self.set_location(50,50)
		pyglet.clock.schedule(self._update)
		#pyglet.clock.schedule_interval(self._update, 1/60.0)

	def __del__(self):
		pass

	def run(self):
		pyglet.app.run()

	def initialize(self):
		glEnable(GL_NORMALIZE)
		glShadeModel(GL_SMOOTH)
		glClearDepth(1.0)
		glEnable(GL_DEPTH_TEST)
		glDepthFunc(GL_LEQUAL)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		#glEnable(GL_CULL_FACE)
		#glCullFace(GL_BACK)
		glEnable(GL_TEXTURE_2D)
		glEnable(GL_COLOR_MATERIAL)
		glClearColor(0.1,0.1,0.1,1.0)

		if self.multisample:
			glEnable(GL_MULTISAMPLE)
		
			buffers = c_int()
			samples = c_int()
			glGetIntegerv(GL_SAMPLE_BUFFERS, byref(buffers));
			glGetIntegerv(GL_SAMPLES, byref(samples));
			print("GL_SAMPLE_BUFFERS: %d / GL_SAMPLES %d samples" % (buffers.value, samples.value));

			glEnable(GL_LINE_SMOOTH)
			glEnable(GL_POINT_SMOOTH)
			glEnable(GL_POLYGON_SMOOTH)

	def resize(self, w, h):
		glViewport(0, 0, w, h)
	
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
	
		gluPerspective(45.0,w/float(h),0.1,1000.0)
	
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def update(self, dt):
		pass

	def draw(self):
		pass

	def on_mouse_motion(self, x, y, dx, dy):
		if self.interactive:
			self.camera.rotateX(dy * 0.1)
			self.camera.rotateY(dx * -0.1)
	
	def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
		if buttons and mouse.LEFT and not self.interactive:
			self.camera.rotateX(dy * 0.1)
			self.camera.rotateY(dx * -0.1)

	def on_key_press(self, symbol, modifiers):
		super(Window, self).on_key_press(symbol, modifiers)

		if symbol == key.F12:
			glPixelTransferf(GL_ALPHA_BIAS, 1.0)
			image = pyglet.image.ColorBufferImage(0, 0, self.width, self.height)
			image.save(datetime.datetime.now().strftime('screenshot_%Y-%m-%d_%H:%M:%S.%f.png'))
			glPixelTransferf(GL_ALPHA_BIAS, 0.0)
			#pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot.png')
		elif symbol == key.P:
			self.perf = not self.perf
		elif symbol == key.F:
			self.set_fullscreen(not self.fullscreen)
		elif symbol == key.I:
			self.interactive = not self.interactive
			self.set_exclusive_mouse(self.interactive)

		return pyglet.event.EVENT_HANDLED

	def on_resize(self, w, h):
		self.resize(w,h)
		return pyglet.event.EVENT_HANDLED

	def on_draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		self.camera.update()
		self.draw()
		if self.perf == True:
			self.fps.draw()

	def _update(self, dt):
		self._update_keys(dt)
		self.update(dt)

	def _update_keys(self, dt):
		if self.keys[key.W]:
			self.camera.move(-0.1)
		elif self.keys[key.S]:
			self.camera.move(0.1)

		if self.keys[key.D]:
			self.camera.strafe(0.1)
		elif self.keys[key.A]:
			self.camera.strafe(-0.1)
