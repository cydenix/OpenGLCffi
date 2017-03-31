@params('n', 'fences', api='gles1')
def glDeleteFencesNV(n, fences):
	pass


@params('n', 'fences', api='gles1')
def glGenFencesNV(n, fences):
	pass


@params('fence', api='gles1')
def glIsFenceNV(fence):
	pass


@params('fence', api='gles1')
def glTestFenceNV(fence):
	pass


@params('fence', 'pname', 'params', api='gles1')
def glGetFenceivNV(fence, pname):
	pass


@params('fence', api='gles1')
def glFinishFenceNV(fence):
	pass


@params('fence', 'condition', api='gles1')
def glSetFenceNV(fence, condition):
	pass


