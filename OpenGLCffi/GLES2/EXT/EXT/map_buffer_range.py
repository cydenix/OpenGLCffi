from OpenGLCffi.GLES2 import params
@params('target', 'offset', 'length', 'access', api='gles2')
def glMapBufferRangeEXT(target, offset, length, access):
	pass


@params('target', 'offset', 'length', api='gles2')
def glFlushMappedBufferRangeEXT(target, offset, length):
	pass


