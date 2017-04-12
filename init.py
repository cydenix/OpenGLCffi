from functools import wraps
from FFI import *
from ctypes.util import find_library


LIB_PATH = '/usr/lib/'
libs = {}


def load_lib(api=None):
    '''
    api's are EGL, GL, GLESv2, GLESv1_CM, GLX
    '''
    ffi = globals()["_" + api.lower().replace('v', '') + "ffi"].ffi
    return ffi, ffi.dlopen(find_library(api))


def _new(api, func, prm_inx, size=None):
    p = libs[api][1].typeof(func).args[prm_inx].cname.split()
    if size is not None:
        return libs[api][1].new(' '.join(p[:-1]) + '[{}]'.format(size))
    else:
        return libs[api][1].new(' '.join(p))


def _cast(api, func, prm_inx, prm):
    p = libs[api][1].typeof(func).args[prm_inx].cname.split()
    return libs[api][1].cast(' '.join(p), prm)


def params(*largs, **lkwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            ret_dict = {}
            prms = list(lkwargs['prms'])
            api = lkwargs['api']
            #counters = ['num_config', 'nelements', 'count']
            f = getattr(libs[lkwargs['api']][0], func.__name__)
            arg_dict = dict(zip(func.func_code.co_varnames, args))
            for i, pr in enumerate(prms):
                if pr in arg_dict.keys():
                    prms[i] = arg_dict[pr]
                    if pr in libs[api][3].keys():
                        ptr = prms.index([x for x in libs[api][3][pr] if x in prms][0])
                        prms[ptr] = _new(api, f, ptr, size=arg_dict[pr])
                        ret_dict[lkwargs['prms'][ptr]] = prms[ptr]
                elif pr not in [y for l in libs[api][3].values() for y in l]:
                    prms[i] = _new(api, f, i)
                    ret_dict[pr] = prms[i]
            ret = f(*prms)
            if ret_dict:
                return ret_dict
            else:
                return ret
        return wrapper
    return decorator

'''
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
                if p not in varn:
                    if p in libs[api][2]:
                        retdict[p] = inx
                    p = ffi.new(ffi.typeof(f).args[inx].cname)
                    prms[inx] = p
            r = f(*prms)
            if len(retdict) > 0:
                for k, v in retdict.items():
                    retdict[k] = prms[v]
                return r, retdict
            else:
                return r
        return wrapper
    return decorator
'''