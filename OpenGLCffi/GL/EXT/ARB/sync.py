@params('condition', 'flags', api='gl')
def glFenceSync(condition, flags):
	pass


@params('sync', api='gl')
def glIsSync(sync):
	pass


@params('sync', api='gl')
def glDeleteSync(sync):
	pass


@params('sync', 'flags', 'timeout', api='gl')
def glClientWaitSync(sync, flags, timeout):
	pass


@params('sync', 'flags', 'timeout', api='gl')
def glWaitSync(sync, flags, timeout):
	pass


@params('pname', 'data', api='gl')
def glGetInteger64v(pname, data):
	pass


@params('sync', 'pname', 'bufSize', 'length', 'values', api='gl')
def glGetSynciv(sync, pname, bufSize, length, values):
	pass


