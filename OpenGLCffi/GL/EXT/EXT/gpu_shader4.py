from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'location', 'params'])
def glGetUniformuivEXT(program, location, params):
	pass


@params(api='gl', prms=['program', 'color', 'name'])
def glBindFragDataLocationEXT(program, color, name):
	pass


@params(api='gl', prms=['program', 'name'])
def glGetFragDataLocationEXT(program, name):
	pass


@params(api='gl', prms=['location', 'v0'])
def glUniform1uiEXT(location, v0):
	pass


@params(api='gl', prms=['location', 'v0', 'v1'])
def glUniform2uiEXT(location, v0, v1):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3uiEXT(location, v0, v1, v2):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4uiEXT(location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1uivEXT(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2uivEXT(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3uivEXT(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4uivEXT(location, count, value):
	pass


