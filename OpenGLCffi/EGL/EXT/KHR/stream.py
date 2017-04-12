from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'attrib_list'])
def eglCreateStreamKHR(dpy, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'stream'])
def eglDestroyStreamKHR(dpy, stream):
	pass


@params(api='egl', prms=['dpy', 'stream', 'attribute', 'value'])
def eglStreamAttribKHR(dpy, stream, attribute):
	pass


@params(api='egl', prms=['dpy', 'stream', 'attribute', 'value'])
def eglQueryStreamKHR(dpy, stream, attribute):
	pass


@params(api='egl', prms=['dpy', 'stream', 'attribute', 'value'])
def eglQueryStreamu64KHR(dpy, stream, attribute):
	pass


