from OpenGLCffi.GLES3 import params
@params(api = 'gles3')
def glGetGraphicsResetStatusEXT():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles3')
def glReadnPixelsEXT(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformfvEXT(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles3')
def glGetnUniformivEXT(program, location, bufSize):
	pass


