from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'colorNumber', 'index', 'name'])
def glBindFragDataLocationIndexed(program, colorNumber, index, name):
	pass


@params(api='gl', prms=['program', 'name'])
def glGetFragDataIndex(program, name):
	pass


