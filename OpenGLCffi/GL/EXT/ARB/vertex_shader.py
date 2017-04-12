from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1fARB(index, x):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1sARB(index, x):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1dARB(index, x):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2fARB(index, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2sARB(index, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2dARB(index, x, y):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3fARB(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3sARB(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3dARB(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4fARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4sARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4dARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4NubARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1svARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2svARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3svARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4svARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4ivARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4bvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4ubvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4usvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4uivARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NbvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NsvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NivARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NubvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NusvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NuivARB(index, v):
	pass


@params(api='gl', prms=['index', 'size', 'type', 'normalized', 'stride', 'pointer'])
def glVertexAttribPointerARB(index, size, type, normalized, stride, pointer):
	pass


@params(api='gl', prms=['index'])
def glEnableVertexAttribArrayARB(index):
	pass


@params(api='gl', prms=['index'])
def glDisableVertexAttribArrayARB(index):
	pass


@params(api='gl', prms=['programObj', 'index', 'name'])
def glBindAttribLocationARB(programObj, index, name):
	pass


@params(api='gl', prms=['programObj', 'index', 'maxLength', 'length', 'size', 'type', 'name'])
def glGetActiveAttribARB(programObj, index, maxLength, length, size, type, name):
	pass


@params(api='gl', prms=['programObj', 'name'])
def glGetAttribLocationARB(programObj, name):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribdvARB(index, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribfvARB(index, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribivARB(index, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'pointer'])
def glGetVertexAttribPointervARB(index, pname, pointer):
	pass


