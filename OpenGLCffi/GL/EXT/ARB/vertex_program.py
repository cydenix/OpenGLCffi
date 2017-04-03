from OpenGLCffi.GL import params
@params('index', 'x', api='gl')
def glVertexAttrib1dARB(index, x):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1dvARB(index, v):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1fARB(index, x):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1fvARB(index, v):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1sARB(index, x):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1svARB(index, v):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2dARB(index, x, y):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2dvARB(index, v):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2fARB(index, x, y):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2fvARB(index, v):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2sARB(index, x, y):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2svARB(index, v):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3dARB(index, x, y, z):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3dvARB(index, v):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3fARB(index, x, y, z):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3fvARB(index, v):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3sARB(index, x, y, z):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3svARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NbvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NivARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NsvARB(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4NubARB(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NubvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NuivARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4NusvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4bvARB(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4dARB(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4dvARB(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4fARB(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4fvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4ivARB(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4sARB(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4svARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4ubvARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4uivARB(index, v):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4usvARB(index, v):
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


@params('target', 'format', 'len', 'string', api='gl')
def glProgramStringARB(target, format, len, string):
	pass


@params('target', 'program', api='gl')
def glBindProgramARB(target, program):
	pass


@params('n', 'programs', api='gl')
def glDeleteProgramsARB(n, programs):
	pass


@params('n', 'programs', api='gl')
def glGenProgramsARB(n, programs):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramEnvParameter4dARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramEnvParameter4dvARB(target, index, params):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramEnvParameter4fARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramEnvParameter4fvARB(target, index, params):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramLocalParameter4dARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramLocalParameter4dvARB(target, index, params):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramLocalParameter4fARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramLocalParameter4fvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramEnvParameterdvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramEnvParameterfvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramLocalParameterdvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramLocalParameterfvARB(target, index, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetProgramivARB(target, pname, params):
	pass


@params('target', 'pname', 'string', api='gl')
def glGetProgramStringARB(target, pname, string):
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


@params('program', api='gl')
def glIsProgramARB(program):
	pass


