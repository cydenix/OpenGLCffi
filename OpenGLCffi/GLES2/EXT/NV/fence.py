from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['n', 'fences'])
def glDeleteFencesNV(n, fences):
	pass


@params(api='gles2', prms=['n', 'fences'])
def glGenFencesNV(n, fences):
	pass


@params(api='gles2', prms=['fence'])
def glIsFenceNV(fence):
	pass


@params(api='gles2', prms=['fence'])
def glTestFenceNV(fence):
	pass


@params(api='gles2', prms=['fence', 'pname', 'params'])
def glGetFenceivNV(fence, pname):
	pass


@params(api='gles2', prms=['fence'])
def glFinishFenceNV(fence):
	pass


@params(api='gles2', prms=['fence', 'condition'])
def glSetFenceNV(fence, condition):
	pass


