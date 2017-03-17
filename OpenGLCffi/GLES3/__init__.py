import OpenGLCffi
from OpenGLCffi import load_lib, params

ffi, lib = load_lib('GLESv2')
retList = ['framebuffers', 'shaders', 'count', 'params', 'length', 'infoLog', 'data', 'source', 'renderbuffers', 'buffers', 'size', 'type', 'textures', 'pointer', 'range', 'precision', 'val', 'label', 'pipelinesids', 'propCount', 'binary', 'arrays']
sizeSetters = {'maxCount': ['shaders'], 'n': ['framebuffers']}
OpenGLCffi.libs['gles3'] = [lib, ffi, retList, sizeSetters]
