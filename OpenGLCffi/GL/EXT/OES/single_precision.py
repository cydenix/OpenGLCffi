from OpenGLCffi.GL import params
@params('depth', api='gl')
def glClearDepthfOES(depth):
	pass


@params('plane', 'equation', api='gl')
def glClipPlanefOES(plane, equation):
	pass


@params('n', 'f', api='gl')
def glDepthRangefOES(n, f):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gl')
def glFrustumfOES(l, r, b, t, n, f):
	pass


@params('plane', 'equation', api='gl')
def glGetClipPlanefOES(plane, equation):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gl')
def glOrthofOES(l, r, b, t, n, f):
	pass


