import os, sys
from functools import wraps
from FFI import *
from glob import glob
from ctypes.util import find_library

LIB_PATH = '/usr/lib/'
libs = {}


def load_lib(api=None):
    '''
    api's are EGL, GL, GLESv2, GLESv1_CM, GLX
    '''
    ffi = globals()["_" + api.lower().replace('v', '') + "ffi"].ffi
    return ffi, ffi.dlopen(find_library(api))


def params(*largs, **lkwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            varn = func.__code__.co_varnames
            prms = list(largs)
            retdict = {}
            api = lkwargs['api']
            ffi = libs[api][1]
            f = getattr(libs[api][0], func.__name__)
            for inx, p in enumerate(largs):
                for i, a in enumerate(varn):
                    if a == p:
                        prms[inx] = args[i]
                if p not in varn:
                    if p in libs[api][2]:
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
        return wrapper
    return decorator
