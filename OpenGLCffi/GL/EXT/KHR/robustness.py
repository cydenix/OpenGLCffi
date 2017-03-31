@params(api = 'gl')
def glGetGraphicsResetStatus():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gl')
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformfv(program, location, bufSize, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformiv(program, location, bufSize, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformuiv(program, location, bufSize, params):
	pass


@params(api = 'gl')
def glGetGraphicsResetStatusKHR():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gl')
def glReadnPixelsKHR(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformfvKHR(program, location, bufSize, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformivKHR(program, location, bufSize, params):
	pass


@params('program', 'location', 'bufSize', 'params', api='gl')
def glGetnUniformuivKHR(program, location, bufSize, params):
	pass


