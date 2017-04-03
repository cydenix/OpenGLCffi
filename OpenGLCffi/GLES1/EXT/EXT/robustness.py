from OpenGLCffi.GLES1 import params
@params(api = 'gles1')
def glGetGraphicsResetStatusEXT():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles1')
def glReadnPixelsEXT(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles1')
def glGetnUniformfvEXT(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles1')
def glGetnUniformivEXT(program, location, bufSize):
	pass


