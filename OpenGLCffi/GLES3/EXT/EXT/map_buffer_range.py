from OpenGLCffi.GLES3 import params
@params('target', 'offset', 'length', 'access', api='gles3')
def glMapBufferRangeEXT(target, offset, length, access):
	pass


@params('target', 'offset', 'length', api='gles3')
def glFlushMappedBufferRangeEXT(target, offset, length):
	pass


