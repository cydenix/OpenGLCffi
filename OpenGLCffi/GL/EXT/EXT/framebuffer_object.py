from OpenGLCffi.GL import params
@params(api='gl', prms=['renderbuffer'])
def glIsRenderbufferEXT(renderbuffer):
	pass


@params(api='gl', prms=['target', 'renderbuffer'])
def glBindRenderbufferEXT(target, renderbuffer):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glDeleteRenderbuffersEXT(n, renderbuffers):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glGenRenderbuffersEXT(n, renderbuffers):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'height'])
def glRenderbufferStorageEXT(target, internalformat, width, height):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetRenderbufferParameterivEXT(target, pname, params):
	pass


@params(api='gl', prms=['framebuffer'])
def glIsFramebufferEXT(framebuffer):
	pass


@params(api='gl', prms=['target', 'framebuffer'])
def glBindFramebufferEXT(target, framebuffer):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glDeleteFramebuffersEXT(n, framebuffers):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glGenFramebuffersEXT(n, framebuffers):
	pass


@params(api='gl', prms=['target'])
def glCheckFramebufferStatusEXT(target):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture1DEXT(target, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture2DEXT(target, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level', 'zoffset'])
def glFramebufferTexture3DEXT(target, attachment, textarget, texture, level, zoffset):
	pass


@params(api='gl', prms=['target', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glFramebufferRenderbufferEXT(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gl', prms=['target', 'attachment', 'pname', 'params'])
def glGetFramebufferAttachmentParameterivEXT(target, attachment, pname, params):
	pass


@params(api='gl', prms=['target'])
def glGenerateMipmapEXT(target):
	pass


