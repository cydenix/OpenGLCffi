from OpenGLCffi.GL import params
@params(api='gl', prms=['condition', 'flags'])
def glFenceSync(condition, flags):
	pass


@params(api='gl', prms=['sync'])
def glIsSync(sync):
	pass


@params(api='gl', prms=['sync'])
def glDeleteSync(sync):
	pass


@params(api='gl', prms=['sync', 'flags', 'timeout'])
def glClientWaitSync(sync, flags, timeout):
	pass


@params(api='gl', prms=['sync', 'flags', 'timeout'])
def glWaitSync(sync, flags, timeout):
	pass


@params(api='gl', prms=['pname', 'data'])
def glGetInteger64v(pname, data):
	pass


@params(api='gl', prms=['sync', 'pname', 'bufSize', 'length', 'values'])
def glGetSynciv(sync, pname, bufSize, length, values):
	pass


