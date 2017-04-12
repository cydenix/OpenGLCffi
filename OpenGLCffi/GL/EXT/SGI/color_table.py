from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'internalformat', 'width', 'format', 'type', 'table'])
def glColorTableSGI(target, internalformat, width, format, type, table):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glColorTableParameterfvSGI(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glColorTableParameterivSGI(target, pname, params):
	pass


@params(api='gl', prms=['target', 'internalformat', 'x', 'y', 'width'])
def glCopyColorTableSGI(target, internalformat, x, y, width):
	pass


@params(api='gl', prms=['target', 'format', 'type', 'table'])
def glGetColorTableSGI(target, format, type, table):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetColorTableParameterfvSGI(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetColorTableParameterivSGI(target, pname, params):
	pass


