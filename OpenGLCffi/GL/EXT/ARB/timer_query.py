from OpenGLCffi.GL import params
@params(api='gl', prms=['id', 'target'])
def glQueryCounter(id, target):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjecti64v(id, pname, params):
	pass


@params(api='gl', prms=['id', 'pname', 'params'])
def glGetQueryObjectui64v(id, pname, params):
	pass


