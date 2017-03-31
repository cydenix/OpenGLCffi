@params('condition', 'flags', api='gles3')
def glFenceSyncAPPLE(condition, flags):
	pass


@params('sync', api='gles3')
def glIsSyncAPPLE(sync):
	pass


@params('sync', api='gles3')
def glDeleteSyncAPPLE(sync):
	pass


@params('sync', 'flags', 'timeout', api='gles3')
def glClientWaitSyncAPPLE(sync, flags, timeout):
	pass


@params('sync', 'flags', 'timeout', api='gles3')
def glWaitSyncAPPLE(sync, flags, timeout):
	pass


@params('pname', 'params', api='gles3')
def glGetInteger64vAPPLE(pname):
	pass


@params('sync', 'pname', 'bufSize', 'length', 'values', api='gles3')
def glGetSyncivAPPLE(sync, pname, bufSize, length, values):
	pass


