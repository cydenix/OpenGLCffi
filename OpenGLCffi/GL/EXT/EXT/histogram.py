from OpenGLCffi.GL import params
@params('target', 'reset', 'format', 'type', 'values', api='gl')
def glGetHistogramEXT(target, reset, format, type, values):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetHistogramParameterfvEXT(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetHistogramParameterivEXT(target, pname, params):
	pass


@params('target', 'reset', 'format', 'type', 'values', api='gl')
def glGetMinmaxEXT(target, reset, format, type, values):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetMinmaxParameterfvEXT(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetMinmaxParameterivEXT(target, pname, params):
	pass


@params('target', 'width', 'internalformat', 'sink', api='gl')
def glHistogramEXT(target, width, internalformat, sink):
	pass


@params('target', 'internalformat', 'sink', api='gl')
def glMinmaxEXT(target, internalformat, sink):
	pass


@params('target', api='gl')
def glResetHistogramEXT(target):
	pass


@params('target', api='gl')
def glResetMinmaxEXT(target):
	pass


