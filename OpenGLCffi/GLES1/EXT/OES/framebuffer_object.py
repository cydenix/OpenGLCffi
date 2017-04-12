from OpenGLCffi.GLES1 import params
@params(api='gles1', prms=['renderbuffer'])
def glIsRenderbufferOES(renderbuffer):
	pass


@params(api='gles1', prms=['target', 'renderbuffer'])
def glBindRenderbufferOES(target, renderbuffer):
	pass


@params(api='gles1', prms=['n', 'renderbuffers'])
def glDeleteRenderbuffersOES(n, renderbuffers):
	pass


@params(api='gles1', prms=['n', 'renderbuffers'])
def glGenRenderbuffersOES(n, renderbuffers):
	pass


@params(api='gles1', prms=['target', 'internalformat', 'width', 'height'])
def glRenderbufferStorageOES(target, internalformat, width, height):
	pass


@params(api='gles1', prms=['target', 'pname', 'params'])
def glGetRenderbufferParameterivOES(target, pname):
	pass


@params(api='gles1', prms=['framebuffer'])
def glIsFramebufferOES(framebuffer):
	pass


@params(api='gles1', prms=['target', 'framebuffer'])
def glBindFramebufferOES(target, framebuffer):
	pass


@params(api='gles1', prms=['n', 'framebuffers'])
def glDeleteFramebuffersOES(n, framebuffers):
	pass


@params(api='gles1', prms=['n', 'framebuffers'])
def glGenFramebuffersOES(n, framebuffers):
	pass


@params(api='gles1', prms=['target'])
def glCheckFramebufferStatusOES(target):
	pass


@params(api='gles1', prms=['target', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glFramebufferRenderbufferOES(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gles1', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture2DOES(target, attachment, textarget, texture, level):
	pass


@params(api='gles1', prms=['target', 'attachment', 'pname', 'params'])
def glGetFramebufferAttachmentParameterivOES(target, attachment, pname):
	pass


@params(api='gles1', prms=['target'])
def glGenerateMipmapOES(target):
	pass


