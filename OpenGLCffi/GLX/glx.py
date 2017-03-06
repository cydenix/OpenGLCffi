def glXCreateContext(dpy, vis, shareList, direct):
	return lib.glXCreateContext(dpy, vis, shareList, direct)

def glXCreateGLXPixmap(dpy, visual, pixmap):
	return lib.glXCreateGLXPixmap(dpy, visual, pixmap)

def glXGetProcAddress(procName):
	return lib.glXGetProcAddress(procName)

def glXDestroyWindow(dpy, win):
	return lib.glXDestroyWindow(dpy, win)

def glXQueryDrawable(dpy, draw, attribute):
	value = ffi.new('unsigned int *')
	return lib.glXQueryDrawable(dpy, draw, attribute, value)

def glXSwapBuffers(dpy, drawable):
	return lib.glXSwapBuffers(dpy, drawable)

def glXGetCurrentDisplay():
	return lib.glXGetCurrentDisplay()

def glXChooseVisual(dpy, screen, attribList):
	attr_lst = ffi.new('int []', attribList)
	return lib.glXChooseVisual(dpy, screen, attribList)

def glXDestroyPbuffer(dpy, pbuf):
	return lib.glXDestroyPbuffer(dpy, pbuf)

def glXCreatePixmap(dpy, config, pixmap, attrib_list):
	attr_lst = ffi.new('const int []', attrib_list)
	return lib.glXCreatePixmap(dpy, config, pixmap, attr_lst)

def glXSelectEvent(dpy, draw, event_mask):
	return lib.glXSelectEvent(dpy, draw, event_mask)

def glXGetSelectedEvent(dpy, draw, event_mask):
	return lib.glXGetSelectedEvent(dpy, draw, event_mask)

def glXQueryExtension(dpy, errorb, event):
	return lib.glXQueryExtension(dpy, errorb, event)

def glXMakeCurrent(dpy, drawable, ctx):
	return lib.glXMakeCurrent(dpy, drawable, ctx)

def glXCreatePbuffer(dpy, config, attrib_list):
	attr_lst = ffi.new('const int []', attrib_list)
	return lib.glXCreatePbuffer(dpy, config, attr_lst)

def glXDestroyGLXPixmap(dpy, pixmap):
	return lib.glXDestroyGLXPixmap(dpy, pixmap)

def glXChooseFBConfig(dpy, screen, attrib_list):
	attr_lst = ffi.new('const int []', attrib_list)
	nelements = ffi.new('int *')
	return lib.glXChooseFBConfig(dpy, screen, attr_lst, nelements)

def glXGetConfig(dpy, visual, attrib):
	value = ffi.new('int *')
	return lib.glXGetConfig(dpy, visual, attrib, value)

def glXWaitX():
	return lib.glXWaitX()

def glXGetCurrentContext():
	return lib.glXGetCurrentContext()

def glXWaitGL():
	return lib.glXWaitGL()

def glXQueryVersion(dpy):
	maj = ffi.new('int *')
	min = ffi.new('int *')
	return lib.glXQueryVersion(dpy, maj, min)

def glXDestroyPixmap(dpy, pixmap):
	return lib.glXDestroyPixmap(dpy, pixmap)

def glXIsDirect(dpy, ctx):
	return lib.glXIsDirect(dpy, ctx)

def glXDestroyContext(dpy, ctx):
	return lib.glXDestroyContext(dpy, ctx)

def glXCreateNewContext(dpy, config, render_type, share_list, direct):
	return lib.glXCreateNewContext(dpy, config, render_type, share_list, direct)

def glXGetClientString(dpy, name):
	return lib.glXGetClientString(dpy, name)

def glXGetVisualFromFBConfig(dpy, config):
	return lib.glXGetVisualFromFBConfig(dpy, config)

def glXGetFBConfigs(dpy, screen):
	nelements = ffi.new('int *')
	return lib.glXGetFBConfigs(dpy, screen, nelements)

def glXGetCurrentReadDrawable():
	return lib.glXGetCurrentReadDrawable()

def glXQueryContext(dpy, ctx, attribute):
	value = ffi.new('int *')
	return lib.glXQueryContext(dpy, ctx, attribute, value)

def glXCreateWindow(dpy, config, win, attrib_list):
	attr_lst = ffi.new('const int []', attrib_list)
	return lib.glXCreateWindow(dpy, config, win, attr_lst)

def glXCopyContext(dpy, src, dst, mask):
	return lib.glXCopyContext(dpy, src, dst, mask)

def glXQueryServerString(dpy, screen, name):
	return lib.glXQueryServerString(dpy, screen, name)

def glXGetFBConfigAttrib(dpy, config, attribute):
	value = ffi.new('int *')
	return lib.glXGetFBConfigAttrib(dpy, config, attribute, value)

def glXUseXFont(font, first, count, list):
	return lib.glXUseXFont(font, first, count, list)

def glXMakeContextCurrent(dpy, draw, read, ctx):
	return lib.glXMakeContextCurrent(dpy, draw, read, ctx)

def glXGetCurrentDrawable():
	return lib.glXGetCurrentDrawable()

def glXQueryExtensionsString(dpy, screen):
	return lib.glXQueryExtensionsString(dpy, screen)

