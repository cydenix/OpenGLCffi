import os, sys
sys.path.append(os.path.abspath(".."))
from OpenGLCffi.GLX import glx, ffi
from OpenGLCffi.GL import gl, const
from OpenGLCffi.GL import ffi as glffi
from OpenGLCffi.GLX.const import *
from OpenGLCffi import *
from OpenGLCffi import util
import xcffib
from xcffib import xproto
from OpenGL.GLU import gluLookAt
from datetime import datetime

timeval = {}
framesPerFPS = 0
FPS = 0
Frame = 1
lastFrameTimeCounter = 0.0
TimeCounter = 0.0
DT = 0.0
prevTime = 0.0
rot_Z = 50.0
rot_Y = 30.0
rotation_matrix = glffi.new("GLfloat [16]")

d, conn = util.get_xdsp_xcb_connection(api='GLX')

def drawCube(size):

    gl.glBegin(const.GL_QUADS)

    gl.glColor3f(0.7, 0.0, 0.0)
    gl.glVertex3f(-size, -size, -size)
    gl.glVertex3f(size, -size, -size)
    gl.glVertex3f(size, size, -size)
    gl.glVertex3f(-size, size, -size)

    gl.glVertex3f(-size, -size, size)
    gl.glVertex3f(size, -size, size)
    gl.glVertex3f(size, size, size)
    gl.glVertex3f(-size, size, size)

    gl.glColor3f(0.0, 0.0, 0.7)

    gl.glVertex3f(-size, -size, -size)
    gl.glVertex3f(-size, -size, size)
    gl.glVertex3f(-size, size, size)
    gl.glVertex3f(-size, size, -size)

    gl.glVertex3f(size, -size, -size)
    gl.glVertex3f(size, -size, size)
    gl.glVertex3f(size, size, size)
    gl.glVertex3f(size, size, -size)

    gl.glColor3f(0.0, 0.7, 0.0)

    gl.glVertex3f(-size, -size, -size)
    gl.glVertex3f(-size, -size, size)
    gl.glVertex3f(size, -size, size)
    gl.glVertex3f(size, -size, -size)

    gl.glVertex3f(-size, size, -size)
    gl.glVertex3f(-size, size, size)
    gl.glVertex3f(size, size, size)
    gl.glVertex3f(size, size, -size)

    gl.glEnd()

def rotateCube():
    global rot_Z, rot_Y, rotation_matrix
    gl.glMatrixMode(const.GL_MODELVIEW)
    gl.glLoadIdentity()
    gl.glRotatef(rot_Y*DT, 0.0, 1.0, 0.0)
    gl.glRotatef(rot_Z*DT, 0.0, 0.0, 1.0)
    gl.glMultMatrixf(rotation_matrix)
    gl.glGetFloatv(const.GL_MODELVIEW_MATRIX, rotation_matrix)

def exposeFunc(dsp, w):
    global TimeCounter, FPS, rotation_matrix
    aspec = 600.0 / 600.0
    gl.glViewport(0, 0, 600, 600)
    gl.glMatrixMode(const.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-2.5 * aspec, 2.5*aspec, -2.5, 2.5, 1.0, 100.0)

    gl.glMatrixMode(const.GL_MODELVIEW)
    gl.glLoadIdentity()
    gluLookAt(10., 0., 0., 0., 0., 0., 0., 0., 1.)
    gl.glMultMatrixf(rotation_matrix)

    gl.glClear(const.GL_COLOR_BUFFER_BIT | const.GL_DEPTH_BUFFER_BIT)
    drawCube(1.0)

    gl.glMatrixMode(const.GL_MODELVIEW)
    gl.glLoadIdentity()

    gl.glColor3f(1.0, 1.0, 1.0)
    info_str = '{} fps'.format(FPS)
    print info_str
    gl.glRasterPos2i(10, 10)
    gl.glCallLists(len(info_str), const.GL_UNSIGNED_BYTE, info_str)
    glx.glXSwapBuffers(dsp, w)

