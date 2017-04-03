from OpenGLCffi.GLX import params
@params('dpy', 'draw', 'read', 'ctx', api='glx')
def glXMakeCurrentReadSGI(dpy, draw, read, ctx):
	pass


@params(api = 'glx')
def glXGetCurrentReadDrawableSGI():
	pass


