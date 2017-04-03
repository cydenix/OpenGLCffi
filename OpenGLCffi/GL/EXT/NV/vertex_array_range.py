from OpenGLCffi.GL import params
@params(api = 'gl')
def glFlushVertexArrayRangeNV():
	pass


@params('length', 'pointer', api='gl')
def glVertexArrayRangeNV(length, pointer):
	pass


