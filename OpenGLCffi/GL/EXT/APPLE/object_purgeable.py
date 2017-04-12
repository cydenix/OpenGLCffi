from OpenGLCffi.GL import params
@params(api='gl', prms=['objectType', 'name', 'option'])
def glObjectPurgeableAPPLE(objectType, name, option):
	pass


@params(api='gl', prms=['objectType', 'name', 'option'])
def glObjectUnpurgeableAPPLE(objectType, name, option):
	pass


@params(api='gl', prms=['objectType', 'name', 'pname', 'params'])
def glGetObjectParameterivAPPLE(objectType, name, pname, params):
	pass


