from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'programs', 'residences'])
def glAreProgramsResidentNV(n, programs, residences):
	pass


@params(api='gl', prms=['target', 'id'])
def glBindProgramNV(target, id):
	pass


@params(api='gl', prms=['n', 'programs'])
def glDeleteProgramsNV(n, programs):
	pass


@params(api='gl', prms=['target', 'id', 'params'])
def glExecuteProgramNV(target, id, params):
	pass


@params(api='gl', prms=['n', 'programs'])
def glGenProgramsNV(n, programs):
	pass


@params(api='gl', prms=['target', 'index', 'pname', 'params'])
def glGetProgramParameterdvNV(target, index, pname, params):
	pass


@params(api='gl', prms=['target', 'index', 'pname', 'params'])
def glGetProgramParameterfvNV(target, index, pname, params):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetProgramivNV(id, pname, params):
	pass


@params(api='gl', prms=['id', 'pname', 'program'])
def glGetProgramStringNV(id, pname, program):
	pass


@params(api='gl', prms=['target', 'address', 'pname', 'params'])
def glGetTrackMatrixivNV(target, address, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribdvNV(index, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribfvNV(index, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribivNV(index, pname, params):
	pass


@params(api='gl', prms=['index', 'pname', 'pointer'])
def glGetVertexAttribPointervNV(index, pname, pointer):
	pass


@params(api='gl', prms=['id'])
def glIsProgramNV(id):
	pass


@params(api='gl', prms=['target', 'id', 'len', 'program'])
def glLoadProgramNV(target, id, len, program):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramParameter4dNV(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'v'])
def glProgramParameter4dvNV(target, index, v):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramParameter4fNV(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'v'])
def glProgramParameter4fvNV(target, index, v):
	pass


@params(api='gl', prms=['target', 'index', 'count', 'v'])
def glProgramParameters4dvNV(target, index, count, v):
	pass


@params(api='gl', prms=['target', 'index', 'count', 'v'])
def glProgramParameters4fvNV(target, index, count, v):
	pass


@params(api='gl', prms=['n', 'programs'])
def glRequestResidentProgramsNV(n, programs):
	pass


@params(api='gl', prms=['target', 'address', 'matrix', 'transform'])
def glTrackMatrixNV(target, address, matrix, transform):
	pass


@params(api='gl', prms=['index', 'fsize', 'type', 'stride', 'pointer'])
def glVertexAttribPointerNV(index, fsize, type, stride, pointer):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1dNV(index, x):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1dvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1fNV(index, x):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1fvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttrib1sNV(index, x):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib1svNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2dNV(index, x, y):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2dvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2fNV(index, x, y):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2fvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y'])
def glVertexAttrib2sNV(index, x, y):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib2svNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3dNV(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3dvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3fNV(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3fvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z'])
def glVertexAttrib3sNV(index, x, y, z):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib3svNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4dNV(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4dvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4fNV(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4fvNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4sNV(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4svNV(index, v):
	pass


@params(api='gl', prms=['index', 'x', 'y', 'z', 'w'])
def glVertexAttrib4ubNV(index, x, y, z, w):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttrib4ubvNV(index, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs1dvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs1fvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs1svNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs2dvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs2fvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs2svNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs3dvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs3fvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs3svNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs4dvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs4fvNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs4svNV(index, count, v):
	pass


@params(api='gl', prms=['index', 'count', 'v'])
def glVertexAttribs4ubvNV(index, count, v):
	pass


