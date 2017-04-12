from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'programInterface', 'pname', 'params'])
def glGetProgramInterfaceiv(program, programInterface, pname, params):
	pass


@params(api='gl', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceIndex(program, programInterface, name):
	pass


@params(api='gl', prms=['program', 'programInterface', 'index', 'bufSize', 'length', 'name'])
def glGetProgramResourceName(program, programInterface, index, bufSize, length, name):
	pass


@params(api='gl', prms=['program', 'programInterface', 'index', 'propCount', 'props', 'bufSize', 'length', 'params'])
def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params):
	pass


@params(api='gl', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceLocation(program, programInterface, name):
	pass


@params(api='gl', prms=['program', 'programInterface', 'name'])
def glGetProgramResourceLocationIndex(program, programInterface, name):
	pass


