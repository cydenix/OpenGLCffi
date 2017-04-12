from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'fences'])
def glDeleteFencesNV(n, fences):
	pass


@params(api='gl', prms=['n', 'fences'])
def glGenFencesNV(n, fences):
	pass


@params(api='gl', prms=['fence'])
def glIsFenceNV(fence):
	pass


@params(api='gl', prms=['fence'])
def glTestFenceNV(fence):
	pass


@params(api='gl', prms=['fence', 'pname', 'params'])
def glGetFenceivNV(fence, pname, params):
	pass


@params(api='gl', prms=['fence'])
def glFinishFenceNV(fence):
	pass


@params(api='gl', prms=['fence', 'condition'])
def glSetFenceNV(fence, condition):
	pass


