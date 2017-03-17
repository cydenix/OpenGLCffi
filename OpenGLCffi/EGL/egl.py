from OpenGLCffi.EGL import params
@params('readdraw', api='egl')
def eglGetCurrentSurface(readdraw):
	pass


@params('dpy', 'surface', 'buffer', api='egl')
def eglBindTexImage(dpy, surface, buffer):
	pass


@params(api = 'egl')
def eglGetError():
	pass


@params('dpy', 'config', 'share_context', 'attrib_list', api='egl')
def eglCreateContext(dpy, config, share_context, attrib_list):
	pass


@params(api = 'egl')
def eglWaitGL():
	pass


@params('api', api='egl')
def eglBindAPI(api):
	pass


@params(api = 'egl')
def eglReleaseThread():
	pass


@params('dpy', api='egl')
def eglTerminate(dpy):
	pass


@params('dpy', 'ctx', 'target', 'buffer', 'attrib_list', api='egl')
def eglCreateImage(dpy, ctx, target, buffer, attrib_list):
	pass


@params('dpy', 'surface', 'attribute', 'value', api='egl')
def eglSurfaceAttrib(dpy, surface, attribute):
	pass


@params('dpy', 'interval', api='egl')
def eglSwapInterval(dpy, interval):
	pass


@params('dpy', 'sync', 'attribute', 'value', api='egl')
def eglGetSyncAttrib(dpy, sync, attribute):
	pass


@params('dpy', 'config', 'native_window', 'attrib_list', api='egl')
def eglCreatePlatformWindowSurface(dpy, config, native_window, attrib_list):
	pass


@params(api = 'egl')
def eglGetCurrentContext():
	pass


@params('dpy', 'name', api='egl')
def eglQueryString(dpy, name):
	pass


@params('dpy', 'sync', 'flags', api='egl')
def eglWaitSync(dpy, sync, flags):
	pass


@params(api = 'egl')
def eglWaitClient():
	pass


@params('procname', api='egl')
def eglGetProcAddress(procname):
	pass


@params('dpy', 'major', 'minor', api='egl')
def eglInitialize(dpy):
	pass


@params('platform', 'native_display', 'attrib_list', api='egl')
def eglGetPlatformDisplay(platform, native_display, attrib_list):
	pass


@params('dpy', 'ctx', 'attribute', 'value', api='egl')
def eglQueryContext(dpy, ctx, attribute):
	pass


@params('dpy', 'buftype', 'buffer', 'config', 'attrib_list', api='egl')
def eglCreatePbufferFromClientBuffer(dpy, buftype, buffer, config, attrib_list):
	pass


@params('dpy', 'attrib_list', 'configs', 'config_size', 'num_config', api='egl')
def eglChooseConfig(dpy, attrib_list, config_size):
	pass


@params('engine', api='egl')
def eglWaitNative(engine):
	pass


@params('dpy', 'surface', 'attribute', 'value', api='egl')
def eglQuerySurface(dpy, surface, attribute):
	pass


@params('dpy', 'config', 'native_pixmap', 'attrib_list', api='egl')
def eglCreatePlatformPixmapSurface(dpy, config, native_pixmap, attrib_list):
	pass


@params('dpy', 'config', 'attribute', 'value', api='egl')
def eglGetConfigAttrib(dpy, config, attribute):
	pass


@params('dpy', 'sync', 'flags', 'timeout', api='egl')
def eglClientWaitSync(dpy, sync, flags, timeout):
	pass


@params('dpy', 'ctx', api='egl')
def eglDestroyContext(dpy, ctx):
	pass


@params('dpy', 'surface', 'buffer', api='egl')
def eglReleaseTexImage(dpy, surface, buffer):
	pass


@params('dpy', 'config', 'win', 'attrib_list', api='egl')
def eglCreateWindowSurface(dpy, config, win, attrib_list):
	pass


@params('dpy', 'type', 'attrib_list', api='egl')
def eglCreateSync(dpy, type, attrib_list):
	pass


@params('dpy', 'configs', 'config_size', 'num_config', api='egl')
def eglGetConfigs(dpy, config_size):
	pass


@params('dpy', 'surface', 'target', api='egl')
def eglCopyBuffers(dpy, surface, target):
	pass


@params('dpy', 'surface', api='egl')
def eglSwapBuffers(dpy, surface):
	pass


@params('dpy', 'config', 'pixmap', 'attrib_list', api='egl')
def eglCreatePixmapSurface(dpy, config, pixmap, attrib_list):
	pass


@params('dpy', 'draw', 'read', 'ctx', api='egl')
def eglMakeCurrent(dpy, draw, read, ctx):
	pass


@params('dpy', 'image', api='egl')
def eglDestroyImage(dpy, image):
	pass


@params('dpy', 'sync', api='egl')
def eglDestroySync(dpy, sync):
	pass


@params('dpy', 'config', 'attrib_list', api='egl')
def eglCreatePbufferSurface(dpy, config, attrib_list):
	pass


@params('dpy', 'surface', api='egl')
def eglDestroySurface(dpy, surface):
	pass


@params(api = 'egl')
def eglQueryAPI():
	pass


@params(api = 'egl')
def eglGetCurrentDisplay():
	pass


@params('display_id', api='egl')
def eglGetDisplay(display_id):
	pass


