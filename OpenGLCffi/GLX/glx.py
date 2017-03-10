@params('dpy', 'vis', 'shareList', 'direct')
def glXCreateContext(dpy, vis, shareList, direct):
	pass


@params('dpy', 'visual', 'pixmap')
def glXCreateGLXPixmap(dpy, visual, pixmap):
	pass


@params('procName',)
def glXGetProcAddress(procName):
	pass


@params('dpy', 'win')
def glXDestroyWindow(dpy, win):
	pass


@params('dpy', 'draw', 'attribute', 'value')
def glXQueryDrawable(dpy, draw, attribute):
	pass


@params('dpy', 'drawable')
def glXSwapBuffers(dpy, drawable):
	pass


@params()
def glXGetCurrentDisplay():
	pass


@params('dpy', 'screen', 'attribList')
def glXChooseVisual(dpy, screen, attribList):
	pass


@params('dpy', 'pbuf')
def glXDestroyPbuffer(dpy, pbuf):
	pass


@params('dpy', 'config', 'pixmap', 'attrib_list')
def glXCreatePixmap(dpy, config, pixmap, attrib_list):
	pass


@params('dpy', 'draw', 'event_mask')
def glXSelectEvent(dpy, draw, event_mask):
	pass


@params('dpy', 'draw', 'event_mask')
def glXGetSelectedEvent(dpy, draw, event_mask):
	pass


@params('dpy', 'errorb', 'event')
def glXQueryExtension(dpy, errorb, event):
	pass


@params('dpy', 'drawable', 'ctx')
def glXMakeCurrent(dpy, drawable, ctx):
	pass


@params('dpy', 'config', 'attrib_list')
def glXCreatePbuffer(dpy, config, attrib_list):
	pass


@params('dpy', 'pixmap')
def glXDestroyGLXPixmap(dpy, pixmap):
	pass


@params('dpy', 'screen', 'attrib_list', 'nelements')
def glXChooseFBConfig(dpy, screen, attrib_list):
	pass


@params('dpy', 'visual', 'attrib', 'value')
def glXGetConfig(dpy, visual, attrib):
	pass


@params()
def glXWaitX():
	pass


@params()
def glXGetCurrentContext():
	pass


@params()
def glXWaitGL():
	pass


@params('dpy', 'maj', 'min')
def glXQueryVersion(dpy):
	pass


@params('dpy', 'pixmap')
def glXDestroyPixmap(dpy, pixmap):
	pass


@params('dpy', 'ctx')
def glXIsDirect(dpy, ctx):
	pass


@params('dpy', 'ctx')
def glXDestroyContext(dpy, ctx):
	pass


@params('dpy', 'config', 'render_type', 'share_list', 'direct')
def glXCreateNewContext(dpy, config, render_type, share_list, direct):
	pass


@params('dpy', 'name')
def glXGetClientString(dpy, name):
	pass


@params('dpy', 'config')
def glXGetVisualFromFBConfig(dpy, config):
	pass


@params('dpy', 'screen', 'nelements')
def glXGetFBConfigs(dpy, screen):
	pass


@params()
def glXGetCurrentReadDrawable():
	pass


@params('dpy', 'ctx', 'attribute', 'value')
def glXQueryContext(dpy, ctx, attribute):
	pass


@params('dpy', 'config', 'win', 'attrib_list')
def glXCreateWindow(dpy, config, win, attrib_list):
	pass


@params('dpy', 'src', 'dst', 'mask')
def glXCopyContext(dpy, src, dst, mask):
	pass


@params('dpy', 'screen', 'name')
def glXQueryServerString(dpy, screen, name):
	pass


@params('dpy', 'config', 'attribute', 'value')
def glXGetFBConfigAttrib(dpy, config, attribute):
	pass


@params('font', 'first', 'count', 'list')
def glXUseXFont(font, first, count, list):
	pass


@params('dpy', 'draw', 'read', 'ctx')
def glXMakeContextCurrent(dpy, draw, read, ctx):
	pass


@params()
def glXGetCurrentDrawable():
	pass


@params('dpy', 'screen')
def glXQueryExtensionsString(dpy, screen):
	pass


