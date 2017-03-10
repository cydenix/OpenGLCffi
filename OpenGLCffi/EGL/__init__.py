import os, sys
sys.path.append(os.path.abspath("../.."))
from OpenGLCffi.FFI import *
from OpenGLCffi import load_lib, params


ffi, lib = load_lib("EGL")