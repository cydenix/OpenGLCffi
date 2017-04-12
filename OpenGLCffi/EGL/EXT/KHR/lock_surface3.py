from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'surface', 'attrib_list'])
def eglLockSurfaceKHR(dpy, surface, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'surface'])
def eglUnlockSurfaceKHR(dpy, surface):
	pass


@params(api='egl', prms=['dpy', 'surface', 'attribute', 'value'])
def eglQuerySurface64KHR(dpy, surface, attribute):
	pass


