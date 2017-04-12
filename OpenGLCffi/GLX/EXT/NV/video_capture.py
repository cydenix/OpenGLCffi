from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'video_capture_slot', 'device'])
def glXBindVideoCaptureDeviceNV(dpy, video_capture_slot, device):
	pass


@params(api='glx', prms=['dpy', 'screen', 'nelements'])
def glXEnumerateVideoCaptureDevicesNV(dpy, screen):
	pass


@params(api='glx', prms=['dpy', 'device'])
def glXLockVideoCaptureDeviceNV(dpy, device):
	pass


@params(api='glx', prms=['dpy', 'device', 'attribute', 'value'])
def glXQueryVideoCaptureDeviceNV(dpy, device, attribute):
	pass


@params(api='glx', prms=['dpy', 'device'])
def glXReleaseVideoCaptureDeviceNV(dpy, device):
	pass


