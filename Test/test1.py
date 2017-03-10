import os, sys
sys.path.append(os.path.abspath(".."))
from OpenGLCffi.FFI import *
from OpenGLCffi import load_lib
from OpenGLCffi.EGL.const import *
from functools import wraps


ffi, lib = load_lib("EGL")
ffinew_retlist = ['configs', 'num_configs', 'value']


def params(*largs):
    def deco(func):
        @wraps(func)
        def wrap(*args):
            varn = func.__code__.co_varnames
            prms = list(largs)
            retdict = {}
            f = getattr(lib, func.__name__)
            for inx, p in enumerate(largs):
                for i, a in enumerate(varn):
                    if a == p:
                        prms[inx] = args[i]
                if p not in varn:
                    if p in ffinew_retlist:
                        retdict[p] = inx
                    p = ffi.new(ffi.typeof(f).args[inx].cname)
                    prms[inx] = p
            r = f(*prms)
            if len(retdict) > 0:
                for k, v in retdict.items():
                    retdict[k] = prms[v][0]
                return retdict
            else:
                return r
        return wrap
    return deco

@params('dsp', 'attrib_list', 'configs', 'config_size', 'num_configs')
def eglChooseConfig(dsp, attrib_list, config_size):
    '''
    dsp, attrib_list, config_size
    '''
    pass

att = [EGL_COLOR_BUFFER_TYPE, EGL_RGB_BUFFER, EGL_BUFFER_SIZE, 24, EGL_DEPTH_SIZE, 24, EGL_RED_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_RED_SIZE, 8, EGL_STENCIL_SIZE, 8, EGL_SURFACE_TYPE, EGL_WINDOW_BIT | EGL_PIXMAP_BIT, EGL_NONE]

d = lib.XOpenDisplay(ffi.NULL)
edsp = lib.eglGetDisplay(d)
lib.eglInitialize(edsp, ffi.NULL, ffi.NULL)

print eglChooseConfig(edsp, att, 2)

#n = ffi.new("EGLint *")
#cnf = ffi.new("EGLConfig [2]")
#lib.eglChooseConfig(edsp, att, cnf, 100, n)
#lib.eglGetConfigs(edsp, cnf, 100, n)
#print n[0]
