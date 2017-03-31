@params('target', 'limit', api='gl')
def glProgramVertexLimitNV(target, limit):
	pass


@params('target', 'attachment', 'texture', 'level', api='gl')
def glFramebufferTextureEXT(target, attachment, texture, level):
	pass


@params('target', 'attachment', 'texture', 'level', 'layer', api='gl')
def glFramebufferTextureLayerEXT(target, attachment, texture, level, layer):
	pass


@params('target', 'attachment', 'texture', 'level', 'face', api='gl')
def glFramebufferTextureFaceEXT(target, attachment, texture, level, face):
	pass


