from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'start', 'count', 'v'])
def glFramebufferSampleLocationsfvNV(target, start, count, v):
	pass


@params(api='gl', prms=['framebuffer', 'start', 'count', 'v'])
def glNamedFramebufferSampleLocationsfvNV(framebuffer, start, count, v):
	pass


@params(api='gl', prms=[])
def glResolveDepthValuesNV():
	pass


