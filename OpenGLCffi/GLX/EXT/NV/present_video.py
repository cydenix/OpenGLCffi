from OpenGLCffi.GLX import params
@params('dpy', 'screen', 'nelements', api='glx')
def glXEnumerateVideoDevicesNV(dpy, screen):
	pass


@params('dpy', 'video_slot', 'video_device', 'attrib_list', api='glx')
def glXBindVideoDeviceNV(dpy, video_slot, video_device, attrib_list):
	pass


