from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'reset', 'format', 'type', 'values'])
def glGetHistogramEXT(target, reset, format, type, values):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetHistogramParameterfvEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetHistogramParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'reset', 'format', 'type', 'values'])
def glGetMinmaxEXT(target, reset, format, type, values):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetMinmaxParameterfvEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetMinmaxParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'width', 'internalformat', 'sink'])
def glHistogramEXT(target, width, internalformat, sink):
	pass


@params(api='gl', prms=['target', 'internalformat', 'sink'])
def glMinmaxEXT(target, internalformat, sink):
	pass


@params(api='gl', prms=['target'])
def glResetHistogramEXT(target):
	pass


@params(api='gl', prms=['target'])
def glResetMinmaxEXT(target):
	pass


