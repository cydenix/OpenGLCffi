from OpenGLCffi.GL import params
@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1dARB(index, x):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1fARB(index, x):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1sARB(index, x):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1svARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2dARB(index, x, y):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2fARB(index, x, y):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2sARB(index, x, y):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2svARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3dARB(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3fARB(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3sARB(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3svARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NbvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NivARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NsvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4NubARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NubvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NuivARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4NusvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4bvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4dARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4dvARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4fARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4fvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4ivARB(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4sARB(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4svARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4ubvARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4uivARB(index, v):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4usvARB(index, v):
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


@params(api='gl', prms=['target', 'format', 'len', 'string'])
def glProgramStringARB(target, format, len, string):
	pass


@params(api='gl', prms=['target', 'program'])
def glBindProgramARB(target, program):
	pass


@params(api='gl', prms=['n', 'programs'])
def glDeleteProgramsARB(n, programs):
	pass


@params(api='gl', prms=['n', 'programs'])
def glGenProgramsARB(n, programs):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramEnvParameter4dARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramEnvParameter4dvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramEnvParameter4fARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramEnvParameter4fvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramLocalParameter4dARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramLocalParameter4dvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramLocalParameter4fARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramLocalParameter4fvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramEnvParameterdvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramEnvParameterfvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramLocalParameterdvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramLocalParameterfvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetProgramivARB(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'string'])
def glGetProgramStringARB(target, pname, string):
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


@params(api='gl', prms=['program'])
def glIsProgramARB(program):
	pass


