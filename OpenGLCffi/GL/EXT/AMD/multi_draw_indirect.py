from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'indirect', 'primcount', 'stride'])
def glMultiDrawArraysIndirectAMD(mode, indirect, primcount, stride):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect', 'primcount', 'stride'])
def glMultiDrawElementsIndirectAMD(mode, type, indirect, primcount, stride):
	pass


