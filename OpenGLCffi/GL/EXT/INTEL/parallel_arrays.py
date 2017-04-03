from OpenGLCffi.GL import params
@params('size', 'type', 'pointer', api='gl')
def glVertexPointervINTEL(size, type, pointer):
	pass


@params('type', 'pointer', api='gl')
def glNormalPointervINTEL(type, pointer):
	pass


@params('size', 'type', 'pointer', api='gl')
def glColorPointervINTEL(size, type, pointer):
	pass


@params('size', 'type', 'pointer', api='gl')
def glTexCoordPointervINTEL(size, type, pointer):
	pass


