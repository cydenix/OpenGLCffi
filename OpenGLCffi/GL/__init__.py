import OpenGLCffi
from OpenGLCffi import load_lib, params

ffi, lib = load_lib('GL')
retList = []
sizeSetters = {}
OpenGLCffi.libs['gl'] = [lib, ffi, retList, sizeSetters]
