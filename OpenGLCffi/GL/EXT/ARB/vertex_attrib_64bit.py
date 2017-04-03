from OpenGLCffi.GL import params
@params('index', 'x', api='gl')
def glVertexAttribL1d(index, x):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttribL2d(index, x, y):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttribL3d(index, x, y, z):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttribL4d(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL1dv(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL2dv(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL3dv(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL4dv(index, v):
	pass


@params('index', 'size', 'type', 'stride', 'pointer', api='gl')
def glVertexAttribLPointer(index, size, type, stride, pointer):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribLdv(index, pname, params):
	pass


