@params('n', 'fences', api='gles3')
def glDeleteFencesNV(n, fences):
	pass


@params('n', 'fences', api='gles3')
def glGenFencesNV(n, fences):
	pass


@params('fence', api='gles3')
def glIsFenceNV(fence):
	pass


@params('fence', api='gles3')
def glTestFenceNV(fence):
	pass


@params('fence', 'pname', 'params', api='gles3')
def glGetFenceivNV(fence, pname):
	pass


@params('fence', api='gles3')
def glFinishFenceNV(fence):
	pass


@params('fence', 'condition', api='gles3')
def glSetFenceNV(fence, condition):
	pass


