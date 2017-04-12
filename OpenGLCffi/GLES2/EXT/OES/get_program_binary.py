from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['program', 'bufSize', 'length', 'binaryFormat', 'binary'])
def glGetProgramBinaryOES(program, bufSize, length, binaryFormat, binary):
	pass


@params(api='gles2', prms=['program', 'binaryFormat', 'binary', 'length'])
def glProgramBinaryOES(program, binaryFormat, binary, length):
	pass


