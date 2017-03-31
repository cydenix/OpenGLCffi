@params('n', 'ids', api='gl')
def glGenOcclusionQueriesNV(n, ids):
	pass


@params('n', 'ids', api='gl')
def glDeleteOcclusionQueriesNV(n, ids):
	pass


@params('id', api='gl')
def glIsOcclusionQueryNV(id):
	pass


@params('id', api='gl')
def glBeginOcclusionQueryNV(id):
	pass


@params(api = 'gl')
def glEndOcclusionQueryNV():
	pass


@params('id', 'pname', 'params', api='gl')
def glGetOcclusionQueryivNV(id, pname, params):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetOcclusionQueryuivNV(id, pname, params):
	pass


