from OpenGLCffi.EGL import params
@params(api='egl', prms=['platform', 'native_display', 'attrib_list'])
def eglGetPlatformDisplayEXT(platform, native_display, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'config', 'native_window', 'attrib_list'])
def eglCreatePlatformWindowSurfaceEXT(dpy, config, native_window, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'config', 'native_pixmap', 'attrib_list'])
def eglCreatePlatformPixmapSurfaceEXT(dpy, config, native_pixmap, attrib_list):
	pass


