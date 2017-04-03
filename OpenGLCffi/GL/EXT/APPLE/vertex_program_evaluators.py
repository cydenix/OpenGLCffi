from OpenGLCffi.GL import params
@params('index', 'pname', api='gl')
def glEnableVertexAttribAPPLE(index, pname):
	pass


@params('index', 'pname', api='gl')
def glDisableVertexAttribAPPLE(index, pname):
	pass


@params('index', 'pname', api='gl')
def glIsVertexAttribEnabledAPPLE(index, pname):
	pass


@params('index', 'size', 'u1', 'u2', 'stride', 'order', 'points', api='gl')
def glMapVertexAttrib1dAPPLE(index, size, u1, u2, stride, order, points):
	pass


@params('index', 'size', 'u1', 'u2', 'stride', 'order', 'points', api='gl')
def glMapVertexAttrib1fAPPLE(index, size, u1, u2, stride, order, points):
	pass


@params('index', 'size', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points', api='gl')
def glMapVertexAttrib2dAPPLE(index, size, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params('index', 'size', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points', api='gl')
def glMapVertexAttrib2fAPPLE(index, size, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


