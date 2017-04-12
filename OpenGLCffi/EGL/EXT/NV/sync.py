from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'condition', 'attrib_list'])
def eglCreateFenceSyncNV(dpy, condition, attrib_list):
	pass


@params(api='egl', prms=['sync'])
def eglDestroySyncNV(sync):
	pass


@params(api='egl', prms=['sync'])
def eglFenceNV(sync):
	pass


@params(api='egl', prms=['sync', 'flags', 'timeout'])
def eglClientWaitSyncNV(sync, flags, timeout):
	pass


@params(api='egl', prms=['sync', 'mode'])
def eglSignalSyncNV(sync, mode):
	pass


@params(api='egl', prms=['sync', 'attribute', 'value'])
def eglGetSyncAttribNV(sync, attribute):
	pass


