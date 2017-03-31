@params('dpy', 'attrib_list', api='egl')
def eglCreateStreamAttribKHR(dpy, attrib_list):
	pass


@params('dpy', 'stream', 'attribute', 'value', api='egl')
def eglSetStreamAttribKHR(dpy, stream, attribute):
	pass


@params('dpy', 'stream', 'attribute', 'value', api='egl')
def eglQueryStreamAttribKHR(dpy, stream, attribute):
	pass


@params('dpy', 'stream', 'attrib_list', api='egl')
def eglStreamConsumerAcquireAttribKHR(dpy, stream, attrib_list):
	pass


@params('dpy', 'stream', 'attrib_list', api='egl')
def eglStreamConsumerReleaseAttribKHR(dpy, stream, attrib_list):
	pass


