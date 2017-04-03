from OpenGLCffi.GL import params
@params('n', 'fences', api='gl')
def glDeleteFencesNV(n, fences):
	pass


@params('n', 'fences', api='gl')
def glGenFencesNV(n, fences):
	pass


@params('fence', api='gl')
def glIsFenceNV(fence):
	pass


@params('fence', api='gl')
def glTestFenceNV(fence):
	pass


@params('fence', 'pname', 'params', api='gl')
def glGetFenceivNV(fence, pname, params):
	pass


@params('fence', api='gl')
def glFinishFenceNV(fence):
	pass


@params('fence', 'condition', api='gl')
def glSetFenceNV(fence, condition):
	pass


