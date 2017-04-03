from OpenGLCffi.EGL import params
@params('dpy', 'type', 'attrib_list', api='egl')
def eglCreateSyncKHR(dpy, type, attrib_list):
	pass


@params('dpy', 'sync', api='egl')
def eglDestroySyncKHR(dpy, sync):
	pass


@params('dpy', 'sync', 'flags', 'timeout', api='egl')
def eglClientWaitSyncKHR(dpy, sync, flags, timeout):
	pass


@params('dpy', 'sync', 'mode', api='egl')
def eglSignalSyncKHR(dpy, sync, mode):
	pass


@params('dpy', 'sync', 'attribute', 'value', api='egl')
def eglGetSyncAttribKHR(dpy, sync, attribute):
	pass


