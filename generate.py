import sys
import os
import shutil
import parser
from urllib2 import urlopen, HTTPError, URLError, Request

GL_URL = "https://cvs.khronos.org/svn/repos/ogl/trunk/doc/registry/public/api/"

GL_REGISTRY_FILES = ["egl.xml", "gl.xml", "glx.xml"]

GL_DIRS = ["GL",
           "GLES1",
           "GLES2",
           "GLES3",
           "GLX",
           "EGL",
           "FFI",
           "Registry",
           "Defs"]

RET_DICT = {'gl': [],
            'glx': ['value',
                    'errorb',
                    'event',
                    'nelements',
                    'maj', 'min',
                    'name'],
            'gles1': ['equation',
                      'params',
                      'data',
                      'buffers',
                      'textures'],
            'gles2': ['framebuffers',
                      'shaders',
                      'params',
                      'infoLog',
                      'data',
                      'source',
                      'renderbuffers',
                      'buffers',
                      'textures',
                      'range',
                      'precision'],
            'gles3': ['framebuffers',
                      'shaders',
                      'params',
                      'infoLog',
                      'data',
                      'source',
                      'renderbuffers',
                      'buffers',
                      'textures',
                      'range',
                      'precision',
                      'val',
                      'label',
                      'pipelines'
                      'ids',
                      'propCount',
                      'binary',
                      'arrays'],
            'egl': ['configs',
                    'num_config',
                    'value',
                    'major', 'minor']}

SIZE_SET = {'egl': {'config_size': ['configs']},
            'glx': {},
            'gles1': {'n': ['framebuffers']},
            'gles2': {'n': ['framebuffers'],
                      'maxCount': ['shaders'],
                      'bufSize': ['infoLog', 'source']},
            'gles3': {'n': ['framebuffers'],
                      'maxCount': ['shaders']},
            'gl': {}}

BASE_DIR = os.getcwd()
def create_dirs(dirs):
    if not os.path.isdir("OpenGLCffi"):
        with open('init.py', 'r') as init_file:
            init_lines = init_file.readlines()
        os.mkdir("OpenGLCffi")
        os.chdir("OpenGLCffi")
        if not os.path.isfile('__init__.py'):
            with open('__init__.py', 'w+') as main_init:
                main_init.writelines(init_lines)
        for d in dirs:
            if not os.path.isdir(d):
                os.mkdir(d)
                if os.path.isdir(d):
                    os.mknod(os.path.join(d, "__init__.py"))
            else:
                break
    else:
        os.chdir("OpenGLCffi")

def create_extdirs(dirs):
    for d in dirs:
        if not os.path.isdir(d):
            os.mkdir(d)
            if os.path.isdir(d):
                os.mknod(os.path.join(d, "__init__.py"))
            else:
                break


def delete_dirs(dirs):
    for d in dirs:
        if os.path.isdir(d):
            shutil.rmtree(d)


def get_registry_files(glfiles):
    for glfile in glfiles:
        try:
            req = Request(GL_URL + glfile)
            fl = urlopen(req)
            print "Downloading ... %s" % (glfile)
            with open(os.path.join("Registry", glfile), 'wb') as f:
                f.write(fl.read())
        except HTTPError, e:
            print "HTTP Problem", e.msg
        except URLError, e:
            print "URL Problem", e.reason


def gen_cons(lstEnums, dictObj, fileObj):
    print "Generating Constants"
    fl_api_enums = []
    api_enums = [x.enums for v in dictObj.values() for x in v]
    map(fl_api_enums.extend, api_enums)
    for e in lstEnums:
        if e.name in fl_api_enums and not e.value.startswith("("):
            fileObj.write(e.__str__())


