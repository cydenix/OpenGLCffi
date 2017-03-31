@params('dpy', 'surface', 'attrib_list', api='egl')
def eglLockSurfaceKHR(dpy, surface, attrib_list):
	pass


@params('dpy', 'surface', api='egl')
def eglUnlockSurfaceKHR(dpy, surface):
	pass


@params('dpy', 'surface', 'attribute', 'value', api='egl')
def eglQuerySurface64KHR(dpy, surface, attribute):
	pass


