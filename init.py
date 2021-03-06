from functools import wraps
from FFI import *
from ctypes.util import find_library
from weakref import WeakKeyDictionary

libs = {}
_wkdict_ = WeakKeyDictionary()


def load_lib(api=None):
    '''
    api's are EGL, GL, GLESv2, GLESv1_CM, GLX
    '''
    ffi = globals()["_" + api.lower().replace('v', '') + "ffi"].ffi
    return ffi, ffi.dlopen(find_library(api))


def _new(api, func, args, prm_inx, prm_name):
    p = libs[api][1].typeof(func).args[prm_inx].cname.split()
    if len(libs[api][3]) != 0 and prm_name in sum(libs[api][3].values(), []):
        x = {i: k for k, v in libs[api][3].items() for i in v}[prm_name]
        n_pr = libs[api][1].new(' '.join(p[:-1]) + '[{}]'.format(args[x]))
        _wkdict_[n_pr] = prm_name
        return n_pr
    else:
        n_pr = libs[api][1].new(' '.join(p))
        _wkdict_[n_pr] = prm_name
        return n_pr


def _cast(api, func, prm_inx, prm):
    p = libs[api][1].typeof(func).args[prm_inx].cname.split()
    ptr = libs[api][1].cast(' '.join(p), prm)
    _wkdict_[ptr] = prm
    return ptr


def params(*largs, **lkwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            ret_dict = {}
            prms = list(lkwargs['prms'])
            api = lkwargs['api']
            f = getattr(libs[lkwargs['api']][0], func.__name__)
            arg_dict = dict(zip(func.func_code.co_varnames, args))
            for i, pr in enumerate(prms):
                if pr in arg_dict.keys():
                    prms[i] = arg_dict[pr]
                else:
                    prms[i] = _new(api, f, arg_dict, i, pr)
                    if pr in libs[api][2]:
                        ret_dict[pr] = prms[i]
            ret = f(*prms)
            if isinstance(ret, libs[api][1].CData):
                if libs[api][1].typeof(ret).kind == 'pointer':
                    if len(ret_dict) > 0:
                        return ret, ret_dict
                    else:
                        return ret
                else:
                    return ret, ret_dict
            elif len(ret_dict) > 0:
                return ret_dict
            else:
                return ret
        return wrapper
    return decorator
