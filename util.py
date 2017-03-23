import xcffib
#from OpenGLCffi.EGL import xlib, xlibxcb, ffi


def get_xdsp_xcb_connection(api=None):
    if api is 'EGL':
        from OpenGLCffi.EGL import xlib, xlibxcb
    elif api is 'GLX':
        from OpenGLCffi.GLX import xlib, xlibxcb
    d = xlib.XOpenDisplay(ffi.NULL)
    xlibxcb.XSetEventQueueOwner(d, 1)
    c = xlibxcb.XGetXCBConnection(d)
    return d, xcffib.wrap(c)



