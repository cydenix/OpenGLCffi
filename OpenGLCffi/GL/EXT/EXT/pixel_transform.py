from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'pname', 'param'])
def glPixelTransformParameteriEXT(target, pname, param):
	pass


@params(api='gl', prms=['target', 'pname', 'param'])
def glPixelTransformParameterfEXT(target, pname, param):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glPixelTransformParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glPixelTransformParameterfvEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetPixelTransformParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetPixelTransformParameterfvEXT(target, pname, params):
	pass


