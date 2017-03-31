@params('dpy', 'attribute', 'value', api='egl')
def eglQueryDisplayAttribNV(dpy, attribute):
	pass


@params('dpy', 'stream', 'n', 'offset', 'size', 'data', api='egl')
def eglSetStreamMetadataNV(dpy, stream, n, offset, size, data):
	pass


@params('dpy', 'stream', 'name', 'n', 'offset', 'size', 'data', api='egl')
def eglQueryStreamMetadataNV(dpy, stream, name, n, offset, size, data):
	pass


