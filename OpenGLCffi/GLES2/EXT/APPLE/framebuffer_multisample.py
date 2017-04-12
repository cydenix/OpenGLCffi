from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisampleAPPLE(target, samples, internalformat, width, height):
	pass


@params(api='gles2', prms=[])
def glResolveMultisampleFramebufferAPPLE():
	pass


