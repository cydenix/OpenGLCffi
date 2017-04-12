from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'buffer'])
def glBindBufferARB(target, buffer):
	pass


@params(api='gl', prms=['n', 'buffers'])
def glDeleteBuffersARB(n, buffers):
	pass


@params(api='gl', prms=['n', 'buffers'])
def glGenBuffersARB(n, buffers):
	pass


@params(api='gl', prms=['buffer'])
def glIsBufferARB(buffer):
	pass


@params(api='gl', prms=['target', 'size', 'data', 'usage'])
def glBufferDataARB(target, size, data, usage):
	pass


@params(api='gl', prms=['target', 'offset', 'size', 'data'])
def glBufferSubDataARB(target, offset, size, data):
	pass


@params(api='gl', prms=['target', 'offset', 'size', 'data'])
def glGetBufferSubDataARB(target, offset, size, data):
	pass


@params(api='gl', prms=['target', 'access'])
def glMapBufferARB(target, access):
	pass


@params(api='gl', prms=['target'])
def glUnmapBufferARB(target):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetBufferParameterivARB(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetBufferPointervARB(target, pname, params):
	pass


