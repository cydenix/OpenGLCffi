from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['samples', 'fixedsamplelocations'])
def glRasterSamplesEXT(samples, fixedsamplelocations):
	pass


@params(api='gles2', prms=['n', 'v'])
def glCoverageModulationTableNV(n, v):
	pass


@params(api='gles2', prms=['bufsize', 'v'])
def glGetCoverageModulationTableNV(bufsize, v):
	pass


@params(api='gles2', prms=['components'])
def glCoverageModulationNV(components):
	pass


