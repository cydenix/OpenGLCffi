from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'access'])
def glMakeBufferResidentNV(target, access):
	pass


@params(api='gl', prms=['target'])
def glMakeBufferNonResidentNV(target):
	pass


@params(api='gl', prms=['target'])
def glIsBufferResidentNV(target):
	pass


@params(api='gl', prms=['buffer', 'access'])
def glMakeNamedBufferResidentNV(buffer, access):
	pass


@params(api='gl', prms=['buffer'])
def glMakeNamedBufferNonResidentNV(buffer):
	pass


@params(api='gl', prms=['buffer'])
def glIsNamedBufferResidentNV(buffer):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetBufferParameterui64vNV(target, pname, params):
	pass


@params(api='gl', prms=['buffer', 'pname', 'params'])
def glGetNamedBufferParameterui64vNV(buffer, pname, params):
	pass


@params(api='gl', prms=['value', 'result'])
def glGetIntegerui64vNV(value, result):
	pass


@params(api='gl', prms=['location', 'value'])
def glUniformui64NV(location, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniformui64vNV(location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'params'])
def glGetUniformui64vNV(program, location, params):
	pass


@params(api='gl', prms=['program', 'location', 'value'])
def glProgramUniformui64NV(program, location, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'value'])
def glProgramUniformui64vNV(program, location, count, value):
	pass


