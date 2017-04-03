from OpenGLCffi.GL import params
@params('mode', 'first', 'count', 'primcount', api='gl')
def glMultiDrawArraysEXT(mode, first, count, primcount):
	pass


@params('mode', 'count', 'type', 'constindices', 'primcount', api='gl')
def glMultiDrawElementsEXT(mode, count, type, constindices, primcount):
	pass


