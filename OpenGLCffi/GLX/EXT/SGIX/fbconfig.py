from OpenGLCffi.GLX import params
@params('dpy', 'config', 'attribute', 'value', api='glx')
def glXGetFBConfigAttribSGIX(dpy, config, attribute):
	pass


@params('dpy', 'screen', 'attrib_list', 'nelements', api='glx')
def glXChooseFBConfigSGIX(dpy, screen, attrib_list):
	pass


@params('dpy', 'config', 'pixmap', api='glx')
def glXCreateGLXPixmapWithConfigSGIX(dpy, config, pixmap):
	pass


@params('dpy', 'config', 'render_type', 'share_list', 'direct', api='glx')
def glXCreateContextWithConfigSGIX(dpy, config, render_type, share_list, direct):
	pass


@params('dpy', 'config', api='glx')
def glXGetVisualFromFBConfigSGIX(dpy, config):
	pass


@params('dpy', 'vis', api='glx')
def glXGetFBConfigFromVisualSGIX(dpy, vis):
	pass


