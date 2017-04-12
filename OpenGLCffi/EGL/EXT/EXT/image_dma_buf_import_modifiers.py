from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'max_formats', 'formats', 'num_formats'])
def eglQueryDmaBufFormatsEXT(dpy, max_formats, formats, num_formats):
	pass


@params(api='egl', prms=['dpy', 'format', 'max_modifiers', 'modifiers', 'external_only', 'num_modifiers'])
def eglQueryDmaBufModifiersEXT(dpy, format, max_modifiers, modifiers, external_only, num_modifiers):
	pass


