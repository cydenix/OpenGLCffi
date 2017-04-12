from OpenGLCffi.GL import params
@params(api='gl', prms=['program', 'pname', 'value'])
def glProgramParameteriARB(program, pname, value):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level'])
def glFramebufferTextureARB(target, attachment, texture, level):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level', 'layer'])
def glFramebufferTextureLayerARB(target, attachment, texture, level, layer):
	pass


@params(api='gl', prms=['target', 'attachment', 'texture', 'level', 'face'])
def glFramebufferTextureFaceARB(target, attachment, texture, level, face):
	pass


