from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'pname'])
def glEnableVertexAttribAPPLE(index, pname):
	pass


@params(api='gl', prms=['index', 'pname'])
def glDisableVertexAttribAPPLE(index, pname):
	pass


@params(api='gl', prms=['index', 'pname'])
def glIsVertexAttribEnabledAPPLE(index, pname):
	pass


@params(api='gl', prms=['index', 'size', 'u1', 'u2', 'stride', 'order', 'points'])
def glMapVertexAttrib1dAPPLE(index, size, u1, u2, stride, order, points):
	pass


@params(api='gl', prms=['index', 'size', 'u1', 'u2', 'stride', 'order', 'points'])
def glMapVertexAttrib1fAPPLE(index, size, u1, u2, stride, order, points):
	pass


@params(api='gl', prms=['index', 'size', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points'])
def glMapVertexAttrib2dAPPLE(index, size, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


@params(api='gl', prms=['index', 'size', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'points'])
def glMapVertexAttrib2fAPPLE(index, size, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
	pass


