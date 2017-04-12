from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'screen', 'numVideoDevices', 'pVideoDevice'])
def glXGetVideoDeviceNV(dpy, screen, numVideoDevices, pVideoDevice):
	pass


@params(api='glx', prms=['dpy', 'screen', 'VideoDevice'])
def glXReleaseVideoDeviceNV(dpy, screen, VideoDevice):
	pass


@params(api='glx', prms=['dpy', 'VideoDevice', 'pbuf', 'iVideoBuffer'])
def glXBindVideoImageNV(dpy, VideoDevice, pbuf, iVideoBuffer):
	pass


@params(api='glx', prms=['dpy', 'pbuf'])
def glXReleaseVideoImageNV(dpy, pbuf):
	pass


@params(api='glx', prms=['dpy', 'pbuf', 'iBufferType', 'pulCounterPbuffer', 'bBlock'])
def glXSendPbufferToVideoNV(dpy, pbuf, iBufferType, pulCounterPbuffer, bBlock):
	pass


@params(api='glx', prms=['dpy', 'screen', 'VideoDevice', 'pulCounterOutputPbuffer', 'pulCounterOutputVideo'])
def glXGetVideoInfoNV(dpy, screen, VideoDevice, pulCounterOutputPbuffer, pulCounterOutputVideo):
	pass


