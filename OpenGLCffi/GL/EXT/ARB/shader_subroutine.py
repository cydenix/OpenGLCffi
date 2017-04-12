from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'shadertype', 'name'])
def glGetSubroutineUniformLocation(program, shadertype, name):
	pass


@params(api='gl', prms=['program', 'shadertype', 'name'])
def glGetSubroutineIndex(program, shadertype, name):
	pass


@params(api='gl', prms=['program', 'shadertype', 'index', 'pname', 'values'])
def glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values):
	pass


@params(api='gl', prms=['program', 'shadertype', 'index', 'bufsize', 'length', 'name'])
def glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length, name):
	pass


@params(api='gl', prms=['program', 'shadertype', 'index', 'bufsize', 'length', 'name'])
def glGetActiveSubroutineName(program, shadertype, index, bufsize, length, name):
	pass


@params(api='gl', prms=['shadertype', 'count', 'indices'])
def glUniformSubroutinesuiv(shadertype, count, indices):
	pass


@params(api='gl', prms=['shadertype', 'location', 'params'])
def glGetUniformSubroutineuiv(shadertype, location, params):
	pass


@params(api='gl', prms=['program', 'shadertype', 'pname', 'values'])
def glGetProgramStageiv(program, shadertype, pname, values):
	pass


