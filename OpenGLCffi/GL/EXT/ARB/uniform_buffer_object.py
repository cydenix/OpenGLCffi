@params('program', 'uniformCount', 'constuniformNames', 'uniformIndices', api='gl')
def glGetUniformIndices(program, uniformCount, constuniformNames, uniformIndices):
	pass


@params('program', 'uniformCount', 'uniformIndices', 'pname', 'params', api='gl')
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params):
	pass


@params('program', 'uniformIndex', 'bufSize', 'length', 'uniformName', api='gl')
def glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName):
	pass


@params('program', 'uniformBlockName', api='gl')
def glGetUniformBlockIndex(program, uniformBlockName):
	pass


@params('program', 'uniformBlockIndex', 'pname', 'params', api='gl')
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params):
	pass


@params('program', 'uniformBlockIndex', 'bufSize', 'length', 'uniformBlockName', api='gl')
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
	pass


@params('program', 'uniformBlockIndex', 'uniformBlockBinding', api='gl')
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
	pass


@params('target', 'index', 'buffer', 'offset', 'size', api='gl')
def glBindBufferRange(target, index, buffer, offset, size):
	pass


@params('target', 'index', 'buffer', api='gl')
def glBindBufferBase(target, index, buffer):
	pass


@params('target', 'index', 'data', api='gl')
def glGetIntegeri_v(target, index, data):
	pass


