@params(api = 'gles2')
def glGetGraphicsResetStatus():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles2')
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformfv(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformiv(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformuiv(program, location, bufSize):
	pass


@params(api = 'gles2')
def glGetGraphicsResetStatusKHR():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles2')
def glReadnPixelsKHR(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformfvKHR(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformivKHR(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformuivKHR(program, location, bufSize):
	pass


