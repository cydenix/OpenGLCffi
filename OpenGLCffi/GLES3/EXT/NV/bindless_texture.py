from OpenGLCffi.GLES3 import params
@params('texture', api='gles3')
def glGetTextureHandleNV(texture):
	pass


@params('texture', 'sampler', api='gles3')
def glGetTextureSamplerHandleNV(texture, sampler):
	pass


@params('handle', api='gles3')
def glMakeTextureHandleResidentNV(handle):
	pass


@params('handle', api='gles3')
def glMakeTextureHandleNonResidentNV(handle):
	pass


@params('texture', 'level', 'layered', 'layer', 'format', api='gles3')
def glGetImageHandleNV(texture, level, layered, layer, format):
	pass


@params('handle', 'access', api='gles3')
def glMakeImageHandleResidentNV(handle, access):
	pass


@params('handle', api='gles3')
def glMakeImageHandleNonResidentNV(handle):
	pass


@params('location', 'value', api='gles3')
def glUniformHandleui64NV(location, value):
	pass


@params('location', 'count', 'value', api='gles3')
def glUniformHandleui64vNV(location, count, value):
	pass


@params('program', 'location', 'value', api='gles3')
def glProgramUniformHandleui64NV(program, location, value):
	pass


@params('program', 'location', 'count', 'values', api='gles3')
def glProgramUniformHandleui64vNV(program, location, count, values):
	pass


@params('handle', api='gles3')
def glIsTextureHandleResidentNV(handle):
	pass


@params('handle', api='gles3')
def glIsImageHandleResidentNV(handle):
	pass


