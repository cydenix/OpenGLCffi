from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'image', 'fourcc', 'num_planes', 'modifiers'])
def eglExportDMABUFImageQueryMESA(dpy, image, fourcc, num_planes, modifiers):
	pass


@params(api='egl', prms=['dpy', 'image', 'fds', 'strides', 'offsets'])
def eglExportDMABUFImageMESA(dpy, image, fds, strides, offsets):
	pass


