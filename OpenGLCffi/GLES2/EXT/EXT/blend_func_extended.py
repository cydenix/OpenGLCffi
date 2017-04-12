from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['program', 'colorNumber', 'index', 'name'])
def glBindFragDataLocationIndexedEXT(program, colorNumber, index, name):
	pass


@params(api='gles2', prms=['program', 'color', 'name'])
def glBindFragDataLocationEXT(program, color, name):
	pass


@params(api='gles2', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceLocationIndexEXT(program, programInterface, name):
	pass


@params(api='gles2', prms=['program', 'name'])
def glGetFragDataIndexEXT(program, name):
	pass


