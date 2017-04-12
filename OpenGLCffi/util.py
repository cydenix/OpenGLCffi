import OpenGLCffi


def get_xdsp_xcb_connection(api=None):
    if api is 'EGL':
        from OpenGLCffi.EGL import xlib, xlibxcb, ffi
    elif api is 'GLX':
        from OpenGLCffi.GLX import xlib, xlibxcb, ffi
    d = xlib.XOpenDisplay(ffi.NULL)
    xlibxcb.XSetEventQueueOwner(d, 1)
    c = xlibxcb.XGetXCBConnection(d)
    return d, c


def xvinfo_to_py(ptr):
    pass


class Connection:
    def __init__(self, api=None, event_owner=1):
        self.api = api
        self.xdsp = None
        self.xcb_conn = None
        self.event_owner = event_owner
        if api is not None:
            self.get_connect()

    def get_connect(self):
        if self.api == 'EGL':
            from OpenGLCffi.EGL import xlib, xlibxcb, ffi
        elif self.api == 'GLX':
            from OpenGLCffi.GLX import xlib, xlibxcb, ffi
        self.xdsp = xlib.XOpenDisplay(ffi.NULL)
        xlibxcb.XSetEventQueueOwner(self.xdsp, self.event_owner)
        self.xcb_conn = xlibxcb.XGetXCBConnection(self.xdsp)

