from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=[])
def glGetGraphicsResetStatus():
	pass


@params(api='gles3', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfv(program, location, bufSize):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformiv(program, location, bufSize):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuiv(program, location, bufSize):
	pass


@params(api='gles3', prms=[])
def glGetGraphicsResetStatusKHR():
	pass


@params(api='gles3', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixelsKHR(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfvKHR(program, location, bufSize):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformivKHR(program, location, bufSize):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuivKHR(program, location, bufSize):
	pass


