from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'fixedsamplelocations'])
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height', 'depth', 'fixedsamplelocations'])
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
	pass


