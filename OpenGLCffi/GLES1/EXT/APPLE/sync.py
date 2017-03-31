@params('condition', 'flags', api='gles1')
def glFenceSyncAPPLE(condition, flags):
	pass


@params('sync', api='gles1')
def glIsSyncAPPLE(sync):
	pass


@params('sync', api='gles1')
def glDeleteSyncAPPLE(sync):
	pass


@params('sync', 'flags', 'timeout', api='gles1')
def glClientWaitSyncAPPLE(sync, flags, timeout):
	pass


@params('sync', 'flags', 'timeout', api='gles1')
def glWaitSyncAPPLE(sync, flags, timeout):
	pass


@params('pname', 'params', api='gles1')
def glGetInteger64vAPPLE(pname):
	pass


@params('sync', 'pname', 'bufSize', 'length', 'values', api='gles1')
def glGetSyncivAPPLE(sync, pname, bufSize, length, values):
	pass


