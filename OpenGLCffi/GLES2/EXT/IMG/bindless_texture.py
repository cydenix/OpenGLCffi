from OpenGLCffi.GLES2 import params
@params('texture', api='gles2')
def glGetTextureHandleIMG(texture):
	pass


@params('texture', 'sampler', api='gles2')
def glGetTextureSamplerHandleIMG(texture, sampler):
	pass


@params('location', 'value', api='gles2')
def glUniformHandleui64IMG(location, value):
	pass


@params('location', 'count', 'value', api='gles2')
def glUniformHandleui64vIMG(location, count, value):
	pass


@params('program', 'location', 'value', api='gles2')
def glProgramUniformHandleui64IMG(program, location, value):
	pass


@params('program', 'location', 'count', 'values', api='gles2')
def glProgramUniformHandleui64vIMG(program, location, count, values):
	pass


