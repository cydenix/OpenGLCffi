from OpenGLCffi.GL import params
@params('target', 'buffer', api='gl')
def glBindBufferARB(target, buffer):
	pass


@params('n', 'buffers', api='gl')
def glDeleteBuffersARB(n, buffers):
	pass


@params('n', 'buffers', api='gl')
def glGenBuffersARB(n, buffers):
	pass


@params('buffer', api='gl')
def glIsBufferARB(buffer):
	pass


@params('target', 'size', 'data', 'usage', api='gl')
def glBufferDataARB(target, size, data, usage):
	pass


@params('target', 'offset', 'size', 'data', api='gl')
def glBufferSubDataARB(target, offset, size, data):
	pass


@params('target', 'offset', 'size', 'data', api='gl')
def glGetBufferSubDataARB(target, offset, size, data):
	pass


@params('target', 'access', api='gl')
def glMapBufferARB(target, access):
	pass


@params('target', api='gl')
def glUnmapBufferARB(target):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetBufferParameterivARB(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetBufferPointervARB(target, pname, params):
	pass


