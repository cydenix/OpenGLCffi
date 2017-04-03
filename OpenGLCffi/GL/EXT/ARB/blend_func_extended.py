from OpenGLCffi.GL import params
@params('program', 'colorNumber', 'index', 'name', api='gl')
def glBindFragDataLocationIndexed(program, colorNumber, index, name):
	pass


@params('program', 'name', api='gl')
def glGetFragDataIndex(program, name):
	pass


