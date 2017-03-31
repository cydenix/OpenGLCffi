@params('program', 'bufSize', 'length', 'binaryFormat', 'binary', api='gl')
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
	pass


@params('program', 'binaryFormat', 'binary', 'length', api='gl')
def glProgramBinary(program, binaryFormat, binary, length):
	pass


@params('program', 'pname', 'value', api='gl')
def glProgramParameteri(program, pname, value):
	pass


