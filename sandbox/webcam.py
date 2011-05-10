"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import opencv
from opencv import highgui
from pyglet.gl import *
from pyglet import image
import Image
from sandbox.texture import Texture

class WebCam(Texture):
	def __init__(self, w=512, h=512):
		super(WebCam, self).__init__(w=w,h=h,frm=None)
		self.camera = highgui.cvCreateCameraCapture(0)
		print('Initializing WebCam ...')

	def __del__(self):
		highgui.cvReleaseCapture(self.camera)
		print('Releasing WebCam ...')

	def bind(self):
		super(WebCam, self).bind()
		self.grab_frame().blit_to_texture(GL_TEXTURE_2D, 0, 0, 0, 0)

	def grab_frame(self):
		cv_img = highgui.cvQueryFrame(self.camera)
		pil_img = opencv.adaptors.Ipl2PIL(cv_img).resize([self.texture.width,self.texture.height])
		width, height = pil_img.size
		return  image.ImageData(width, height, pil_img.mode, pil_img.tostring()) 
