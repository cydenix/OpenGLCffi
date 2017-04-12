from OpenGLCffi.GL import params
@params(api='gl', prms=['array'])
def glBindVertexArray(array):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glDeleteVertexArrays(n, arrays):
	pass


@params(api='gl', prms=['n', 'arrays'])
def glGenVertexArrays(n, arrays):
	pass


@params(api='gl', prms=['array'])
def glIsVertexArray(array):
	pass


