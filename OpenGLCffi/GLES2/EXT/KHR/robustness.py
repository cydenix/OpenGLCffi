from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=[])
def glGetGraphicsResetStatus():
	pass


@params(api='gles2', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixels(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfv(program, location, bufSize):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformiv(program, location, bufSize):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuiv(program, location, bufSize):
	pass


@params(api='gles2', prms=[])
def glGetGraphicsResetStatusKHR():
	pass


@params(api='gles2', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixelsKHR(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfvKHR(program, location, bufSize):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformivKHR(program, location, bufSize):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformuivKHR(program, location, bufSize):
	pass


