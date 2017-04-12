from OpenGLCffi.GL import params
@params(api='gl', prms=['identifier', 'num', 'names'])
def glGenNamesAMD(identifier, num, names):
	pass


@params(api='gl', prms=['identifier', 'num', 'names'])
def glDeleteNamesAMD(identifier, num, names):
	pass


@params(api='gl', prms=['identifier', 'name'])
def glIsNameAMD(identifier, name):
	pass


