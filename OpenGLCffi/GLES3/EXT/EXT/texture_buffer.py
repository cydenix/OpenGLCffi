from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'internalformat', 'buffer'])
def glTexBufferEXT(target, internalformat, buffer):
	pass


@params(api='gles3', prms=['target', 'internalformat', 'buffer', 'offset', 'size'])
def glTexBufferRangeEXT(target, internalformat, buffer, offset, size):
	pass


