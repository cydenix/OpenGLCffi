import OpenGLCffi
from OpenGLCffi import load_lib, params

ffi, lib = load_lib('GLX')
retList = ['value', 'errorb', 'event', 'nelements', 'maj', 'min', 'name']
sizeSetters = {}
OpenGLCffi.libs['glx'] = [lib, ffi, retList, sizeSetters]
