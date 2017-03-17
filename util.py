import xcffib
from OpenGLCffi.EGL import xlib, xlibxcb, ffi


def get_xdsp_xcb_connection():
    d = xlib.XOpenDisplay(ffi.NULL)
    xlibxcb.XSetEventQueueOwner(d, 1)
    c = xlibxcb.XGetXCBConnection(d)
    return d, xcffib.wrap(c)



