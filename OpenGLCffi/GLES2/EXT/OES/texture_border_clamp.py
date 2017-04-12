from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'pname', 'params'])
def glTexParameterIivOES(target, pname, params):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glTexParameterIuivOES(target, pname, params):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetTexParameterIivOES(target, pname):
	pass


@params(api='gles2', prms=['target', 'pname', 'params'])
def glGetTexParameterIuivOES(target, pname):
	pass


@params(api='gles2', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIivOES(sampler, pname, param):
	pass


@params(api='gles2', prms=['sampler', 'pname', 'param'])
def glSamplerParameterIuivOES(sampler, pname, param):
	pass


@params(api='gles2', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIivOES(sampler, pname):
	pass


@params(api='gles2', prms=['sampler', 'pname', 'params'])
def glGetSamplerParameterIuivOES(sampler, pname):
	pass