def gen_def(prsr=None, api=None, ver=None):
    print "Generating Defs for {}".format(api)
    defpath = os.path.join(os.path.abspath('.'), "Defs")
    with open(os.path.join(defpath, "__init__.py"), "w+") as init:
        init.write("from os.path import dirname, basename\n")
        init.write("import glob\n")
        init.write("modules = glob.glob(dirname(__file__) + '/*.py')\n")
        init.write("__all__ = [basename(f)[:-3] for f in modules if not basename(f).startswith('_')]\n")

    if api == 'gles2' and float(ver) > 2.0:
        defname = api[:-1] + '3' + 'defs.py'
    else:
        defname = api + 'defs.py'

    deffile = os.path.join(defpath, defname)
    with open(deffile, "w+") as f:
        f.write("\n")
        f.write("DEF = '''\n")
        prsr.write_header("khronos.h", f)
        f.write("\n")
        if api and api in ['egl', 'glx']:
            prsr.write_header("xorg.h", f)
            f.write('\n')
            prsr.write_header("xorg_xcb.h", f)
            f.write("\n")
        if api == 'egl':
            prsr.write_header("eglx11platform.h", f)
            f.write("\n")
        if api and api in ['glsc2', 'gles1', 'gles2', 'gles3']:
            if api == 'gles3':
                api = 'gles2'
            for x in prsr.tdict[api]:
                f.write(x.__str__())
            for t in prsr.tdict['gl']:
                if t.name not in [a.name for a in prsr.tdict[api]]:
                    f.write(t.__str__())
        elif api and api == 'glx':
            for v in prsr.tdict['dummy']:
                if v[:2] in ['GL', 'VL', 'DM']:
                    f.write("typedef ... " + v + ";\n")
            f.write("\n")
            for v in prsr.tdict[api]:
                f.write(v.__str__())
        elif api:
            for v in prsr.tdict[api]:
                f.write(v.__str__())
        if "GLhandleARB" in prsr.tdict['dummy']:
            f.write("typedef unsigned int GLhandleARB;\n")
        f.write("\n")
        prsr.write_commands(prsr.cdict, prsr.fdict, prsr.edict, f)
        f.write("'''\n")


def gen_api_funcs(api, enumLst, cmdDict, ftrDict):
    global RET_DICT
    if os.path.isdir(api.upper()):
        with open(os.path.join(api.upper(), 'const.py'), 'w+') as cons:
            gen_cons(enumLst, ftrDict, cons)
        with open(os.path.join(api.upper(), api + '.py'), 'w+') as f:
            f.write("from OpenGLCffi.{} import params\n".format(api.upper()))
            fcmd = [frqv for fv in p.fdict.values() for frqv in fv[0].req]
            for ck in p.cdict.keys():
                if ck in fcmd:
                    marg = map(lambda x: x.split()[-1:][0].translate(None, "*"), p.cdict[ck].params)

                    if ck[:3] in ['glX', 'egl', 'glG']:

                        farg = filter(lambda y: y not in RET_DICT[api], marg)
                    else:
                        farg = marg

                    if len(marg) == 0:
                        f.write("@params(api = '{}')\n".format(api))
                    else:
                        f.write("@params({})\n".format(repr(map(str, marg)).strip("[]") + ", api='{}'".format(api)))
                    f.write("def {}({}):\n".format(ck, ', '.join(farg)))
                    f.write("\tpass\n")
                    f.write("\n\n")


def gen_api_extfunc(api, enumLst, cmdDict, extDict):
    global RET_DICT

    ext_path = os.path.join(api.upper(), "EXT")

    if not os.path.isdir(ext_path):
        os.mkdir(ext_path)
    os.chdir(ext_path)

    if not os.path.isfile("__init__.py"):
        os.mknod("__init__.py")

    with open('const.py', 'w+') as cons:
            gen_cons(enumLst, extDict, cons)

    create_extdirs(extDict.keys())
    efls = [(e.vendor, e.name, e.req) for v in extDict.itervalues() for e in v if len(e.req) > 0]
    for i in efls:
        if os.path.isdir(i[0]):
            with open(os.path.join(i[0], i[1] + ".py"), "w+") as f:
                f.write("from OpenGLCffi.{} import params\n".format(api.upper()))
                for ck in i[2]:
                    marg = map(lambda x: x.split()[-1:][0].translate(None, "*"), cmdDict[ck].params)
                    if ck[:3] in ['glX', 'egl', 'glG']:
                        farg = filter(lambda y: y not in RET_DICT[api], marg)
                    else:
                        farg = marg
                    if len(marg) == 0:
                        f.write("@params(api = '{}')\n".format(api))
                    else:
                        f.write("@params({})\n".format(repr(map(str, marg)).strip("[]") + ", api='{}'".format(api)))
                    f.write("def {}({}):\n".format(ck, ", ".join(farg)))
                    f.write("\tpass\n")
                    f.write("\n\n")
    os.chdir(os.path.join(BASE_DIR, 'OpenGLCffi'))


