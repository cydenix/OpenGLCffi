def eglGetCurrentSurface(readdraw):
	return lib.eglGetCurrentSurface(readdraw)

def eglBindTexImage(dpy, surface, buffer):
	return lib.eglBindTexImage(dpy, surface, buffer)

def eglGetError():
	return lib.eglGetError()

def eglCreateContext(dpy, config, share_context, attrib_list):
	attr_lst = ffi.new('const EGLint []', attrib_list)
	return lib.eglCreateContext(dpy, config, share_context, attr_lst)

def eglWaitGL():
	return lib.eglWaitGL()

def eglBindAPI(api):
	return lib.eglBindAPI(api)

def eglReleaseThread():
	return lib.eglReleaseThread()

def eglTerminate(dpy):
	return lib.eglTerminate(dpy)

def eglCreateImage(dpy, ctx, target, buffer, attrib_list):
	attr_lst = ffi.new('const EGLAttrib []', attrib_list)
	return lib.eglCreateImage(dpy, ctx, target, buffer, attr_lst)

def eglSurfaceAttrib(dpy, surface, attribute):
	value = ffi.new('EGLint *')
	return lib.eglSurfaceAttrib(dpy, surface, attribute, value)

def eglSwapInterval(dpy, interval):
	return lib.eglSwapInterval(dpy, interval)

def eglGetSyncAttrib(dpy, sync, attribute):
	value = ffi.new('EGLAttrib *')
	return lib.eglGetSyncAttrib(dpy, sync, attribute, value)

def eglCreatePlatformWindowSurface(dpy, config, native_window, attrib_list):
	attr_lst = ffi.new('const EGLAttrib []', attrib_list)
	return lib.eglCreatePlatformWindowSurface(dpy, config, native_window, attr_lst)

def eglGetCurrentContext():
	return lib.eglGetCurrentContext()

def eglQueryString(dpy, name):
	return lib.eglQueryString(dpy, name)

def eglWaitSync(dpy, sync, flags):
	return lib.eglWaitSync(dpy, sync, flags)

def eglWaitClient():
	return lib.eglWaitClient()

def eglGetProcAddress(procname):
	return lib.eglGetProcAddress(procname)

def eglInitialize(dpy):
	major = ffi.new('EGLint *')
	minor = ffi.new('EGLint *')
	return lib.eglInitialize(dpy, major, minor)

def eglGetPlatformDisplay(platform, native_display, attrib_list):
	attr_lst = ffi.new('const EGLAttrib []', attrib_list)
	return lib.eglGetPlatformDisplay(platform, native_display, attr_lst)

def eglQueryContext(dpy, ctx, attribute):
	value = ffi.new('EGLint *')
	return lib.eglQueryContext(dpy, ctx, attribute, value)

def eglCreatePbufferFromClientBuffer(dpy, buftype, buffer, config, attrib_list):
	attr_lst = ffi.new('const EGLint []', attrib_list)
	return lib.eglCreatePbufferFromClientBuffer(dpy, buftype, buffer, config, attr_lst)

def eglChooseConfig(dpy, attrib_list, config_size):
	attr_lst = ffi.new('const EGLint []', attrib_list)
	configs = ffi.new('EGLConfig [config_size]')
	num_config = ffi.new('EGLint *')
	return lib.eglChooseConfig(dpy, attr_lst, configs, config_size, num_config)

def eglWaitNative(engine):
	return lib.eglWaitNative(engine)

def eglQuerySurface(dpy, surface, attribute):
	value = ffi.new('EGLint *')
	return lib.eglQuerySurface(dpy, surface, attribute, value)

def eglCreatePlatformPixmapSurface(dpy, config, native_pixmap, attrib_list):
	attr_lst = ffi.new('const EGLAttrib []', attrib_list)
	return lib.eglCreatePlatformPixmapSurface(dpy, config, native_pixmap, attr_lst)

def eglGetConfigAttrib(dpy, config, attribute):
	value = ffi.new('EGLint *')
	return lib.eglGetConfigAttrib(dpy, config, attribute, value)

def eglClientWaitSync(dpy, sync, flags, timeout):
	return lib.eglClientWaitSync(dpy, sync, flags, timeout)

def eglDestroyContext(dpy, ctx):
	return lib.eglDestroyContext(dpy, ctx)

def eglReleaseTexImage(dpy, surface, buffer):
	return lib.eglReleaseTexImage(dpy, surface, buffer)

def eglCreateWindowSurface(dpy, config, win, attrib_list):
	attr_lst = ffi.new('const EGLint []', attrib_list)
	return lib.eglCreateWindowSurface(dpy, config, win, attr_lst)

def eglCreateSync(dpy, type, attrib_list):
	attr_lst = ffi.new('const EGLAttrib []', attrib_list)
	return lib.eglCreateSync(dpy, type, attr_lst)

def eglGetConfigs(dpy, config_size):
	configs = ffi.new('EGLConfig [config_size]')
	num_config = ffi.new('EGLint *')
	return lib.eglGetConfigs(dpy, configs, config_size, num_config)

def eglCopyBuffers(dpy, surface, target):
	return lib.eglCopyBuffers(dpy, surface, target)

def eglSwapBuffers(dpy, surface):
	return lib.eglSwapBuffers(dpy, surface)

def eglCreatePixmapSurface(dpy, config, pixmap, attrib_list):
	attr_lst = ffi.new('const EGLint []', attrib_list)
	return lib.eglCreatePixmapSurface(dpy, config, pixmap, attr_lst)

def eglMakeCurrent(dpy, draw, read, ctx):
	return lib.eglMakeCurrent(dpy, draw, read, ctx)

def eglDestroyImage(dpy, image):
	return lib.eglDestroyImage(dpy, image)

def eglDestroySync(dpy, sync):
	return lib.eglDestroySync(dpy, sync)

def eglCreatePbufferSurface(dpy, config, attrib_list):
	attr_lst = ffi.new('const EGLint []', attrib_list)
	return lib.eglCreatePbufferSurface(dpy, config, attr_lst)

def eglDestroySurface(dpy, surface):
	return lib.eglDestroySurface(dpy, surface)

def eglQueryAPI():
	return lib.eglQueryAPI()

def eglGetCurrentDisplay():
	return lib.eglGetCurrentDisplay()

def eglGetDisplay(display_id):
	return lib.eglGetDisplay(display_id)

