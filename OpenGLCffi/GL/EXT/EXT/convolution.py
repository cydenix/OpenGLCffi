from OpenGLCffi.GL import params
@params('target', 'internalformat', 'width', 'format', 'type', 'image', api='gl')
def glConvolutionFilter1DEXT(target, internalformat, width, format, type, image):
	pass


@params('target', 'internalformat', 'width', 'height', 'format', 'type', 'image', api='gl')
def glConvolutionFilter2DEXT(target, internalformat, width, height, format, type, image):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameterfEXT(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameterfvEXT(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameteriEXT(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glConvolutionParameterivEXT(target, pname, params):
	pass


@params('target', 'internalformat', 'x', 'y', 'width', api='gl')
def glCopyConvolutionFilter1DEXT(target, internalformat, x, y, width):
	pass


@params('target', 'internalformat', 'x', 'y', 'width', 'height', api='gl')
def glCopyConvolutionFilter2DEXT(target, internalformat, x, y, width, height):
	pass


@params('target', 'format', 'type', 'image', api='gl')
def glGetConvolutionFilterEXT(target, format, type, image):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetConvolutionParameterfvEXT(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetConvolutionParameterivEXT(target, pname, params):
	pass


@params('target', 'format', 'type', 'row', 'column', 'span', api='gl')
def glGetSeparableFilterEXT(target, format, type, row, column, span):
	pass


@params('target', 'internalformat', 'width', 'height', 'format', 'type', 'row', 'column', api='gl')
def glSeparableFilter2DEXT(target, internalformat, width, height, format, type, row, column):
	pass


