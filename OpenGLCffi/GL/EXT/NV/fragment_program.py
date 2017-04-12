from OpenGLCffi.GL import params
@params(api='gl', prms=['id', 'len', 'name', 'x', 'y', 'z', 'w'])
def glProgramNamedParameter4fNV(id, len, name, x, y, z, w):
	pass


@params(api='gl', prms=['id', 'len', 'name', 'v'])
def glProgramNamedParameter4fvNV(id, len, name, v):
	pass


@params(api='gl', prms=['id', 'len', 'name', 'x', 'y', 'z', 'w'])
def glProgramNamedParameter4dNV(id, len, name, x, y, z, w):
	pass


@params(api='gl', prms=['id', 'len', 'name', 'v'])
def glProgramNamedParameter4dvNV(id, len, name, v):
	pass


@params(api='gl', prms=['id', 'len', 'name', 'params'])
def glGetProgramNamedParameterfvNV(id, len, name, params):
	pass


@params(api='gl', prms=['id', 'len', 'name', 'params'])
def glGetProgramNamedParameterdvNV(id, len, name, params):
	pass


