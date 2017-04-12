from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['array'])
def glBindVertexArrayOES(array):
	pass


@params(api='gles2', prms=['n', 'arrays'])
def glDeleteVertexArraysOES(n, arrays):
	pass


@params(api='gles2', prms=['n', 'arrays'])
def glGenVertexArraysOES(n, arrays):
	pass


@params(api='gles2', prms=['array'])
def glIsVertexArrayOES(array):
	pass


