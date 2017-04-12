from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'start', 'count', 'v'])
def glFramebufferSampleLocationsfvNV(target, start, count, v):
	pass


@params(api='gles2', prms=['framebuffer', 'start', 'count', 'v'])
def glNamedFramebufferSampleLocationsfvNV(framebuffer, start, count, v):
	pass


@params(api='gles2', prms=[])
def glResolveDepthValuesNV():
	pass


