@params(api = 'gles3')
def glGetGraphicsResetStatus():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles3')
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformfv(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformiv(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformuiv(program, location, bufSize):
	pass


@params(api = 'gles3')
def glGetGraphicsResetStatusKHR():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles3')
def glReadnPixelsKHR(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformfvKHR(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformivKHR(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformuivKHR(program, location, bufSize):
	pass


