from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'size'])
def glFramebufferPixelLocalStorageSizeEXT(target, size):
	pass


@params(api='gles2', prms=['target'])
def glGetFramebufferPixelLocalStorageSizeEXT(target):
	pass


@params(api='gles2', prms=['offset', 'n', 'values'])
def glClearPixelLocalStorageuiEXT(offset, n, values):
	pass


