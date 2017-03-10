from functools import wraps
from FFI import *
from glob import glob

LIB_PATH = '/usr/lib/'


def load_lib(api=None):
    global ffi
    if api == "GLX":
        api = api[:-1]
    for f in glob(LIB_PATH + '/lib{}*.so.*.*'.format(api)):
        dl_lib = f
    ffi = globals()["_" + api.lower().replace('v', '') + "ffi"].ffi
    return ffi, ffi.dlopen(dl_lib)

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