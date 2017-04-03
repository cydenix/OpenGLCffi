from OpenGLCffi.GL import params
@params('program', 'location', 'params', api='gl')
def glGetUniformuivEXT(program, location, params):
	pass


@params('program', 'color', 'name', api='gl')
def glBindFragDataLocationEXT(program, color, name):
	pass


@params('program', 'name', api='gl')
def glGetFragDataLocationEXT(program, name):
	pass


@params('location', 'v0', api='gl')
def glUniform1uiEXT(location, v0):
	pass


@params('location', 'v0', 'v1', api='gl')
def glUniform2uiEXT(location, v0, v1):
	pass


@params('location', 'v0', 'v1', 'v2', api='gl')
def glUniform3uiEXT(location, v0, v1, v2):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glUniform4uiEXT(location, v0, v1, v2, v3):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1uivEXT(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2uivEXT(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3uivEXT(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4uivEXT(location, count, value):
	pass


