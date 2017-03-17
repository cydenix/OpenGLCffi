import os, sys
sys.path.append(os.path.abspath(".."))
from OpenGLCffi.FFI import *
from OpenGLCffi import load_lib
from OpenGLCffi.EGL.const import *
from OpenGLCffi.EGL import *


ffi, lib = load_lib('GL')

print dir(ffi.typeof(lib.glBegin))
print ffi.typeof(lib.glBegin).abi








