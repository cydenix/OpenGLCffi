from OpenGLCffi.GL import params
@params(api='gl', prms=['array'])
def glBindVertexArrayAPPLE(array):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glDeleteVertexArraysAPPLE(n, arrays):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glGenVertexArraysAPPLE(n, arrays):
	pass


@params(api='gl', prms=['array'])
def glIsVertexArrayAPPLE(array):
	pass


