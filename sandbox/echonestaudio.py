"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
import sys
import echonest.audio as audio

class EchonestAudio:
	def __init__(self, filename):
		self.filename = filename
		self.audio = audio.LocalAudioFile(filename)
			
	def dump(self):
		with open("%s.beats" % self.filename, 'w') as f:
			# format: kind, start, end, duration, confidence
			for b in self.audio.analysis.beats:
				f.write("%s %f %f %f %f\n" % (b.kind, b.start, b.end, b.duration, b.confidence))
				
def main(argv):
	if len(argv) < 1:
		print('usage: echonestaudio filename')
		return 1
		
	audio = EchonestAudio(argv[0])
	audio.dump()
	
if __name__ == "__main__":
	exit(main(sys.argv[1:]))
