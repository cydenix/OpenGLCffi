import OpenGLCffi
from OpenGLCffi import load_lib, params
from ctypes.util import find_library

ffi, lib = load_lib('GLESv1_CM')
retList = ['equation', 'params', 'data', 'buffers', 'textures']
sizeSetters = {'n': ['framebuffers']}
OpenGLCffi.libs['gles1'] = [lib, ffi, retList, sizeSetters]
