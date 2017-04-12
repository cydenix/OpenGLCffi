from OpenGLCffi.GL import params
@params(api='gl', prms=['mode', 'first', 'count', 'primcount'])
def glMultiDrawArraysEXT(mode, first, count, primcount):
	pass


@params(api='gl', prms=['mode', 'count', 'type', 'constindices', 'primcount'])
def glMultiDrawElementsEXT(mode, count, type, constindices, primcount):
	pass


