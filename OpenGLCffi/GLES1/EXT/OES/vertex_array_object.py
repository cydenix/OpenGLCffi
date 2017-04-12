from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['array'])
def glBindVertexArrayOES(array):
	pass


@params(api='gles1', prms=['n', 'arrays'])
def glDeleteVertexArraysOES(n, arrays):
	pass


@params(api='gles1', prms=['n', 'arrays'])
def glGenVertexArraysOES(n, arrays):
	pass


@params(api='gles1', prms=['array'])
def glIsVertexArrayOES(array):
	pass


