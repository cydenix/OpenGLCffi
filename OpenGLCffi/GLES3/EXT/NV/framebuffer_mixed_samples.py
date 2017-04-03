from OpenGLCffi.GLES3 import params
@params('samples', 'fixedsamplelocations', api='gles3')
def glRasterSamplesEXT(samples, fixedsamplelocations):
	pass


@params('n', 'v', api='gles3')
def glCoverageModulationTableNV(n, v):
	pass


@params('bufsize', 'v', api='gles3')
def glGetCoverageModulationTableNV(bufsize, v):
	pass


@params('components', api='gles3')
def glCoverageModulationNV(components):
	pass


