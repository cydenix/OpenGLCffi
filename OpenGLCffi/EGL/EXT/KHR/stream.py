@params('dpy', 'attrib_list', api='egl')
def eglCreateStreamKHR(dpy, attrib_list):
	pass


@params('dpy', 'stream', api='egl')
def eglDestroyStreamKHR(dpy, stream):
	pass


@params('dpy', 'stream', 'attribute', 'value', api='egl')
def eglStreamAttribKHR(dpy, stream, attribute):
	pass


@params('dpy', 'stream', 'attribute', 'value', api='egl')
def eglQueryStreamKHR(dpy, stream, attribute):
	pass


@params('dpy', 'stream', 'attribute', 'value', api='egl')
def eglQueryStreamu64KHR(dpy, stream, attribute):
	pass


