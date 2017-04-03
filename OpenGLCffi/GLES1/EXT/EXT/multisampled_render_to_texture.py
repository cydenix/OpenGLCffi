from OpenGLCffi.GLES1 import params
@params('target', 'samples', 'internalformat', 'width', 'height', api='gles1')
def glRenderbufferStorageMultisampleEXT(target, samples, internalformat, width, height):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', 'samples', api='gles1')
def glFramebufferTexture2DMultisampleEXT(target, attachment, textarget, texture, level, samples):
	pass


