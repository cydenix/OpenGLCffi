from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['condition', 'flags'])
def glFenceSyncAPPLE(condition, flags):
	pass


@params(api='gles3', prms=['sync'])
def glIsSyncAPPLE(sync):
	pass


@params(api='gles3', prms=['sync'])
def glDeleteSyncAPPLE(sync):
	pass


@params(api='gles3', prms=['sync', 'flags', 'timeout'])
def glClientWaitSyncAPPLE(sync, flags, timeout):
	pass


@params(api='gles3', prms=['sync', 'flags', 'timeout'])
def glWaitSyncAPPLE(sync, flags, timeout):
	pass


@params(api='gles3', prms=['pname', 'params'])
def glGetInteger64vAPPLE(pname):
	pass


@params(api='gles3', prms=['sync', 'pname', 'bufSize', 'length', 'values'])
def glGetSyncivAPPLE(sync, pname, bufSize, length, values):
	pass


