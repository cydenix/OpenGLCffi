from OpenGLCffi.GLES1 import params
@params('target', 'offset', 'length', 'access', api='gles1')
def glMapBufferRangeEXT(target, offset, length, access):
	pass


@params('target', 'offset', 'length', api='gles1')
def glFlushMappedBufferRangeEXT(target, offset, length):
	pass


