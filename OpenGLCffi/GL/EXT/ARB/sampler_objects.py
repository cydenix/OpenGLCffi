@params('count', 'samplers', api='gl')
def glGenSamplers(count, samplers):
	pass


@params('count', 'samplers', api='gl')
def glDeleteSamplers(count, samplers):
	pass


@params('sampler', api='gl')
def glIsSampler(sampler):
	pass


@params('unit', 'sampler', api='gl')
def glBindSampler(unit, sampler):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameteri(sampler, pname, param):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameteriv(sampler, pname, param):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterf(sampler, pname, param):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterfv(sampler, pname, param):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params('sampler', 'pname', 'param', api='gl')
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameteriv(sampler, pname, params):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameterIiv(sampler, pname, params):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameterfv(sampler, pname, params):
	pass


@params('sampler', 'pname', 'params', api='gl')
def glGetSamplerParameterIuiv(sampler, pname, params):
	pass


