from OpenGLCffi.GL import params
@params('i', api='gl')
def glArrayElementEXT(i):
	pass


@params('size', 'type', 'stride', 'count', 'pointer', api='gl')
def glColorPointerEXT(size, type, stride, count, pointer):
	pass


@params('mode', 'first', 'count', api='gl')
def glDrawArraysEXT(mode, first, count):
	pass


@params('stride', 'count', 'pointer', api='gl')
def glEdgeFlagPointerEXT(stride, count, pointer):
	pass


@params('pname', 'params', api='gl')
def glGetPointervEXT(pname, params):
	pass


@params('type', 'stride', 'count', 'pointer', api='gl')
def glIndexPointerEXT(type, stride, count, pointer):
	pass


@params('type', 'stride', 'count', 'pointer', api='gl')
def glNormalPointerEXT(type, stride, count, pointer):
	pass


@params('size', 'type', 'stride', 'count', 'pointer', api='gl')
def glTexCoordPointerEXT(size, type, stride, count, pointer):
	pass


@params('size', 'type', 'stride', 'count', 'pointer', api='gl')
def glVertexPointerEXT(size, type, stride, count, pointer):
	pass


