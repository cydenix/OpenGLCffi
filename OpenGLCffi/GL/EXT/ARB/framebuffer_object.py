from OpenGLCffi.GL import params
@params(api='gl', prms=['renderbuffer'])
def glIsRenderbuffer(renderbuffer):
	pass


@params(api='gl', prms=['target', 'renderbuffer'])
def glBindRenderbuffer(target, renderbuffer):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glDeleteRenderbuffers(n, renderbuffers):
	pass


@params(api='gl', prms=['n', 'renderbuffers'])
def glGenRenderbuffers(n, renderbuffers):
	pass


@params(api='gl', prms=['target', 'internalformat', 'width', 'height'])
def glRenderbufferStorage(target, internalformat, width, height):
	pass


@params(api='gl', prms=['target', 'pname', 'params'])
def glGetRenderbufferParameteriv(target, pname, params):
	pass


@params(api='gl', prms=['framebuffer'])
def glIsFramebuffer(framebuffer):
	pass


@params(api='gl', prms=['target', 'framebuffer'])
def glBindFramebuffer(target, framebuffer):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glDeleteFramebuffers(n, framebuffers):
	pass


@params(api='gl', prms=['n', 'framebuffers'])
def glGenFramebuffers(n, framebuffers):
	pass


@params(api='gl', prms=['target'])
def glCheckFramebufferStatus(target):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture1D(target, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level'])
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
	pass


@params(api='gl', prms=['target', 'attachment', 'textarget', 'texture', 'level', 'zoffset'])
def glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset):
	pass


@params(api='gl', prms=['target', 'attachment', 'renderbuffertarget', 'renderbuffer'])
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
	pass


@params(api='gl', prms=['target', 'attachment', 'pname', 'params'])
def glGetFramebufferAttachmentParameteriv(target, attachment, pname, params):
	pass


@params(api='gl', prms=['target'])
def glGenerateMipmap(target):
	pass


@params(api='gl', prms=['srcX0', 'srcY0', 'srcX1', 'srcY1', 'dstX0', 'dstY0', 'dstX1', 'dstY1', 'mask', 'filter'])
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
	pass


@params(api='gl', prms=['target', 'samples', 'internalformat', 'width', 'height'])
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level', 'layer'])
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
	pass


