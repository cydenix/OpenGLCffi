from OpenGLCffi.GLES1 import params
@params('target', 'samples', 'internalformat', 'width', 'height', api='gles1')
def glRenderbufferStorageMultisampleAPPLE(target, samples, internalformat, width, height):
	pass


@params(api = 'gles1')
def glResolveMultisampleFramebufferAPPLE():
	pass


