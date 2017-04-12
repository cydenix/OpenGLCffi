from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'pname', 'params'])
def glTexParameterIivEXT(target, pname, params):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glTexParameterIuivEXT(target, pname, params):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetTexParameterIivEXT(target, pname):
	pass


@params(api='gles3', prms=['target', 'pname', 'params'])
def glGetTexParameterIuivEXT(target, pname):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIivEXT(sampler, pname, param):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIuivEXT(sampler, pname, param):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIivEXT(sampler, pname):
	pass


@params(api='gles3', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIuivEXT(sampler, pname):
	pass


