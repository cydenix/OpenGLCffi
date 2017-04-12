from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'x'])
def glVertexAttribL1d(index, x):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttribL2d(index, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttribL3d(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttribL4d(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL1dv(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL2dv(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL3dv(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL4dv(index, v):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'stride', 'pointer'])
def glVertexAttribLPointer(index, size, type, stride, pointer):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribLdv(index, pname, params):
	pass


