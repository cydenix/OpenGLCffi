from OpenGLCffi.GLES3 import params
@params('target', 'pname', 'params', api='gles3')
def glTexParameterIivOES(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gles3')
def glTexParameterIuivOES(target, pname, params):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetTexParameterIivOES(target, pname):
	pass


@params('target', 'pname', 'params', api='gles3')
def glGetTexParameterIuivOES(target, pname):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameterIivOES(sampler, pname, param):
	pass


@params('sampler', 'pname', 'param', api='gles3')
def glSamplerParameterIuivOES(sampler, pname, param):
	pass


@params('sampler', 'pname', 'params', api='gles3')
def glGetSamplerParameterIivOES(sampler, pname):
	pass


@params('sampler', 'pname', 'params', api='gles3')
def glGetSamplerParameterIuivOES(sampler, pname):
	pass


