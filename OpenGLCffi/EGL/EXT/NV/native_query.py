from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'display_id'])
def eglQueryNativeDisplayNV(dpy, display_id):
	pass


@params(api='egl', prms=['dpy', 'surf', 'window'])
def eglQueryNativeWindowNV(dpy, surf, window):
	pass


@params(api='egl', prms=['dpy', 'surf', 'pixmap'])
def eglQueryNativePixmapNV(dpy, surf, pixmap):
	pass


