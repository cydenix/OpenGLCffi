from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'type', 'attrib_list'])
def eglCreateSyncKHR(dpy, type, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'sync'])
def eglDestroySyncKHR(dpy, sync):
	pass


@params(api='egl', prms=['dpy', 'sync', 'flags', 'timeout'])
def eglClientWaitSyncKHR(dpy, sync, flags, timeout):
	pass


@params(api='egl', prms=['dpy', 'sync', 'attribute', 'value'])
def eglGetSyncAttribKHR(dpy, sync, attribute):
	pass


