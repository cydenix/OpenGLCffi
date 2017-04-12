from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'ctx', 'target', 'buffer', 'attrib_list'])
def eglCreateImageKHR(dpy, ctx, target, buffer, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'image'])
def eglDestroyImageKHR(dpy, image):
	pass


