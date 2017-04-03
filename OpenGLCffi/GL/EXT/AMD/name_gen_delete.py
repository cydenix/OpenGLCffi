from OpenGLCffi.GL import params
@params('identifier', 'num', 'names', api='gl')
def glGenNamesAMD(identifier, num, names):
	pass


@params('identifier', 'num', 'names', api='gl')
def glDeleteNamesAMD(identifier, num, names):
	pass


@params('identifier', 'name', api='gl')
def glIsNameAMD(identifier, name):
	pass


