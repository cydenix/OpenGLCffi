import os, sys
sys.path.append(os.path.abspath(".."))
from OpenGLCffi.EGL import egl, ffi

xlib = ffi.dlopen("libX11.so.6")
xlibxcb = ffi.dlopen("libX11-xcb.so.1")

d = xlib.XOpenDisplay(ffi.NULL)
c = xlibxcb.XGetXCBConnection(d)

def deco(func):
    def wrap(*args):
        print func
    return wrap

@deco
def a(x, y, z):
    pass

edsp = egl.eglGetDisplay(d)
egl.eglInitialize(edsp)