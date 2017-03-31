@params('program', 'shadertype', 'name', api='gl')
def glGetSubroutineUniformLocation(program, shadertype, name):
	pass


@params('program', 'shadertype', 'name', api='gl')
def glGetSubroutineIndex(program, shadertype, name):
	pass


@params('program', 'shadertype', 'index', 'pname', 'values', api='gl')
def glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values):
	pass


@params('program', 'shadertype', 'index', 'bufsize', 'length', 'name', api='gl')
def glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length, name):
	pass


@params('program', 'shadertype', 'index', 'bufsize', 'length', 'name', api='gl')
def glGetActiveSubroutineName(program, shadertype, index, bufsize, length, name):
	pass


@params('shadertype', 'count', 'indices', api='gl')
def glUniformSubroutinesuiv(shadertype, count, indices):
	pass


@params('shadertype', 'location', 'params', api='gl')
def glGetUniformSubroutineuiv(shadertype, location, params):
	pass


@params('program', 'shadertype', 'pname', 'values', api='gl')
def glGetProgramStageiv(program, shadertype, pname, values):
	pass


