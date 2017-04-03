from OpenGLCffi.GLES3 import params
@params('target', 'samples', 'internalformat', 'width', 'height', api='gles3')
def glRenderbufferStorageMultisampleAPPLE(target, samples, internalformat, width, height):
	pass


@params(api = 'gles3')
def glResolveMultisampleFramebufferAPPLE():
	pass


