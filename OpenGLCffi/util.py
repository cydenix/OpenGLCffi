import xcffib
from xcffib import xproto

def get_xdsp_xcb_connection(api=None):
    if api is 'EGL':
        from OpenGLCffi.EGL import xlib, xlibxcb, ffi
    elif api is 'GLX':
        from OpenGLCffi.GLX import xlib, xlibxcb, ffi
    d = xlib.XOpenDisplay(ffi.NULL)
    xlibxcb.XSetEventQueueOwner(d, 1)
    c = xlibxcb.XGetXCBConnection(d)
    return d, xcffib.wrap(c)



