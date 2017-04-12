from OpenGLCffi.GL import params
@params(api='gl', prms=['obj'])
def glDeleteObjectARB(obj):
	pass


@params(api='gl', prms=['pname'])
def glGetHandleARB(pname):
	pass


@params(api='gl', prms=['containerObj', 'attachedObj'])
def glDetachObjectARB(containerObj, attachedObj):
	pass


@params(api='gl', prms=['shaderType'])
def glCreateShaderObjectARB(shaderType):
	pass


@params(api='gl', prms=['shaderObj', 'count', 'string', 'length'])
def glShaderSourceARB(shaderObj, count, string, length):
	pass


@params(api='gl', prms=['shaderObj'])
def glCompileShaderARB(shaderObj):
	pass


@params(api='gl', prms=[])
def glCreateProgramObjectARB():
	pass


@params(api='gl', prms=['containerObj', 'obj'])
def glAttachObjectARB(containerObj, obj):
	pass


@params(api='gl', prms=['programObj'])
def glLinkProgramARB(programObj):
	pass


@params(api='gl', prms=['programObj'])
def glUseProgramObjectARB(programObj):
	pass


@params(api='gl', prms=['programObj'])
def glValidateProgramARB(programObj):
	pass


@params(api='gl', prms=['location', 'v0'])
def glUniform1fARB(location, v0):
	pass


@params(api='gl', prms=['location', 'v0', 'v1'])
def glUniform2fARB(location, v0, v1):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3fARB(location, v0, v1, v2):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4fARB(location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['location', 'v0'])
def glUniform1iARB(location, v0):
	pass


@params(api='gl', prms=['location', 'v0', 'v1'])
def glUniform2iARB(location, v0, v1):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2'])
def glUniform3iARB(location, v0, v1, v2):
	pass


@params(api='gl', prms=['location', 'v0', 'v1', 'v2', 'v3'])
def glUniform4iARB(location, v0, v1, v2, v3):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1fvARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2fvARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3fvARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4fvARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform1ivARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform2ivARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform3ivARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniform4ivARB(location, count, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix2fvARB(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix3fvARB(location, count, transpose, value):
	pass


@params(api='gl', prms=['location', 'count', 'transpose', 'value'])
def glUniformMatrix4fvARB(location, count, transpose, value):
	pass


@params(api='gl', prms=['obj', 'pname', 'params'])
def glGetObjectParameterfvARB(obj, pname, params):
	pass


@params(api='gl', prms=['obj', 'pname', 'params'])
def glGetObjectParameterivARB(obj, pname, params):
	pass


@params(api='gl', prms=['obj', 'maxLength', 'length', 'infoLog'])
def glGetInfoLogARB(obj, maxLength, length, infoLog):
	pass


@params(api='gl', prms=['containerObj', 'maxCount', 'count', 'obj'])
def glGetAttachedObjectsARB(containerObj, maxCount, count, obj):
	pass


@params(api='gl', prms=['programObj', 'name'])
def glGetUniformLocationARB(programObj, name):
	pass


@params(api='gl', prms=['programObj', 'index', 'maxLength', 'length', 'size', 'type', 'name'])
def glGetActiveUniformARB(programObj, index, maxLength, length, size, type, name):
	pass


@params(api='gl', prms=['programObj', 'location', 'params'])
def glGetUniformfvARB(programObj, location, params):
	pass


@params(api='gl', prms=['programObj', 'location', 'params'])
def glGetUniformivARB(programObj, location, params):
	pass


@params(api='gl', prms=['obj', 'maxLength', 'length', 'source'])
def glGetShaderSourceARB(obj, maxLength, length, source):
	pass


