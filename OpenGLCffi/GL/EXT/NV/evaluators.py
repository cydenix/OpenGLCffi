from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'index', 'type', 'ustride', 'vstride', 'uorder', 'vorder', 'packed', 'points'])
def glMapControlPointsNV(target, index, type, ustride, vstride, uorder, vorder, packed, points):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glMapParameterivNV(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glMapParameterfvNV(target, pname, params):
	pass


@params(api='gl', prms=['target', 'index', 'type', 'ustride', 'vstride', 'packed', 'points'])
def glGetMapControlPointsNV(target, index, type, ustride, vstride, packed, points):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetMapParameterivNV(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetMapParameterfvNV(target, pname, params):
	pass


@params(api='gl', prms=['target', 'index', 'pname', 'params'])
def glGetMapAttribParameterivNV(target, index, pname, params):
	pass


@params(api='gl', prms=['target', 'index', 'pname', 'params'])
def glGetMapAttribParameterfvNV(target, index, pname, params):
	pass


@params(api='gl', prms=['target', 'mode'])
def glEvalMapsNV(target, mode):
	pass


