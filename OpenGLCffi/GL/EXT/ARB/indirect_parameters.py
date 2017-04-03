from OpenGLCffi.GL import params
@params('mode', 'indirect', 'drawcount', 'maxdrawcount', 'stride', api='gl')
def glMultiDrawArraysIndirectCountARB(mode, indirect, drawcount, maxdrawcount, stride):
	pass


@params('mode', 'type', 'indirect', 'drawcount', 'maxdrawcount', 'stride', api='gl')
def glMultiDrawElementsIndirectCountARB(mode, type, indirect, drawcount, maxdrawcount, stride):
	pass


