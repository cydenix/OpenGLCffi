from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['src', 'index'])
def glReadBufferIndexedEXT(src, index):
	pass


@params(api='gles3', prms=['n', 'location', 'indices'])
def glDrawBuffersIndexedEXT(n, location, indices):
	pass


@params(api='gles3', prms=['target', 'index', 'data'])
def glGetIntegeri_vEXT(target, index):
	pass


