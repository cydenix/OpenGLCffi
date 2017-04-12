from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'stream'])
def eglStreamConsumerGLTextureExternalKHR(dpy, stream):
	pass


@params(api='egl', prms=['dpy', 'stream'])
def eglStreamConsumerAcquireKHR(dpy, stream):
	pass


@params(api='egl', prms=['dpy', 'stream'])
def eglStreamConsumerReleaseKHR(dpy, stream):
	pass


