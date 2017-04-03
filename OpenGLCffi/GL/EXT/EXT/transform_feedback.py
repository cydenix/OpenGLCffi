from OpenGLCffi.GL import params
@params('primitiveMode', api='gl')
def glBeginTransformFeedbackEXT(primitiveMode):
	pass


@params(api = 'gl')
def glEndTransformFeedbackEXT():
	pass


@params('target', 'index', 'buffer', 'offset', 'size', api='gl')
def glBindBufferRangeEXT(target, index, buffer, offset, size):
	pass


@params('target', 'index', 'buffer', 'offset', api='gl')
def glBindBufferOffsetEXT(target, index, buffer, offset):
	pass


@params('target', 'index', 'buffer', api='gl')
def glBindBufferBaseEXT(target, index, buffer):
	pass


@params('program', 'count', 'constvaryings', 'bufferMode', api='gl')
def glTransformFeedbackVaryingsEXT(program, count, constvaryings, bufferMode):
	pass


@params('program', 'index', 'bufSize', 'length', 'size', 'type', 'name', api='gl')
def glGetTransformFeedbackVaryingEXT(program, index, bufSize, length, size, type, name):
	pass


