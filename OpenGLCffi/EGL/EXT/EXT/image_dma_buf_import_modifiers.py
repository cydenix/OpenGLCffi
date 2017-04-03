from OpenGLCffi.EGL import params
@params('dpy', 'max_formats', 'formats', 'num_formats', api='egl')
def eglQueryDmaBufFormatsEXT(dpy, max_formats, formats, num_formats):
	pass


@params('dpy', 'format', 'max_modifiers', 'modifiers', 'external_only', 'num_modifiers', api='egl')
def eglQueryDmaBufModifiersEXT(dpy, format, max_modifiers, modifiers, external_only, num_modifiers):
	pass


