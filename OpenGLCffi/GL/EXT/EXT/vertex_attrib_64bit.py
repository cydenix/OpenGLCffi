from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'x'])
def glVertexAttribL1dEXT(index, x):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttribL2dEXT(index, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttribL3dEXT(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttribL4dEXT(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL1dvEXT(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL2dvEXT(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL3dvEXT(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL4dvEXT(index, v):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'stride', 'pointer'])
def glVertexAttribLPointerEXT(index, size, type, stride, pointer):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribLdvEXT(index, pname, params):
	pass


