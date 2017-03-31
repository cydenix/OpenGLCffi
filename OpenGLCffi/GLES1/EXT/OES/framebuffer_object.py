@params('renderbuffer', api='gles1')
def glIsRenderbufferOES(renderbuffer):
	pass


@params('target', 'renderbuffer', api='gles1')
def glBindRenderbufferOES(target, renderbuffer):
	pass


@params('n', 'renderbuffers', api='gles1')
def glDeleteRenderbuffersOES(n, renderbuffers):
	pass


@params('n', 'renderbuffers', api='gles1')
def glGenRenderbuffersOES(n, renderbuffers):
	pass


@params('target', 'internalformat', 'width', 'height', api='gles1')
def glRenderbufferStorageOES(target, internalformat, width, height):
	pass


@params('target', 'pname', 'params', api='gles1')
def glGetRenderbufferParameterivOES(target, pname):
	pass


@params('framebuffer', api='gles1')
def glIsFramebufferOES(framebuffer):
	pass


@params('target', 'framebuffer', api='gles1')
def glBindFramebufferOES(target, framebuffer):
	pass


@params('n', 'framebuffers', api='gles1')
def glDeleteFramebuffersOES(n, framebuffers):
	pass


@params('n', 'framebuffers', api='gles1')
def glGenFramebuffersOES(n, framebuffers):
	pass


@params('target', api='gles1')
def glCheckFramebufferStatusOES(target):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gles1')
def glFramebufferRenderbufferOES(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gles1')
def glFramebufferTexture2DOES(target, attachment, textarget, texture, level):
	pass


@params('target', 'attachment', 'pname', 'params', api='gles1')
def glGetFramebufferAttachmentParameterivOES(target, attachment, pname):
	pass


@params('target', api='gles1')
def glGenerateMipmapOES(target):
	pass


