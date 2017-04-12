from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'config', 'attribute', 'value'])
def glXGetFBConfigAttribSGIX(dpy, config, attribute):
	pass


@params(api='glx', prms=['dpy', 'screen', 'attrib_list', 'nelements'])
def glXChooseFBConfigSGIX(dpy, screen, attrib_list):
	pass


@params(api='glx', prms=['dpy', 'config', 'pixmap'])
def glXCreateGLXPixmapWithConfigSGIX(dpy, config, pixmap):
	pass


@params(api='glx', prms=['dpy', 'config', 'render_type', 'share_list', 'direct'])
def glXCreateContextWithConfigSGIX(dpy, config, render_type, share_list, direct):
	pass


@params(api='glx', prms=['dpy', 'config'])
def glXGetVisualFromFBConfigSGIX(dpy, config):
	pass


@params(api='glx', prms=['dpy', 'vis'])
def glXGetFBConfigFromVisualSGIX(dpy, vis):
	pass


