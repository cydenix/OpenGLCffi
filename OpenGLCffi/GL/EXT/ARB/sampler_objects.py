from OpenGLCffi.GL import params
@params(api='gl', prms=['count', 'samplers'])
def glGenSamplers(count, samplers):
	pass


@params(api='gl', prms=['count', 'samplers'])
def glDeleteSamplers(count, samplers):
	pass


@params(api='gl', prms=['sampler'])
def glIsSampler(sampler):
	pass


@params(api='gl', prms=['unit', 'sampler'])
def glBindSampler(unit, sampler):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameteri(sampler, pname, param):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameteriv(sampler, pname, param):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterf(sampler, pname, param):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterfv(sampler, pname, param):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIiv(sampler, pname, param):
	pass


@params(api='gl', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIuiv(sampler, pname, param):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameteriv(sampler, pname, params):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIiv(sampler, pname, params):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterfv(sampler, pname, params):
	pass


@params(api='gl', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIuiv(sampler, pname, params):
	pass


