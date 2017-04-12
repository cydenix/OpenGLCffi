from OpenGLCffi.GLX import params
@params(api='glx', prms=['attribute', 'value'])
def glXQueryCurrentRendererIntegerMESA(attribute):
	pass


@params(api='glx', prms=['attribute'])
def glXQueryCurrentRendererStringMESA(attribute):
	pass


@params(api='glx', prms=['dpy', 'screen', 'renderer', 'attribute', 'value'])
def glXQueryRendererIntegerMESA(dpy, screen, renderer, attribute):
	pass


@params(api='glx', prms=['dpy', 'screen', 'renderer', 'attribute'])
def glXQueryRendererStringMESA(dpy, screen, renderer, attribute):
	pass


