from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=[])
def glGetGraphicsResetStatusEXT():
	pass


@params(api='gles3', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixelsEXT(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfvEXT(program, location, bufSize):
	pass


@params(api='gles3', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformivEXT(program, location, bufSize):
	pass


