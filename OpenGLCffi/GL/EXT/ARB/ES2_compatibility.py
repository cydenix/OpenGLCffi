@params(api = 'gl')
def glReleaseShaderCompiler():
	pass


@params('count', 'shaders', 'binaryformat', 'binary', 'length', api='gl')
def glShaderBinary(count, shaders, binaryformat, binary, length):
	pass


@params('shadertype', 'precisiontype', 'range', 'precision', api='gl')
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
	pass


@params('n', 'f', api='gl')
def glDepthRangef(n, f):
	pass


@params('d', api='gl')
def glClearDepthf(d):
	pass


