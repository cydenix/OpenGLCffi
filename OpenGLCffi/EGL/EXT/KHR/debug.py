from OpenGLCffi.EGL import params
@params('callback', 'attrib_list', api='egl')
def eglDebugMessageControlKHR(callback, attrib_list):
	pass


@params('attribute', 'value', api='egl')
def eglQueryDebugKHR(attribute):
	pass


@params('display', 'objectType', 'object', 'label', api='egl')
def eglLabelObjectKHR(display, objectType, object, label):
	pass


