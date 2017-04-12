from OpenGLCffi.GLES3 import params
@params(api='gles3', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisampleEXT(target, samples, internalformat, width, height):
	pass


@params(api='gles3', prms=['target', 'attachment', 'textarget', 'texture', 'level', 'samples'])
def glFramebufferTexture2DMultisampleEXT(target, attachment, textarget, texture, level, samples):
	pass


