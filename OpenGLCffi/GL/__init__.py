import OpenGLCffi
from OpenGLCffi import load_lib, params
from ctypes.util import find_library

ffi, lib = load_lib('GL')
retList = []
sizeSetters = {}
OpenGLCffi.libs['gl'] = [lib, ffi, retList, sizeSetters]
