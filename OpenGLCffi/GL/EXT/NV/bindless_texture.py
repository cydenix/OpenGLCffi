from OpenGLCffi.GL import params
@params(api='gl', prms=['texture'])
def glGetTextureHandleNV(texture):
	pass


@params(api='gl', prms=['texture', 'sampler'])
def glGetTextureSamplerHandleNV(texture, sampler):
	pass


@params(api='gl', prms=['handle'])
def glMakeTextureHandleResidentNV(handle):
	pass


@params(api='gl', prms=['handle'])
def glMakeTextureHandleNonResidentNV(handle):
	pass


@params(api='gl', prms=['texture', 'level', 'layered', 'layer', 'format'])
def glGetImageHandleNV(texture, level, layered, layer, format):
	pass


@params(api='gl', prms=['handle', 'access'])
def glMakeImageHandleResidentNV(handle, access):
	pass


@params(api='gl', prms=['handle'])
def glMakeImageHandleNonResidentNV(handle):
	pass


@params(api='gl', prms=['location', 'value'])
def glUniformHandleui64NV(location, value):
	pass


@params(api='gl', prms=['location', 'count', 'value'])
def glUniformHandleui64vNV(location, count, value):
	pass


@params(api='gl', prms=['program', 'location', 'value'])
def glProgramUniformHandleui64NV(program, location, value):
	pass


@params(api='gl', prms=['program', 'location', 'count', 'values'])
def glProgramUniformHandleui64vNV(program, location, count, values):
	pass


@params(api='gl', prms=['handle'])
def glIsTextureHandleResidentNV(handle):
	pass


@params(api='gl', prms=['handle'])
def glIsImageHandleResidentNV(handle):
	pass


