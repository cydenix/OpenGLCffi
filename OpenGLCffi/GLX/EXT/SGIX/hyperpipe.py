from OpenGLCffi.GLX import params
@params(api='glx', prms=['dpy', 'npipes'])
def glXQueryHyperpipeNetworkSGIX(dpy, npipes):
	pass


@params(api='glx', prms=['dpy', 'networkId', 'npipes', 'cfg', 'hpId'])
def glXHyperpipeConfigSGIX(dpy, networkId, npipes, cfg, hpId):
	pass


@params(api='glx', prms=['dpy', 'hpId', 'npipes'])
def glXQueryHyperpipeConfigSGIX(dpy, hpId, npipes):
	pass


@params(api='glx', prms=['dpy', 'hpId'])
def glXDestroyHyperpipeConfigSGIX(dpy, hpId):
	pass


@params(api='glx', prms=['dpy', 'hpId'])
def glXBindHyperpipeSGIX(dpy, hpId):
	pass


@params(api='glx', prms=['dpy', 'timeSlice', 'attrib', 'size', 'attribList', 'returnAttribList'])
def glXQueryHyperpipeBestAttribSGIX(dpy, timeSlice, attrib, size, attribList, returnAttribList):
	pass


@params(api='glx', prms=['dpy', 'timeSlice', 'attrib', 'size', 'attribList'])
def glXHyperpipeAttribSGIX(dpy, timeSlice, attrib, size, attribList):
	pass


@params(api='glx', prms=['dpy', 'timeSlice', 'attrib', 'size', 'returnAttribList'])
def glXQueryHyperpipeAttribSGIX(dpy, timeSlice, attrib, size, returnAttribList):
	pass


