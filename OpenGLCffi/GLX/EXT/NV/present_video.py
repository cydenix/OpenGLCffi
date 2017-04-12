from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'screen', 'nelements'])
def glXEnumerateVideoDevicesNV(dpy, screen):
	pass


@params(api='glx', prms=['dpy', 'video_slot', 'video_device', 'attrib_list'])
def glXBindVideoDeviceNV(dpy, video_slot, video_device, attrib_list):
	pass


