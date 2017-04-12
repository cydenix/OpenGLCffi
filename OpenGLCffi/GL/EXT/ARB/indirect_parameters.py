from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'indirect', 'drawcount', 'maxdrawcount', 'stride'])
def glMultiDrawArraysIndirectCountARB(mode, indirect, drawcount, maxdrawcount, stride):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect', 'drawcount', 'maxdrawcount', 'stride'])
def glMultiDrawElementsIndirectCountARB(mode, type, indirect, drawcount, maxdrawcount, stride):
	pass


