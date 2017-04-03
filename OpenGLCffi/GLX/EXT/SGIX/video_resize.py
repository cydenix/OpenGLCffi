from OpenGLCffi.GLX import params
@params('display', 'screen', 'channel', 'window', api='glx')
def glXBindChannelToWindowSGIX(display, screen, channel, window):
	pass


@params('display', 'screen', 'channel', 'x', 'y', 'w', 'h', api='glx')
def glXChannelRectSGIX(display, screen, channel, x, y, w, h):
	pass


@params('display', 'screen', 'channel', 'dx', 'dy', 'dw', 'dh', api='glx')
def glXQueryChannelRectSGIX(display, screen, channel, dx, dy, dw, dh):
	pass


@params('display', 'screen', 'channel', 'x', 'y', 'w', 'h', api='glx')
def glXQueryChannelDeltasSGIX(display, screen, channel, x, y, w, h):
	pass


@params('display', 'screen', 'channel', 'synctype', api='glx')
def glXChannelRectSyncSGIX(display, screen, channel, synctype):
	pass


