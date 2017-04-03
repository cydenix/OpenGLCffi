from OpenGLCffi.GL import params
@params('first', 'count', 'v', api='gl')
def glViewportArrayv(first, count, v):
	pass


@params('index', 'x', 'y', 'w', 'h', api='gl')
def glViewportIndexedf(index, x, y, w, h):
	pass


@params('index', 'v', api='gl')
def glViewportIndexedfv(index, v):
	pass


@params('first', 'count', 'v', api='gl')
def glScissorArrayv(first, count, v):
	pass


@params('index', 'left', 'bottom', 'width', 'height', api='gl')
def glScissorIndexed(index, left, bottom, width, height):
	pass


@params('index', 'v', api='gl')
def glScissorIndexedv(index, v):
	pass


@params('first', 'count', 'v', api='gl')
def glDepthRangeArrayv(first, count, v):
	pass


@params('index', 'n', 'f', api='gl')
def glDepthRangeIndexed(index, n, f):
	pass


@params('target', 'index', 'data', api='gl')
def glGetFloati_v(target, index, data):
	pass


@params('target', 'index', 'data', api='gl')
def glGetDoublei_v(target, index, data):
	pass


