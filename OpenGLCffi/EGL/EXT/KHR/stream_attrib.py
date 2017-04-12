from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'attrib_list'])
def eglCreateStreamAttribKHR(dpy, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'stream', 'attribute', 'value'])
def eglSetStreamAttribKHR(dpy, stream, attribute):
	pass


@params(api='egl', prms=['dpy', 'stream', 'attribute', 'value'])
def eglQueryStreamAttribKHR(dpy, stream, attribute):
	pass


@params(api='egl', prms=['dpy', 'stream', 'attrib_list'])
def eglStreamConsumerAcquireAttribKHR(dpy, stream, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'stream', 'attrib_list'])
def eglStreamConsumerReleaseAttribKHR(dpy, stream, attrib_list):
	pass


