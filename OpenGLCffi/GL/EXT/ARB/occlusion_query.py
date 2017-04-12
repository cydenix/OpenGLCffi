from OpenGLCffi.GL import params
@params(api='gl', prms=['n', 'ids'])
def glGenQueriesARB(n, ids):
	pass


@params(api='gl', prms=['n', 'ids'])
def glDeleteQueriesARB(n, ids):
	pass


@params(api='gl', prms=['id'])
def glIsQueryARB(id):
	pass


@params(api='gl', prms=['target', 'id'])
def glBeginQueryARB(target, id):
	pass


@params(api='gl', prms=['target'])
def glEndQueryARB(target):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetQueryivARB(target, pname, params):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjectivARB(id, pname, params):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjectuivARB(id, pname, params):
	pass


