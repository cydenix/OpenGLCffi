from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['n', 'ids'])
def glGenQueriesEXT(n, ids):
	pass


@params(api='gles2', prms=['n', 'ids'])
def glDeleteQueriesEXT(n, ids):
	pass


@params(api='gles2', prms=['id'])
def glIsQueryEXT(id):
	pass


@params(api='gles2', prms=['target', 'id'])
def glBeginQueryEXT(target, id):
	pass


@params(api='gles2', prms=['target'])
def glEndQueryEXT(target):
	pass


@params(api='gles2', prms=['id', 'target'])
def glQueryCounterEXT(id, target):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetQueryivEXT(target, pname):
	pass


@params(api='gles2', prms=['id', 'pname', 'params'])
def glGetQueryObjectivEXT(id, pname):
	pass


@params(api='gles2', prms=['id', 'pname', 'params'])
def glGetQueryObjectuivEXT(id, pname):
	pass


@params(api='gles2', prms=['id', 'pname', 'params'])
def glGetQueryObjecti64vEXT(id, pname):
	pass


@params(api='gles2', prms=['id', 'pname', 'params'])
def glGetQueryObjectui64vEXT(id, pname):
	pass


