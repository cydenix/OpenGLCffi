@params('texture', api='gl')
def glGetTextureHandleARB(texture):
	pass


@params('texture', 'sampler', api='gl')
def glGetTextureSamplerHandleARB(texture, sampler):
	pass


@params('handle', api='gl')
def glMakeTextureHandleResidentARB(handle):
	pass


@params('handle', api='gl')
def glMakeTextureHandleNonResidentARB(handle):
	pass


@params('texture', 'level', 'layered', 'layer', 'format', api='gl')
def glGetImageHandleARB(texture, level, layered, layer, format):
	pass


@params('handle', 'access', api='gl')
def glMakeImageHandleResidentARB(handle, access):
	pass


@params('handle', api='gl')
def glMakeImageHandleNonResidentARB(handle):
	pass


@params('location', 'value', api='gl')
def glUniformHandleui64ARB(location, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniformHandleui64vARB(location, count, value):
	pass


@params('program', 'location', 'value', api='gl')
def glProgramUniformHandleui64ARB(program, location, value):
	pass


@params('program', 'location', 'count', 'values', api='gl')
def glProgramUniformHandleui64vARB(program, location, count, values):
	pass


@params('handle', api='gl')
def glIsTextureHandleResidentARB(handle):
	pass


@params('handle', api='gl')
def glIsImageHandleResidentARB(handle):
	pass


@params('index', 'x', api='gl')
def glVertexAttribL1ui64ARB(index, x):
	pass


@params('index', 'v', api='gl')
def glVertexAttribL1ui64vARB(index, v):
	pass


@params('index', 'pname', 'params', api='gl')
def glGetVertexAttribLui64vARB(index, pname, params):
	pass


