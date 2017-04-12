from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisampleAPPLE(target, samples, internalformat, width, height):
	pass


@params(api='gles3', prms=[])
def glResolveMultisampleFramebufferAPPLE():
	pass


