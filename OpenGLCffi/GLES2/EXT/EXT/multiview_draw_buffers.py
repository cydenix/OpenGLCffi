from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['src', 'index'])
def glReadBufferIndexedEXT(src, index):
	pass


@params(api='gles2', prms=['n', 'location', 'indices'])
def glDrawBuffersIndexedEXT(n, location, indices):
	pass


@params(api='gles2', prms=['target', 'index', 'data'])
def glGetIntegeri_vEXT(target, index):
	pass


