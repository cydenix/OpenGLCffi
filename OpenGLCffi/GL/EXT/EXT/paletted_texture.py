@params('target', 'internalFormat', 'width', 'format', 'type', 'table', api='gl')
def glColorTableEXT(target, internalFormat, width, format, type, table):
	pass


@params('target', 'format', 'type', 'data', api='gl')
def glGetColorTableEXT(target, format, type, data):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetColorTableParameterivEXT(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetColorTableParameterfvEXT(target, pname, params):
	pass


