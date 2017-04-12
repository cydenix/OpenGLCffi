from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'format', 'len', 'string'])
def glProgramStringARB(target, format, len, string):
	pass


@params(api='gl', prms=['target', 'program'])
def glBindProgramARB(target, program):
	pass


@params(api='gl', prms=['n', 'programs'])
def glDeleteProgramsARB(n, programs):
	pass


@params(api='gl', prms=['n', 'programs'])
def glGenProgramsARB(n, programs):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramEnvParameter4dARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramEnvParameter4dvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramEnvParameter4fARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramEnvParameter4fvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramLocalParameter4dARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramLocalParameter4dvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'x', 'y', 'z', 'w'])
def glProgramLocalParameter4fARB(target, index, x, y, z, w):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glProgramLocalParameter4fvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramEnvParameterdvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramEnvParameterfvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramLocalParameterdvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'index', 'params'])
def glGetProgramLocalParameterfvARB(target, index, params):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetProgramivARB(target, pname, params):
	pass


@params(api='gl', prms=['target', 'pname', 'string'])
def glGetProgramStringARB(target, pname, string):
	pass


@params(api='gl', prms=['program'])
def glIsProgramARB(program):
	pass


