from OpenGLCffi.GLES2 import params
@params(api = 'gles2')
def glGetGraphicsResetStatusEXT():
	pass


@params('x', 'y', 'width', 'height', 'format', 'type', 'bufSize', 'data', api='gles2')
def glReadnPixelsEXT(x, y, width, height, format, type, bufSize, data):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformfvEXT(program, location, bufSize):
	pass


@params('program', 'location', 'bufSize', 'params', api='gles2')
def glGetnUniformivEXT(program, location, bufSize):
	pass


