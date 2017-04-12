from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'internalformat', 'width', 'format', 'type', 'image'])
def glConvolutionFilter1DEXT(target, internalformat, width, format, type, image):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'height', 'format', 'type', 'image'])
def glConvolutionFilter2DEXT(target, internalformat, width, height, format, type, image):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameterfEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameterfvEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameteriEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glConvolutionParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'internalformat', 'x', 'y', 'width'])
def glCopyConvolutionFilter1DEXT(target, internalformat, x, y, width):
	pass


@params(api='gl', prms=['target', 'internalformat', 'x', 'y', 'width', 'height'])
def glCopyConvolutionFilter2DEXT(target, internalformat, x, y, width, height):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'image'])
def glGetConvolutionFilterEXT(target, format, type, image):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetConvolutionParameterfvEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetConvolutionParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'row', 'column', 'span'])
def glGetSeparableFilterEXT(target, format, type, row, column, span):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'height', 'format', 'type', 'row', 'column'])
def glSeparableFilter2DEXT(target, internalformat, width, height, format, type, row, column):
	pass


