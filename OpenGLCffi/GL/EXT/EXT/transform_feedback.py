from OpenGLCffi.GL import params
@params(api='gl', prms=['primitiveMode'])
def glBeginTransformFeedbackEXT(primitiveMode):
	pass


@params(api='gl', prms=[])
def glEndTransformFeedbackEXT():
	pass


@params(api='gl', prms=['target', 'index', 'buffer', 'offset', 'size'])
def glBindBufferRangeEXT(target, index, buffer, offset, size):
	pass


@params(api='gl', prms=['target', 'index', 'buffer', 'offset'])
def glBindBufferOffsetEXT(target, index, buffer, offset):
	pass


@params(api='gl', prms=['target', 'index', 'buffer'])
def glBindBufferBaseEXT(target, index, buffer):
	pass


@params(api='gl', prms=['program', 'count', 'constvaryings', 'bufferMode'])
def glTransformFeedbackVaryingsEXT(program, count, constvaryings, bufferMode):
	pass


@params(api='gl', prms=['program', 'index', 'bufSize', 'length', 'size', 'type', 'name'])
def glGetTransformFeedbackVaryingEXT(program, index, bufSize, length, size, type, name):
	pass


