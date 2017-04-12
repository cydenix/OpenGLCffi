from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['array'])
def glBindVertexArrayOES(array):
	pass


@params(api='gles3', prms=['n', 'arrays'])
def glDeleteVertexArraysOES(n, arrays):
	pass


@params(api='gles3', prms=['n', 'arrays'])
def glGenVertexArraysOES(n):
	pass


@params(api='gles3', prms=['array'])
def glIsVertexArrayOES(array):
	pass


