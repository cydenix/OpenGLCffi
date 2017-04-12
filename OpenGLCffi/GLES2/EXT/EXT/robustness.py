from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=[])
def glGetGraphicsResetStatusEXT():
	pass


@params(api='gles2', prms=['x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data'])
def glReadnPixelsEXT(x, y, width, height, format, type, bufSize, data):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformfvEXT(program, location, bufSize):
	pass


@params(api='gles2', prms=['program', 'location', 'bufSize', 'params'])
def glGetnUniformivEXT(program, location, bufSize):
	pass


