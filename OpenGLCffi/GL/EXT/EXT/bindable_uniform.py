from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'location', 'buffer'])
def glUniformBufferEXT(program, location, buffer):
	pass


@params(api='gl', prms=['program', 'location'])
def glGetUniformBufferSizeEXT(program, location):
	pass


@params(api='gl', prms=['program', 'location'])
def glGetUniformOffsetEXT(program, location):
	pass


