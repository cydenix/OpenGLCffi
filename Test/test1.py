import os, sys
sys.path.append(os.path.abspath(".."))
from OpenGLCffi.FFI import *
from OpenGLCffi import load_lib
from OpenGLCffi.EGL.const import *
from functools import wraps


def p(func):
    @wraps(func):
    def wrap(*args):
        print dir(func)

