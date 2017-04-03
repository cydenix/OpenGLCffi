from OpenGLCffi.GLX import params
@params('dpy', 'video_capture_slot', 'device', api='glx')
def glXBindVideoCaptureDeviceNV(dpy, video_capture_slot, device):
	pass


@params('dpy', 'screen', 'nelements', api='glx')
def glXEnumerateVideoCaptureDevicesNV(dpy, screen):
	pass


@params('dpy', 'device', api='glx')
def glXLockVideoCaptureDeviceNV(dpy, device):
	pass


@params('dpy', 'device', 'attribute', 'value', api='glx')
def glXQueryVideoCaptureDeviceNV(dpy, device, attribute):
	pass


@params('dpy', 'device', api='glx')
def glXReleaseVideoCaptureDeviceNV(dpy, device):
	pass


