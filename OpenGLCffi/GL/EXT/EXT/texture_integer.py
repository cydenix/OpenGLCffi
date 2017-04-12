from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'pname', 'params'])
def glTexParameterIivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glTexParameterIuivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexParameterIivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexParameterIuivEXT(target, pname, params):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glClearColorIiEXT(red, green, blue, alpha):
	pass


@params(api='gl', prms=['red', 'green', 'blue', 'alpha'])
def glClearColorIuiEXT(red, green, blue, alpha):
	pass


