from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'w1', 'w2', 'wstride', 'worder', 'points'])
def glDeformationMap3dSGIX(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, w1, w2, wstride, worder, points):
	pass


@params(api='gl', prms=['target', 'u1', 'u2', 'ustride', 'uorder', 'v1', 'v2', 'vstride', 'vorder', 'w1', 'w2', 'wstride', 'worder', 'points'])
def glDeformationMap3fSGIX(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, w1, w2, wstride, worder, points):
	pass


@params(api='gl', prms=['mask'])
def glDeformSGIX(mask):
	pass


@params(api='gl', prms=['mask'])
def glLoadIdentityDeformationMapSGIX(mask):
	pass


