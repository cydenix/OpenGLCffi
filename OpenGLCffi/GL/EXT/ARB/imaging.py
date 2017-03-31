@params('red', 'green', 'blue', 'alpha', api='gl')
def glBlendColor(red, green, blue, alpha):
	pass


@params('mode', api='gl')
def glBlendEquation(mode):
	pass


@params('target', 'internalformat', 'width', 'format', 'type', 'table', api='gl')
def glColorTable(target, internalformat, width, format, type, table):
	pass


@params('target', 'pname', 'params', api='gl')
def glColorTableParameterfv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glColorTableParameteriv(target, pname, params):
	pass


@params('target', 'internalformat', 'x', 'y', 'width', api='gl')
def glCopyColorTable(target, internalformat, x, y, width):
	pass


@params('target', 'format', 'type', 'table', api='gl')
def glGetColorTable(target, format, type, table):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetColorTableParameterfv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetColorTableParameteriv(target, pname, params):
	pass


@params('target', 'start', 'count', 'format', 'type', 'data', api='gl')
def glColorSubTable(target, start, count, format, type, data):
	pass


@params('target', 'start', 'x', 'y', 'width', api='gl')
def glCopyColorSubTable(target, start, x, y, width):
	pass


@params('target', 'internalformat', 'width', 'format', 'type', 'image', api='gl')
def glConvolutionFilter1D(target, internalformat, width, format, type, image):
	pass


@params('target', 'internalformat', 'width', 'height', 'format', 'type', 'image', api='gl')
def glConvolutionFilter2D(target, internalformat, width, height, format, type, image):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameterf(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameterfv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameteri(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameteriv(target, pname, params):
	pass


@params('target', 'internalformat', 'x', 'y', 'width', api='gl')
def glCopyConvolutionFilter1D(target, internalformat, x, y, width):
	pass


@params('target', 'internalformat', 'x', 'y', 'width', 'height', api='gl')
def glCopyConvolutionFilter2D(target, internalformat, x, y, width, height):
	pass


@params('target', 'format', 'type', 'image', api='gl')
def glGetConvolutionFilter(target, format, type, image):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetConvolutionParameterfv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetConvolutionParameteriv(target, pname, params):
	pass


@params('target', 'format', 'type', 'row', 'column', 'span', api='gl')
def glGetSeparableFilter(target, format, type, row, column, span):
	pass


@params('target', 'internalformat', 'width', 'height', 'format', 'type', 'row', 'column', api='gl')
def glSeparableFilter2D(target, internalformat, width, height, format, type, row, column):
	pass


@params('target', 'reset', 'format', 'type', 'values', api='gl')
def glGetHistogram(target, reset, format, type, values):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetHistogramParameterfv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetHistogramParameteriv(target, pname, params):
	pass


@params('target', 'reset', 'format', 'type', 'values', api='gl')
def glGetMinmax(target, reset, format, type, values):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetMinmaxParameterfv(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetMinmaxParameteriv(target, pname, params):
	pass


@params('target', 'width', 'internalformat', 'sink', api='gl')
def glHistogram(target, width, internalformat, sink):
	pass


@params('target', 'internalformat', 'sink', api='gl')
def glMinmax(target, internalformat, sink):
	pass


@params('target', api='gl')
def glResetHistogram(target):
	pass


@params('target', api='gl')
def glResetMinmax(target):
	pass


