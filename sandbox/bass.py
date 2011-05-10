"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import sys
import os
import time
from ctypes import cdll, c_ulong, c_int64, c_double, CFUNCTYPE

# TODO: take care of Windows, OSX, etc.	
libbass = cdll.LoadLibrary('libbass.so')

BASSVERSION = 0x204	# API version
BASSVERSIONTEXT = '2.4'

# BASS_ChannelGetLength/GetPosition/SetPosition modes
BASS_POS_BYTE           = 0 # byte position
BASS_POS_MUSIC_ORDER    = 1 # order.row position, MAKELONG(order,row)

HIWORD = lambda x: (x >> 16) & 0xffff
LOWORD = lambda x: (x & 0xFFFF)
	
def BASS_GetVersion():
	return libbass.BASS_GetVersion()
	
def BASS_Init(device, freq, flags, win, clsid):
	return libbass.BASS_Init(device, freq, flags, win, clsid)
	
def BASS_Free():
	return libbass.BASS_Free()

def BASS_Play():
	return libbass.BASS_Play()
	
def BASS_Stop():
	return libbass.BASS_Stop()
	
def BASS_Pause():
	return libbass.BASS_Pause()	
	
def BASS_SetVolume(volume):
	return libbass.BASS_SetVolume(volume)
	
def BASS_GetVolume():
	return libbass.BASS_GetVolume()
		
def BASS_StreamCreateFile(mem, f, offset, length, flags):
	return libbass.BASS_StreamCreateFile(mem, f, offset, length, flags)
	
def BASS_StreamFree(handle):
	return libbass.BASS_StreamFree(handle)
	
def BASS_ChannelPlay(handle, restart):
	return libbass.BASS_ChannelPlay(handle, restart)

def BASS_ChannelStop(handle):
	return libbass.BASS_ChannelStop(handle)

def BASS_ChannelPause(handle):
	return libbass.BASS_ChannelPause(handle)
	
def BASS_ChannelIsActive(handle):
	return libbass.BASS_ChannelIsActive(handle)
	
def BASS_ChannelGetLength(handle, mode):
	return libbass.BASS_ChannelGetLength(handle, mode)
	
def BASS_ChannelSetPosition(handle, pos, mode):
	return libbass.BASS_ChannelSetPosition(handle, pos, mode)

def BASS_ChannelGetPosition(handle, mode):
	return libbass.BASS_ChannelGetPosition(handle, mode)
	
#def BASS_ChannelBytes2Seconds(handle, pos):
#	return libbass.BASS_ChannelBytes2Seconds(handle, pos)

BASS_ChannelBytes2Seconds = CFUNCTYPE(c_double, c_ulong, c_int64)(('BASS_ChannelBytes2Seconds', libbass))

def main(argv):
	if len(argv) < 1:
		print('usage: python bass.py filename')
		return 1
	
	filename = argv[0]
	if not os.path.exists(filename):
		print('%s doesn\'t exist' % filename)
		return 1
	
	if HIWORD(BASS_GetVersion()) != BASSVERSION:
		print('An incorrect version of BASS was loaded')
		return 1

	if not BASS_Init(-1, 44000, 0, None, None):
		print('Can\'t initialize device')
		return 1
	
	handle = BASS_StreamCreateFile(False, filename, 0, 0, 0)
	BASS_ChannelPlay(handle,False)
	
	playing = True
	while playing and BASS_ChannelIsActive(handle):
		try:
			pos = BASS_ChannelGetPosition(handle, BASS_POS_BYTE)
			length = BASS_ChannelGetLength(handle, BASS_POS_BYTE)
			
			p = BASS_ChannelBytes2Seconds(handle, pos)
			l = BASS_ChannelBytes2Seconds(handle, length)
			
			sys.stdout.write('Now playing %s - %02d - %u:%02u of %u:%02u\r' % (filename,p,p/60,p%60,l/60,l%60))
			sys.stdout.flush()
			
			time.sleep(1)
		except KeyboardInterrupt:
			playing = False

	BASS_StreamFree(handle)
	BASS_Free()
	
	print('Bye, Bye ...')
	
if __name__ == '__main__':
	exit(main(sys.argv[1:]))

