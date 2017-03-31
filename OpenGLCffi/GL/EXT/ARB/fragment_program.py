@params('target', 'format', 'len', 'string', api='gl')
def glProgramStringARB(target, format, len, string):
	pass


@params('target', 'program', api='gl')
def glBindProgramARB(target, program):
	pass


@params('n', 'programs', api='gl')
def glDeleteProgramsARB(n, programs):
	pass


@params('n', 'programs', api='gl')
def glGenProgramsARB(n, programs):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramEnvParameter4dARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramEnvParameter4dvARB(target, index, params):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramEnvParameter4fARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramEnvParameter4fvARB(target, index, params):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramLocalParameter4dARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramLocalParameter4dvARB(target, index, params):
	pass


@params('target', 'index', 'x', 'y', 'z', 'w', api='gl')
def glProgramLocalParameter4fARB(target, index, x, y, z, w):
	pass


@params('target', 'index', 'params', api='gl')
def glProgramLocalParameter4fvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramEnvParameterdvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramEnvParameterfvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramLocalParameterdvARB(target, index, params):
	pass


@params('target', 'index', 'params', api='gl')
def glGetProgramLocalParameterfvARB(target, index, params):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetProgramivARB(target, pname, params):
	pass


@params('target', 'pname', 'string', api='gl')
def glGetProgramStringARB(target, pname, string):
	pass


@params('program', api='gl')
def glIsProgramARB(program):
	pass


