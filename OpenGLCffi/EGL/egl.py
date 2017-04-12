from OpenGLCffi.EGL import params
@params(api='egl', prms=['readdraw'])
def eglGetCurrentSurface(readdraw):
	pass


@params(api='egl', prms=['dpy', 'surface', 'buffer'])
def eglBindTexImage(dpy, surface, buffer):
	pass


@params(api='egl', prms=[])
def eglGetError():
	pass


@params(api='egl', prms=['dpy', 'config', 'share_context', 'attrib_list'])
def eglCreateContext(dpy, config, share_context, attrib_list):
	pass


@params(api='egl', prms=[])
def eglWaitGL():
	pass


@params(api='egl', prms=['api'])
def eglBindAPI(api):
	pass


@params(api='egl', prms=[])
def eglReleaseThread():
	pass


@params(api='egl', prms=['dpy'])
def eglTerminate(dpy):
	pass


@params(api='egl', prms=['dpy', 'ctx', 'target', 'buffer', 'attrib_list'])
def eglCreateImage(dpy, ctx, target, buffer, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'surface', 'attribute', 'value'])
def eglSurfaceAttrib(dpy, surface, attribute):
	pass


@params(api='egl', prms=['dpy', 'interval'])
def eglSwapInterval(dpy, interval):
	pass


@params(api='egl', prms=['dpy', 'sync', 'attribute', 'value'])
def eglGetSyncAttrib(dpy, sync, attribute):
	pass


@params(api='egl', prms=['dpy', 'config', 'native_window', 'attrib_list'])
def eglCreatePlatformWindowSurface(dpy, config, native_window, attrib_list):
	pass


@params(api='egl', prms=[])
def eglGetCurrentContext():
	pass


@params(api='egl', prms=['dpy', 'name'])
def eglQueryString(dpy, name):
	pass


@params(api='egl', prms=['dpy', 'sync', 'flags'])
def eglWaitSync(dpy, sync, flags):
	pass


@params(api='egl', prms=[])
def eglWaitClient():
	pass


@params(api='egl', prms=['procname'])
def eglGetProcAddress(procname):
	pass


@params(api='egl', prms=['dpy', 'major', 'minor'])
def eglInitialize(dpy):
	pass


@params(api='egl', prms=['platform', 'native_display', 'attrib_list'])
def eglGetPlatformDisplay(platform, native_display, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'ctx', 'attribute', 'value'])
def eglQueryContext(dpy, ctx, attribute):
	pass


@params(api='egl', prms=['dpy', 'buftype', 'buffer', 'config', 'attrib_list'])
def eglCreatePbufferFromClientBuffer(dpy, buftype, buffer, config, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'attrib_list', 'configs', 'config_size', 'num_config'])
def eglChooseConfig(dpy, attrib_list, config_size):
	pass


@params(api='egl', prms=['engine'])
def eglWaitNative(engine):
	pass


@params(api='egl', prms=['dpy', 'surface', 'attribute', 'value'])
def eglQuerySurface(dpy, surface, attribute):
	pass


@params(api='egl', prms=['dpy', 'config', 'native_pixmap', 'attrib_list'])
def eglCreatePlatformPixmapSurface(dpy, config, native_pixmap, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'config', 'attribute', 'value'])
def eglGetConfigAttrib(dpy, config, attribute):
	pass


@params(api='egl', prms=['dpy', 'sync', 'flags', 'timeout'])
def eglClientWaitSync(dpy, sync, flags, timeout):
	pass


@params(api='egl', prms=['dpy', 'ctx'])
def eglDestroyContext(dpy, ctx):
	pass


@params(api='egl', prms=['dpy', 'surface', 'buffer'])
def eglReleaseTexImage(dpy, surface, buffer):
	pass


@params(api='egl', prms=['dpy', 'config', 'win', 'attrib_list'])
def eglCreateWindowSurface(dpy, config, win, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'type', 'attrib_list'])
def eglCreateSync(dpy, type, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'configs', 'config_size', 'num_config'])
def eglGetConfigs(dpy, config_size):
	pass


@params(api='egl', prms=['dpy', 'surface', 'target'])
def eglCopyBuffers(dpy, surface, target):
	pass


@params(api='egl', prms=['dpy', 'surface'])
def eglSwapBuffers(dpy, surface):
	pass


@params(api='egl', prms=['dpy', 'config', 'pixmap', 'attrib_list'])
def eglCreatePixmapSurface(dpy, config, pixmap, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'draw', 'read', 'ctx'])
def eglMakeCurrent(dpy, draw, read, ctx):
	pass


@params(api='egl', prms=['dpy', 'image'])
def eglDestroyImage(dpy, image):
	pass


@params(api='egl', prms=['dpy', 'sync'])
def eglDestroySync(dpy, sync):
	pass


@params(api='egl', prms=['dpy', 'config', 'attrib_list'])
def eglCreatePbufferSurface(dpy, config, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'surface'])
def eglDestroySurface(dpy, surface):
	pass


@params(api='egl', prms=[])
def eglQueryAPI():
	pass


@params(api='egl', prms=[])
def eglGetCurrentDisplay():
	pass


@params(api='egl', prms=['display_id'])
def eglGetDisplay(display_id):
	pass


