from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['samples', 'fixedsamplelocations'])
def glRasterSamplesEXT(samples, fixedsamplelocations):
	pass


@params(api='gles3', prms=['n', 'v'])
def glCoverageModulationTableNV(n, v):
	pass


@params(api='gles3', prms=['bufsize', 'v'])
def glGetCoverageModulationTableNV(bufsize, v):
	pass


@params(api='gles3', prms=['components'])
def glCoverageModulationNV(components):
	pass


