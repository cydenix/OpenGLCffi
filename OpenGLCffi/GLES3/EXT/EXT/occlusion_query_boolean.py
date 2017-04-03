from OpenGLCffi.GLES3 import params
@params('n', 'ids', api='gles3')
def glGenQueriesEXT(n, ids):
	pass


@params('n', 'ids', api='gles3')
def glDeleteQueriesEXT(n, ids):
	pass


@params('id', api='gles3')
def glIsQueryEXT(id):
	pass


@params('target', 'id', api='gles3')
def glBeginQueryEXT(target, id):
	pass


@params('target', api='gles3')
def glEndQueryEXT(target):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetQueryivEXT(target, pname):
	pass


@params('id', 'pname', 'params', api='gles3')
def glGetQueryObjectuivEXT(id, pname):
	pass


