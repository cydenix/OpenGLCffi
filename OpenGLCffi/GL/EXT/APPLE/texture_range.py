from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'length', 'pointer'])
def glTextureRangeAPPLE(target, length, pointer):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetTexParameterPointervAPPLE(target, pname, params):
	pass


