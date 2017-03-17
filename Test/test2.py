import os, sys
sys.path.append(os.path.abspath(".."))
from OpenGLCffi.EGL import egl, ffi, util
from OpenGLCffi.GLES2 import gles2
from OpenGLCffi.EGL.const import *
from OpenGLCffi import *
import xcffib
from xcffib import xproto


d, conn = util.get_xdsp_xcb_connection()
edsp = egl.eglGetDisplay(d)
print egl.eglInitialize(edsp)
print egl.eglBindAPI(EGL_OPENGL_ES_API)

egl_atts = [EGL_COLOR_BUFFER_TYPE, EGL_RGB_BUFFER,
        EGL_BUFFER_SIZE, 24,
        EGL_RED_SIZE, 8,
        EGL_GREEN_SIZE, 8,
        EGL_BLUE_SIZE, 8,
        EGL_DEPTH_SIZE, 24,
        EGL_STENCIL_SIZE, 8,
        EGL_SURFACE_TYPE, EGL_WINDOW_BIT | EGL_PIXMAP_BIT,
        EGL_NONE]

ctx_atts = [EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE]
sfs_atts = [EGL_RENDER_BUFFER, EGL_BACK_BUFFER, EGL_NONE]

conf = egl.eglChooseConfig(edsp, egl_atts, 3)['configs'][0]

vid = egl.eglGetConfigAttrib(edsp, conf, EGL_NATIVE_VISUAL_ID)

print vid['value'][0]
print conn.get_setup().roots[0].root_visual