from OpenGLCffi.GLX import params
@params('attribute', 'value', api='glx')
def glXQueryCurrentRendererIntegerMESA(attribute):
	pass


@params('attribute', api='glx')
def glXQueryCurrentRendererStringMESA(attribute):
	pass


@params('dpy', 'screen', 'renderer', 'attribute', 'value', api='glx')
def glXQueryRendererIntegerMESA(dpy, screen, renderer, attribute):
	pass


@params('dpy', 'screen', 'renderer', 'attribute', api='glx')
def glXQueryRendererStringMESA(dpy, screen, renderer, attribute):
	pass


