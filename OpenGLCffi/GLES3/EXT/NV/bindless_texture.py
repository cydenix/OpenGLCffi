from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['texture'])
def glGetTextureHandleNV(texture):
	pass


@params(api='gles3', prms=['texture', 'sampler'])
def glGetTextureSamplerHandleNV(texture, sampler):
	pass


@params(api='gles3', prms=['handle'])
def glMakeTextureHandleResidentNV(handle):
	pass


@params(api='gles3', prms=['handle'])
def glMakeTextureHandleNonResidentNV(handle):
	pass


@params(api='gles3', prms=['texture', 'level', 'layered', 'layer', 'format'])
def glGetImageHandleNV(texture, level, layered, layer, format):
	pass


@params(api='gles3', prms=['handle', 'access'])
def glMakeImageHandleResidentNV(handle, access):
	pass


@params(api='gles3', prms=['handle'])
def glMakeImageHandleNonResidentNV(handle):
	pass


@params(api='gles3', prms=['location', 'value'])
def glUniformHandleui64NV(location, value):
	pass


@params(api='gles3', prms=['location', 'count', 'value'])
def glUniformHandleui64vNV(location, count, value):
	pass


@params(api='gles3', prms=['program', 'location', 'value'])
def glProgramUniformHandleui64NV(program, location, value):
	pass


@params(api='gles3', prms=['program', 'location', 'count', 'values'])
def glProgramUniformHandleui64vNV(program, location, count, values):
	pass


@params(api='gles3', prms=['handle'])
def glIsTextureHandleResidentNV(handle):
	pass


@params(api='gles3', prms=['handle'])
def glIsImageHandleResidentNV(handle):
	pass


