from OpenGLCffi.GL import params
@params(api='gl', prms=['location', 'x'])
def glUniform1d(location, x):
	pass


@params(api='gl', prms=['location', 'x', 'y'])
def glUniform2d(location, x, y):
	pass


@params(api='gl', prms=['location', 'x', 'y', 'z'])
def glUniform3d(location, x, y, z):
	pass


@params(api='gl', prms=['location', 'x', 'y', 'z', 'w'])
def glUniform4d(location, x, y, z, w):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1dv(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2dv(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3dv(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4dv(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x3dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2x4dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x2dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3x4dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x2dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4x3dv(location, count, transpose, value):
	pass


@params(api='gl', prms=['program', 'location', 'params'])
def glGetUniformdv(program, location, params):
	pass


