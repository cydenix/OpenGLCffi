from OpenGLCffi.GL import params
@params('index', 'x', api='gl')
def glVertexAttrib1fARB(index, x):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1sARB(index, x):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1dARB(index, x):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2fARB(index, x, y):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2sARB(index, x, y):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2dARB(index, x, y):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3fARB(index, x, y, z):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3sARB(index, x, y, z):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3dARB(index, x, y, z):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4fARB(index, x, y, z, w):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4sARB(index, x, y, z, w):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4dARB(index, x, y, z, w):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4NubARB(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1fvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1svARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1dvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2fvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2svARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2dvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3fvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3svARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3dvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4fvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4svARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4dvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4ivARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4bvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4ubvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4usvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4uivARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NbvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NsvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NivARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NubvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NusvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NuivARB(index, v):
	pass


@params('index', 'size', 'type', 'normalized', 'stride', 'pointer', api='gl')
def glVertexAttribPointerARB(index, size, type, normalized, stride, pointer):
	pass


@params('index', api='gl')
def glEnableVertexAttribArrayARB(index):
	pass


@params('index', api='gl')
def glDisableVertexAttribArrayARB(index):
	pass


@params('programObj', 'index', 'name', api='gl')
def glBindAttribLocationARB(programObj, index, name):
	pass


@params('programObj', 'index', 'maxLength', 'length', 'size', 'type', 'name', api='gl')
def glGetActiveAttribARB(programObj, index, maxLength, length, size, type, name):
	pass


@params('programObj', 'name', api='gl')
def glGetAttribLocationARB(programObj, name):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribdvARB(index, pname, params):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribfvARB(index, pname, params):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribivARB(index, pname, params):
	pass


@params('index', 'pname', 'pointer', api='gl')
def glGetVertexAttribPointervARB(index, pname, pointer):
	pass


