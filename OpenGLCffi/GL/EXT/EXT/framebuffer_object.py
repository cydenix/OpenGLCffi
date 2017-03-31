@params('renderbuffer', api='gl')
def glIsRenderbufferEXT(renderbuffer):
	pass


@params('target', 'renderbuffer', api='gl')
def glBindRenderbufferEXT(target, renderbuffer):
	pass


@params('n', 'renderbuffers', api='gl')
def glDeleteRenderbuffersEXT(n, renderbuffers):
	pass


@params('n', 'renderbuffers', api='gl')
def glGenRenderbuffersEXT(n, renderbuffers):
	pass


@params('target', 'internalformat', 'width', 'height', api='gl')
def glRenderbufferStorageEXT(target, internalformat, width, height):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetRenderbufferParameterivEXT(target, pname, params):
	pass


@params('framebuffer', api='gl')
def glIsFramebufferEXT(framebuffer):
	pass


@params('target', 'framebuffer', api='gl')
def glBindFramebufferEXT(target, framebuffer):
	pass


@params('n', 'framebuffers', api='gl')
def glDeleteFramebuffersEXT(n, framebuffers):
	pass


@params('n', 'framebuffers', api='gl')
def glGenFramebuffersEXT(n, framebuffers):
	pass


@params('target', api='gl')
def glCheckFramebufferStatusEXT(target):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glFramebufferTexture1DEXT(target, attachment, textarget, texture, level):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glFramebufferTexture2DEXT(target, attachment, textarget, texture, level):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', 'zoffset', api='gl')
def glFramebufferTexture3DEXT(target, attachment, textarget, texture, level, zoffset):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gl')
def glFramebufferRenderbufferEXT(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('target', 'attachment', 'pname', 'params', api='gl')
def glGetFramebufferAttachmentParameterivEXT(target, attachment, pname, params):
	pass


@params('target', api='gl')
def glGenerateMipmapEXT(target):
	pass


