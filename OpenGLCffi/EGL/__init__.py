import OpenGLCffi
from OpenGLCffi import load_lib, params

ffi, lib = load_lib('EGL')
retList = ['configs', 'num_config', 'value', 'major', 'minor']
sizeSetters = {'config_size': ['configs']}
OpenGLCffi.libs['egl'] = [lib, ffi, retList, sizeSetters]
