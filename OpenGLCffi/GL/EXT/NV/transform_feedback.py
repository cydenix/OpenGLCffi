@params('primitiveMode', api='gl')
def glBeginTransformFeedbackNV(primitiveMode):
	pass


@params(api = 'gl')
def glEndTransformFeedbackNV():
	pass


@params('count', 'attribs', 'bufferMode', api='gl')
def glTransformFeedbackAttribsNV(count, attribs, bufferMode):
	pass


@params('target', 'index', 'buffer', 'offset', 'size', api='gl')
def glBindBufferRangeNV(target, index, buffer, offset, size):
	pass


@params('target', 'index', 'buffer', 'offset', api='gl')
def glBindBufferOffsetNV(target, index, buffer, offset):
	pass


@params('target', 'index', 'buffer', api='gl')
def glBindBufferBaseNV(target, index, buffer):
	pass


@params('program', 'count', 'locations', 'bufferMode', api='gl')
def glTransformFeedbackVaryingsNV(program, count, locations, bufferMode):
	pass


@params('program', 'name', api='gl')
def glActiveVaryingNV(program, name):
	pass


@params('program', 'name', api='gl')
def glGetVaryingLocationNV(program, name):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gl')
def glGetActiveVaryingNV(program, index, bufSize, length, size, type, name):
	pass


@params('program', 'index', 'location', api='gl')
def glGetTransformFeedbackVaryingNV(program, index, location):
	pass


@params('count', 'attribs', 'nbuffers', 'bufstreams', 'bufferMode', api='gl')
def glTransformFeedbackStreamAttribsNV(count, attribs, nbuffers, bufstreams, bufferMode):
	pass


