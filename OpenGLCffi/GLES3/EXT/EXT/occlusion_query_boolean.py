from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['n', 'ids'])
def glGenQueriesEXT(n, ids):
	pass


@params(api='gles3', prms=['n', 'ids'])
def glDeleteQueriesEXT(n, ids):
	pass


@params(api='gles3', prms=['id'])
def glIsQueryEXT(id):
	pass


@params(api='gles3', prms=['target', 'id'])
def glBeginQueryEXT(target, id):
	pass


@params(api='gles3', prms=['target'])
def glEndQueryEXT(target):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetQueryivEXT(target, pname):
	pass


@params(api='gles3', prms=['id', 'pname', 'params'])
def glGetQueryObjectuivEXT(id, pname):
	pass


