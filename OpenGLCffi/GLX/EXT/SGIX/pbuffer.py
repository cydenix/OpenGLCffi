from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'config', 'width', 'height', 'attrib_list'])
def glXCreateGLXPbufferSGIX(dpy, config, width, height, attrib_list):
	pass


@params(api='glx', prms=['dpy', 'pbuf'])
def glXDestroyGLXPbufferSGIX(dpy, pbuf):
	pass


@params(api='glx', prms=['dpy', 'pbuf', 'attribute', 'value'])
def glXQueryGLXPbufferSGIX(dpy, pbuf, attribute):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'mask'])
def glXSelectEventSGIX(dpy, drawable, mask):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'mask'])
def glXGetSelectedEventSGIX(dpy, drawable, mask):
	pass


