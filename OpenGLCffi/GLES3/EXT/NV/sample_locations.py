from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'start', 'count', 'v'])
def glFramebufferSampleLocationsfvNV(target, start, count, v):
	pass


@params(api='gles3', prms=['framebuffer', 'start', 'count', 'v'])
def glNamedFramebufferSampleLocationsfvNV(framebuffer, start, count, v):
	pass


@params(api='gles3', prms=[])
def glResolveDepthValuesNV():
	pass


