from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'indirect'])
def glDrawArraysIndirect(mode, indirect):
	pass


@params(api='gl', prms=['mode', 'type', 'indirect'])
def glDrawElementsIndirect(mode, type, indirect):
	pass


