from OpenGLCffi.GL import params
@params('target', 'start', 'count', 'v', api='gl')
def glFramebufferSampleLocationsfvNV(target, start, count, v):
	pass


@params('framebuffer', 'start', 'count', 'v', api='gl')
def glNamedFramebufferSampleLocationsfvNV(framebuffer, start, count, v):
	pass


@params(api = 'gl')
def glResolveDepthValuesNV():
	pass


