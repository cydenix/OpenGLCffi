#Working Example
import os, sys
sys.path.append(os.path.abspath(".."))
from OpenGLCffi.EGL import egl, ffi, util
from OpenGLCffi.GLES2 import gles2, const
from OpenGLCffi.GLES2 import ffi as es2
from OpenGLCffi.EGL.const import *
from OpenGLCffi import *
import xcffib
from xcffib import xproto


d, conn = util.get_xdsp_xcb_connection()
edsp = egl.eglGetDisplay(d)


print egl.eglInitialize(edsp)
print egl.eglBindAPI(EGL_OPENGL_ES_API)

setup = conn.get_setup()
scr = setup.roots[0]
root = scr.root
ddepth = scr.root_depth
white = scr.white_pixel
black = scr.black_pixel
dvisualid = scr.root_visual

egl_atts = [EGL_COLOR_BUFFER_TYPE, EGL_RGB_BUFFER,
            EGL_BUFFER_SIZE, 24,
            EGL_RED_SIZE, 8,
            EGL_GREEN_SIZE, 8,
            EGL_BLUE_SIZE, 8,
            EGL_DEPTH_SIZE, 24,
            EGL_STENCIL_SIZE, 8,
            EGL_SURFACE_TYPE, EGL_WINDOW_BIT | EGL_PIXMAP_BIT,
            EGL_NONE]

win = conn.generate_id()
mask = xproto.CW.BackPixel | xproto.CW.EventMask
value = [white, xproto.EventMask.Exposure | xproto.EventMask.KeyPress]
conn.core.CreateWindow(ddepth, win, root, 0, 0, 600, 600, 2, xproto.WindowClass.InputOutput, dvisualid, mask, value)
conn.core.MapWindow(win)
conn.flush()

ctx_atts = [EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE]
sfs_atts = [EGL_RENDER_BUFFER, EGL_BACK_BUFFER, EGL_NONE]

conf = egl.eglChooseConfig(edsp, egl_atts, 3)['configs'][0]

vid = egl.eglGetConfigAttrib(edsp, conf, EGL_NATIVE_VISUAL_ID)['value'][0]

ctx = egl.eglCreateContext(edsp, conf, ffi.NULL, ctx_atts)

sfs = egl.eglCreateWindowSurface(edsp, conf, win, sfs_atts)
egl.eglMakeCurrent(edsp, sfs, sfs, ctx)

vShStr = es2.new("char []", "attribute highp vec4 vPosition;\n"
                            "void main()\n"
                            "{\n"
                            "   gl_Position = vPosition;\n"
                            "}\n")

fShStr = es2.new("char []", "precision mediump float;\n"
                            "void main()\n"
                            "{\n"
                            "   gl_FragColor = vec4 (1.0, 0.0, 0.0, 1.0)\n;"
                            "}\n")
vshader = gles2.glCreateShader(const.GL_VERTEX_SHADER)
gles2.glShaderSource(vshader, 1, es2.new("char **", vShStr), ffi.NULL)
gles2.glCompileShader(vshader)
print gles2.glGetShaderiv(vshader, const.GL_COMPILE_STATUS)['params'][0]
fshader = gles2.glCreateShader(const.GL_FRAGMENT_SHADER)
gles2.glShaderSource(fshader, 1, es2.new("char **", fShStr), ffi.NULL)
gles2.glCompileShader(fshader)
print gles2.glGetShaderiv(fshader, const.GL_COMPILE_STATUS)['params'][0]
prObj = gles2.glCreateProgram()
gles2.glAttachShader(prObj, vshader)
gles2.glAttachShader(prObj, fshader)
gles2.glBindAttribLocation(prObj, 0, 'vPosition')
gles2.glLinkProgram(prObj)

while True:
    ev = conn.wait_for_event()
    if isinstance(ev, xproto.ExposeEvent):
        gles2.glClearColor(0.0, 0.0, 0.0, 1.0)

        vVerts = es2.new("GLfloat []", [0.0, 0.5, 0.0,
                                        -0.5, -0.5, 0.0,
                                        0.5, -0.5, 0.0])
        gles2.glViewport(0, 0, 600, 600)
        gles2.glClear(const.GL_COLOR_BUFFER_BIT)
        gles2.glUseProgram(prObj)
        gles2.glVertexAttribPointer(0, 3, const.GL_FLOAT, const.GL_FALSE, 0, vVerts)
        gles2.glEnableVertexAttribArray(0)
        gles2.glDrawArrays(const.GL_TRIANGLES, 0, 3)
        egl.eglSwapBuffers(edsp, sfs)
        
    if isinstance(ev, xproto.KeyPressEvent):
        break
