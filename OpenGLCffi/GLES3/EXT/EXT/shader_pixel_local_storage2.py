from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'size'])
def glFramebufferPixelLocalStorageSizeEXT(target, size):
	pass


@params(api='gles3', prms=['target'])
def glGetFramebufferPixelLocalStorageSizeEXT(target):
	pass


@params(api='gles3', prms=['offset', 'n', 'values'])
def glClearPixelLocalStorageuiEXT(offset, n, values):
	pass


