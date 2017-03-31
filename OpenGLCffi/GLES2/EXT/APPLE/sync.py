@params('condition', 'flags', api='gles2')
def glFenceSyncAPPLE(condition, flags):
	pass


@params('sync', api='gles2')
def glIsSyncAPPLE(sync):
	pass


@params('sync', api='gles2')
def glDeleteSyncAPPLE(sync):
	pass


@params('sync', 'flags', 'timeout', api='gles2')
def glClientWaitSyncAPPLE(sync, flags, timeout):
	pass


@params('sync', 'flags', 'timeout', api='gles2')
def glWaitSyncAPPLE(sync, flags, timeout):
	pass


@params('pname', 'params', api='gles2')
def glGetInteger64vAPPLE(pname):
	pass


@params('sync', 'pname', 'bufSize', 'length', 'values', api='gles2')
def glGetSyncivAPPLE(sync, pname, bufSize, length, values):
	pass


