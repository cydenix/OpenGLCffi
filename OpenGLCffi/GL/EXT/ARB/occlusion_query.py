from OpenGLCffi.GL import params
@params('n', 'ids', api='gl')
def glGenQueriesARB(n, ids):
	pass


@params('n', 'ids', api='gl')
def glDeleteQueriesARB(n, ids):
	pass


@params('id', api='gl')
def glIsQueryARB(id):
	pass


@params('target', 'id', api='gl')
def glBeginQueryARB(target, id):
	pass


@params('target', api='gl')
def glEndQueryARB(target):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetQueryivARB(target, pname, params):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetQueryObjectivARB(id, pname, params):
	pass


@params('id', 'pname', 'params', api='gl')
def glGetQueryObjectuivARB(id, pname, params):
	pass


