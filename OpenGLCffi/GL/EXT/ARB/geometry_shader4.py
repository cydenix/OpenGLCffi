@params('program', 'pname', 'value', api='gl')
def glProgramParameteriARB(program, pname, value):
	pass


@params('target', 'attachment', 'texture', 'level', api='gl')
def glFramebufferTextureARB(target, attachment, texture, level):
	pass


@params('target', 'attachment', 'texture', 'level', 'layer', api='gl')
def glFramebufferTextureLayerARB(target, attachment, texture, level, layer):
	pass


@params('target', 'attachment', 'texture', 'level', 'face', api='gl')
def glFramebufferTextureFaceARB(target, attachment, texture, level, face):
	pass


