from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'offset', 'length', 'access'])
def glMapBufferRange(target, offset, length, access):
	pass


@params(api='gl', prms=['target', 'offset', 'length'])
def glFlushMappedBufferRange(target, offset, length):
	pass


