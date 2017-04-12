from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['program', 'bufSize', 'length', 'binaryFormat', 'binary'])
def glGetProgramBinaryOES(program, bufSize, length, binaryFormat):
	pass


@params(api='gles3', prms=['program', 'binaryFormat', 'binary', 'length'])
def glProgramBinaryOES(program, binaryFormat, binary, length):
	pass


