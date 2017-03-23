import OpenGLCffi
from OpenGLCffi import load_lib, params
from ctypes.util import find_library

ffi, lib = load_lib('GLESv2')
retList = ['framebuffers', 'shaders', 'params', 'infoLog', 'data', 'source', 'renderbuffers', 'buffers', 'textures', 'range', 'precision', 'val', 'label', 'pipelinesids', 'propCount', 'binary', 'arrays']
sizeSetters = {'maxCount': ['shaders'], 'n': ['framebuffers']}
OpenGLCffi.libs['gles3'] = [lib, ffi, retList, sizeSetters]
