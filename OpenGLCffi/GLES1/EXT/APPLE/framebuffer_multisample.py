from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisampleAPPLE(target, samples, internalformat, width, height):
	pass


@params(api='gles1', prms=[])
def glResolveMultisampleFramebufferAPPLE():
	pass


