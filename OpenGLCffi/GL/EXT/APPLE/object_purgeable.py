from OpenGLCffi.GL import params
@params('objectType', 'name', 'option', api='gl')
def glObjectPurgeableAPPLE(objectType, name, option):
	pass


@params('objectType', 'name', 'option', api='gl')
def glObjectUnpurgeableAPPLE(objectType, name, option):
	pass


@params('objectType', 'name', 'pname', 'params', api='gl')
def glGetObjectParameterivAPPLE(objectType, name, pname, params):
	pass


