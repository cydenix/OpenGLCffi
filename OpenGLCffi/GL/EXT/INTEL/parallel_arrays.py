from OpenGLCffi.GL import params
@params(api='gl', prms=['size', 'type', 'pointer'])
def glVertexPointervINTEL(size, type, pointer):
	pass


@params(api='gl', prms=['type', 'pointer'])
def glNormalPointervINTEL(type, pointer):
	pass


@params(api='gl', prms=['size', 'type', 'pointer'])
def glColorPointervINTEL(size, type, pointer):
	pass


@params(api='gl', prms=['size', 'type', 'pointer'])
def glTexCoordPointervINTEL(size, type, pointer):
	pass


