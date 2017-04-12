from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'bufSize', 'length', 'binaryFormat', 'binary'])
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
	pass


@params(api='gl', prms=['program', 'binaryFormat', 'binary', 'length'])
def glProgramBinary(program, binaryFormat, binary, length):
	pass


@params(api='gl', prms=['program', 'pname', 'value'])
def glProgramParameteri(program, pname, value):
	pass


