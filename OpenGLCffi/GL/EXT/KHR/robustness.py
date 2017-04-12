from OpenGLCffi.GL import params
@params(api='gl', prms=[])
def glGetGraphicsResetStatus():
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfv(program, location, bufSize, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformiv(program, location, bufSize, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuiv(program, location, bufSize, params):
	pass


@params(api='gl', prms=[])
def glGetGraphicsResetStatusKHR():
	pass


@params(api='gl', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixelsKHR(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfvKHR(program, location, bufSize, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformivKHR(program, location, bufSize, params):
	pass


@params(api='gl', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuivKHR(program, location, bufSize, params):
	pass


