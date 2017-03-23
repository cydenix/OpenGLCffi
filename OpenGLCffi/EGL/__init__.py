import OpenGLCffi
from OpenGLCffi import load_lib, params
from ctypes.util import find_library

ffi, lib = load_lib('EGL')
retList = ['configs', 'num_config', 'value', 'major', 'minor']
sizeSetters = {'config_size': ['configs']}
OpenGLCffi.libs['egl'] = [lib, ffi, retList, sizeSetters]
xlib = ffi.dlopen(find_library('X11'))
xlibxcb = ffi.dlopen(find_library('X11-xcb'))
