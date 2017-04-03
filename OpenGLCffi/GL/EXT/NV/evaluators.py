from OpenGLCffi.GL import params
@params('target', 'index', 'type', 'ustride', 'vstride', 'uorder', 'vorder', 'packed', 'points', api='gl')
def glMapControlPointsNV(target, index, type, ustride, vstride, uorder, vorder, packed, points):
	pass


@params('target', 'pname', 'params', api='gl')
def glMapParameterivNV(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glMapParameterfvNV(target, pname, params):
	pass


@params('target', 'index', 'type', 'ustride', 'vstride', 'packed', 'points', api='gl')
def glGetMapControlPointsNV(target, index, type, ustride, vstride, packed, points):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetMapParameterivNV(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetMapParameterfvNV(target, pname, params):
	pass


@params('target', 'index', 'pname', 'params', api='gl')
def glGetMapAttribParameterivNV(target, index, pname, params):
	pass


@params('target', 'index', 'pname', 'params', api='gl')
def glGetMapAttribParameterfvNV(target, index, pname, params):
	pass


@params('target', 'mode', api='gl')
def glEvalMapsNV(target, mode):
	pass


