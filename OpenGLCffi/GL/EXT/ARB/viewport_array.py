from OpenGLCffi.GL import params
@params(api='gl', prms=['first', 'count', 'v'])
def glViewportArrayv(first, count, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'w', 'h'])
def glViewportIndexedf(index, x, y, w, h):
	pass


@params(api='gl', prms=['index', 'v'])
def glViewportIndexedfv(index, v):
	pass


@params(api='gl', prms=['first', 'count', 'v'])
def glScissorArrayv(first, count, v):
	pass


@params(api='gl', prms=['index', 'left', 'bottom', 'width', 'height'])
def glScissorIndexed(index, left, bottom, width, height):
	pass


@params(api='gl', prms=['index', 'v'])
def glScissorIndexedv(index, v):
	pass


@params(api='gl', prms=['first', 'count', 'v'])
def glDepthRangeArrayv(first, count, v):
	pass


@params(api='gl', prms=['index', 'n', 'f'])
def glDepthRangeIndexed(index, n, f):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetFloati_v(target, index, data):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetDoublei_v(target, index, data):
	pass


