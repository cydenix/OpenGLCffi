@params('readdraw',)
def eglGetCurrentSurface(readdraw):
	pass


@params('dpy', 'surface', 'buffer')
def eglBindTexImage(dpy, surface, buffer):
	pass


@params()
def eglGetError():
	pass


@params('dpy', 'config', 'share_context', 'attrib_list')
def eglCreateContext(dpy, config, share_context, attrib_list):
	pass


@params()
def eglWaitGL():
	pass


@params('api',)
def eglBindAPI(api):
	pass


@params()
def eglReleaseThread():
	pass


@params('dpy',)
def eglTerminate(dpy):
	pass


@params('dpy', 'ctx', 'target', 'buffer', 'attrib_list')
def eglCreateImage(dpy, ctx, target, buffer, attrib_list):
	pass


@params('dpy', 'surface', 'attribute', 'value')
def eglSurfaceAttrib(dpy, surface, attribute):
	pass


@params('dpy', 'interval')
def eglSwapInterval(dpy, interval):
	pass


@params('dpy', 'sync', 'attribute', 'value')
def eglGetSyncAttrib(dpy, sync, attribute):
	pass


@params('dpy', 'config', 'native_window', 'attrib_list')
def eglCreatePlatformWindowSurface(dpy, config, native_window, attrib_list):
	pass


@params()
def eglGetCurrentContext():
	pass


@params('dpy', 'name')
def eglQueryString(dpy, name):
	pass


@params('dpy', 'sync', 'flags')
def eglWaitSync(dpy, sync, flags):
	pass


@params()
def eglWaitClient():
	pass


@params('procname',)
def eglGetProcAddress(procname):
	pass


@params('dpy', 'major', 'minor')
def eglInitialize(dpy):
	pass


@params('platform', 'native_display', 'attrib_list')
def eglGetPlatformDisplay(platform, native_display, attrib_list):
	pass


@params('dpy', 'ctx', 'attribute', 'value')
def eglQueryContext(dpy, ctx, attribute):
	pass


@params('dpy', 'buftype', 'buffer', 'config', 'attrib_list')
def eglCreatePbufferFromClientBuffer(dpy, buftype, buffer, config, attrib_list):
	pass


@params('dpy', 'attrib_list', 'configs', 'config_size', 'num_config')
def eglChooseConfig(dpy, attrib_list, config_size):
	pass


@params('engine',)
def eglWaitNative(engine):
	pass


@params('dpy', 'surface', 'attribute', 'value')
def eglQuerySurface(dpy, surface, attribute):
	pass


@params('dpy', 'config', 'native_pixmap', 'attrib_list')
def eglCreatePlatformPixmapSurface(dpy, config, native_pixmap, attrib_list):
	pass


@params('dpy', 'config', 'attribute', 'value')
def eglGetConfigAttrib(dpy, config, attribute):
	pass


@params('dpy', 'sync', 'flags', 'timeout')
def eglClientWaitSync(dpy, sync, flags, timeout):
	pass


@params('dpy', 'ctx')
def eglDestroyContext(dpy, ctx):
	pass


@params('dpy', 'surface', 'buffer')
def eglReleaseTexImage(dpy, surface, buffer):
	pass


@params('dpy', 'config', 'win', 'attrib_list')
def eglCreateWindowSurface(dpy, config, win, attrib_list):
	pass


@params('dpy', 'type', 'attrib_list')
def eglCreateSync(dpy, type, attrib_list):
	pass


@params('dpy', 'configs', 'config_size', 'num_config')
def eglGetConfigs(dpy, config_size):
	pass


@params('dpy', 'surface', 'target')
def eglCopyBuffers(dpy, surface, target):
	pass


@params('dpy', 'surface')
def eglSwapBuffers(dpy, surface):
	pass


@params('dpy', 'config', 'pixmap', 'attrib_list')
def eglCreatePixmapSurface(dpy, config, pixmap, attrib_list):
	pass


@params('dpy', 'draw', 'read', 'ctx')
def eglMakeCurrent(dpy, draw, read, ctx):
	pass


@params('dpy', 'image')
def eglDestroyImage(dpy, image):
	pass


@params('dpy', 'sync')
def eglDestroySync(dpy, sync):
	pass


@params('dpy', 'config', 'attrib_list')
def eglCreatePbufferSurface(dpy, config, attrib_list):
	pass


@params('dpy', 'surface')
def eglDestroySurface(dpy, surface):
	pass


@params()
def eglQueryAPI():
	pass


@params()
def eglGetCurrentDisplay():
	pass


@params('display_id',)
def eglGetDisplay(display_id):
	pass


