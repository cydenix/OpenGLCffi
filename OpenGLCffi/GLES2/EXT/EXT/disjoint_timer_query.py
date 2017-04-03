from OpenGLCffi.GLES2 import params
@params('n', 'ids', api='gles2')
def glGenQueriesEXT(n, ids):
	pass


@params('n', 'ids', api='gles2')
def glDeleteQueriesEXT(n, ids):
	pass


@params('id', api='gles2')
def glIsQueryEXT(id):
	pass


@params('target', 'id', api='gles2')
def glBeginQueryEXT(target, id):
	pass


@params('target', api='gles2')
def glEndQueryEXT(target):
	pass


@params('id', 'target', api='gles2')
def glQueryCounterEXT(id, target):
	pass


@params('target', 'pname', 'params', api='gles2')
def glGetQueryivEXT(target, pname):
	pass


@params('id', 'pname', 'params', api='gles2')
def glGetQueryObjectivEXT(id, pname):
	pass


@params('id', 'pname', 'params', api='gles2')
def glGetQueryObjectuivEXT(id, pname):
	pass


@params('id', 'pname', 'params', api='gles2')
def glGetQueryObjecti64vEXT(id, pname):
	pass


@params('id', 'pname', 'params', api='gles2')
def glGetQueryObjectui64vEXT(id, pname):
	pass


