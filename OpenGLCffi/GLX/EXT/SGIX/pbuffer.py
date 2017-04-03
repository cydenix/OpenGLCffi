from OpenGLCffi.GLX import params
@params('dpy', 'config', 'width', 'height', 'attrib_list', api='glx')
def glXCreateGLXPbufferSGIX(dpy, config, width, height, attrib_list):
	pass


@params('dpy', 'pbuf', api='glx')
def glXDestroyGLXPbufferSGIX(dpy, pbuf):
	pass


@params('dpy', 'pbuf', 'attribute', 'value', api='glx')
def glXQueryGLXPbufferSGIX(dpy, pbuf, attribute):
	pass


@params('dpy', 'drawable', 'mask', api='glx')
def glXSelectEventSGIX(dpy, drawable, mask):
	pass


@params('dpy', 'drawable', 'mask', api='glx')
def glXGetSelectedEventSGIX(dpy, drawable, mask):
	pass


