@params('target', 'internalformat', 'width', 'format', 'type', 'table', api='gl')
def glColorTableSGI(target, internalformat, width, format, type, table):
	pass


@params('target', 'pname', 'params', api='gl')
def glColorTableParameterfvSGI(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glColorTableParameterivSGI(target, pname, params):
	pass


@params('target', 'internalformat', 'x', 'y', 'width', api='gl')
def glCopyColorTableSGI(target, internalformat, x, y, width):
	pass


@params('target', 'format', 'type', 'table', api='gl')
def glGetColorTableSGI(target, format, type, table):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetColorTableParameterfvSGI(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetColorTableParameterivSGI(target, pname, params):
	pass


