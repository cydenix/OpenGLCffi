from OpenGLCffi.GLX import params
@params('dpy', 'vis', 'shareList', 'direct', api='glx')
def glXCreateContext(dpy, vis, shareList, direct):
	pass


@params('dpy', 'visual', 'pixmap', api='glx')
def glXCreateGLXPixmap(dpy, visual, pixmap):
	pass


@params('procName', api='glx')
def glXGetProcAddress(procName):
	pass


@params('dpy', 'win', api='glx')
def glXDestroyWindow(dpy, win):
	pass


@params('dpy', 'draw', 'attribute', 'value', api='glx')
def glXQueryDrawable(dpy, draw, attribute):
	pass


@params('dpy', 'drawable', api='glx')
def glXSwapBuffers(dpy, drawable):
	pass


@params(api = 'glx')
def glXGetCurrentDisplay():
	pass


@params('dpy', 'screen', 'attribList', api='glx')
def glXChooseVisual(dpy, screen, attribList):
	pass


@params('dpy', 'pbuf', api='glx')
def glXDestroyPbuffer(dpy, pbuf):
	pass


@params('dpy', 'config', 'pixmap', 'attrib_list', api='glx')
def glXCreatePixmap(dpy, config, pixmap, attrib_list):
	pass


@params('dpy', 'draw', 'event_mask', api='glx')
def glXSelectEvent(dpy, draw, event_mask):
	pass


@params('dpy', 'draw', 'event_mask', api='glx')
def glXGetSelectedEvent(dpy, draw, event_mask):
	pass


@params('dpy', 'errorb', 'event', api='glx')
def glXQueryExtension(dpy):
	pass


@params('dpy', 'drawable', 'ctx', api='glx')
def glXMakeCurrent(dpy, drawable, ctx):
	pass


@params('dpy', 'config', 'attrib_list', api='glx')
def glXCreatePbuffer(dpy, config, attrib_list):
	pass


@params('dpy', 'pixmap', api='glx')
def glXDestroyGLXPixmap(dpy, pixmap):
	pass


@params('dpy', 'screen', 'attrib_list', 'nelements', api='glx')
def glXChooseFBConfig(dpy, screen, attrib_list):
	pass


@params('dpy', 'visual', 'attrib', 'value', api='glx')
def glXGetConfig(dpy, visual, attrib):
	pass


@params(api = 'glx')
def glXWaitX():
	pass


@params(api = 'glx')
def glXGetCurrentContext():
	pass


@params(api = 'glx')
def glXWaitGL():
	pass


@params('dpy', 'maj', 'min', api='glx')
def glXQueryVersion(dpy):
	pass


@params('dpy', 'pixmap', api='glx')
def glXDestroyPixmap(dpy, pixmap):
	pass


@params('dpy', 'ctx', api='glx')
def glXIsDirect(dpy, ctx):
	pass


@params('dpy', 'ctx', api='glx')
def glXDestroyContext(dpy, ctx):
	pass


@params('dpy', 'config', 'render_type', 'share_list', 'direct', api='glx')
def glXCreateNewContext(dpy, config, render_type, share_list, direct):
	pass


@params('dpy', 'name', api='glx')
def glXGetClientString(dpy):
	pass


@params('dpy', 'config', api='glx')
def glXGetVisualFromFBConfig(dpy, config):
	pass


@params('dpy', 'screen', 'nelements', api='glx')
def glXGetFBConfigs(dpy, screen):
	pass


@params(api = 'glx')
def glXGetCurrentReadDrawable():
	pass


@params('dpy', 'ctx', 'attribute', 'value', api='glx')
def glXQueryContext(dpy, ctx, attribute):
	pass


@params('dpy', 'config', 'win', 'attrib_list', api='glx')
def glXCreateWindow(dpy, config, win, attrib_list):
	pass


@params('dpy', 'src', 'dst', 'mask', api='glx')
def glXCopyContext(dpy, src, dst, mask):
	pass


@params('dpy', 'screen', 'name', api='glx')
def glXQueryServerString(dpy, screen):
	pass


@params('dpy', 'config', 'attribute', 'value', api='glx')
def glXGetFBConfigAttrib(dpy, config, attribute):
	pass


@params('font', 'first', 'count', 'list', api='glx')
def glXUseXFont(font, first, count, list):
	pass


@params('dpy', 'draw', 'read', 'ctx', api='glx')
def glXMakeContextCurrent(dpy, draw, read, ctx):
	pass


@params(api = 'glx')
def glXGetCurrentDrawable():
	pass


@params('dpy', 'screen', api='glx')
def glXQueryExtensionsString(dpy, screen):
	pass


