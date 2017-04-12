from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['n', 'fences'])
def glDeleteFencesNV(n, fences):
	pass


@params(api='gles1', prms=['n', 'fences'])
def glGenFencesNV(n, fences):
	pass


@params(api='gles1', prms=['fence'])
def glIsFenceNV(fence):
	pass


@params(api='gles1', prms=['fence'])
def glTestFenceNV(fence):
	pass


@params(api='gles1', prms=['fence', 'pname', 'params'])
def glGetFenceivNV(fence, pname):
	pass


@params(api='gles1', prms=['fence'])
def glFinishFenceNV(fence):
	pass


@params(api='gles1', prms=['fence', 'condition'])
def glSetFenceNV(fence, condition):
	pass


