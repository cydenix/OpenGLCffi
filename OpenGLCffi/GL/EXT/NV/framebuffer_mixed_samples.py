from OpenGLCffi.GL import params
@params(api='gl', prms=['samples', 'fixedsamplelocations'])
def glRasterSamplesEXT(samples, fixedsamplelocations):
	pass


@params(api='gl', prms=['n', 'v'])
def glCoverageModulationTableNV(n, v):
	pass


@params(api='gl', prms=['bufsize', 'v'])
def glGetCoverageModulationTableNV(bufsize, v):
	pass


@params(api='gl', prms=['components'])
def glCoverageModulationNV(components):
	pass


