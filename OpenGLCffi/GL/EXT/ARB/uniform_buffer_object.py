from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'uniformCount', 'constuniformNames', 'uniformIndices'])
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params(api='gl', prms=['program', 'uniformCount', 'uniformIndices', 'pname', 'params'])
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params):
	pass


@params(api='gl', prms=['program', 'uniformIndex', 'bufSize', 'length', 'uniformName'])
def glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName):
	pass


@params(api='gl', prms=['program', 'uniformBlockName'])
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params(api='gl', prms=['program', 'uniformBlockIndex', 'pname', 'params'])
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params):
	pass


@params(api='gl', prms=['program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName'])
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	pass


@params(api='gl', prms=['program', 'uniformBlockIndex', 'uniformBlockBinding'])
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	pass


@params(api='gl', prms=['target', 'index', 'buffer', 'offset', 'size'])
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params(api='gl', prms=['target', 'index', 'buffer'])
def glBindBufferBase(target, index, buffer):
	pass


@params(api='gl', prms=['target', 'index', 'data'])
def glGetIntegeri_v(target, index, data):
	pass


