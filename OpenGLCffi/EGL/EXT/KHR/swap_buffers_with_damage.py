from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'surface', 'rects', 'n_rects'])
def eglSwapBuffersWithDamageKHR(dpy, surface, rects, n_rects):
	pass


