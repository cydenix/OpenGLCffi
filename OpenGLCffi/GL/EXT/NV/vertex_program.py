from OpenGLCffi.GL import params
@params('n', 'programs', 'residences', api='gl')
def glAreProgramsResidentNV(n, programs, residences):
	pass


@params('target', 'id', api='gl')
def glBindProgramNV(target, id):
	pass


@params('n', 'programs', api='gl')
def glDeleteProgramsNV(n, programs):
	pass


@params('target', 'id', 'params', api='gl')
def glExecuteProgramNV(target, id, params):
	pass


@params('n', 'programs', api='gl')
def glGenProgramsNV(n, programs):
	pass


@params('target', 'index', 'pname', 'params', api='gl')
def glGetProgramParameterdvNV(target, index, pname, params):
	pass


@params('target', 'index', 'pname', 'params', api='gl')
def glGetProgramParameterfvNV(target, index, pname, params):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetProgramivNV(id, pname, params):
	pass


@params('id', 'pname', 'program', api='gl')
def glGetProgramStringNV(id, pname, program):
	pass


@params('target', 'address', 'pname', 'params', api='gl')
def glGetTrackMatrixivNV(target, address, pname, params):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribdvNV(index, pname, params):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribfvNV(index, pname, params):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribivNV(index, pname, params):
	pass


@params('index', 'pname', 'pointer', api='gl')
def glGetVertexAttribPointervNV(index, pname, pointer):
	pass


@params('id', api='gl')
def glIsProgramNV(id):
	pass


@params('target', 'id', 'len', 'program', api='gl')
def glLoadProgramNV(target, id, len, program):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramParameter4dNV(target, index, x, y, z, w):
	pass


@params('target', 'index', 'v', api='gl')
def glProgramParameter4dvNV(target, index, v):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramParameter4fNV(target, index, x, y, z, w):
	pass


@params('target', 'index', 'v', api='gl')
def glProgramParameter4fvNV(target, index, v):
	pass


@params('target', 'index', 'count', 'v', api='gl')
def glProgramParameters4dvNV(target, index, count, v):
	pass


@params('target', 'index', 'count', 'v', api='gl')
def glProgramParameters4fvNV(target, index, count, v):
	pass


@params('n', 'programs', api='gl')
def glRequestResidentProgramsNV(n, programs):
	pass


@params('target', 'address', 'matrix', 'transform', api='gl')
def glTrackMatrixNV(target, address, matrix, transform):
	pass


@params('index', 'fsize', 'type', 'stride', 'pointer', api='gl')
def glVertexAttribPointerNV(index, fsize, type, stride, pointer):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1dNV(index, x):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1dvNV(index, v):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1fNV(index, x):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1fvNV(index, v):
	pass


@params('index', 'x', api='gl')
def glVertexAttrib1sNV(index, x):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib1svNV(index, v):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2dNV(index, x, y):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2dvNV(index, v):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2fNV(index, x, y):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2fvNV(index, v):
	pass


@params('index', 'x', 'y', api='gl')
def glVertexAttrib2sNV(index, x, y):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib2svNV(index, v):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3dNV(index, x, y, z):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3dvNV(index, v):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3fNV(index, x, y, z):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3fvNV(index, v):
	pass


@params('index', 'x', 'y', 'z', api='gl')
def glVertexAttrib3sNV(index, x, y, z):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib3svNV(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4dNV(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4dvNV(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4fNV(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4fvNV(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4sNV(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4svNV(index, v):
	pass


@params('index', 'x', 'y', 'z', 'w', api='gl')
def glVertexAttrib4ubNV(index, x, y, z, w):
	pass


@params('index', 'v', api='gl')
def glVertexAttrib4ubvNV(index, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs1dvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs1fvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs1svNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs2dvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs2fvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs2svNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs3dvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs3fvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs3svNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs4dvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs4fvNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs4svNV(index, count, v):
	pass


@params('index', 'count', 'v', api='gl')
def glVertexAttribs4ubvNV(index, count, v):
	pass


