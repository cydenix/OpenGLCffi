@params('program', 'programInterface', 'pname', 'params', api='gl')
def glGetProgramInterfaceiv(program, programInterface, pname, params):
	pass


@params('program', 'programInterface', 'name', api='gl')
def glGetProgramResourceIndex(program, programInterface, name):
	pass


@params('program', 'programInterface', 'index', 'bufSize', 'length', 'name', api='gl')
def glGetProgramResourceName(program, programInterface, index, bufSize, length, name):
	pass


@params('program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params', api='gl')
def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params):
	pass


@params('program', 'programInterface', 'name', api='gl')
def glGetProgramResourceLocation(program, programInterface, name):
	pass


@params('program', 'programInterface', 'name', api='gl')
def glGetProgramResourceLocationIndex(program, programInterface, name):
	pass


