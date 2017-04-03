from OpenGLCffi.GL import params
@params('renderbuffer', api='gl')
def glIsRenderbuffer(renderbuffer):
	pass


@params('target', 'renderbuffer', api='gl')
def glBindRenderbuffer(target, renderbuffer):
	pass


@params('n', 'renderbuffers', api='gl')
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params('n', 'renderbuffers', api='gl')
def glGenRenderbuffers(n, renderbuffers):
	pass


@params('target', 'internalformat', 'width', 'height', api='gl')
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params('target', 'pname', 'params', api='gl')
def glGetRenderbufferParameteriv(target, pname, params):
	pass


@params('framebuffer', api='gl')
def glIsFramebuffer(framebuffer):
	pass


@params('target', 'framebuffer', api='gl')
def glBindFramebuffer(target, framebuffer):
	pass


@params('n', 'framebuffers', api='gl')
def glDeleteFramebuffers(n, framebuffers):
	pass


@params('n', 'framebuffers', api='gl')
def glGenFramebuffers(n, framebuffers):
	pass


@params('target', api='gl')
def glCheckFramebufferStatus(target):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glFramebufferTexture1D(target, attachment, textarget, texture, level):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', api='gl')
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params('target', 'attachment', 'textarget', 'texture', 'level', 'zoffset', api='gl')
def glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset):
	pass


@params('target', 'attachment', 'renderbuffertarget', 'renderbuffer', api='gl')
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params('target', 'attachment', 'pname', 'params', api='gl')
def glGetFramebufferAttachmentParameteriv(target, attachment, pname, params):
	pass


@params('target', api='gl')
def glGenerateMipmap(target):
	pass


@params('srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter', api='gl')
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params('target', 'samples', 'internalformat', 'width', 'height', api='gl')
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params('target', 'attachment', 'texture', 'level', 'layer', api='gl')
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


