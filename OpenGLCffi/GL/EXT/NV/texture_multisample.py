from OpenGLCffi.GL import params
@params('target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'fixedSampleLocations', api='gl')
def glTexImage2DMultisampleCoverageNV(target, coverageSamples, colorSamples, internalFormat, width, height, fixedSampleLocations):
	pass


@params('target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'depth', 'fixedSampleLocations', api='gl')
def glTexImage3DMultisampleCoverageNV(target, coverageSamples, colorSamples, internalFormat, width, height, depth, fixedSampleLocations):
	pass


@params('texture', 'target', 'samples', 'internalFormat', 'width', 'height', 'fixedSampleLocations', api='gl')
def glTextureImage2DMultisampleNV(texture, target, samples, internalFormat, width, height, fixedSampleLocations):
	pass


@params('texture', 'target', 'samples', 'internalFormat', 'width', 'height', 'depth', 'fixedSampleLocations', api='gl')
def glTextureImage3DMultisampleNV(texture, target, samples, internalFormat, width, height, depth, fixedSampleLocations):
	pass


@params('texture', 'target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'fixedSampleLocations', api='gl')
def glTextureImage2DMultisampleCoverageNV(texture, target, coverageSamples, colorSamples, internalFormat, width, height, fixedSampleLocations):
	pass


@params('texture', 'target', 'coverageSamples', 'colorSamples', 'internalFormat', 'width', 'height', 'depth', 'fixedSampleLocations', api='gl')
def glTextureImage3DMultisampleCoverageNV(texture, target, coverageSamples, colorSamples, internalFormat, width, height, depth, fixedSampleLocations):
	pass


