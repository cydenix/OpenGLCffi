from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'draw', 'read', 'ctx'])
def glXMakeCurrentReadSGI(dpy, draw, read, ctx):
	pass


@params(api='glx', prms=[])
def glXGetCurrentReadDrawableSGI():
	pass


