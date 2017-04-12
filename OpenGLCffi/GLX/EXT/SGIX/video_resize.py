from OpenGLCffi.GLX import params
@params(api='glx', prms=['display', 'screen', 'channel', 'window'])
def glXBindChannelToWindowSGIX(display, screen, channel, window):
	pass


@params(api='glx', prms=['display', 'screen', 'channel', 'x', 'y', 'w', 'h'])
def glXChannelRectSGIX(display, screen, channel, x, y, w, h):
	pass


@params(api='glx', prms=['display', 'screen', 'channel', 'dx', 'dy', 'dw', 'dh'])
def glXQueryChannelRectSGIX(display, screen, channel, dx, dy, dw, dh):
	pass


@params(api='glx', prms=['display', 'screen', 'channel', 'x', 'y', 'w', 'h'])
def glXQueryChannelDeltasSGIX(display, screen, channel, x, y, w, h):
	pass


@params(api='glx', prms=['display', 'screen', 'channel', 'synctype'])
def glXChannelRectSyncSGIX(display, screen, channel, synctype):
	pass


