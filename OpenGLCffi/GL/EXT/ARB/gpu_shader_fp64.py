from OpenGLCffi.GL import params
@params('location', 'x', api='gl')
def glUniform1d(location, x):
	pass


@params('location', 'x', 'y', api='gl')
def glUniform2d(location, x, y):
	pass


@params('location', 'x', 'y', 'z', api='gl')
def glUniform3d(location, x, y, z):
	pass


@params('location', 'x', 'y', 'z', 'w', api='gl')
def glUniform4d(location, x, y, z, w):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1dv(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2dv(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3dv(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4dv(location, count, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2x3dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2x4dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3x2dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3x4dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4x2dv(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4x3dv(location, count, transpose, value):
	pass


@params('program', 'location', 'params', api='gl')
def glGetUniformdv(program, location, params):
	pass


