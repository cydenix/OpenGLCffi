from OpenGLCffi.GL import params
@params(api='gl', prms=['i'])
def glArrayElementEXT(i):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'count', 'pointer'])
def glColorPointerEXT(size, type, stride, count, pointer):
	pass


@params(api='gl', prms=['mode', 'first', 'count'])
def glDrawArraysEXT(mode, first, count):
	pass


@params(api='gl', prms=['stride', 'count', 'pointer'])
def glEdgeFlagPointerEXT(stride, count, pointer):
	pass


@params(api='gl', prms=['pname', 'params'])
def glGetPointervEXT(pname, params):
	pass


@params(api='gl', prms=['type', 'stride', 'count', 'pointer'])
def glIndexPointerEXT(type, stride, count, pointer):
	pass


@params(api='gl', prms=['type', 'stride', 'count', 'pointer'])
def glNormalPointerEXT(type, stride, count, pointer):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'count', 'pointer'])
def glTexCoordPointerEXT(size, type, stride, count, pointer):
	pass


@params(api='gl', prms=['size', 'type', 'stride', 'count', 'pointer'])
def glVertexPointerEXT(size, type, stride, count, pointer):
	pass


