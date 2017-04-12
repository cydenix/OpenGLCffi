from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'pname', 'param'])
def glFramebufferParameteri(target, pname, param):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetFramebufferParameteriv(target, pname, params):
	pass


