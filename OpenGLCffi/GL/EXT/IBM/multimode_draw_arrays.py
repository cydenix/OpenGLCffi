from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'first', 'count', 'primcount', 'modestride'])
def glMultiModeDrawArraysIBM(mode, first, count, primcount, modestride):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'constindices', 'primcount', 'modestride'])
def glMultiModeDrawElementsIBM(mode, count, type, constindices, primcount, modestride):
	pass


