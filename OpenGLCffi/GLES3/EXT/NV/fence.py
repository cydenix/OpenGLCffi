from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['n', 'fences'])
def glDeleteFencesNV(n, fences):
	pass


@params(api='gles3', prms=['n', 'fences'])
def glGenFencesNV(n, fences):
	pass


@params(api='gles3', prms=['fence'])
def glIsFenceNV(fence):
	pass


@params(api='gles3', prms=['fence'])
def glTestFenceNV(fence):
	pass


@params(api='gles3', prms=['fence', 'pname', 'params'])
def glGetFenceivNV(fence, pname):
	pass


@params(api='gles3', prms=['fence'])
def glFinishFenceNV(fence):
	pass


@params(api='gles3', prms=['fence', 'condition'])
def glSetFenceNV(fence, condition):
	pass


