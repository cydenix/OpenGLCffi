from OpenGLCffi.GL import params
@params('samples', 'fixedsamplelocations', api='gl')
def glRasterSamplesEXT(samples, fixedsamplelocations):
	pass


@params('n', 'v', api='gl')
def glCoverageModulationTableNV(n, v):
	pass


@params('bufsize', 'v', api='gl')
def glGetCoverageModulationTableNV(bufsize, v):
	pass


@params('components', api='gl')
def glCoverageModulationNV(components):
	pass


