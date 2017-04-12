from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'stream'])
def eglGetStreamFileDescriptorKHR(dpy, stream):
	pass


@params(api='egl', prms=['dpy', 'file_descriptor'])
def eglCreateStreamFromFileDescriptorKHR(dpy, file_descriptor):
	pass


