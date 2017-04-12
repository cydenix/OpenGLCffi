from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'drawable', 'buffer', 'attrib_list'])
def glXBindTexImageEXT(dpy, drawable, buffer, attrib_list):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'buffer'])
def glXReleaseTexImageEXT(dpy, drawable, buffer):
	pass


