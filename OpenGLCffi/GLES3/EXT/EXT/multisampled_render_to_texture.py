from OpenGLCffi.GLES3 import params
@params('target', 'samples', 'internalformat', 'width', 'height', api='gles3')
def glRenderbufferStorageMultisampleEXT(target, samples, internalformat, width, height):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', 'samples', api='gles3')
def glFramebufferTexture2DMultisampleEXT(target, attachment, textarget, texture, level, samples):
	pass


