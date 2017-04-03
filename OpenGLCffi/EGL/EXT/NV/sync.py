from OpenGLCffi.EGL import params
@params('dpy', 'condition', 'attrib_list', api='egl')
def eglCreateFenceSyncNV(dpy, condition, attrib_list):
	pass


@params('sync', api='egl')
def eglDestroySyncNV(sync):
	pass


@params('sync', api='egl')
def eglFenceNV(sync):
	pass


@params('sync', 'flags', 'timeout', api='egl')
def eglClientWaitSyncNV(sync, flags, timeout):
	pass


@params('sync', 'mode', api='egl')
def eglSignalSyncNV(sync, mode):
	pass


@params('sync', 'attribute', 'value', api='egl')
def eglGetSyncAttribNV(sync, attribute):
	pass


