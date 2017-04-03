from OpenGLCffi.GLX import params
@params('dpy', 'screen', 'numVideoDevices', 'pVideoDevice', api='glx')
def glXGetVideoDeviceNV(dpy, screen, numVideoDevices, pVideoDevice):
	pass


@params('dpy', 'screen', 'VideoDevice', api='glx')
def glXReleaseVideoDeviceNV(dpy, screen, VideoDevice):
	pass


@params('dpy', 'VideoDevice', 'pbuf', 'iVideoBuffer', api='glx')
def glXBindVideoImageNV(dpy, VideoDevice, pbuf, iVideoBuffer):
	pass


@params('dpy', 'pbuf', api='glx')
def glXReleaseVideoImageNV(dpy, pbuf):
	pass


@params('dpy', 'pbuf', 'iBufferType', 'pulCounterPbuffer', 'bBlock', api='glx')
def glXSendPbufferToVideoNV(dpy, pbuf, iBufferType, pulCounterPbuffer, bBlock):
	pass


@params('dpy', 'screen', 'VideoDevice', 'pulCounterOutputPbuffer', 'pulCounterOutputVideo', api='glx')
def glXGetVideoInfoNV(dpy, screen, VideoDevice, pulCounterOutputPbuffer, pulCounterOutputVideo):
	pass


