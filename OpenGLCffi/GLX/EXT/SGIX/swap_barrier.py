from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'drawable', 'barrier'])
def glXBindSwapBarrierSGIX(dpy, drawable, barrier):
	pass


@params(api='glx', prms=['dpy', 'screen', 'max'])
def glXQueryMaxSwapBarriersSGIX(dpy, screen, max):
	pass


