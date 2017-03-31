@params('n', 'fences', api='gles2')
def glDeleteFencesNV(n, fences):
	pass


@params('n', 'fences', api='gles2')
def glGenFencesNV(n, fences):
	pass


@params('fence', api='gles2')
def glIsFenceNV(fence):
	pass


@params('fence', api='gles2')
def glTestFenceNV(fence):
	pass


@params('fence', 'pname', 'params', api='gles2')
def glGetFenceivNV(fence, pname):
	pass


@params('fence', api='gles2')
def glFinishFenceNV(fence):
	pass


@params('fence', 'condition', api='gles2')
def glSetFenceNV(fence, condition):
	pass


