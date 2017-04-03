from OpenGLCffi.GLES2 import params
@params('target', 'internalformat', 'buffer', api='gles2')
def glTexBufferEXT(target, internalformat, buffer):
	pass


@params('target', 'internalformat', 'buffer', 'offset', 'size', api='gles2')
def glTexBufferRangeEXT(target, internalformat, buffer, offset, size):
	pass


