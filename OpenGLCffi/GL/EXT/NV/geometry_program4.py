from OpenGLCffi.GL import params
@params(api='gl', prms=['target', 'limit'])
def glProgramVertexLimitNV(target, limit):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level'])
def glFramebufferTextureEXT(target, attachment, texture, level):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level', 'layer'])
def glFramebufferTextureLayerEXT(target, attachment, texture, level, layer):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level', 'face'])
def glFramebufferTextureFaceEXT(target, attachment, texture, level, face):
	pass


