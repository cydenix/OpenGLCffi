from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'offset', 'length', 'access'])
def glMapBufferRangeEXT(target, offset, length, access):
	pass


@params(api='gles3', prms=['target', 'offset', 'length'])
def glFlushMappedBufferRangeEXT(target, offset, length):
	pass


