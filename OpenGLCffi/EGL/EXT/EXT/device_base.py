from OpenGLCffi.EGL import params
@params(api='egl', prms=['device', 'attribute', 'value'])
def eglQueryDeviceAttribEXT(device, attribute):
	pass


@params(api='egl', prms=['device', 'name'])
def eglQueryDeviceStringEXT(device, name):
	pass


@params(api='egl', prms=['max_devices', 'devices', 'num_devices'])
def eglQueryDevicesEXT(max_devices, devices, num_devices):
	pass


@params(api='egl', prms=['dpy', 'attribute', 'value'])
def eglQueryDisplayAttribEXT(dpy, attribute):
	pass


