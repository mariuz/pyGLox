"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import os
from bass import *
from collections import namedtuple
from pyglet import media

AudioBeat = namedtuple('AudioBeat',['kind','start','end','duration','confidence'])

class AudioDevice:
	def __init__(self):
		if HIWORD(BASS_GetVersion()) != BASSVERSION:
			print('An incorrect version of BASS was loaded')

		if not BASS_Init(-1, 44000, 0, None, None):
			print('Can\'t initialize device')

	def __del__(self):
		BASS_Free()

class AudioStream:
	def __init__(self, filename):
		self.beats = []
		self.num_beats = 0
		self.last_beat = -1
		self.subscribers = []
		self.filename = filename
		self.load_beats(filename)

		self.handle = BASS_StreamCreateFile(False, filename, 0, 0, 0)
		self.dt = 0

	def __del__(self):
		BASS_StreamFree(self.handle)

	def update(self, dt, confidence):
		if self.playing():
			time = self.position()
			for i in range(self.last_beat, self.num_beats):
				b = self.beats[i]
				if time >= b.start and time <= b.end and b.confidence > confidence:
					if self.last_beat != i:
						self.last_beat = i
						self.emit(b)

					break

	def emit(self, beat):
		for s in self.subscribers:
			s(beat)

	def subscribe(self, fn):
		self.subscribers.append(fn)

	def position(self):
		return BASS_ChannelBytes2Seconds(self.handle, BASS_ChannelGetPosition(self.handle, BASS_POS_BYTE))

	def playing(self):
		return BASS_ChannelIsActive(self.handle)

	def play(self):
		BASS_ChannelPlay(self.handle,False)
	
	def pause(self):
		BASS_ChannelPause(self.handle)

	def stop(self):
		BASS_ChannelStop(self.handle)

	def load_beats(self, filename):
		beatsfilename = "%s.beats" % filename
		if os.path.exists(beatsfilename):
			with open(beatsfilename) as f:
				for line in f.readlines():
					kind, start, end, duration, confidence = line.split(" ")
					
					beat = AudioBeat(kind=kind, 
									 start=float(start), 
									 end=float(end), 
									 duration=float(duration),
									 confidence=float(confidence))

					self.beats.append(beat)

			self.num_beats = len(self.beats)
