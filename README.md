pyGLox
======
pyGLox is a small *wrapper* over the PyGLet family by abstracting and providing some high-level
interfaces for things like *"Render Targets"* (FBO), *"Textures"* and *"GLSL Shaders"*, basic *"Geometry"*,
*"Audio"* and others.

It's ideal for *rapid prototyping* new and interesting ideas, or writing real time visual demos as shown
in the included *example*.

Dependencies
------------
* [Pyglet](http://www.pyglet.org/) **(required)**
* [NumPy](http://numpy.scipy.org/) **(required)**
* [BASS audio library](http://www.un4seen.com/) *(semi-required, see below)*
* [Echo Nest Remix API](http://code.google.com/p/echo-nest-remix/) *(optional, see below)*
* [OpenCV](http://opencv.willowgarage.com/wiki/) *(optional, see below)*

I didn't use [pyBASS](http://pypi.python.org/pypi/pybass/), wrote my own light-weight ctypes bindings and therefore
it is not truly portable as of now and it needs a little bit of work in order
to make it work under **non-linux** (what a hell of a word *sighs*) platforms.

*(look inside sandbox/bass.py for more juicy details)*

**The Echo Nest Remix API** is needed **ONLY** if you want to *extract* beats from your own songs.

*(look inside sandbox/echonestaudio.py for more goofy details)*

**OpenCV** is needed **ONLY** if you intend to capture images from your WebCam and use them as textures.

*(look inside sandbox/webcam.py for more dirty details)*

pyMedia
-------
* textures - various *textures* gathered from all over the place ( [creative commons](http://creativecommons.org/licenses/by/3.0/) )
* shaders - some basic *GLSL* shaders written specifically for the included `demo` (  [creative commons](http://creativecommons.org/licenses/by/3.0/) )
* geometry - various *models* gathered from all over the place ( [creative commons](http://creativecommons.org/licenses/by/3.0/) )
* music
	* [Grapes - I dunno](http://dig.ccmixter.org/dig?user=grapes)
	* [Sinatra - Electric Gumpop](http://pouet.net/prod.php?which=54489) *(used in the included real time demo)*
	* [Vincenzo - Compofiller](http://www.freshmindworkz.hu/vincenzo/music.html)
	
If *you* are the author of any of these and you *have any concerns* regarding
the distribution or use of these *media*, please drop me a line and I'll take the necessary
actions / steps.

pyDemo
------
Curious? See this [video](http://vimeo.com/23434817) about the *included real time demo*.

*(if you are brave enough look inside demo.py for the real thing a.k.a source code)*

Contribute
----------
* Fork the project.
* Make your feature addition or bug fix.
* Send me a pull request. Bonus points for topic branches.

License
-------
Copyright (c) 2011, Mihail Szabolcs

pyGLox is provided as-is under the **MIT** license. For more information 
see *LICENSE* .
