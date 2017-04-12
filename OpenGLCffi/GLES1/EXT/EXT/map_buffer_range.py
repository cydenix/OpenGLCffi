from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['target', 'offset', 'length', 'access'])
def glMapBufferRangeEXT(target, offset, length, access):
	pass


@params(api='gles1', prms=['target', 'offset', 'length'])
def glFlushMappedBufferRangeEXT(target, offset, length):
	pass


