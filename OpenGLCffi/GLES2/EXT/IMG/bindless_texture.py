from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['texture'])
def glGetTextureHandleIMG(texture):
	pass


@params(api='gles2', prms=['texture', 'sampler'])
def glGetTextureSamplerHandleIMG(texture, sampler):
	pass


@params(api='gles2', prms=['location', 'value'])
def glUniformHandleui64IMG(location, value):
	pass


@params(api='gles2', prms=['location', 'count', 'value'])
def glUniformHandleui64vIMG(location, count, value):
	pass


@params(api='gles2', prms=['program', 'location', 'value'])
def glProgramUniformHandleui64IMG(program, location, value):
	pass


@params(api='gles2', prms=['program', 'location', 'count', 'values'])
def glProgramUniformHandleui64vIMG(program, location, count, values):
	pass


