@params('depth', api='gles1')
def glClearDepthfOES(depth):
	pass


@params('plane', 'equation', api='gles1')
def glClipPlanefOES(plane, equation):
	pass


@params('n', 'f', api='gles1')
def glDepthRangefOES(n, f):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glFrustumfOES(l, r, b, t, n, f):
	pass


@params('plane', 'equation', api='gles1')
def glGetClipPlanefOES(plane):
	pass


@params('l', 'r', 'b', 't', 'n', 'f', api='gles1')
def glOrthofOES(l, r, b, t, n, f):
	pass


