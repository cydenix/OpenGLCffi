from OpenGLCffi.EGL import params
@params('dpy', 'display_id', api='egl')
def eglQueryNativeDisplayNV(dpy, display_id):
	pass


@params('dpy', 'surf', 'window', api='egl')
def eglQueryNativeWindowNV(dpy, surf, window):
	pass


@params('dpy', 'surf', 'pixmap', api='egl')
def eglQueryNativePixmapNV(dpy, surf, pixmap):
	pass


