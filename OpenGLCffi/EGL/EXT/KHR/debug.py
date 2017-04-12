from OpenGLCffi.EGL import params
@params(api='egl', prms=['callback', 'attrib_list'])
def eglDebugMessageControlKHR(callback, attrib_list):
	pass


@params(api='egl', prms=['attribute', 'value'])
def eglQueryDebugKHR(attribute):
	pass


@params(api='egl', prms=['display', 'objectType', 'object', 'label'])
def eglLabelObjectKHR(display, objectType, object, label):
	pass