if __name__ == '__main__':
    create_dirs(GL_DIRS)
    reg_dir = [f for f in os.listdir("Registry") if not f.startswith('__')]
    reg_dir.sort()
    if reg_dir != GL_REGISTRY_FILES:
        get_registry_files(GL_REGISTRY_FILES)

    apis = {'egl': ['egl.xml', '1.5'],
            'glx': ['glx.xml', '1.4'],
            'gles1': ['gl.xml', '1.0'],
            'gles2': ['gl.xml', '2.0'],
            'gles3': ['gl.xml', '3.2'],
            'gl': ['gl.xml', '4.5']
            }

    ld_libs = {'egl': 'EGL',
               'glx': 'GLX',
               'gles1': 'GLESv1_CM',
               'gles2': 'GLESv2',
               'gles3': 'GLESv2',
               'gl': 'GL'}

    for k, v in apis.items():
        p = parser.Parser(v[0], k, v[1])
        gen_def(p, k, v[1])
        gen_api_funcs(k, p.endict, p.cdict, p.fdict)
        gen_api_extfunc(k, p.endict, p.cdict, p.edict)
    del p

    libs = ['GL', 'GLESv1_CM', 'GLESv2', 'GLESv3', 'X11', 'X11-xcb', 'xcb']
    from cffi import FFI
    from xcffib.ffi_build import ffi as xcbffi
    from OpenGLCffi.Defs import *

    for k in apis.keys():
        print "Compiling {}".format(k)
        ffi = FFI()
        if k not in ['egl', 'glx']:
            ffi.cdef(globals()[k + 'defs'].DEF)
        else:
            ffi.include(xcbffi)
            ffi.cdef(globals()[k + 'defs'].DEF)
        ffi.set_source("FFI._{}ffi".format(k), None, libs)
        ffi.compile()

    with open("FFI/__init__.py", 'w+') as init_ffi:
        init_ffi.write('from os.path import dirname, basename\n')
        init_ffi.write('import glob\n')
        init_ffi.write('\n')
        init_ffi.write('modules = glob.glob(dirname(__file__) + "/*.py")\n')
        init_ffi.write('__all__ = [basename(f)[:-3] for f in modules if not basename(f).startswith("__")]\n')

    for k in apis.keys():
        with open(os.path.join(k.upper(), '__init__.py'), "w+") as api_init:
            api_init.write("import OpenGLCffi\n")
            api_init.write("from OpenGLCffi import load_lib, params\n")
            api_init.write("from ctypes.util import find_library\n")
            api_init.write("\n")
            api_init.write("ffi, lib = load_lib('{}')\n".format(ld_libs[k]))
            api_init.write("retList = {}\n".format("".join(repr(map(str, RET_DICT[k])))))
            api_init.write("sizeSetters = {}\n".format(SIZE_SET[k]))
            api_init.write("OpenGLCffi.libs['{}'] = [lib, ffi, retList, sizeSetters]\n".format(k))
            if k.upper() in ['EGL', 'GLX']:
                api_init.write("xlib = ffi.dlopen(find_library('X11'))\n")
                api_init.write("xlibxcb = ffi.dlopen(find_library('X11-xcb'))\n")

