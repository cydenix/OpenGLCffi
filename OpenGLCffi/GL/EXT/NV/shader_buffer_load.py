from OpenGLCffi.GL import params
@params('target', 'access', api='gl')
def glMakeBufferResidentNV(target, access):
	pass


@params('target', api='gl')
def glMakeBufferNonResidentNV(target):
	pass


@params('target', api='gl')
def glIsBufferResidentNV(target):
	pass


@params('buffer', 'access', api='gl')
def glMakeNamedBufferResidentNV(buffer, access):
	pass


@params('buffer', api='gl')
def glMakeNamedBufferNonResidentNV(buffer):
	pass


@params('buffer', api='gl')
def glIsNamedBufferResidentNV(buffer):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetBufferParameterui64vNV(target, pname, params):
	pass


@params('buffer', 'pname', 'params', api='gl')
def glGetNamedBufferParameterui64vNV(buffer, pname, params):
	pass


@params('value', 'result', api='gl')
def glGetIntegerui64vNV(value, result):
	pass


@params('location', 'value', api='gl')
def glUniformui64NV(location, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniformui64vNV(location, count, value):
	pass


@params('program', 'location', 'params', api='gl')
def glGetUniformui64vNV(program, location, params):
	pass


@params('program', 'location', 'value', api='gl')
def glProgramUniformui64NV(program, location, value):
	pass


@params('program', 'location', 'count', 'value', api='gl')
def glProgramUniformui64vNV(program, location, count, value):
	pass


