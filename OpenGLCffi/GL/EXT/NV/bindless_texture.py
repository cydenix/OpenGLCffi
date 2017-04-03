from OpenGLCffi.GL import params
@params('texture', api='gl')
def glGetTextureHandleNV(texture):
	pass


@params('texture', 'sampler', api='gl')
def glGetTextureSamplerHandleNV(texture, sampler):
	pass


@params('handle', api='gl')
def glMakeTextureHandleResidentNV(handle):
	pass


@params('handle', api='gl')
def glMakeTextureHandleNonResidentNV(handle):
	pass


@params('texture', 'level', 'layered', 'layer', 'format', api='gl')
def glGetImageHandleNV(texture, level, layered, layer, format):
	pass


@params('handle', 'access', api='gl')
def glMakeImageHandleResidentNV(handle, access):
	pass


@params('handle', api='gl')
def glMakeImageHandleNonResidentNV(handle):
	pass


@params('location', 'value', api='gl')
def glUniformHandleui64NV(location, value):
	pass


@params('location', 'count', 'value', api='gl')
def glUniformHandleui64vNV(location, count, value):
	pass


@params('program', 'location', 'value', api='gl')
def glProgramUniformHandleui64NV(program, location, value):
	pass


@params('program', 'location', 'count', 'values', api='gl')
def glProgramUniformHandleui64vNV(program, location, count, values):
	pass


@params('handle', api='gl')
def glIsTextureHandleResidentNV(handle):
	pass


@params('handle', api='gl')
def glIsImageHandleResidentNV(handle):
	pass


