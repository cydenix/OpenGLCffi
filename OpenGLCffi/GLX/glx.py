from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'vis', 'shareList', 'direct'])
def glXCreateContext(dpy, vis, shareList, direct):
	pass


@params(api='glx', prms=['dpy', 'visual', 'pixmap'])
def glXCreateGLXPixmap(dpy, visual, pixmap):
	pass


@params(api='glx', prms=['procName'])
def glXGetProcAddress(procName):
	pass


@params(api='glx', prms=['dpy', 'win'])
def glXDestroyWindow(dpy, win):
	pass


@params(api='glx', prms=['dpy', 'draw', 'attribute', 'value'])
def glXQueryDrawable(dpy, draw, attribute):
	pass


@params(api='glx', prms=['dpy', 'drawable'])
def glXSwapBuffers(dpy, drawable):
	pass


@params(api='glx', prms=[])
def glXGetCurrentDisplay():
	pass


@params(api='glx', prms=['dpy', 'screen', 'attribList'])
def glXChooseVisual(dpy, screen, attribList):
	pass


@params(api='glx', prms=['dpy', 'pbuf'])
def glXDestroyPbuffer(dpy, pbuf):
	pass


@params(api='glx', prms=['dpy', 'config', 'pixmap', 'attrib_list'])
def glXCreatePixmap(dpy, config, pixmap, attrib_list):
	pass


@params(api='glx', prms=['dpy', 'draw', 'event_mask'])
def glXSelectEvent(dpy, draw, event_mask):
	pass


@params(api='glx', prms=['dpy', 'draw', 'event_mask'])
def glXGetSelectedEvent(dpy, draw, event_mask):
	pass


@params(api='glx', prms=['dpy', 'errorb', 'event'])
def glXQueryExtension(dpy):
	pass


@params(api='glx', prms=['dpy', 'drawable', 'ctx'])
def glXMakeCurrent(dpy, drawable, ctx):
	pass


@params(api='glx', prms=['dpy', 'config', 'attrib_list'])
def glXCreatePbuffer(dpy, config, attrib_list):
	pass


@params(api='glx', prms=['dpy', 'pixmap'])
def glXDestroyGLXPixmap(dpy, pixmap):
	pass


@params(api='glx', prms=['dpy', 'screen', 'attrib_list', 'nelements'])
def glXChooseFBConfig(dpy, screen, attrib_list):
	pass


@params(api='glx', prms=['dpy', 'visual', 'attrib', 'value'])
def glXGetConfig(dpy, visual, attrib):
	pass


@params(api='glx', prms=[])
def glXWaitX():
	pass


@params(api='glx', prms=[])
def glXGetCurrentContext():
	pass


@params(api='glx', prms=[])
def glXWaitGL():
	pass


@params(api='glx', prms=['dpy', 'maj', 'min'])
def glXQueryVersion(dpy):
	pass


@params(api='glx', prms=['dpy', 'pixmap'])
def glXDestroyPixmap(dpy, pixmap):
	pass


@params(api='glx', prms=['dpy', 'ctx'])
def glXIsDirect(dpy, ctx):
	pass


@params(api='glx', prms=['dpy', 'ctx'])
def glXDestroyContext(dpy, ctx):
	pass


@params(api='glx', prms=['dpy', 'config', 'render_type', 'share_list', 'direct'])
def glXCreateNewContext(dpy, config, render_type, share_list, direct):
	pass


@params(api='glx', prms=['dpy', 'name'])
def glXGetClientString(dpy):
	pass


@params(api='glx', prms=['dpy', 'config'])
def glXGetVisualFromFBConfig(dpy, config):
	pass


@params(api='glx', prms=['dpy', 'screen', 'nelements'])
def glXGetFBConfigs(dpy, screen):
	pass


@params(api='glx', prms=[])
def glXGetCurrentReadDrawable():
	pass


@params(api='glx', prms=['dpy', 'ctx', 'attribute', 'value'])
def glXQueryContext(dpy, ctx, attribute):
	pass


@params(api='glx', prms=['dpy', 'config', 'win', 'attrib_list'])
def glXCreateWindow(dpy, config, win, attrib_list):
	pass


@params(api='glx', prms=['dpy', 'src', 'dst', 'mask'])
def glXCopyContext(dpy, src, dst, mask):
	pass


@params(api='glx', prms=['dpy', 'screen', 'name'])
def glXQueryServerString(dpy, screen):
	pass


@params(api='glx', prms=['dpy', 'config', 'attribute', 'value'])
def glXGetFBConfigAttrib(dpy, config, attribute):
	pass


@params(api='glx', prms=['font', 'first', 'count', 'list'])
def glXUseXFont(font, first, count, list):
	pass


@params(api='glx', prms=['dpy', 'draw', 'read', 'ctx'])
def glXMakeContextCurrent(dpy, draw, read, ctx):
	pass


@params(api='glx', prms=[])
def glXGetCurrentDrawable():
	pass


@params(api='glx', prms=['dpy', 'screen'])
def glXQueryExtensionsString(dpy, screen):
	pass


