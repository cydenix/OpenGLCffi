from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'ids'])
def glGenOcclusionQueriesNV(n, ids):
	pass


@params(api='gl', prms=['n', 'ids'])
def glDeleteOcclusionQueriesNV(n, ids):
	pass


@params(api='gl', prms=['id'])
def glIsOcclusionQueryNV(id):
	pass


@params(api='gl', prms=['id'])
def glBeginOcclusionQueryNV(id):
	pass


@params(api='gl', prms=[])
def glEndOcclusionQueryNV():
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetOcclusionQueryivNV(id, pname, params):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetOcclusionQueryuivNV(id, pname, params):
	pass


