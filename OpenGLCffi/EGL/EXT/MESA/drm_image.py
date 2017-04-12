from OpenGLCffi.EGL import params
@params(api='egl', prms=['dpy', 'attrib_list'])
def eglCreateDRMImageMESA(dpy, attrib_list):
	pass


@params(api='egl', prms=['dpy', 'image', 'name', 'handle', 'stride'])
def eglExportDRMImageMESA(dpy, image, name, handle, stride):
	pass


