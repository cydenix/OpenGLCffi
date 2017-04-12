from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'internalformat', 'format', 'type', 'data'])
def glClearBufferData(target, internalformat, format, type, data):
	pass


@params(api='gl', prms=['target', 'internalformat', 'offset', 'size', 'format', 'type', 'data'])
def glClearBufferSubData(target, internalformat, offset, size, format, type, data):
	pass


