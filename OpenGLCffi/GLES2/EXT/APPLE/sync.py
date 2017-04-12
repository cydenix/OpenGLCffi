from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['condition', 'flags'])
def glFenceSyncAPPLE(condition, flags):
	pass


@params(api='gles2', prms=['sync'])
def glIsSyncAPPLE(sync):
	pass


@params(api='gles2', prms=['sync'])
def glDeleteSyncAPPLE(sync):
	pass


@params(api='gles2', prms=['sync', 'flags', 'timeout'])
def glClientWaitSyncAPPLE(sync, flags, timeout):
	pass


@params(api='gles2', prms=['sync', 'flags', 'timeout'])
def glWaitSyncAPPLE(sync, flags, timeout):
	pass


@params(api='gles2', prms=['pname', 'params'])
def glGetInteger64vAPPLE(pname):
	pass


@params(api='gles2', prms=['sync', 'pname', 'bufSize', 'length', 'values'])
def glGetSyncivAPPLE(sync, pname, bufSize, length, values):
	pass


