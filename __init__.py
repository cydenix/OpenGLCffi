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
            size = int()
            f = getattr(libs[api][0], func.__name__)
            sizeSetters = libs[api][3]
            retList = libs[api][2]
            for inx, p in enumerate(largs):
                for i, a in enumerate(varn):
                    if a == p:
                        prms[inx] = args[i]
                if p in sizeSetters.keys():
                    size = args[varn.index(p)]
                    svarLsts = sizeSetters[p]
                    svar = [x for x in svarLsts if x in largs][0]
                    ptr = largs.index(svar)
                    ptr_typ = ffi.typeof(f).args[ptr].cname.split()
                    if svar in retList:
                        retdict[svar] = ptr
                    if len(ptr_typ) == 3:
                        ptr_typ[2] = "[{}]".format(size)
                        prms[ptr] = ffi.new(' '.join(ptr_typ))
                    elif len(ptr_typ) == 2:
                        ptr_typ[1] = "[{}]".format(size)
                        prms[ptr] = ffi.new(' '.join(ptr_typ))
                if p in retList and p not in sizeSetters.values():
                    typ = ffi.typeof(f).args[largs.index(p)].cname
                    prms[largs.index(p)] = ffi.new(typ)
                    retdict[p] = largs.index(p)
            r = f(*prms)
            if len(retdict) > 0:
                for k, v in retdict.items():
                    retdict[k] = prms[v]
                return retdict
            else:
                return r
        return wrapper
    return decorator
