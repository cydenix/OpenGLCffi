from OpenGLCffi.EGL import params
@params('device', 'attribute', 'value', api='egl')
def eglQueryDeviceAttribEXT(device, attribute):
	pass


@params('device', 'name', api='egl')
def eglQueryDeviceStringEXT(device, name):
	pass


@params('dpy', 'attribute', 'value', api='egl')
def eglQueryDisplayAttribEXT(dpy, attribute):
	pass


