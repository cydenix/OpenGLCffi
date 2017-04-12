from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'internalFormat', 'width', 'format', 'type', 'table'])
def glColorTableEXT(target, internalFormat, width, format, type, table):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'data'])
def glGetColorTableEXT(target, format, type, data):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetColorTableParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetColorTableParameterfvEXT(target, pname, params):
	pass


