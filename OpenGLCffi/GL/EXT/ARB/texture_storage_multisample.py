from OpenGLCffi.GL import params
@params('target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations', api='gl')
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations', api='gl')
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


