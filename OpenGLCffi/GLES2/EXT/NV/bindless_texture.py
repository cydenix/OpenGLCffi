from OpenGLCffi.GLES2 import params
@params('texture', api='gles2')
def glGetTextureHandleNV(texture):
	pass


@params('texture', 'sampler', api='gles2')
def glGetTextureSamplerHandleNV(texture, sampler):
	pass


@params('handle', api='gles2')
def glMakeTextureHandleResidentNV(handle):
	pass


@params('handle', api='gles2')
def glMakeTextureHandleNonResidentNV(handle):
	pass


@params('texture', 'level', 'layered', 'layer', 'format', api='gles2')
def glGetImageHandleNV(texture, level, layered, layer, format):
	pass


@params('handle', 'access', api='gles2')
def glMakeImageHandleResidentNV(handle, access):
	pass


@params('handle', api='gles2')
def glMakeImageHandleNonResidentNV(handle):
	pass


@params('location', 'value', api='gles2')
def glUniformHandleui64NV(location, value):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniformHandleui64vNV(location, count, value):
	pass


@params('program', 'location', 'value', api='gles2')
def glProgramUniformHandleui64NV(program, location, value):
	pass


@params('program', 'location', 'count', 'values', api='gles2')
def glProgramUniformHandleui64vNV(program, location, count, values):
	pass


@params('handle', api='gles2')
def glIsTextureHandleResidentNV(handle):
	pass


@params('handle', api='gles2')
def glIsImageHandleResidentNV(handle):
	pass


