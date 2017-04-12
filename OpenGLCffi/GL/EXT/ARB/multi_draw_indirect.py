from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'indirect', 'drawcount', 'stride'])
def glMultiDrawArraysIndirect(mode, indirect, drawcount, stride):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect', 'drawcount', 'stride'])
def glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride):
	pass


