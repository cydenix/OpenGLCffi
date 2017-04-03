from OpenGLCffi.GL import params
@params('target', 'offset', 'length', 'access', api='gl')
def glMapBufferRange(target, offset, length, access):
	pass


@params('target', 'offset', 'length', api='gl')
def glFlushMappedBufferRange(target, offset, length):
	pass


