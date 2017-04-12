from OpenGLCffi.GL import params
@params(api='gl', prms=['texture'])
def glGetTextureHandleARB(texture):
	pass


@params(api='gl', prms=['texture', 'sampler'])
def glGetTextureSamplerHandleARB(texture, sampler):
	pass


@params(api='gl', prms=['handle'])
def glMakeTextureHandleResidentARB(handle):
	pass


@params(api='gl', prms=['handle'])
def glMakeTextureHandleNonResidentARB(handle):
	pass


@params(api='gl', prms=['texture', 'level', 'layered', 'layer', 'format'])
def glGetImageHandleARB(texture, level, layered, layer, format):
	pass


@params(api='gl', prms=['handle', 'access'])
def glMakeImageHandleResidentARB(handle, access):
	pass


@params(api='gl', prms=['handle'])
def glMakeImageHandleNonResidentARB(handle):
	pass


@params(api='gl', prms=['location', 'value'])
def glUniformHandleui64ARB(location, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniformHandleui64vARB(location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'value'])
def glProgramUniformHandleui64ARB(program, location, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'values'])
def glProgramUniformHandleui64vARB(program, location, count, values):
	pass


@params(api='gl', prms=['handle'])
def glIsTextureHandleResidentARB(handle):
	pass


@params(api='gl', prms=['handle'])
def glIsImageHandleResidentARB(handle):
	pass


@params(api='gl', prms=['index', 'x'])
def glVertexAttribL1ui64ARB(index, x):
	pass


@params(api='gl', prms=['index', 'v'])
def glVertexAttribL1ui64vARB(index, v):
	pass


@params(api='gl', prms=['index', 'pname', 'params'])
def glGetVertexAttribLui64vARB(index, pname, params):
	pass