def CreateWindow(cn):
    global win
    cmap_id = cn.generate_id()
    cn.core.CreateColormap(xproto.ColormapAlloc._None, cmap_id, root, vid)

    win = cn.generate_id()
    mask = xproto.CW.EventMask | xproto.CW.Colormap
    val = [xproto.EventMask.KeyPress, cmap_id]
    cn.core.CreateWindow(24, win, root, 0, 0, 700, 700, 0, xproto.WindowClass.InputOutput, vid, mask, val)
    cn.core.MapWindow(win)
    cn.flush()
    return win

def setupGL(cn, dsp, w, v):
    vi_attrib = [GLX_X_RENDERABLE, True,
                 GLX_DRAWABLE_TYPE, GLX_WINDOW_BIT,
                 GLX_RENDER_TYPE, GLX_RGBA_BIT,
                 GLX_X_VISUAL_TYPE, GLX_TRUE_COLOR,
                 GLX_RED_SIZE, 8,
                 GLX_GREEN_SIZE, 8,
                 GLX_BLUE_SIZE, 8,
                 GLX_ALPHA_SIZE, 8,
                 GLX_DEPTH_SIZE, 24,
                 GLX_STENCIL_SIZE, 8,
                 GLX_DOUBLEBUFFER, True,
                 GLX_NONE]

    conf = glx.glXChooseFBConfig(dsp, 0, vi_attrib)
    
    for i in xrange(conf['nelements'][0]):
        v_id = glx.glXGetFBConfigAttrib(dsp, conf['fn_ret'][i], GLX_VISUAL_ID)
        if v_id['value'][0] == v:
            dconf = conf['fn_ret'][i]

    ctx = glx.glXCreateNewContext(dsp, dconf, GLX_RGBA_TYPE, ffi.NULL, True)

    glx.glXMakeCurrent(dsp, w, ctx)
    gl.glEnable(const.GL_DEPTH_TEST)
    gl.glShadeModel(const.GL_SMOOTH)
    gl.glClearColor(0.0, 0.0, 0.40, 1.0)
    gl.glMatrixMode(const.GL_MODELVIEW)
    gl.glLoadIdentity()
    gl.glGetFloatv(const.GL_MODELVIEW_MATRIX, rotation_matrix)

def initTimeCounter():
    global framesPerFPS, timeval
    timeval['tv0'] = datetime.now()
    framesPerFPS = 30


def updateTimeCounter():
    global lastFrameTimeCounter, TimeCounter, DT, timeval
    lastFrameTimeCounter = TimeCounter
    timeval['tv'] = datetime.now()
    TimeCounter = float(timeval['tv'].second - timeval['tv0'].second) + 0.000001 * float(timeval['tv'].microsecond - timeval['tv0'].microsecond)
    DT = TimeCounter - lastFrameTimeCounter


def calculateFPS():
    global FPS, Frame, prevTime
    Frame += 1
    if (Frame % framesPerFPS) == 0:
        FPS = (float(framesPerFPS)) / (TimeCounter - prevTime)
        prevTime = TimeCounter

if __name__ == '__main__':
    import time
    setup = conn.get_setup()
    scr = setup.roots[0]
    root = scr.root
    vid = scr.root_visual
    white = scr.white_pixel
    black = scr.black_pixel
    win = None
    win = CreateWindow(conn)
    setupGL(conn, d, win, vid)
    initTimeCounter()
    print framesPerFPS, FPS

    while True:
        updateTimeCounter()
        calculateFPS()
        rotateCube()
        exposeFunc(d, win)
        time.sleep(0.001)
        print TimeCounter
        ev = conn.poll_for_event()
        if isinstance(ev, xproto.KeyPressEvent):
            if ev.detail == 114:
                rot_Z -= 200.0 * DT
                print DT, rot_Z
            elif ev.detail == 113:
                rot_Z += 200 * DT
            elif ev.detail == 111:
                rot_Y -= 200 * DT
            elif ev.detail == 116:
                rot_Y += 200 * DT
            elif ev.detail == 67:
                rot_Y = 0.0
                rot_Z = 0.0
            elif ev.detail == 9:
                break