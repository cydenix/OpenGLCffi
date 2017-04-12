from OpenGLCffi.GL import params
@params(api='gl', prms=['depth'])
def glClearDepthfOES(depth):
	pass


@params(api='gl', prms=['plane', 'equation'])
def glClipPlanefOES(plane, equation):
	pass


@params(api='gl', prms=['n', 'f'])
def glDepthRangefOES(n, f):
	pass


@params(api='gl', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glFrustumfOES(l, r, b, t, n, f):
	pass


@params(api='gl', prms=['plane', 'equation'])
def glGetClipPlanefOES(plane, equation):
	pass


@params(api='gl', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glOrthofOES(l, r, b, t, n, f):
	pass


