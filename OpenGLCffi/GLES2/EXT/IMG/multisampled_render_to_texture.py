from OpenGLCffi.GLES2 import params
@params(api='gles2', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisampleIMG(target, samples, internalformat, width, height):
	pass


@params(api='gles2', prms=['target', 'attachment', 'textarget', 'texture', 'level', 'samples'])
def glFramebufferTexture2DMultisampleIMG(target, attachment, textarget, texture, level, samples):
	pass


