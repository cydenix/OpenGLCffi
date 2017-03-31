@params('device', 'attribute', 'value', api='egl')
def eglQueryDeviceAttribEXT(device, attribute):
	pass


@params('device', 'name', api='egl')
def eglQueryDeviceStringEXT(device, name):
	pass


@params('max_devices', 'devices', 'num_devices', api='egl')
def eglQueryDevicesEXT(max_devices, devices, num_devices):
	pass


@params('dpy', 'attribute', 'value', api='egl')
def eglQueryDisplayAttribEXT(dpy, attribute):
	pass


