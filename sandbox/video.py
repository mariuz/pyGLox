"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from pyglet import media

class Video:
	def __init__(self, filename):
		self.player = media.Player()
		self.player.queue(media.load(filename))

	def __del__(self):
		pass

	def play(self):
		self.player.play()
	
	def stop(self):
		self.player.stop()

	def bind(self):
		self.player.get_texture().blit(0,0)
