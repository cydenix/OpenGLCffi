from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'start', 'count', 'v'])
def glFramebufferSampleLocationsfvARB(target, start, count, v):
	pass


@params(api='gl', prms=['framebuffer', 'start', 'count', 'v'])
def glNamedFramebufferSampleLocationsfvARB(framebuffer, start, count, v):
	pass


@params(api='gl', prms=[])
def glEvaluateDepthValuesARB():
	pass


