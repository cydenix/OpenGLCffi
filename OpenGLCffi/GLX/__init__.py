import OpenGLCffi
from OpenGLCffi import load_lib, params
from ctypes.util import find_library

ffi, lib = load_lib('GLX')
retList = ['value', 'errorb', 'event', 'nelements', 'maj', 'min', 'name']
sizeSetters = {}
OpenGLCffi.libs['glx'] = [lib, ffi, retList, sizeSetters]
xlib = ffi.dlopen(find_library('X11'))
xlibxcb = ffi.dlopen(find_library('X11-xcb'))
