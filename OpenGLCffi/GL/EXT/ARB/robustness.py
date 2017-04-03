from OpenGLCffi.GL import params
@params(api = 'gl')
def glGetGraphicsResetStatusARB():
	pass


@params('target', 'level', 'format', 'type', 'bufSize', 'img', api='gl')
def glGetnTexImageARB(target, level, format, type, bufSize, img):
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gl')
def glReadnPixelsARB(x, y, width, height, format, type, bufSize, data):
	pass


@params('target', 'lod', 'bufSize', 'img', api='gl')
def glGetnCompressedTexImageARB(target, lod, bufSize, img):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformfvARB(program, location, bufSize, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformivARB(program, location, bufSize, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformuivARB(program, location, bufSize, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformdvARB(program, location, bufSize, params):
	pass


@params('target', 'query', 'bufSize', 'v', api='gl')
def glGetnMapdvARB(target, query, bufSize, v):
	pass


@params('target', 'query', 'bufSize', 'v', api='gl')
def glGetnMapfvARB(target, query, bufSize, v):
	pass


@params('target', 'query', 'bufSize', 'v', api='gl')
def glGetnMapivARB(target, query, bufSize, v):
	pass


@params('map', 'bufSize', 'values', api='gl')
def glGetnPixelMapfvARB(map, bufSize, values):
	pass


@params('map', 'bufSize', 'values', api='gl')
def glGetnPixelMapuivARB(map, bufSize, values):
	pass


@params('map', 'bufSize', 'values', api='gl')
def glGetnPixelMapusvARB(map, bufSize, values):
	pass


@params('bufSize', 'pattern', api='gl')
def glGetnPolygonStippleARB(bufSize, pattern):
	pass


@params('target', 'format', 'type', 'bufSize', 'table', api='gl')
def glGetnColorTableARB(target, format, type, bufSize, table):
	pass


@params('target', 'format', 'type', 'bufSize', 'image', api='gl')
def glGetnConvolutionFilterARB(target, format, type, bufSize, image):
	pass


@params('target', 'format', 'type', 'rowBufSize', 'row', 'columnBufSize', 'column', 'span', api='gl')
def glGetnSeparableFilterARB(target, format, type, rowBufSize, row, columnBufSize, column, span):
	pass


@params('target', 'reset', 'format', 'type', 'bufSize', 'values', api='gl')
def glGetnHistogramARB(target, reset, format, type, bufSize, values):
	pass


@params('target', 'reset', 'format', 'type', 'bufSize', 'values', api='gl')
def glGetnMinmaxARB(target, reset, format, type, bufSize, values):
	pass


