from OpenGLCffi.GL import params
@params('id', 'len', 'name', 'x', 'y', 'z', 'w', api='gl')
def glProgramNamedParameter4fNV(id, len, name, x, y, z, w):
	pass


@params('id', 'len', 'name', 'v', api='gl')
def glProgramNamedParameter4fvNV(id, len, name, v):
	pass


@params('id', 'len', 'name', 'x', 'y', 'z', 'w', api='gl')
def glProgramNamedParameter4dNV(id, len, name, x, y, z, w):
	pass


@params('id', 'len', 'name', 'v', api='gl')
def glProgramNamedParameter4dvNV(id, len, name, v):
	pass


@params('id', 'len', 'name', 'params', api='gl')
def glGetProgramNamedParameterfvNV(id, len, name, params):
	pass


@params('id', 'len', 'name', 'params', api='gl')
def glGetProgramNamedParameterdvNV(id, len, name, params):
	pass


