from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['depth'])
def glClearDepthfOES(depth):
	pass


@params(api='gles1', prms=['plane', 'equation'])
def glClipPlanefOES(plane, equation):
	pass


@params(api='gles1', prms=['n', 'f'])
def glDepthRangefOES(n, f):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glFrustumfOES(l, r, b, t, n, f):
	pass


@params(api='gles1', prms=['plane', 'equation'])
def glGetClipPlanefOES(plane):
	pass


@params(api='gles1', prms=['l', 'r', 'b', 't', 'n', 'f'])
def glOrthofOES(l, r, b, t, n, f):
	pass


