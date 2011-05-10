"""
	Copyright (c) 2011, Mihail Szabolcs
	All rights reserved.

	See LICENSE for more information.
"""
from ctypes import *
from pyglet.gl import *

class Shader(object):
	def __init__(self, vs, fs, isFile=False):
		self.id = glCreateProgram()

		if vs != None:
			self.vs = self.create_shader(vs,GL_VERTEX_SHADER,isFile)
			glAttachShader(self.id, self.vs)

		if fs != None:
			self.fs = self.create_shader(fs,GL_FRAGMENT_SHADER,isFile)
			glAttachShader(self.id, self.fs)

		glLinkProgram(self.id)
		self.print_log(self.id, glGetProgramInfoLog)

	def __del__(self):
		pass

	def __setitem__(self, name, value):
		# FIXME: cache locations
		u = glGetUniformLocation(self.id, name)

		if isinstance(value, float):
			glUniform1f(u, value)
		elif isinstance(value, int):
			glUniform1i(u, value)
		elif isinstance(value, list):
			l = len(value)
			if l == 2:
				glUniform2fv(u,l,(GLfloat * l)(*value))
			elif l == 3:
				glUniform3fv(u,l,(GLfloat * l)(*value))
			elif l == 4:
				glUniform4fv(u,l,(GLfloat * l)(*value))
		else:
			raise TypeError("The given type is not supported as uniform, at the moment.")

	def create_shader(self, source, stype, isFile=False):
		if isFile:
			source = open(source).read()

		shader = glCreateShader(stype)
		glShaderSource(shader, 1, cast(byref(c_char_p(source)), POINTER(POINTER(c_char))), None)
		glCompileShader(shader)

		self.print_log(shader, glGetShaderInfoLog)
		return shader

	def bind(self):
		glUseProgram(self.id)

	def release(self):
		glUseProgram(0)

	def print_log(self, obj, func):
		log = create_string_buffer(4096)
		written = c_int()
		func(obj, 4096, pointer(written), cast(pointer(log), POINTER(c_char)))
		print(log.value)
