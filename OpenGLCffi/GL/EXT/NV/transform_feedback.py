from OpenGLCffi.GL import params
@params(api='gl', prms=['primitiveMode'])
def glBeginTransformFeedbackNV(primitiveMode):
	pass


@params(api='gl', prms=[])
def glEndTransformFeedbackNV():
	pass


@params(api='gl', prms=['count', 'attribs', 'bufferMode'])
def glTransformFeedbackAttribsNV(count, attribs, bufferMode):
	pass


@params(api='gl', prms=['target', 'index', 'buffer', 'offset', 'size'])
def glBindBufferRangeNV(target, index, buffer, offset, size):
	pass


@params(api='gl', prms=['target', 'index', 'buffer', 'offset'])
def glBindBufferOffsetNV(target, index, buffer, offset):
	pass


@params(api='gl', prms=['target', 'index', 'buffer'])
def glBindBufferBaseNV(target, index, buffer):
	pass


@params(api='gl', prms=['program', 'count', 'locations', 'bufferMode'])
def glTransformFeedbackVaryingsNV(program, count, locations, bufferMode):
	pass


@params(api='gl', prms=['program', 'name'])
def glActiveVaryingNV(program, name):
	pass


@params(api='gl', prms=['program', 'name'])
def glGetVaryingLocationNV(program, name):
	pass


@params(api='gl', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetActiveVaryingNV(program, index, bufSize, length, size, type, name):
	pass


@params(api='gl', prms=['program', 'index', 'location'])
def glGetTransformFeedbackVaryingNV(program, index, location):
	pass


@params(api='gl', prms=['count', 'attribs', 'nbuffers', 'bufstreams', 'bufferMode'])
def glTransformFeedbackStreamAttribsNV(count, attribs, nbuffers, bufstreams, bufferMode):
	pass


