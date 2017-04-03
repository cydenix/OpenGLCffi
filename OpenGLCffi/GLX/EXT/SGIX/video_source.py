from OpenGLCffi.GLX import params
@params('display', 'screen', 'server', 'path', 'nodeClass', 'drainNode', api='glx')
def glXCreateGLXVideoSourceSGIX(display, screen, server, path, nodeClass, drainNode):
	pass


@params('dpy', 'glxvideosource', api='glx')
def glXDestroyGLXVideoSourceSGIX(dpy, glxvideosource):
	pass


