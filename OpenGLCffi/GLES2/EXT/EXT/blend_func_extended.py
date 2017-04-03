from OpenGLCffi.GLES2 import params
@params('program', 'colorNumber', 'index', 'name', api='gles2')
def glBindFragDataLocationIndexedEXT(program, colorNumber, index, name):
	pass


@params('program', 'color', 'name', api='gles2')
def glBindFragDataLocationEXT(program, color, name):
	pass


@params('program', 'programInterface', 'name', api='gles2')
def glGetProgramResourceLocationIndexEXT(program, programInterface, name):
	pass


@params('program', 'name', api='gles2')
def glGetFragDataIndexEXT(program, name):
	pass


