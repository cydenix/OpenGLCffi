from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'attribute', 'value'])
def eglQueryDisplayAttribNV(dpy, attribute):
	pass


@params(api='egl', prms=['dpy', 'stream', 'n', 'offset', 'size', 'data'])
def eglSetStreamMetadataNV(dpy, stream, n, offset, size, data):
	pass


@params(api='egl', prms=['dpy', 'stream', 'name', 'n', 'offset', 'size', 'data'])
def eglQueryStreamMetadataNV(dpy, stream, name, n, offset, size, data):
	pass


