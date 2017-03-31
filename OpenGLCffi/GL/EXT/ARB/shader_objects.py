@params('obj', api='gl')
def glDeleteObjectARB(obj):
	pass


@params('pname', api='gl')
def glGetHandleARB(pname):
	pass


@params('containerObj', 'attachedObj', api='gl')
def glDetachObjectARB(containerObj, attachedObj):
	pass


@params('shaderType', api='gl')
def glCreateShaderObjectARB(shaderType):
	pass


@params('shaderObj', 'count', 'string', 'length', api='gl')
def glShaderSourceARB(shaderObj, count, string, length):
	pass


@params('shaderObj', api='gl')
def glCompileShaderARB(shaderObj):
	pass


@params(api = 'gl')
def glCreateProgramObjectARB():
	pass


@params('containerObj', 'obj', api='gl')
def glAttachObjectARB(containerObj, obj):
	pass


@params('programObj', api='gl')
def glLinkProgramARB(programObj):
	pass


@params('programObj', api='gl')
def glUseProgramObjectARB(programObj):
	pass


@params('programObj', api='gl')
def glValidateProgramARB(programObj):
	pass


@params('location', 'v0', api='gl')
def glUniform1fARB(location, v0):
	pass


@params('location', 'v0', 'v1', api='gl')
def glUniform2fARB(location, v0, v1):
	pass


@params('location', 'v0', 'v1', 'v2', api='gl')
def glUniform3fARB(location, v0, v1, v2):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glUniform4fARB(location, v0, v1, v2, v3):
	pass


@params('location', 'v0', api='gl')
def glUniform1iARB(location, v0):
	pass


@params('location', 'v0', 'v1', api='gl')
def glUniform2iARB(location, v0, v1):
	pass


@params('location', 'v0', 'v1', 'v2', api='gl')
def glUniform3iARB(location, v0, v1, v2):
	pass


@params('location', 'v0', 'v1', 'v2', 'v3', api='gl')
def glUniform4iARB(location, v0, v1, v2, v3):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1fvARB(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2fvARB(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3fvARB(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4fvARB(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform1ivARB(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform2ivARB(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform3ivARB(location, count, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniform4ivARB(location, count, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix2fvARB(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix3fvARB(location, count, transpose, value):
	pass


@params('location', 'count', 'transpose', 'value', api='gl')
def glUniformMatrix4fvARB(location, count, transpose, value):
	pass


@params('obj', 'pname', 'params', api='gl')
def glGetObjectParameterfvARB(obj, pname, params):
	pass


@params('obj', 'pname', 'params', api='gl')
def glGetObjectParameterivARB(obj, pname, params):
	pass


@params('obj', 'maxLength', 'length', 'infoLog', api='gl')
def glGetInfoLogARB(obj, maxLength, length, infoLog):
	pass


@params('containerObj', 'maxCount', 'count', 'obj', api='gl')
def glGetAttachedObjectsARB(containerObj, maxCount, count, obj):
	pass


@params('programObj', 'name', api='gl')
def glGetUniformLocationARB(programObj, name):
	pass


@params('programObj', 'index', 'maxLength', 'length', 'size', 'type', 'name', api='gl')
def glGetActiveUniformARB(programObj, index, maxLength, length, size, type, name):
	pass


@params('programObj', 'location', 'params', api='gl')
def glGetUniformfvARB(programObj, location, params):
	pass


@params('programObj', 'location', 'params', api='gl')
def glGetUniformivARB(programObj, location, params):
	pass


@params('obj', 'maxLength', 'length', 'source', api='gl')
def glGetShaderSourceARB(obj, maxLength, length, source):
	pass


