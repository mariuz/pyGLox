"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
def run(argv,klass):
	win = klass(argv)
	win.run()
	win.__del__() # call the destructor manually!
