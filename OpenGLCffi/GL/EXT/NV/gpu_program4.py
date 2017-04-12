from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramLocalParameterI4iNV(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramLocalParameterI4ivNV(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'count', 'params'])
def glProgramLocalParametersI4ivNV(target, index, count, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramLocalParameterI4uiNV(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramLocalParameterI4uivNV(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'count', 'params'])
def glProgramLocalParametersI4uivNV(target, index, count, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramEnvParameterI4iNV(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramEnvParameterI4ivNV(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'count', 'params'])
def glProgramEnvParametersI4ivNV(target, index, count, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramEnvParameterI4uiNV(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramEnvParameterI4uivNV(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'count', 'params'])
def glProgramEnvParametersI4uivNV(target, index, count, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramLocalParameterIivNV(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramLocalParameterIuivNV(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramEnvParameterIivNV(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramEnvParameterIuivNV(target, index, params):
	pass


