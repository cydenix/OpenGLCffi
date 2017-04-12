from OpenGLCffi.GL import params
@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glBlendColor(red, green, blue, alpha):
	pass


@params(api='gl', prms=['mode'])
def glBlendEquation(mode):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'format', 'type', 'table'])
def glColorTable(target, internalformat, width, format, type, table):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glColorTableParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glColorTableParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'internalformat', 'x', 'y', 'width'])
def glCopyColorTable(target, internalformat, x, y, width):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'table'])
def glGetColorTable(target, format, type, table):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetColorTableParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetColorTableParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'start', 'count', 'format', 'type', 'data'])
def glColorSubTable(target, start, count, format, type, data):
	pass


@params(api='gl', prms=['target', 'start', 'x', 'y', 'width'])
def glCopyColorSubTable(target, start, x, y, width):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'format', 'type', 'image'])
def glConvolutionFilter1D(target, internalformat, width, format, type, image):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'height', 'format', 'type', 'image'])
def glConvolutionFilter2D(target, internalformat, width, height, format, type, image):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameterf(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameteri(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'internalformat', 'x', 'y', 'width'])
def glCopyConvolutionFilter1D(target, internalformat, x, y, width):
	pass


@params(api='gl', prms=['target', 'internalformat', 'x', 'y', 'width', 'height'])
def glCopyConvolutionFilter2D(target, internalformat, x, y, width, height):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'image'])
def glGetConvolutionFilter(target, format, type, image):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetConvolutionParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetConvolutionParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'row', 'column', 'span'])
def glGetSeparableFilter(target, format, type, row, column, span):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'height', 'format', 'type', 'row', 'column'])
def glSeparableFilter2D(target, internalformat, width, height, format, type, row, column):
	pass


@params(api='gl', prms=['target', 'reset', 'format', 'type', 'values'])
def glGetHistogram(target, reset, format, type, values):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetHistogramParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetHistogramParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'reset', 'format', 'type', 'values'])
def glGetMinmax(target, reset, format, type, values):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetMinmaxParameterfv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetMinmaxParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['target', 'width', 'internalformat', 'sink'])
def glHistogram(target, width, internalformat, sink):
	pass


@params(api='gl', prms=['target', 'internalformat', 'sink'])
def glMinmax(target, internalformat, sink):
	pass


@params(api='gl', prms=['target'])
def glResetHistogram(target):
	pass


@params(api='gl', prms=['target'])
def glResetMinmax(target):
	pass


