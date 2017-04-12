from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'internalformat', 'buffer'])
def glTexBufferOES(target, internalformat, buffer):
	pass


@params(api='gles3', prms=['target', 'internalformat', 'buffer', 'offset', 'size'])
def glTexBufferRangeOES(target, internalformat, buffer, offset, size):
	pass


