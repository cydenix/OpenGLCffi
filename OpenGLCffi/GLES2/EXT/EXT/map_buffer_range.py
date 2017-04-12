from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'offset', 'length', 'access'])
def glMapBufferRangeEXT(target, offset, length, access):
	pass


@params(api='gles2', prms=['target', 'offset', 'length'])
def glFlushMappedBufferRangeEXT(target, offset, length):
	pass


