from OpenGLCffi.GLX import params
@params('dpy', 'npipes', api='glx')
def glXQueryHyperpipeNetworkSGIX(dpy, npipes):
	pass


@params('dpy', 'networkId', 'npipes', 'cfg', 'hpId', api='glx')
def glXHyperpipeConfigSGIX(dpy, networkId, npipes, cfg, hpId):
	pass


@params('dpy', 'hpId', 'npipes', api='glx')
def glXQueryHyperpipeConfigSGIX(dpy, hpId, npipes):
	pass


@params('dpy', 'hpId', api='glx')
def glXDestroyHyperpipeConfigSGIX(dpy, hpId):
	pass


@params('dpy', 'hpId', api='glx')
def glXBindHyperpipeSGIX(dpy, hpId):
	pass


@params('dpy', 'timeSlice', 'attrib', 'size', 'attribList', 'returnAttribList', api='glx')
def glXQueryHyperpipeBestAttribSGIX(dpy, timeSlice, attrib, size, attribList, returnAttribList):
	pass


@params('dpy', 'timeSlice', 'attrib', 'size', 'attribList', api='glx')
def glXHyperpipeAttribSGIX(dpy, timeSlice, attrib, size, attribList):
	pass


@params('dpy', 'timeSlice', 'attrib', 'size', 'returnAttribList', api='glx')
def glXQueryHyperpipeAttribSGIX(dpy, timeSlice, attrib, size, returnAttribList):
	pass


