from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'fixedSampleLocations'])
def glTexImage2DMultisampleCoverageNV(target, coverageSamples, colorSamples, internalFormat, width, height, fixedSampleLocations):
	pass


@params(api='gl', prms=['target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'depth', 'fixedSampleLocations'])
def glTexImage3DMultisampleCoverageNV(target, coverageSamples, colorSamples, internalFormat, width, height, depth, fixedSampleLocations):
	pass


@params(api='gl', prms=['texture', 'target', 'samples', 'internalFormat', 'width', 'height', 'fixedSampleLocations'])
def glTextureImage2DMultisampleNV(texture, target, samples, internalFormat, width, height, fixedSampleLocations):
	pass


@params(api='gl', prms=['texture', 'target', 'samples', 'internalFormat', 'width', 'height', 'depth', 'fixedSampleLocations'])
def glTextureImage3DMultisampleNV(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations):
	pass


@params(api='gl', prms=['texture', 'target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'fixedSampleLocations'])
def glTextureImage2DMultisampleCoverageNV(texture, target, coverageSamples, colorSamples, internalFormat, width, height, fixedSampleLocations):
	pass


@params(api='gl', prms=['texture', 'target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'depth', 'fixedSampleLocations'])
def glTextureImage3DMultisampleCoverageNV(texture, target, coverageSamples, colorSamples, internalFormat, width, height, depth, fixedSampleLocations):
	pass


