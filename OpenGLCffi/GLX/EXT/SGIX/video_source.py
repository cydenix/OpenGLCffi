from OpenGLCffi.GLX import params
@params(api='glx', prms=['display', 'screen', 'server', 'path', 'nodeClass', 'drainNode'])
def glXCreateGLXVideoSourceSGIX(display, screen, server, path, nodeClass, drainNode):
	pass


@params(api='glx', prms=['dpy', 'glxvideosource'])
def glXDestroyGLXVideoSourceSGIX(dpy, glxvideosource):
	pass


