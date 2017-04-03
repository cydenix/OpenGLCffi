from OpenGLCffi.GLES2 import params
@params('samples', 'fixedsamplelocations', api='gles2')
def glRasterSamplesEXT(samples, fixedsamplelocations):
	pass


@params('n', 'v', api='gles2')
def glCoverageModulationTableNV(n, v):
	pass


@params('bufsize', 'v', api='gles2')
def glGetCoverageModulationTableNV(bufsize, v):
	pass


@params('components', api='gles2')
def glCoverageModulationNV(components):
	pass


