from OpenGLCffi.GL import params
@params(api='gl', prms=[])
def glGetGraphicsResetStatusARB():
	pass


@params(api='gl', prms=['target', 'level', 'format', 'type', 'bufSize', 'img'])
def glGetnTexImageARB(target, level, format, type, bufSize, img):
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixelsARB(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gl', prms=['target', 'lod', 'bufSize', 'img'])
def glGetnCompressedTexImageARB(target, lod, bufSize, img):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfvARB(program, location, bufSize, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformivARB(program, location, bufSize, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuivARB(program, location, bufSize, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformdvARB(program, location, bufSize, params):
	pass


@params(api='gl', prms=['target', 'query', 'bufSize', 'v'])
def glGetnMapdvARB(target, query, bufSize, v):
	pass


@params(api='gl', prms=['target', 'query', 'bufSize', 'v'])
def glGetnMapfvARB(target, query, bufSize, v):
	pass


@params(api='gl', prms=['target', 'query', 'bufSize', 'v'])
def glGetnMapivARB(target, query, bufSize, v):
	pass


@params(api='gl', prms=['map', 'bufSize', 'values'])
def glGetnPixelMapfvARB(map, bufSize, values):
	pass


@params(api='gl', prms=['map', 'bufSize', 'values'])
def glGetnPixelMapuivARB(map, bufSize, values):
	pass


@params(api='gl', prms=['map', 'bufSize', 'values'])
def glGetnPixelMapusvARB(map, bufSize, values):
	pass


@params(api='gl', prms=['bufSize', 'pattern'])
def glGetnPolygonStippleARB(bufSize, pattern):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'bufSize', 'table'])
def glGetnColorTableARB(target, format, type, bufSize, table):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'bufSize', 'image'])
def glGetnConvolutionFilterARB(target, format, type, bufSize, image):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'rowBufSize', 'row', 'columnBufSize', 'column', 'span'])
def glGetnSeparableFilterARB(target, format, type, rowBufSize, row, columnBufSize, column, span):
	pass


@params(api='gl', prms=['target', 'reset', 'format', 'type', 'bufSize', 'values'])
def glGetnHistogramARB(target, reset, format, type, bufSize, values):
	pass


@params(api='gl', prms=['target', 'reset', 'format', 'type', 'bufSize', 'values'])
def glGetnMinmaxARB(target, reset, format, type, bufSize, values):
	pass


