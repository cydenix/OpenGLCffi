from OpenGLCffi.GL import params
@params(api='gl', prms=[])
def glReleaseShaderCompiler():
	pass


@params(api='gl', prms=['count', 'shaders', 'binaryformat', 'binary', 'length'])
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params(api='gl', prms=['shadertype', 'precisiontype', 'range', 'precision'])
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	pass


@params(api='gl', prms=['n', 'f'])
def glDepthRangef(n, f):
	pass


@params(api='gl', prms=['d'])
def glClearDepthf(d):
	pass


